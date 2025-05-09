print("Thai Van Ngoc ")
print("MSSV:235752020710016 ")
print("#####################")
import numpy as np
ids = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
heights = np.array([40., 42., 45., 41., 38., 40., 42.0])
sorted_indices = np.lexsort((ids, heights))
print("Chỉ số nguyên mô tả thứ tự sắp xếp:")
for i in sorted_indices:
    print(i)
print("\nDữ liệu được sắp xếp:")
for i in sorted_indices:
    print(f"Sinh viên id {ids[i]} có chiều cao {heights[i]} cm")
