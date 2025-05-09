print("Thai Van Ngoc ")
print("MSSV:235752020710016 ")
print("#####################")
import tkinter as tk

def show_choice():
    selected_option = v.get()
    if selected_option == 1:
        result_label.config(text="Bạn đã chọn First")
    elif selected_option == 2:
        result_label.config(text="Bạn đã chọn Second")
    elif selected_option == 3:
        result_label.config(text="Bạn đã chọn Third")
    else:
        result_label.config(text="Bạn chưa chọn")

root = tk.Tk()
root.title("Welcome")

# Tạo biến IntVar để lưu trữ giá trị của radio button
v = tk.IntVar()

# Tạo các radio button
radio_button1 = tk.Radiobutton(root, text="First", variable=v, value=1)
radio_button2 = tk.Radiobutton(root, text="Second", variable=v, value=2)
radio_button3 = tk.Radiobutton(root, text="Third", variable=v, value=3)

# Đặt các radio button lên giao diện theo hướng ngang
radio_button1.pack(side=tk.LEFT)
radio_button2.pack(side=tk.LEFT)
radio_button3.pack(side=tk.LEFT)

# Tạo nút "Click Me" để hiển thị thông tin radio button đang được chọn
click_button = tk.Button(root, text="Click Me", command=show_choice)
click_button.pack(pady=10)

# Nhãn để hiển thị kết quả
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
