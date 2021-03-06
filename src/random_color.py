"""Use Hexbot to pick random colors"""
import requests

HEXBOT_URL = "https://api.noopschallenge.com/hexbot"


class RandomColor:

    def __init__(self, number_of_colors):
        self.number_of_colors = number_of_colors

    def list_of_colors(self):
        """Get a list containing self.number_of_colors hex values
        :return: a list of hex values, the length is given by self.number_of_colors
        """
        hexbot_values = self._call_hexbot()
        result = []
        for item in hexbot_values:
            hexcode = item['value']
            result.append(self._hex_to_rgb(hexcode))
        return result

    def _call_hexbot(self):
        """Call Github's Hexbot API to return a list of self.number_of_colors Color values
        :return: the "colors" list returned by the Hexbot
        """
        parameters = {
            'count': self.number_of_colors
        }
        r = requests.get(url=HEXBOT_URL, params=parameters)
        return r.json()['colors']

    def _hex_to_rgb(self, hex_string):
        """Convert a color given as a hex string to RGB values
        :param hex_string: a color's values as a hex string
        :return: a triplet representing the colors RGB values
        """
        h = hex_string.lstrip("#")
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
