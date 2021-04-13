# lol I still don't know python
# and I still don't know what is the package manager I should use
# I couldn't find my own package.json hack
# if you need to use this install with pip 'pillow' and 'imagehash' packages

import sys
from os import listdir, mkdir
from os.path import isfile, join, exists
from datetime import datetime
from imagecomparer import areImagesSimilar
from imagestorer import imageOperation

# TODO: pass paths as command-line argument
targetPath = './test-data'
limboPath = './limbo'
operationMode = 'move'

if not exists(limboPath):
    mkdir(limboPath)

for arg in sys.argv:
    if (arg == '--copy'):
        operationMode = 'copy'

usedExtensions = ['.png', '.jpg']

print('Process start time:', datetime.now().strftime("%H:%M:%S"))
print('Operation mode:', operationMode)
print('targetPath:', targetPath)

fileArray = [f for f in listdir(targetPath) if isfile(join(targetPath, f))]
imageArray = []

for file in fileArray:
    for extension in usedExtensions:
        if extension in file:
            imageArray.append(join(targetPath, file))
           
print('\nValid images found in targetPath:', imageArray)

for currentImage in imageArray:
    removed = []
    restOfTheImages = list(filter(lambda x: x not in [currentImage], imageArray))
    for imageToCompare in restOfTheImages:
        if (areImagesSimilar(currentImage, imageToCompare)):
            imagePlacedInLimbo = imageOperation(limboPath, currentImage, imageToCompare, operationMode)
            if (operationMode == 'move'):
                imageArray.remove(imagePlacedInLimbo)

print('\nOperation finish time:', datetime.now().strftime("%H:%M:%S"))
