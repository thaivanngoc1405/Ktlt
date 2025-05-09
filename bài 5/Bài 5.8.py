print("Thai Van Ngoc ")
print("MSSV: 235752020710016")
print("#####################")
def Sequential_Search(dlist, item):
    pos = 0
    found = False
    
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos += 1
    
    return found

if __name__ == "__main__":
    n = int(input("Nhập số lượng phần tử của danh sách: "))
    dlist = []
    for i in range(n):
        element = input("Nhập phần tử thứ {}:".format(i+1))
        dlist.append(element)
    item = input("Nhập phần tử cần tìm kiếm: ")
    if Sequential_Search(dlist, item):
        print("Phần tử được tìm thấy trong danh sách.")
    else:
        print("Phần tử không được tìm thấy trong danh sách.")
