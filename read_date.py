from torch.utils.data import Dataset
from PIL import Image
import os
class kai_date(Dataset):
    def __init__(self,root_dir,label_dir):
        self.root = root_dir
        self.label = label_dir
        self.path = os.path.join(self.root,self.label)
        self.suoyou_image = os.listdir(self.path)

    def __getitem__(self, idx):
        name = self.suoyou_image[idx]
        path = os.path.join(self.root,self.label,name)
        img = Image.open(path)
        label = self.label
        return img,label

root_dir = " " #绝对地址
label_dir = "haha" #标签
heihei = kai_date(root_dir,label_dir)
img,label = heihei[0] #显示第几张图像
img.show()