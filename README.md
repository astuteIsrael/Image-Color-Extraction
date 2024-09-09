## Color Quantization using KMeans
  This project demonstrates how to perform color quantization on an image using the KMeans clustering algorithm in Python. Color quantization is useful for image compression, reducing the number of colors in an image while maintaining visual quality.

## Requirements
  Before running this project, ensure you have the following libraries installed:

pip install numpy matplotlib pillow scikit-learn

## How to Use
  Download the project or clone this repository.
  Place the image you want to process in the project directory.
  
## Run the script:
  python color_quantization.py
  The script will output a color palette of dominant colors in the image.

Python program Breakdown
  Load the Image: The script reads the image from a file and reshapes it into a 2D array of pixel colors.
  KMeans Clustering: The KMeans algorithm is applied to group similar colors.
  Palette Visualization: The dominant colors found by KMeans are displayed as a color palette.

## Customization
  You can adjust the number of colors in the palette by changing the n_colors variable. For example, setting n_colors = 5 will reduce the image to 5 dominant colors.
  To use a different image, simply change the file path in mpimg.imread().

## Example
Given an input image, the script will generate an output like this:

##  License
This project is licensed under the MIT License. Feel free to use it and modify it as needed!
