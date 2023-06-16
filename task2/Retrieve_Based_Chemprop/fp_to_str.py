import numpy as np
import pickle
# import torch
import time
from rdkit import Chem
from rdkit.Chem import AllChem

def get_fp_and_val():
    for mode in ['train', 'test']:
        with open(f'./data/MoleculeEvaluationData/{mode}.pkl', 'rb') as f:
            data = pickle.load(f)
        packed_fp = data['packed_fp']
        values = data['values'].numpy().flatten().astype(float)
        fp=np.unpackbits(packed_fp).reshape(-1,2048).astype(bool)
        print(fp.shape, fp.dtype, values.shape, values.dtype)
        # print(np.unique(fp))
        np.save(f'./data/MoleculeEvaluationData/{mode}_fp.npy', fp)
        np.save(f'./data/MoleculeEvaluationData/{mode}_value.npy', values)

def get_fps():
    with open('./data/Multi-Step/starting_mols_list.pkl', 'rb') as f:
        data = pickle.load(f)
    fps = []
    t=time.time()
    for i, product in enumerate(data):
        mol = Chem.MolFromSmiles(product)
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=2048)
        onbits = list(fp.GetOnBits())
        arr = np.zeros(fp.GetNumBits(), dtype=bool)
        arr[onbits]=1
        fps.append(arr)
        if i % 10000 == 0:
            print(i, time.time()-t)

    fps = np.array(fps)
    print(fps.shape, fps.dtype)
    np.save(f'./data/Multi-Step/starting_mols_list_fp_gpu19.npy', fps)


    # with open('./data/Multi-Step/starting_mols_list.pkl', 'rb') as f:
    #     data = pickle.load(f)[:1000000]
    # fps = []
    # t=time.time()
    # for i, product in enumerate(data):
    #     mol = Chem.MolFromSmiles(product)
    #     fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=2048)
    #     onbits = list(fp.GetOnBits())
    #     arr = np.zeros(fp.GetNumBits(), dtype=bool)
    #     arr[onbits]=1
    #     fps.append(arr)
    #     if i % 10000 == 0:
    #         print(i, time.time()-t)

    # fps = np.array(fps)
    # print(fps.shape, fps.dtype)
    # np.save(f'./data/Multi-Step/starting_mols_list_fp_1m.npy', fps)

def get_data():
    for mode in ['test']:
        index = np.load(f'./data/MoleculeEvaluationData/{mode}_full/search.npz')['index'][:,0].flatten()
        value = np.load(f'./data/MoleculeEvaluationData/{mode}_value.npy').flatten()
        with open('./data/Multi-Step/starting_mols_list.pkl', 'rb') as f:
            smile = pickle.load(f)
        print(index.shape, value.shape)
        data = [f'{smile[index[i]]},{str(value[i])}\n' for i in range(len(value))]
        data.insert(0, 'smile,cost\n')
        print(len(data), len(value))
        with open(f'./data/MoleculeEvaluationData/{mode}_full.csv', 'w') as f:
            f.writelines(data)

def get_retrieve_data():
    for mode in ['test']:
        index = np.load(f'./data/MoleculeEvaluationData/{mode}_full/search.npz')['index']
        value = np.load(f'./data/MoleculeEvaluationData/{mode}_value.npy').flatten()
        with open('./data/Multi-Step/starting_mols_list.pkl', 'rb') as f:
            smile = pickle.load(f)
        print(index.shape, value.shape)
        data = [f'{smile[index[i][0]]},{smile[index[i][1]]},{smile[index[i][2]]},{smile[index[i][3]]},{smile[index[i][4]]},{str(value[i])}\n' for i in range(len(value))]
        data.insert(0, 'smile1,smile2,smile3,smile4,smile5,cost\n')
        print(len(data), len(value))
        with open(f'./data/MoleculeEvaluationData/{mode}_retrieve_full.csv', 'w') as f:
            f.writelines(data)

def get_sum_data():
    for mode in ['test']:
        index = np.load(f'./data/MoleculeEvaluationData/{mode}_full/search.npz')['index'][:,0].flatten()
        value = np.load(f'./data/MoleculeEvaluationData/{mode}_value.npy').flatten()
        with open('./data/Multi-Step/starting_mols_list.pkl', 'rb') as f:
            smile = pickle.load(f)
        print(index.shape, value.shape)
        data = [f'{smile[index[i*3]]},{smile[index[i*3+1]]},{smile[index[i*3+2]]},{str((value[i*3]+value[i*3+1]+value[i*3+2]))}\n' for i in range(len(value)//3)]
        data.insert(0, 'smile1,smile2,smile3,sum_cost\n')
        print(len(data), len(value))
        with open(f'./data/MoleculeEvaluationData/{mode}_sum_full.csv', 'w') as f:
            f.writelines(data)

def combine_fp():
    for mode in ['train', 'test']:
        data = np.load(f'./data/MoleculeEvaluationData/{mode}_fp.npy')
        print(data.shape)
        data = data[:(len(data)//3)*3,:]
        print(data.shape)
        data = data.reshape(-1, 2048*3)
        print(data.shape)
        np.save(f'./data/MoleculeEvaluationData/{mode}_sum_fp.npy', data)

def combine_value():
    for mode in ['train', 'test']:
        data = np.load(f'./data/MoleculeEvaluationData/{mode}_value.npy').flatten()
        print(data.shape)
        print(data[:9])
        data = data[:(len(data)//3)*3]
        print(data.shape)
        data = data.reshape(-1, 3)
        print(data.shape)
        data = np.sum(data, axis=1).flatten()
        print(data.shape)
        print(data[:3])
        np.save(f'./data/MoleculeEvaluationData/{mode}_sum_value.npy', data)


# get_fps()

# get_data()
# get_sum_data()
# get_retrieve_data()