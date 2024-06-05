import torch
from torch.utils.data import Dataset
import numpy as np
import os
from PIL import Image
from torchvision import transforms

#图像处理操作，包括随机裁剪，转换张量
transform = transforms.Compose([transforms.RandomCrop(76),
                            transforms.ToTensor()])

path = 'dataset/T91-train/'
class PreprocessDataset(Dataset):
    """预处理数据集类"""

    def __init__(self, imgPath=path, ex=10):
        """初始化预处理数据集类"""
        self.transforms = transform

        for _, _, files in os.walk(imgPath):
            # ex变量是用于扩充数据集的，在这里默认的是扩充十倍
            self.imgs = [imgPath + file for file in files] * ex

        np.random.shuffle(self.imgs)  # 随机打乱

    def __len__(self):
        """获取数据长度"""
        return len(self.imgs)

    def __getitem__(self, index):
        """获取数据"""
        tempImg = self.imgs[index]
        tempImg = Image.open(tempImg)

        sourceImg = self.transforms(tempImg)  # 对原始图像进行处理
        cropImg = torch.nn.MaxPool2d(4)(sourceImg)
        return cropImg, sourceImg
