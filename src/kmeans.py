"""Perform Kmeans"""
import random
import operator
from itertools import groupby

MAX_ITERATIONS = 100


class Kmeans:

    def __init__(self, k, data):
        """Initialize the KMeans algorithm for k clusters. The k centers are initialized with
        values from the given data.

        :param k: the number of clusters
        :param data: a list of values to partition
        """
        self.number_of_clusters = k
        self.data = data

    def process(self):
        """Apply the KMeans algorithm to our data.

        The initial K centers are randomly chosen from the dataset. All values in the dataset are assigned
        to the closest center. For each of the k centers, a new center is calculated depending on the
        values that were assigned to it. These steps of assigning items and recalculating the center
        are repeated for a fixed number of iterations.

        :return: a list of (data value, index of center) tuples
        """
        centers = self._randomize_centers()
        assert len(centers) == self.number_of_clusters
        assigned_items = []

        for _ in range(MAX_ITERATIONS):
            assigned_items = self._assign_items_to_closest_center(centers)
            centers = self._recalculate_centers(assigned_items)

        return assigned_items

    def _randomize_centers(self):
        """Return a list of k random values from the dataset"""
        return random.sample(self.data, self.number_of_clusters)

    def _assign_items_to_closest_center(self, centers):
        """For each item in self.data, find the center that's closest.
        Proximity is defined as the absolute difference between two integer values.

        :param centers: a list of k values
        :return: a list of (data value, index of closest center) tuples
        """
        assigned_items = []
        for item in self.data:
            index_closest_center = self._find_index_of_closest_center(item, centers)
            assigned_items.append((item, index_closest_center))
        return assigned_items

    def _find_index_of_closest_center(self, value, centers):
        """Given a value and a list of center values, find the index of the center
        with the lowest absolute difference in values.

        :param value: an integer
        :return: the index of the closest center
        """
        min_index = 0
        min_value = abs(centers[0] - value)
        for c in range(self.number_of_clusters):
            diff = abs(centers[c] - value)
            if diff < min_value:
                min_index = c
                min_value = diff
        return min_index

    def _recalculate_centers(self, assigned_items):
        """Compute the new centers by calculating the mean of the points that were
        assigned to them.

        :param assigned_items: a list of (data value, index of center) tuples
        :return: a list of k new centers
        """
        new_centers = []
        items_sorted_by_center = sorted(assigned_items, key=lambda x: x[1])
        c = groupby(items_sorted_by_center, key=operator.itemgetter(1))
        for k, v in c:
            values = [x[0] for x in list(v)]
            new_centers[k] = sum(values)/len(values)
        return new_centers

