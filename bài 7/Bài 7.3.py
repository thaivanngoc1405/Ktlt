print("Thai Van Ngoc ")
print("MSSV: 235752020710016")
print("#####################")
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("Nội dung của tệp là:")
            print(content)
    except FileNotFoundError:
        print(f"Tệp '{file_path}' không tồn tại.")
    except IOError:
        print(f"Không thể đọc tệp '{file_path}'.")
file_path = r'D:\a.txt'
read_file(file_path)

