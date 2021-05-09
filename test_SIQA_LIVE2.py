import numpy as np
import scipy.io as scio
import os
import time
import StereoIFNet
import tensorflow as tf
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


def time_change(time_init):   # The function is applied to calculate rest computational time.
    time_list = []
    if time_init/3600 > 1:
        time_h = int(time_init/3600)
        time_m = int((time_init-time_h*3600) / 60)
        time_s = int(time_init - time_h * 3600 - time_m * 60)
        time_list.append(str(time_h))
        time_list.append('h ')
        time_list.append(str(time_m))
        time_list.append('m ')
    elif time_init/60 > 1:
        time_m = int(time_init/60)
        time_s = int(time_init - time_m * 60)
        time_list.append(str(time_m))
        time_list.append('m ')
    else:
        time_s = int(time_init)
    time_list.append(str(time_s))
    time_list.append('s')
    time_str = ''.join(time_list)
    return time_str


path = "./LIVE2/"

print("[INFO] loading model...")
model = StereoIFNet.model()
model.load_weights(path + "/weights_LIVE2.hdf5")
print("[INFO] loading model completed...")

print("[INFO] loading dataset...")
testL = np.load(path + "testDataL.npy")
testR = np.load(path + "testDataR.npy")
testLeft = testL.astype('float32')
testRight = testR.astype('float32')
testLeft /= 255
testRight /= 255
testLeft -= np.mean(testLeft, axis=0)
testRight -= np.mean(testRight, axis=0)
testLeft /= np.std(testLeft, axis=0)
testRight /= np.std(testRight, axis=0)
print("The size of testL:" + str(testL.shape))
print("The size of testR:" + str(testR.shape))
print("[INFO] loading dataset completed...")

print("[INFO] Starting prediction...")
preds = []
count = 0
process = .0
start = time.time()
for test_batch_L, test_batch_R in zip(testLeft, testRight):
    test_batch_L = tf.expand_dims(test_batch_L, axis=0)
    test_batch_R = tf.expand_dims(test_batch_R, axis=0)
    res_pred = model([test_batch_L, test_batch_R])
    res = res_pred.numpy().tolist()
    preds += res
    count = count + 1
    if process < (count * 1.0 / 15840):
        if process != 0:
            end = time.time()
            use_time = end - start
            all_time = use_time / process
            res_time = all_time - use_time
            str_ues_time = time_change(use_time)
            str_res_time = time_change(res_time)
            print("[Percentage INFO] Percentage of progress:%.0f%%  Used time:%s  Rest time:%s " % (
                process * 100, str_ues_time, str_res_time))
        process = process + 0.01
print("Prediction end time： ", time.strftime('%Y.%m.%d %H:%M:%S ', time.localtime(time.time())))
scio.savemat(path + "preds_LIVE2.mat", {'preds': preds})
print("[INFO] Prediction completed...")
