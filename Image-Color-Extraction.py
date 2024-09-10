from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

image = mpimg.imread("Image-Color-Extraction folder\Spot-spider-man.jpg")  # Replace with actual image path

# Get image dimensions
w, h, d = image.shape
pixels = image.reshape(w * h, d)

# KMeans for color quantization
n_colors = 10
kmeans = KMeans(n_clusters=n_colors, random_state=42).fit(pixels)
palette = np.uint8(kmeans.cluster_centers_)

# Display the color palette
plt.imshow([palette])
plt.axis('off')
plt.show()
