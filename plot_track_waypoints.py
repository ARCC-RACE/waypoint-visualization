import matplotlib.pyplot as plt
import numpy as np

track_name = "New_York_Track"
absolute_path = "."
waypoints = np.load("%s/%s.npy" % (absolute_path, track_name))

print("Number of waypoints = " + str(waypoints.shape[0]))
for i, point in enumerate(waypoints):
    waypoint = (point[2], point[3])
    plt.scatter(waypoint[0], waypoint[1])
    print("Waypoint " + str(i) + ": " + str(waypoint))

plt.show()
