from PIL import Image, ImageDraw

def create_dummy_image():
    img = Image.new('RGB', (100, 100), color = 'red')
    d = ImageDraw.Draw(img)
    d.text((10,10), "Test", fill=(255,255,0))
    img.save('to-convert/test_image.png')
    print("Created to-convert/test_image.png")

if __name__ == "__main__":
    create_dummy_image()
