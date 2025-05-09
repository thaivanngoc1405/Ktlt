print("Thai Van Ngoc ")
print("MSSV: 235752020710016")
print("#####################")
def dem_chu_hoa_va_thuong(chuoi):
    chu_hoa = 0
    chu_thuong = 0
    for ky_tu in chuoi:
        if ky_tu.isupper():
            chu_hoa += 1
        elif ky_tu.islower():
            chu_thuong += 1
    return chu_hoa, chu_thuong

chuoi = input("Nhập vào một chuỗi: ")
so_chu_hoa, so_chu_thuong = dem_chu_hoa_va_thuong(chuoi)

print("Chữ hoa:", so_chu_hoa)
print("Chữ thường:", so_chu_thuong)
