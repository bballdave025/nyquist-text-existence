import numpy as np
from PIL import Image

def entropy(path):
  img = np.array(Image.open(path).convert('L'))
  p = np.bincount(img.ravel(), minlength=256) / img.size
  p = p[p > 0]
  return -(p * np.log2(p)).sum()
##endof:  entropy(path)

print("entropy("your_image.png"))
