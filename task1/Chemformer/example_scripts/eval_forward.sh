#!/bin/bash

python -m molbart.evaluate \
  --data_path data/uspto_50.pickle \
  --model_path models/bart/pretrained/fine_tuned/last.ckpt \
  --dataset uspto_50 \
  --task forward_prediction \
  --model_type bart \
  --batch_size 64 \
  --num_beams 10

