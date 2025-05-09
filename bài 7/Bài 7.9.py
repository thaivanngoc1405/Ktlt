print("Thai Van Ngoc ")
print("MSSV:235752020710016 ")
print("#####################")
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print("Đã sao chép nội dung từ {} sang {} thành công.".format(source_file, destination_file))
    except FileNotFoundError:
        print("File nguồn không tồn tại.")
    except IOError:
        print("Có lỗi xảy ra khi sao chép nội dung.")
source_file = "D:/a.txt"
destination_file = "D:/b.txt"
copy_file(source_file, destination_file)
