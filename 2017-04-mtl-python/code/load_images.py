from PIL import Image
import numpy as np

data = []
for filename in filenames:
    img = Image.open(fname)
    img = np.asarray(img)
    data.append({'mean': img.mean(), 'std': img.std()})
