"""A grinder makes a generated license plate looks older and more natural."""
import cv2
import numpy as np


class Grinder:

    def __init__(self) -> None:
        """Create a grinder."""
        pass

    def make_noise(self, image, mean=0, var=0.01):
        """Add Gausses noise to the image."""
        noise = np.random.normal(mean, var ** 0.5, image.shape)
        image = image.astype(np.float32) / 255.0
        image += noise
        image = (np.clip(image, 0, 1.0) * 255).astype(np.uint8)

        return image

    def sharpen(self, image):
        """Make the edge more obvious."""
        k = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
        image = cv2.filter2D(image, -1, k)

        return image

    def blur(self, image, kernel_size):
        """Blur the image."""
        # Create the vertical kernel..
        kernel_v = np.zeros((kernel_size, kernel_size))

        # ..and the horizontal kernel.
        kernel_h = np.copy(kernel_v)

        # Fill the middle row with ones.
        kernel_v[:, int((kernel_size - 1)/2)] = np.ones(kernel_size)
        kernel_h[int((kernel_size - 1)/2), :] = np.ones(kernel_size)

        # Normalize.
        kernel_v /= kernel_size
        image = cv2.filter2D(image, -1, kernel_v)

        return image

    def exposure(self, image, alpha=1.0, beta=0):
        """Adjust the exposure level."""
        return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
