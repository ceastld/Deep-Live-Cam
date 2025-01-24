# import torch
# print(torch.backends.cudnn.version())


import tensorflow as tf
print(tf.sysconfig.get_build_info()["cuda_version"])
print(tf.sysconfig.get_build_info()["cudnn_version"])
