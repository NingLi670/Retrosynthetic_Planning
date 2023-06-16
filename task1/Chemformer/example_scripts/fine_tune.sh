#!/bin/bash

CUDA_VISIBLE_DEVICES=2 python -m molbart.fine_tune \
  --dataset uspto_50 \
  --data_path data/uspto_50.pickle \
  --model_path models/bart/pretrained/combined/step=1000000.ckpt \
  --task backward_prediction \
  --epochs 100 \
  --lr 0.001 \
  --schedule cycle \
  --batch_size 128 \
  --acc_batches 4 \
  --augment all \
  --aug_prob 0.5

