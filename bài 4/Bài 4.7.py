print("Thai Van Ngoc")
print("MSSV:235752020710016 ")
print("#####################")
def loai_bo_chu_so(chuoi):
    chuoi_moi = ''.join(ky_tu for ky_tu in chuoi if not ky_tu.isdigit())
    return chuoi_moi

chuoi = input("Nhập chuỗi từ bàn phím: ")
chuoi_loai_bo = loai_bo_chu_so(chuoi)
print("Chuỗi mới sau khi loại bỏ chữ số:", chuoi_loai_bo)
