print("Thai Van Ngoc ")
print("MSSV: 235752020710016")
print("#####################")
# binary_search.py

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False
def main():
    input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ").split(',')
    arr = [int(x) for x in input_list]
    value = int(input("Nhập giá trị cần tìm kiếm: "))
    if binary_search(arr, value):
        print(f"Phần tử {value} được tìm thấy trong danh sách.")
    else:
        print(f"Phần tử {value} không tồn tại trong danh sách.")

if __name__ == "__main__":
    main()
