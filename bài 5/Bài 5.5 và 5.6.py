print("Thai Van Ngoc ")
print("MSSV: 235752020710016")
print("#####################")
def find_max_min(lst):
    sorted_lst = sorted(lst)
    min_value = sorted_lst[0]
    max_value = sorted_lst[-1]
    return min_value, max_value
def main():
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    my_list = []
    for i in range(n):
        value = int(input(f"Nhập phần tử thứ {i+1}: "))
        my_list.append(value)
    min_val, max_val = find_max_min(my_list)
    print("Phần tử nhỏ nhất trong danh sách là:", min_val)
    print("Phần tử lớn nhất trong danh sách là:", max_val)
if __name__ == "__main__":
    main()
