print("Thai Van Ngoc ")
print("MSSV:235752020710016 ")
print("#####################")
def tong_uoc_so(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def in_so_nguyen_duong(n):
    for i in range(1, n):
        if tong_uoc_so(i) > i:
            print(i)
n = int(input("Nhập số n: "))
print("Các số nguyên dương nhỏ hơn", n, "có tổng ước số lớn hơn chính nó:")
in_so_nguyen_duong(n)

