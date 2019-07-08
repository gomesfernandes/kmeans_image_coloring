import sys
import argparse

from random_color import RandomColor
from image import ImageHandler
from kmeans import Kmeans

DEFAULT_NUMBER_CENTERS = 10

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Recolor an image.',
        add_help=True
    )
    parser.add_argument('imagepath', help='the image path')
    parser.add_argument('k', type=int, default=DEFAULT_NUMBER_CENTERS, nargs='?',
                        help='the number of colors in the final image')

    args = parser.parse_args()

    image_file = args.imagepath

    r = RandomColor(args.k)
    new_colors = r.list_of_colors()

    ih = ImageHandler(image_file)
    kmeans = Kmeans(args.k, ih.pixels_list())
    affected_items = kmeans.process()

    ih.replace_with_new_colors(affected_items, new_colors)
    ih.show_result()
