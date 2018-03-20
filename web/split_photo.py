from math import sqrt, ceil, floor
from PIL import Image

image = Image.open("")
image.show()

def slice(filename, number_tiles):
    print "slicing"
    image = Image.open(filename)

    imageWidth, imageHeight = image.size
    columns, rows = calculateColumnsRows(number_tiles)
    extras = (columns * rows) - number_tiles
    tileWidth, tileHeight = int(floor(imageWidth / columns)), int(floor(imageHeight / rows))

    number = 1
    for pos_y in range(0, imageHeight - rows, tileHeight): # -rows for rounding error.
        for pos_x in range(0, imageWidth - columns, tileWidth): # as above.
            area = (pos_x, pos_y, pos_x + tileWidth, pos_y + tileHeight)
            tileImage = image.crop(area)

            tileImage.show()
            """passToModel(tileImage)"""

def calculateColumnsRows(parts):
    """
    Calculate the number of columns and rows required to divide an image
    into n parts.
    Return a tuple of integers in the format (num_columns, num_rows)
    """
    numColumns = int(ceil(sqrt(parts)))
    numRows = int(ceil(parts / float(numColumns)))
    return (numColumns, numRows)

slice("", )
