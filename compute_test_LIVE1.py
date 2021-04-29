import matlab.engine
import numpy as np
from scipy.io import loadmat

print("[INFO] Start performance evaluation...")
path = "./LIVE1/"
dmos = np.load(path + "testDmos.npy")
preds = loadmat(path + "preds_LIVE1.mat")
preds = np.array(preds["preds"])
dmos = dmos.astype('float32')
preds = preds.astype('float32')
preds = preds.tolist()
dmos = dmos.tolist()
eng = matlab.engine.start_matlab()
res = eng.performance_evaluation(matlab.double(preds),matlab.double(dmos),nargout=2)
PLCC, SROCC = np.array(res).reshape(2,1)
print("[INFO]" + "\tPLCC:" + str(round(PLCC.tolist()[0],4)) + "\tSROCC:" + str(round(SROCC.tolist()[0],4)))
print("[INFO] Performance evaluation completed!")