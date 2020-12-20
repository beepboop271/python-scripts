# opens an image in a folder and saves 9 square images to the
# folder that together form a 3x3 grid of the original image
# (was originally used to create 9 discord emojis that combine
# to form one big emoji lol)
import os

from PIL import Image


def split(folder, filename):
    if not os.path.isdir(folder):
        raise NotADirectoryError(f"not a directory: {folder}")

    im = Image.open(os.path.join(folder, filename))
    if im.width != im.height:
        raise Exception("image is not square")
    if im.width/3 != int(im.width/3):
        print("warning: discarding bottom/right pixels (size not divisible by 3)")

    cell = int(im.width/3)
    count = 1
    name = os.path.splitext(filename)[0]
    for y in range(3):
        for x in range(3):
            im.crop(
                (cell*x, cell*y, cell*x+cell-1, cell*y+cell-1)
            ).save(
                os.path.join(folder, f"{name}_grid_{count}.jpg")
            )
            count += 1
