print("Nguyễn Hồng Pháp")
print("MSSV:235752020710006")
print("#####################")
def tach_ten(ten):
    parts = ten.split()
    ho = parts[0]
    ten_rieng = " ".join(parts[1:])
    return ho, ten_rieng

def main():
    ten_nguoi = input("Nhập tên của người: ")
    ho, ten_rieng = tach_ten(ten_nguoi)
    print("Họ: ", ho)
    print("Tên riêng: ", ten_rieng)

if __name__ == "__main__":
    main()
