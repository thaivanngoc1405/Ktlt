print("Thai Van Ngoc ")
print("MSSV:235752020710016 ")
print("#####################")
def kiem_tra_chia_het_cho_5(nhi_phan):
    decimal = int(nhi_phan, 2)
    if decimal % 5 == 0:
        return True
    else:
        return False

def main():
    chuoi_nhi_phan = input("Nhập chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy: ")
    cac_so_chia_het_cho_5 = []

    danh_sach_nhi_phan = chuoi_nhi_phan.split(',')
    for nhi_phan in danh_sach_nhi_phan:
        if kiem_tra_chia_het_cho_5(nhi_phan):
            cac_so_chia_het_cho_5.append(nhi_phan)

    if cac_so_chia_het_cho_5:
        print("Các số nhị phân chia hết cho 5 là:", ','.join(cac_so_chia_het_cho_5))
    else:
        print("Không có số nào chia hết cho 5 trong chuỗi nhập vào.")

if __name__ == "__main__":
    main()
