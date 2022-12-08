from django.apps import AppConfig

from PIL import Image
from glob import glob
import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
from torch import optim
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms, models, datasets

device = 'cuda' if torch.cuda.is_available() else 'cpu'


class ImgclassifierConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'imgclassifier'

class InceptionConfig(AppConfig):
    model=models.inception_v3(weights='DEFAULT')
    model.to(device=device)
    weights=models.Inception_V3_Weights.IMAGENET1K_V1
    categories=weights.meta["categories"]
    