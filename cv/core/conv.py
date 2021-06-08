
import numpy as np


def im2col(img: np.array, kernel_size: int, stride: int) -> np.array:
    """
    Transforms image to rectangular representation
    for efficient convolution operation

    :param img:          np.array with shape (h, w, c)
    :param kernel_size:  kernel size
    :param stride:       convolution stride (step)
    :return: np.array with shape (kernel_size * kernel_size) x (out_h * out_w * n_channels)
    """
    channel_rows = []

    img_h, img_w, img_c = img.shape

    for c in range(img_c):
        rows = []
        for i in range(0, img_h - kernel_size + 1, stride):
            for j in range(0, img_w - kernel_size + 1, stride):
                window = img[i: i + kernel_size, j: j + kernel_size, c]
                rows.append(window.flatten())
        channel_rows.append(np.transpose(np.array(rows)))

    return np.hstack(channel_rows)


def pad_img(img: np.array, padding: int) -> np.array:
    """
    Pads image with 0's

    :param img:      np.array with shape (img_h x img_w x n_channels)
    :param padding:  width of the padding
    :return:         np.array with shape (img_h + 2 * padding) x (img_w + 2 * padding) x n_channels
    """
    _, _, img_c = img.shape
    img = np.asarray([
        np.pad(
            img[:, :, c],
            padding,
            'constant',
            constant_values=(0)
        )
        for c in range(img_c)
    ])
    return np.moveaxis(img, 0, -1)


def conv_2d(img: np.array, kernel: np.array, padding: int = 0, stride: int = 1) -> np.arry:
    """
    performs 2D convolution operation over image using kernel

    :param img:         np.array with shape (img_h x img_w X n_channels) or (img_h x img_w)
    :param kernel:      np.array with shape (kernel_size x kernel_size)
    :param padding:     constant '0' padding width
    :param stride:      convolution stride (step)
    :return:
    """
    if len(img.shape) == 2:
        img = np.expand_dims(img, axis=-1)

    in_h, in_w, channels = img.shape
    kernel_size = kernel.shape[0]

    img = pad_img(img, padding)

    out_w = (in_w - kernel_size + 2 * padding) // stride + 1
    out_h = (in_h - kernel_size + 2 * padding) // stride + 1

    M = im2col(img, kernel_size, stride)
    # flip kernel to perform convolution instead of cross-correlation
    K = np.flip(kernel.flatten())
    P = K @ M

    o_length = out_w * out_h

    img_out = []

    for i in range(channels):
        data = P[i * o_length: (i + 1) * o_length]
        out = data.reshape((out_h, out_w))
        img_out.append(out)

    img_out = np.array(img_out).astype(np.uint8)
    img_out = np.moveaxis(img_out, 0, -1)
    return img_out
