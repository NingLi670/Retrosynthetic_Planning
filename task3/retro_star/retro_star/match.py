import numpy as np


data1 = np.load('dataset1/target_mol_route.pkl', allow_pickle=True)
data_retro = np.load('results/plan_500.pkl', allow_pickle=True)
data_eg = np.load('/home/huteng/zhuhaokun/EG-MCTS-main/eg_mcts/results/plan_500.pkl', allow_pickle=True)

# print(data_eg)

matches_0_20 = []
matches_20_40 = []
matches_40_60 = []
matches_60_80 = []
matches_80_100 = []

expert_len = [len(x) for x in data1]

route_len_retro = data_retro['route_lens']
route_len_eg = data_eg['route_lens']


route_len_retro = [x for x in route_len_retro if x is not None]
route_len_eg = [x for x in route_len_eg if x is not None]

p_expert, p_retro, p_eg = [], [], []

avg_expert = sum(expert_len) / float(len(expert_len))
avg_retro = sum(route_len_retro) / float(len(route_len_retro))
avg_eg = sum(route_len_eg) / float(len(route_len_eg))

print(avg_expert,avg_retro,avg_eg)
# for i in range(2,18):
#     p_expert.append(expert_len.count(i))
#     p_retro.append(route_len_retro.count(i))
#     p_eg.append(route_len_eg.count(i))

# print(p_expert)
# print(p_retro)
# print(p_eg)

# print(max(route_len_retro))
# print(min(route_len_retro))
#
# print(max(route_len_eg))
# print(min(route_len_eg))
#
# print(max(expert_len))
# print(min(expert_len))

# print(max(route_cost))
# print(min(route_cost))
# for i in range(190):
#     score = 0
#     route1 = data1[i]
#     route2 = data2[i]
#     len = min(len(route1), len(route2))
#     for j in range(len):
#         if route1[j] == route2[j]:
#             score += 1
#     score = score / float(len)
#     if 0 <= score < 20: matches_0_20.append(i)
#     if 20 <= score < 40: matches_20_40.append(i)
#     if 40 <= score < 60: matches_40_60.append(i)
#     if 60 <= score < 80: matches_60_80.append(i)
#     if 80 <= score < 100: matches_80_100.append(i)
#
# matches = [len(matches_0_20), len(matches_20_40), len(matches_40_60), len(matches_60_80), len(matches_80_100), ]