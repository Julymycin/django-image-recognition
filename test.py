import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
from torch import optim
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms, models, datasets
from PIL import Image

img=Image.open("./media/pic_MjQGN8c.jpg")
input_size=(300,300)
        
image_transforms = transforms.Compose(
    [
        transforms.Resize(input_size, interpolation=transforms.InterpolationMode.BILINEAR),
        transforms.ToTensor(),
        transforms.Normalize((0.425,0.415,0.405),(0.205,0.205,0.205)),
    ]
)
tensor=image_transforms(img).unsqueeze(0)
device = 'cuda' if torch.cuda.is_available() else 'cpu'

model=models.inception_v3(weights='DEFAULT')
model.eval()
model.to(device=device)
weights=models.Inception_V3_Weights.IMAGENET1K_V1
categories=weights.meta["categories"]
output=model(tensor)
index=1