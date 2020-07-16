# codes refer to datacamp lecture
# Import image class of matplotlib
import matplotlib.image as img
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans, vq, whiten
import seaborn as sns

# Read batman image and print dimensions
batman_image = img.imread('/Users/jielou/OneDrive/src/data-engineer-path/deliberate_machine_learning/data/images/batman.jpg')
print(batman_image.shape)

# Initialize lists
r,g,b = [], [], []

# Store RGB values of all pixels in lists r, g and b
for pixels in batman_image:
    for temp_r, temp_g, temp_b in pixels:
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)
# create dataframe
batman_df = pd.DataFrame({"red":r, "blue":b, "green":g})
batman_df["scaled_red"] = whiten(batman_df.red)
batman_df["scaled_blue"] = whiten(batman_df.blue)
batman_df["scaled_green"] = whiten(batman_df.green)
# lists
distortions = []
num_clusters = range(1, 7)

# Create a list of distortions from the kmeans function
for i in num_clusters:
    cluster_centers, distortion = kmeans(batman_df[['scaled_red', 'scaled_blue', 'scaled_green']], i)
    distortions.append(distortion)

# Create a data frame with two lists, num_clusters and distortions
elbow_plot = pd.DataFrame({'num_clusters': num_clusters, 'distortions': distortions})

# Create a line plot of num_clusters and distortions
sns.lineplot(x='num_clusters', y='distortions', data = elbow_plot)
plt.xticks(num_clusters)
plt.show()

## choose 3
cluster_centers, distortion = kmeans(batman_df[['scaled_red', 'scaled_blue', 'scaled_green']], 3)
# Get standard deviations of each color
r_std, g_std, b_std = batman_df[['red', 'green', 'blue']].std()

colors = []
for cluster_center in cluster_centers:
    scaled_r, scaled_g, scaled_b = cluster_center
    # Convert each standardized value to scaled value
    colors.append((
        scaled_r * r_std / 255,
        scaled_g * g_std / 255,
        scaled_b * b_std / 255
    ))

# Display colors of cluster centers
plt.imshow([colors])
plt.show()