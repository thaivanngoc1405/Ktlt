print("Thai Van Ngoc ")
print("MSSV:235752020710016 ")
print("#####################")
import tkinter as tk

def submit_form():
    # Lấy dữ liệu từ các ô nhập liệu
    name = name_entry.get()
    dob = dob_entry.get()
    mssv = mssv_entry.get()
    major = major_entry.get()
    
    # Hiển thị thông tin đã nhập
    info_label.config(text=f"Thông tin cá nhân:\nHọ tên: {name}\nNgày tháng năm sinh: {dob}\nMSSV: {mssv}\nNgành học: {major}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Form Thông Tin Cá Nhân")

# Tạo các nhãn và ô nhập liệu cho họ tên, ngày tháng năm sinh, MSSV, ngành học
name_label = tk.Label(root, text="Họ và tên:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

dob_label = tk.Label(root, text="Ngày tháng năm sinh:")
dob_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
dob_entry = tk.Entry(root)
dob_entry.grid(row=1, column=1, padx=10, pady=5)

mssv_label = tk.Label(root, text="MSSV:")
mssv_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
mssv_entry = tk.Entry(root)
mssv_entry.grid(row=2, column=1, padx=10, pady=5)

major_label = tk.Label(root, text="Ngành học:")
major_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
major_entry = tk.Entry(root)
major_entry.grid(row=3, column=1, padx=10, pady=5)

# Tạo nút Submit để gửi thông tin
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Nhãn để hiển thị thông tin cá nhân
info_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
info_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Khởi chạy vòng lặp chính của ứng dụng
root.mainloop()
