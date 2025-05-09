print(" Thai Van Ngoc")
print("MSSV: 235752020710016")
print("#####################")
import numpy as np
dtype = [('name', 'S20'), ('height', float), ('class', int)]
data = [('James', 48.5, 5),
        ('Nail', 52.5, 6),
        ('Paul', 42.1, 5),
        ('Pit', 40.11, 5)]
students_array = np.array(data, dtype=dtype)
sorted_array = np.sort(students_array, order=['class', 'height'])
print("Sorted array:")
print(sorted_array)
