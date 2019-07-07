import random
import operator
from itertools import groupby

MAX_ITERATIONS = 100


class Kmeans:

    def __init__(self, k, data):
        """Initialize the KMeans algorithm for k clusters. The k centers are initialized with
        values from the given data.

        :param k: the number of clusters
        :param data: the data to partition
        """
        self.number_of_clusters = k
        self.data = data
        self.initial_centers = random.sample(data, k)

    def randomize_centers(self):
        """Reset the initial centers to k random values from the dataset"""
        self.initial_centers = random.sample(self.data, self.number_of_clusters)

    def find_index_of_closest_center(self, value, centers):
        """Given a value and a list of center values, find the center
        with the lowest absolute difference in values"""
        min_index = 0
        min_value = abs(centers[0] - value)
        for c in range(self.number_of_clusters):
            diff = abs(centers[c] - value)
            if diff < min_value:
                min_index = c
                min_value = diff
        return min_index

    def affect_items_to_closest_center(self, centers):
        """For each item in self.data, find the center that's closest.
        Proximity is defined as the absolute difference between two integer values.

        :param centers: the current values for the k centers
        :return: a list of (data value, index of center) tuples
        """
        affected_items = []
        for item in self.data:
            index_closest_center = self.find_index_of_closest_center(item, centers)
            affected_items.append((item, index_closest_center))
        return affected_items

    def recalculate_centers(self, affected_items):
        """Calculate the new average for each center given the points that were
        affected to them.

        :param affected_items: a list of (data value, index of center) tuples
        :return: a list of k new center values
        """
        new_centers = self.initial_centers
        sorted_list = sorted(affected_items, key=lambda x: x[1])
        c = groupby(sorted_list, key=operator.itemgetter(1))
        for k, v in c:
            values = [x[0] for x in list(v)]
            new_centers[k] = sum(values)/len(values)
        return new_centers

    def process(self):
        """Apply the KMeans algorithm to our data

        :return: affected_items, a list of (data value, index of center) tuples
        """
        centers = self.initial_centers
        affected_items = []

        for iter in range(MAX_ITERATIONS):
            affected_items = self.affect_items_to_closest_center(centers)
            centers = self.recalculate_centers(affected_items)

        return affected_items
