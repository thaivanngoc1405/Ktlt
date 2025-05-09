print("Thai Van Ngoc ")
print("MSSV: 235752020710016")
print("#####################")
ds = input("Nhập chuỗi: ")
ds = ds.split()

ds = [int(x.strip()) for x in ds]

ds = [x for x in ds if x != 123]

print("Danh sách sau khi loại bỏ phần tử 123:")
print(ds)
