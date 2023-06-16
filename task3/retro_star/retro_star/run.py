import os

iters = [100,200,300,400,500]

for iter in iters:
    os.system(f'python retro_plan.py --iterations {iter}')