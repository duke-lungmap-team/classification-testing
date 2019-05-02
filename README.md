# classification-testing
A scratch repo for classification of regions in lungmap images.

=======

## Purpose
The purpose of this repository is to start with the assumption that the immunofluorescence confocal 
images have adequately had instance segmentation applied, meaning that a contour of an anatomical structure is available. This repo tests difference classification techniques for labeling the segmented regions and also
segmenting cells within these larger anatomical entities and ideally tie these to an ontology which
can tie the color of the cell to the type of cell segmented.

## Usage

To run the entire pipeline:

1. Run `data_generator.py`: This will produce the training and test data in a `model_data` directory.
1. Run `xception_transfer.py`: This will train the Xception pipeline, and can take quite a while.
1. Run `test.py`: This will evaluate the test image for accuracy, saving the results in `results.csv` in the `model_data` directory.
