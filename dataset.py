from torch.utils.data import Dataset
from PIL import Image
import os

# class MyDataset(Dataset):
#     def __init__(self, root_dir, label_dir):
#         self.root_dir = root_dir
#         self.label_dir = label_dir
#         self.path = os.path.join(root_dir, label_dir)
#         self.img_path = os.listdir(self.path)
#
#     def __getitem__(self, index):
#         img_name = self.img_path[index]
#         img_item_path = os.path.join(self.path, img_name)
#         img = Image.open(img_item_path)
#         label = self.label_dir
#         return img, label
#
#     def __len__(self):
#         return len(self.img_path)
#
#
#
# root_dir = r"D:\Document\pytorch\hymenoptera_data\train"
# ants_label_dir = "ants"
# bees_label_dir = "bees"
# ants_dataset = MyDataset(root_dir, ants_label_dir)
# bees_dataset = MyDataset(root_dir, bees_label_dir)
# train_set = ants_dataset + bees_dataset



class MyDataset(Dataset):
    def __init__(self, root_dir, img_dir, label_dir):
        self.root_dir = root_dir
        self.img_path  = os.path.join(self.root_dir, img_dir)
        self.label_path = os.path.join(self.root_dir, label_dir)
        self.imgs = os.listdir(self.img_path)
        self.labels = os.listdir(self.label_path)

    def __len__(self):
        assert len(self.imgs) == len(self.labels)
        return len(self.imgs)

    def __getitem__(self, idx):
        img_name = self.imgs[idx].split('.')[0]
        img_item_path = os.path.join(self.img_path, self.imgs[idx])
        label_path = os.path.join(self.label_path, img_name+'.txt')
        img = Image.open(img_item_path)
        with open(label_path, 'r') as f:
            label = f.readline()
        return img, label


root_dir = r'D:\Document\pytorch\data\train'
img_dir = r'ants_image'
label_dir = r'ants_label'
ants_dataset = MyDataset(root_dir, img_dir, label_dir)
