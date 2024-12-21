from torchvision import transforms
from PIL import Image

img_path = r"D:\Document\pytorch\data\train\ants_image\5650366_e22b7e1065.jpg"
img = Image.open(img_path)
tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)
print(type(tensor_img))
print(tensor_img.shape)