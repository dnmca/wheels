
import numpy as np


class Kernel:

    IDENTITY = np.array([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ])

    GRAD_X = np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]
    ])

    GRAD_Y = np.array([
        [ 1,  2,  1],
        [ 0,  0,  0],
        [-1, -2, -1]
    ])

    LAPLACIAN = np.array([
        [0,  1,  0],
        [1, -4,  1],
        [0,  1,  0]
    ])

    NEGATIVE_LAPLACIAN = np.array([
        [ 0, -1,  0],
        [-1,  4, -1],
        [ 0, -1,  0]
    ])

    GAUSSIAN_3X3 = 1 / 16 * np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ])

    GAUSSIAN_5X5 = 1 / 256 * np.array([
        [1,  4,  6,  4, 1],
        [4, 16, 24, 16, 4],
        [6, 24, 36, 24, 6],
        [4, 16, 24, 16, 4],
        [1,  4,  6,  4, 1],
    ])

    BOX_BLUR = 1 / 9 * np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ])

    SHARP = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    EMBOSS = np.array([
        [-2, -1,  0],
        [-1,  1,  1],
        [ 0,  1,  2]
    ])

    @staticmethod
    def gaussian(size: int, sigma: float = 1.0) -> np.ndarray:
        """
        Constructs gaussian kernel with given size and standard deviation

        :param size:    size of the resulting kernel
        :param sigma:   standard deviation
        """
        half = int(size) // 2
        x, y = np.mgrid[-half:half + 1, -half:half + 1]
        normal = 1 / (2.0 * np.pi * sigma ** 2)
        return np.exp(-((x ** 2 + y ** 2) / (2.0 * sigma ** 2))) * normal

    @staticmethod
    def dog(size: int, s1: float, s2: float) -> np.ndarray:
        """
        Constructs DoG (difference of gaussians) kernel with given size and standard deviations

        :param size:    size of the resulting kernel
        :param s1:      first sd
        :param s2:      second sd
        """
        return Kernel.gaussian(size, sigma=s1) - Kernel.gaussian(size, sigma=s2)
