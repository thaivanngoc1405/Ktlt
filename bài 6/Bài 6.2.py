print("Thai Van Ngoc ")
print("MSSV:235752020710016 ")
print("#####################")
class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
dai = float(input("Nhập chiều dài: "))
rong = float(input("Nhập chiều rộng: "))

hcn = Hinhchunhat(dai, rong)
dien_tich = hcn.tinh_dien_tich()
print("Diện tích của hình chữ nhật là:", dien_tich)
