import argparse
import os
import time
import faiss
import numpy as np

def combine_search(args,start,num):
    print("\n combine_search")
    prepath= args.save_dir

    base_plus = start[:num+1]
    data = [np.load(os.path.join(prepath, f'search_{i}.npz')) for i in range(len(base_plus))]
    data_index = [_['index'] for _ in data]
    data_score = [_['score'] for _ in data]
    print("finish load")
    for i in range(len(base_plus)):
        data_index[i] += base_plus[i]
    final_num = data_index[0].shape[1]
    data_index = np.concatenate(data_index, axis=-1)
    data_score = np.concatenate(data_score, axis=-1)

    top_index = np.argsort(-data_score, axis=-1)[:, :final_num]

    data_index, data_score = np.take_along_axis(data_index, top_index, -1), np.take_along_axis(data_score, top_index, -1)
    store_dir = {'index': data_index, 'score': data_score}
    print(store_dir['index'].shape)
    np.savez(os.path.join(prepath,'search.npz'), **store_dir)
    print("max:",np.max(store_dir['index']))

    del data_index, data_score


def search(args,i,pool,start,end=None):
    print("\n search")
    print(start, end)
    index = faiss.IndexFlatIP(args.dim)
    index = faiss.index_cpu_to_all_gpus(index)
    if end is not None:
        index.add(normalize(pool[start:end, :args.dim]))
    else:
        index.add(normalize(pool[start:, :args.dim]))
    print("Index Add!")

    t1 = time.perf_counter()
    target = np.load(args.target_path).astype('float32')
    target_score, target_index = index.search(normalize(target[:, :args.dim]), args.candidate)
    target_index = target_index.astype('int32')
    store_dir = {'index': target_index, 'score': target_score}
    np.savez(os.path.join(args.save_dir, f'search_{i}.npz'), **store_dir)
    print(time.perf_counter() - t1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # path
    parser.add_argument('--pool_path', type=str, default='./data/Multi-Step/starting_mols_list_fp_1m.npy')
    parser.add_argument('--target_path', type=str, default='./data/MoleculeEvaluationData/test_fp.npy')
    parser.add_argument('--save_dir', type=str, default='./data/MoleculeEvaluationData/test_1m')

    parser.add_argument('--candidate', type=int, default=5, help='Number of neighbors to search')
    parser.add_argument('--num', type=int, default=1, help='Split embedding data if it is too large')
    parser.add_argument('--dim', type=int, default=2048)
    parser.add_argument('--gpu', type=str, default='0', help='Set GPU Ids : Eg: For CPU = 0, GPU = 0,1,2')
    args = parser.parse_args()
    print(args)

    normalize = lambda x: x / np.sqrt(np.sum(x ** 2, axis=-1, keepdims=True) + 1e-9)

    os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu

    t1 = time.perf_counter()
    emb_search = np.load(args.pool_path).astype('float32')
    print("Data Loaded! Costed {}s".format(time.perf_counter() - t1))

    num = args.num
    for i in range(num-1):
        search(args, i, emb_search, i*(len(emb_search)//num), (i+1)*(len(emb_search)//num))
    search(args, num-1, emb_search, (num-1)*(len(emb_search)//num))

    start = [i*(len(emb_search)//num) for i in range(num)]
    combine_search(args, start, num)
