print("Thai Van Ngoc ")
print("MSSV:235752020710016 ")
print("#####################")
import numpy as np
dt = np.dtype([('name', 'S20'), ('height', float), ('class', int)])
students = np.array([('John', 175.2, 10),
                     ('Alice', 162.5, 11),
                     ('Bob', 180.0, 10),
                     ('Diana', 168.9, 11)], dtype=dt)
sorted_students = np.sort(students, order='height')
print("Danh sách sinh viên sau khi sắp xếp theo chiều cao:")
for student in sorted_students:
    print("Name:", student['name'].decode('utf-8'), "- Height:", student['height'], "- Class:", student['class'])
