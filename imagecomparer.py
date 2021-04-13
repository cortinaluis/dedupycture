import imagehash
from PIL import Image

def areImagesSimilar(image1, image2):
    hash1 = imagehash.average_hash(Image.open(image1))
    hash2 = imagehash.average_hash(Image.open(image2))
    cutoff = 5

    if hash1 - hash2 < cutoff:
        return True
    else:
        return False   
