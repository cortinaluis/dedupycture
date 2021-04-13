from os.path import getsize
from shutil import move, copy

def getImageToActOn(currentImage, imageToCompare):
    currentImageSize = getsize(currentImage)
    imageToCompareSize = getsize(imageToCompare)
    
    if currentImageSize > imageToCompareSize:
        return imageToCompare
    else:
        return currentImage

def imageOperation(limboPath, currentImage, imageToCompare, operation = 'move'):
    target = getImageToActOn(currentImage, imageToCompare)
    if (operation == 'copy'):
        copy(target, limboPath)
    elif (operation == 'move'):
        move(target, limboPath)
    else:
        raise Exception('Invalid image operation', operation)
    return target
