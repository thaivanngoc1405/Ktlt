print("Thai Van Ngoc ")
print("MSSV:235752020710016 ")
print("#####################")
input_list = input("Nhập vào danh sách các số, cách nhau bằng dấu phẩy: ").split(',')
input_list = [int(x) for x in input_list]
odd_numbers = [x for x in input_list if x % 2 != 0]
print("Các số lẻ từ danh sách là:", odd_numbers)
