print(" Thai Van Ngoc")
print("MSSV:235752020710016 ")
print("#####################")
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def get_String(self):
        self.input_string = input("Nhập chuỗi: ")

    def print_String(self):
        print("Chuỗi in hoa là:", self.input_string.upper())
manipulator = StringManipulator()
manipulator.get_String()
manipulator.print_String()
