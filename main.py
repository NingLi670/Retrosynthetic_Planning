import numpy as np
import time
import pickle

from rdchiral.template_extractor import extract_from_reaction
from rdchiral.main import rdchiralRunText
from rdkit import Chem
from rdkit.Chem import AllChem


############## task 1
## https://github.com/Hanjun-Dai/GLN
reaction = 'O=[C:1]([CH2:2][F:3])[CH2:4][F:5].[CH3:6][C:7]1([CH3:8])[CH2:9][CH2:10][C:11]([CH2:12][N:13]2[CH2:14][CH2:15][N:16]([c:17]3[cH:18][cH:19][c:20]([C:21](=[O:22])[NH:23][S:24](=[O:25])(=[O:26])[c:27]4[cH:28][cH:29][c:30]([NH:31][CH2:32][CH:33]5[CH2:34][NH:35][CH2:36]5)[c:37]([N+:38](=[O:39])[O-:40])[cH:41]4)[c:42]([O:43][c:44]4[cH:45][n:46][c:47]5[nH:48][cH:49][cH:50][c:51]5[cH:52]4)[cH:53]3)[CH2:54][CH2:55]2)=[C:56]([c:57]2[cH:58][cH:59][c:60]([Cl:61])[cH:62][cH:63]2)[CH2:64]1>>[CH:1]([CH2:2][F:3])([CH2:4][F:5])[N:35]1[CH2:34][CH:33]([CH2:32][NH:31][c:30]2[cH:29][cH:28][c:27]([S:24]([NH:23][C:21]([c:20]3[cH:19][cH:18][c:17]([N:16]4[CH2:15][CH2:14][N:13]([CH2:12][C:11]5=[C:56]([c:57]6[cH:58][cH:59][c:60]([Cl:61])[cH:62][cH:63]6)[CH2:64][C:7]([CH3:6])([CH3:8])[CH2:9][CH2:10]5)[CH2:55][CH2:54]4)[cH:53][c:42]3[O:43][c:44]3[cH:45][n:46][c:47]4[nH:48][cH:49][cH:50][c:51]4[cH:52]3)=[O:22])(=[O:25])=[O:26])[cH:41][c:37]2[N+:38](=[O:39])[O-:40])[CH2:36]1'

def get_template(reaction):
    reactants, products = reaction.split('>>')
    inputRec = {'_id':None, 'reactants':reactants, 'products':products}
    ans = extract_from_reaction(inputRec)
    # template = ans['reaction_smarts']
    # print(template)
    # output = rdchiralRunText(template, ans['products'])
    # print(output)
    if 'reaction_smarts' in ans.keys():
        return ans['reaction_smarts']
    else:
        return None

# t=time.time()
# data = np.loadtxt('./data/schneider50k/raw_train.csv', delimiter=',', comments=None, skiprows=1, dtype='str')
# cnt=0
# template = set()
# for i, line in enumerate(data[:10000]):
#     # print(line)
#     if i%100 == 0:
#         print(i)
#     re = get_template(line[-1])
#     if re == None:
#         cnt+=1
#     else:
#         template.add(re)
# print(cnt, len(template))
# print(time.time()-t)

# mol = Chem.MolFromSmiles(products)
# fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=2048)
# onbits = list(fp.GetOnBits())
# arr = np.zeros(fp.GetNumBits(), dtype=bool)
# arr[onbits]=1
# print(arr, arr.shape)



############## task 2
## train.pkl: dict{'packed_fp':array[298581,256], 'values':tensor[398581,1]}
## test.pkl: dict{'packed_fp':array[125240,256], 'values':tensor[125240,1]}

# with open('./data/MoleculeEvaluationData/test.pkl', 'rb') as f:
#     data = pickle.load(f)
# packed_fp = data['packed_fp']
# values = data['values']
# print(type(packed_fp), type(values))
# print(packed_fp.shape, values.shape)
# fp=np.unpackbits(packed_fp).reshape(-1,2048)
# print(fp.shape)



############## task 3
## https://github.com/binghong-ml/retro_star
## starting_mols.pkl: set[23081629]  str
## target_mol_route.pkl: list[190][x]  str>>str
## test_mols.pkl: list[190]  str

# with open('./data/Multi-Step/starting_mols.pkl', 'rb') as f:
#     data = pickle.load(f)
