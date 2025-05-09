print(" Thai Van Ngoc")
print("MSSV:235752020710016 ")
print("#####################")
def write_list_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            for item in content:
                file.write(str(item) + '\n')
        print("Đã viết nội dung vào tệp thành công.")
    except IOError:
        print("Có lỗi xảy ra khi viết vào tệp.")
my_list = ["Hello", "World", 123, 456]
file_path = "D:/a.txt"
write_list_to_file(file_path, my_list)
