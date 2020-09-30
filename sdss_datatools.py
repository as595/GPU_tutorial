import numpy as np
import pandas as pd

import torch
from torchvision.transforms import transforms
from torch.utils.data import DataLoader
from torch.utils.data import Dataset

def load_sdss(infile):

    # read SDSS data:
    sdss_df = pd.read_pickle(infile)

    features = ['resolvedr', 'psf_u_corr', 'psf_g_corr', 'psf_r_corr', 'psf_i_corr', 'psf_z_corr', 'w1', 'w2', 'w3', 'w4']
    classes = ['class']
    
    sdss_x = sdss_df[features].values
    sdss_y = np.squeeze(sdss_df[classes].values)

    labels = np.unique(sdss_y)
    for i in range(len(labels)):
        sdss_y[np.where(sdss_y==labels[i])] = i

    del sdss_df # free up some memory

    # normalise each feature:
    for i in range(sdss_x.shape[1]):
        mean = np.mean(sdss_x[:,i])
        std = np.std(sdss_x[:,i])
        sdss_x[:,i] = (sdss_x[:,i] - mean)/std

    nobj = len(sdss_y)
    half = int(nobj/2)

    # randomly split dataset into train/test 50:50
    idx = np.random.randint(0,2,nobj).astype(bool)

    # test set:
    Zx_d = sdss_x[idx,:]
    Zy_d = sdss_y[idx]

    # train set:
    Zx = sdss_x[~idx,:]
    Zy = sdss_y[~idx]

    return Zx, Zy, Zx_d, Zy_d


class SDSSDataset(Dataset):
    def __init__(self, features, labels=None, transforms=None, normalise=False):
        self.x = features
        self.y = labels
        self.transforms = transforms
        self.normalise = normalise

    def __len__(self):
        return (len(self.x))

    def __getitem__(self, i):

        data = self.x[i, :]

        if self.normalise:
            mean = np.nanmean(data)
            std = np.nanstd(data)
            data = (data-mean)/std

        data = torch.Tensor(data)

        if self.transforms:
            data = self.transforms(data)

        if self.y is not None:
            return (data, self.y[i])
        else:
            return data
