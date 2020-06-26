"""This is the entry point that takes in an image, performs KMeans clustering and shows the modified image."""
from random_color import RandomColor
from image import ImageHandler
from kmeans import Kmeans

import argparse

DEFAULT_NUMBER_CENTERS = 10

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Recolor an image.',
        add_help=True
    )
    parser.add_argument('imagepath', help='the path to the image')
    parser.add_argument('k', type=int, default=DEFAULT_NUMBER_CENTERS, nargs='?',
                        help='the number of colors in the final image, defaults to 10')

    args = parser.parse_args()

    image_file = args.imagepath

    r = RandomColor(args.k)
    new_colors = r.list_of_colors()

    ih = ImageHandler(image_file)
    kmeans = Kmeans(args.k, ih.pixels_list())
    affected_items = kmeans.process()

    ih.replace_with_new_colors(affected_items, new_colors)
    ih.show_result()
