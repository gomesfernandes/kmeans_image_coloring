import sys

from src.random_color import RandomColor
from src.image import ImageHandler
from src.kmeans import Kmeans

NUMBER_CENTERS = 15

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: Please indicate the image you wish to process.")
        sys.exit(1)

    image_file = sys.argv[1]

    r = RandomColor(NUMBER_CENTERS)
    new_colors = r.list_of_colors()

    ih = ImageHandler(image_file)
    kmeans = Kmeans(NUMBER_CENTERS, ih.pixels_list())
    affected_items = kmeans.process()

    ih.replace_with_new_colors(affected_items, new_colors)
    ih.show_result()
