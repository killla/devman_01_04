from PIL import Image

offset = 50

with Image.open("monro.jpg") as image:
    red, green, blue = image.split()

coordinates = (offset, 0, red.width, red.height)
cropped = red.crop(coordinates)
coordinates = (0, 0, red.width-offset, red.height)
red = red.crop(coordinates)
red = Image.blend(red, cropped, 0.3)

coordinates = (0, 0, blue.width-offset, blue.height)
cropped = blue.crop(coordinates)
coordinates = (offset, 0, blue.width, blue.height)
blue = blue.crop(coordinates)
blue = Image.blend(blue, cropped, 0.3)

coordinates = (offset/2, 0, green.width-offset/2, green.height)
green = green.crop(coordinates)

result = Image.merge('RGB', (red, green, blue))
result.thumbnail((80, 80))
result.save('result.jpg')