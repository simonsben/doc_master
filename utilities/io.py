from PIL.Image import open, fromarray
from pathlib import Path
from numpy import asarray, dot
from pandas import DataFrame
from matplotlib.pyplot import imsave


def make_path(filename):
    return Path(filename)


def to_greyscale(image):
    return dot(image[..., :3], [0.2989, 0.5870, 0.1140])


def load_image(path):
    path = make_path(path)
    if not path.exists():
        raise FileExistsError('Specified file doesn\'t exist')

    image = open(path)
    image = to_greyscale(asarray(image)).copy()

    return image


def save_image(image, path):
    imsave(path, image, cmap='gray')


def save_points(points):
    points = DataFrame(points, columns=('x', 'y'))
    points.to_csv('data/feature_points.csv')
