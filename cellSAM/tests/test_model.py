import pytest
import numpy as np

from cellSAM import segment_cellular_image


def test_segment_cellular_images_no_cells():
    img = np.zeros((512, 512), dtype=np.uint16)
    mask, x, bounding_boxes = segment_cellular_image(img)
    assert mask.shape == np.zeros(img.shape, dtype=int)
