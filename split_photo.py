from PIL import Image

def get_num_pixels(filepath):
    width, height = Image.open(open(filepath)).size
    return (width, height)

print get_num_pixels("recyclables1.jpg")
