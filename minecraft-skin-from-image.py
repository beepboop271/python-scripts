# given a 16x32 image, outputs the minecraft skin produced by
# overlaying the image onto just the front of the body
import itertools
import os

from PIL import Image


def convert(image_path, background_colour=(255, 255, 255)):
    im = Image.open(image_path)
    if im.width != 16 or im.height != 32:
        raise Exception("image is not 16x32")
    if len(background_colour) < 3:
        raise Exception("colour is not RGB")

    colour = (*background_colour[:3], 255)
    # lol
    skin = bytes(itertools.chain.from_iterable(
        colour if n else (0, 0, 0, 0) for n in (
            0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        )
    ))

    target = (
        Image
        .frombytes("RGBA", (16, 16), skin)
        .resize((64, 64), Image.NEAREST)
    )

    # head
    target.paste(im.crop((4, 0, 12, 8)), (8, 8))
    # # chest
    target.paste(im.crop((4, 8, 12, 20)), (20, 20))
    # # right arm
    target.paste(im.crop((0, 8, 4, 20)), (44, 20))
    # # left arm
    target.paste(im.crop((12, 8, 16, 20)), (36, 52))
    # # right leg
    target.paste(im.crop((4, 20, 8, 32)), (4, 20))
    # # left leg
    target.paste(im.crop((8, 20, 12, 32)), (20, 52))

    dir_path, file_name = os.path.split(os.path.abspath(image_path))
    name = os.path.splitext(file_name)[0]+"_skin.png"
    target.save(os.path.join(dir_path, name))
