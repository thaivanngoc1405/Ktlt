print("Thai Van Ngoc")
print("MSSV: 235752020710016")
print("#####################")
def benefit(t, n, k):
    r = t / 100  
    A = n * (1 + r) ** k
    return A
t = float(input("Nhập lãi suất tiết kiệm (%/tháng): "))
n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi tiết kiệm: "))

result = benefit(t, n, k)
print("Số tiền nhận được sau", k, "tháng là:", result)
