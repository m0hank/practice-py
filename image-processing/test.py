from PIL import Image, ImageFilter

img = Image.open("image1.png")
filtered_img = img.convert('L')
crooked = filtered_img.rotate(180)
crooked.save("grey.jpeg", 'jpeg')
crooked.show()