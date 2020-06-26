"""Perform Kmeans"""
import numpy as np

MAX_ITERATIONS = 100


class Kmeans:

    def __init__(self, k, data):
        """Initialize the KMeans algorithm for k clusters. The k centers are initialized with
        values from the given data.

        :param k: the number of clusters
        :param data: a numpy array of values to partition
        """
        self.number_of_clusters = k
        self.data = data

    def process(self):
        """Apply the KMeans algorithm to our data.

        The initial K centers are randomly chosen from the dataset. All values in the dataset are assigned
        to the closest center. For each of the k centers, a new center is calculated depending on the
        values that were assigned to it. These steps of assigning items and recalculating the center
        are repeated for a fixed number of iterations.

        :return: a numpy array of class indexes, each item corresponds to the data point at the same index,
                    i.e. result[i] = class of data[i]
        """
        centers = self._randomize_centers()
        assert centers.shape[0] == self.number_of_clusters
        assigned_centers = np.zeros(self.data.shape)

        for _ in range(MAX_ITERATIONS):
            assigned_centers = self._assign_items_to_closest_center(centers)
            centers = self._recalculate_centers(assigned_centers)

        return assigned_centers

    def _randomize_centers(self):
        """Return a list of k random values from the dataset"""
        return np.random.choice(self.data, self.number_of_clusters, replace=False)

    def _assign_items_to_closest_center(self, centers):
        """For each item in self.data, find the center that's closest.
        Proximity is defined as the absolute difference between two integer values.

        :param centers: a list of k values
        :return: a numpy array of center indexes
        """
        diff_data_center = np.zeros((self.number_of_clusters, self.data.shape[0]))
        for i in range(self.number_of_clusters):
            diff_data_center[i] = np.abs(self.data - centers[i])
        return np.argmin(diff_data_center, axis=0)

    def _recalculate_centers(self, assigned_centers):
        """Compute the new centers by calculating the mean of the points that were
        assigned to them.

        :param assigned_centers: a numpy array of center indexes, i.e. assigned_centers[i] = class of data[i]
        :return: a numpy array of k new centers
        """
        new_centers = np.zeros((self.number_of_clusters,))

        for i in range(self.number_of_clusters):
            if self.data[assigned_centers == i].shape[0] != 0:
                new_centers[i] = self.data[assigned_centers == i].mean()
            else:
                new_centers[i] = -255

        return new_centers

