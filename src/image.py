"""Open, show and handle a Pillow Image. Note that it transforms images to grayscale."""
from PIL import Image, ImageOps
import numpy as np


class ImageHandler:

    def __init__(self, filename):
        self.filename = filename
        self.image = ImageOps.grayscale(Image.open(filename))
        self.result_image = None

    def pixels_list(self):
        """Return a numpy array of grayscale pixels"""
        return np.array(self.image.getdata())

    def show_result(self):
        """Show the new image"""
        if not self.result_image is None:
            self.result_image.show()

    def repaint_with_new_colors(self, color_indexes, new_colors):
        """Repaint the image with new colors, according to the positions in color_indexes.

        Each value in color_indexes represents an index in the new_colors list, which contains k RGB colors.
        The new image has the same dimensions as the original one, and each pixel's color is defined
        by color_index.

        :param color_indexes: a numpy array of color indexes
        :param new_colors: a list of RGB colors
        """
        new_pixel_values = np.zeros((color_indexes.shape[0], 3), dtype=int)

        for i in range(len(new_colors)):
            new_pixel_values[color_indexes == i] = new_colors[i]

        new_pixel_values = [tuple(x) for x in new_pixel_values.tolist()]

        self.result_image = Image.new("RGB", self.image.size)
        self.result_image.putdata(new_pixel_values)
