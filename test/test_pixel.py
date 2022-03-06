import numpy as np
import core.pixel as pixel
import pytest


class TestClass:

    def test_overlay_mask_dim(self):
        """Mask dims should be in 2D."""
        with pytest.raises(AssertionError):
            pixel.overlay(np.zeros((128, 128, 3)), np.ones((128, 128, 3)))

    def test_overlay_mask_shape(self):
        """Mask shape should be smaller than target image."""
        with pytest.raises(AssertionError):
            pixel.overlay(np.zeros((128, 128, 3)), np.ones((128, 129)))

    def test_overlay(self):
        """Does the overlay works?"""
        a = np.zeros((5, 4, 3)) + 128
        mask = np.zeros((3, 3))
        mask[-2:, -2:] = 1
        r = pixel.overlay(a, mask, (0, 0), (1, 2, 3))[1:3, 1:3, :]
        assert np.allclose(r, np.array(
            [[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]]))
