# Env

```bash
conda create -n deeplivecam python==3.10 -y
conda activate deeplivecam
pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1

pip install -r requirements_cuda.txt
pip install numpy==1.24.3
pip install gfpgan
pip install opennsfw2

# pip install tensorflow #2.18
conda install -c anaconda cudnn # cudnn 9.x
```

[Solved] face enhancer not found &#183; Issue #266 &#183; hacksider/Deep-Live-Cam
https://github.com/hacksider/Deep-Live-Cam/issues/266

# no internet install
cd gfpgan/weights
wget https://github.com/xinntao/facexlib/releases/download/v0.1.0/detection_Resnet50_Final.pth
wget https://github.com/xinntao/facexlib/releases/download/v0.2.2/parsing_parsenet.pth


# Env2

```bash
conda create -n dlc python==3.10 -y
conda activate dlc
pip install -r requirements.txt

module load cuda/11.7.1_515.65.01

```