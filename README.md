
### Using Kmeans to recolor an image

This code will partition all pixels into k classes corresponding to a new color, using the KMeans algorithm.

Inspired by Githubs Noops Challenge, this Python project uses 
[Hexbot](https://github.com/noops-challenge/hexbot), an API that returns random colors.

To use it, please install the requirements listed in `requirements.txt`, then run the code 
using the following command:
```bash
python src/kmeans_image_coloring.py path_to_image
```