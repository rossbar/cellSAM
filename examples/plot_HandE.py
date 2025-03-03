"""
Brigthfield: H&E Staining
=========================
"""
import tifffile as tff
import napari

from cellSAM import cellsam_pipeline
img = tff.imread("../sample_imgs/HandE_OpenTest_049.tif")

# %%
# Since the image is >1k x 1k pixels, set ``use_wsi=True`` to run the
# segmentation in tiled mode.
# The `overlap` and `blocksize`

mask = cellsam_pipeline(
    img,
    block_size=500,
    overlap=200,
    iou_depth=200,
    low_contrast_enhancement=False,
    use_wsi=True,
    gauge_cell_size=False,
)

nim = napari.view_image(img, name="H&E");
nim.add_labels(mask, name="Cellsam segmentation");

if __name__ == "__main__":
    napari.run()
