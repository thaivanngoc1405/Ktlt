print("Thai Van Ngoc")
print("MSSV: 235752020710016")
print("#####################")
import math

def Tinh(R):
    if R <= 0:
        print("Bán kính không hợp lệ. Vui lòng nhập giá trị lớn hơn 0.")
        return
    
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R**2
    
    print("Chu vi của hình tròn là:", chu_vi)
    print("Diện tích của hình tròn là:", dien_tich)
ban_kinh = float(input("Nhập bán kính của hình tròn: "))
Tinh(ban_kinh)
