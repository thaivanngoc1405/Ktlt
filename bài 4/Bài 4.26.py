print("Thai Van Ngoc ")
print("MSSV:235752020710016 ")
print("#####################")
def tinh_so_tien_thuc(nhat_ky):
    so_tien_thuc = 0
    for giao_dich in nhat_ky:
        loai, so_tien = giao_dich.split()
        if loai == 'D':
            so_tien_thuc += int(so_tien)
        elif loai == 'W':
            so_tien_thuc -= int(so_tien)
    return so_tien_thuc

if __name__ == "__main__":
    nhap_nhieu_dong = True
    nhat_ky = []
    if nhap_nhieu_dong:
        print("Nhập nhật ký giao dịch (nhập 'done' để kết thúc): ")
        while True:
            dong = input()
            if dong.lower() == 'done':
                break
            nhat_ky.append(dong)
    else:
        nhat_ky = ["D 300", "D 300", "W 200", "D 100"] 
    so_tien_thuc = tinh_so_tien_thuc(nhat_ky)
    print("Số tiền thực của tài khoản ngân hàng là:", so_tien_thuc)
