from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image


writer = SummaryWriter('logs')

image_path = r"D:\Document\pytorch\data\train\ants_image\0013035.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
writer.add_image("test", img_array, dataformats='HWC')

# for i in range(100):
#     writer.add_scalar('y=2x', 2*i, i)
# writer.add_scalar()
writer.close()