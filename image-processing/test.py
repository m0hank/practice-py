from PIL import Image

img = Image.open("image1.png")
filtered_img = img.convert('L')
filtered_img.save("grey.jpeg", 'jpeg')