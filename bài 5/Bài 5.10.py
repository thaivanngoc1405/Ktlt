print("Thai Van Ngoc ")
print("MSSV:235752020710016 ")
print("#####################")
def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                nlist[i], nlist[i+1] = nlist[i+1], nlist[i]
if __name__ == "__main__":
    nlist = input("Nhập danh sách các số cách nhau bằng dấu phẩy: ").split(',')
    nlist = [int(x) for x in nlist]
    bubbleSort(nlist)
    print("Danh sách sau khi sắp xếp:", nlist)
