from PIL import Image, ImageOps


class ImageHandler:

    def __init__(self, filename):
        self.filename = filename
        self.image = ImageOps.grayscale(Image.open(filename))
        self.result_image = None

    def pixels_list(self):
        """Return the images list of pixels (RGB values)"""
        return list(self.image.getdata())

    def show_result(self):
        """Show the new image"""
        if not self.result_image is None:
            self.result_image.show()

    def replace_with_new_colors(self, affected_items, new_colors):
        """Create a new image according to the colors affected by Kmeans.

        :param affected_items: a list of (initial pixel value, color index) tuples
        :param new_colors: a list of new colors, one for each color index
        """
        new_pixel_values = []
        for tuple in affected_items:
            color_index = tuple[1]
            new_pixel_values.append(new_colors[color_index])

        self.result_image = Image.new("RGB", self.image.size)
        self.result_image.putdata(new_pixel_values)
