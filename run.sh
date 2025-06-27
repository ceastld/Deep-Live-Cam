conda activate dlc
ml cuDNN/8.7.0.84-CUDA-11.8.0
python run.py --execution-provider cuda --keep-fps
