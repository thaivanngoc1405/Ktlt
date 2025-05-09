print("Thai Van Ngoc ")
print("MSSV:235752020710016 ")
print("#####################")
def generate_pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = [1]  
        if i > 0:
            prev_row = triangle[-1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        triangle.append(row)

    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 3))

n = int(input("Nhập số dòng của Tam Giác Pascal: "))
pascal_triangle = generate_pascal_triangle(n)
print("\nTam Giác Pascal:")
print_pascal_triangle(pascal_triangle)
