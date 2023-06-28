import PIL.Image
import numpy as np
from PIL import Image

img1 = Image.new("RGB", (600, 600), (205, 100, 100))
img2 = Image.new("RGB", (600, 600), (0, 50, 20))
img3 = Image.new("RGB", (600, 600), (250, 10, 70))

with img1 as one:
    one.load()

with img2 as two:
    two.load()

with img3 as three:
    three.load()

arr1 = np.asarray(one)
arr2 = np.asarray(two)
arr3 = np.asarray(three)

red = np.zeros((600, 600))
green = np.zeros((600, 600))
blue = np.zeros((600, 600))
red[150:350, 150:350] = 255
green[200:400, 200:400] = 255
blue[250:450, 250:450] = 255

arr1_img = Image.fromarray(red).convert("L")
arr2_img = Image.fromarray(green).convert("L")
arr3_img = Image.fromarray(blue).convert("L")

m_img = Image.merge("RGB", (arr1_img, arr2_img, arr3_img))
m_img.show()
