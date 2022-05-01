import pandas as pd
import matplotlib.pyplot as plt

star_data = pd.read_csv("star_data.csv")

star_mass_list = star_data["Mass (M☉)"]
star_radius_list = star_data["Radius (R☉)"]
star_gravity_list = star_data["Surface Gravity (m/s²)"]

sorted_mass_list = star_mass_list.sort_values()
sorted_radius_list = star_radius_list.sort_values()
sorted_gravity_list = star_gravity_list.sort_values()

plt.figure(figsize = (10, 5))
plt.scatter(x = sorted_radius_list, y = sorted_mass_list, label = "Star")
plt.title('Relationship between Radius and Mass of Stars')
plt.ylabel('Radius of Stars')
plt.xlabel('Mass of Stars')
plt.legend(loc = 'upper left')

plt.figure(figsize = (10, 5))
plt.scatter(x = sorted_gravity_list, y = sorted_mass_list, label = "Star")
plt.title('Relationship between Gravity and Mass of Stars')
plt.ylabel('Gravity of Stars')
plt.xlabel('Mass of Stars')
plt.legend(loc = 'upper left')

plt.show()