from ecelms import BaggingECELMs
import os
import argparse
import torchbox as tb
import torch as th
import numpy as np
import torchsar as ts
import matplotlib.pyplot as plt
import scipy
from dataset import saveimage

parser = argparse.ArgumentParser()

parser.add_argument('--datacfg', type=str, default='./data.yaml')
parser.add_argument('--modelcfg', type=str, default='./ecelms.yaml')
cfg = parser.parse_args()
modelcfg = tb.loadyaml(cfg.modelcfg)

X= th.load('./tensors/Xtest.pt')

var = th.sqrt(th.mean(abs(X - X.mean())**2))

def additive_noise(X,var):
    X_noise = np.random.normal([0],th.sqrt(th.mean(abs(X - X.mean())**2))*var,(256,256))
    X_noisy = X+X_noise.reshape((1,256,256,1))
    return th.tensor(X_noisy,dtype=th.float32)

def speckle(X,var):
    X_speckle =np.random.normal([0],1,(256,256))
    X_speckly = X*X_speckle.reshape((1,256,256,1))
    return th.tensor(X_speckly,dtype=th.float32)

def gaussian(X,var):
    def generate_psf(size, sigma):
        x = np.arange(-size // 2 + 1, size // 2 + 1)
        xx, yy = np.meshgrid(x, x)
        psf = np.exp(-(xx ** 2 + yy ** 2) / (2 * sigma ** 2))
        psf /= np.sum(psf)
        return psf
    size=5
    sigma=var
    psf = generate_psf(size,sigma)
    X_blur=th.tensor(np.zeros(X.shape))
    for i in range(X.shape[0]):
        for j in range(2):
            X_blur[i,:,:,j] = th.tensor(scipy.signal.convolve2d(X[i,:,:,j],th.tensor(psf),"same"))

    return th.tensor(X_blur,dtype=th.float32)
