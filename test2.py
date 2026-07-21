import sys
from PIL import Image, ImageOps


threshold = 128

test_1 = Image.open("test.png")

new_size = (80, 30)

new_image = test_1.resize(new_size)


new_image = new_image.point( lambda p: 255 if p > threshold else 0)

pixel_check = list(new_image.getdata())


print(pixel_check)


new_image.show()
