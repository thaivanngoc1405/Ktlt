print("Thai Van Ngoc ")
print("MSSV:235752020710016 ")
print("#####################")
def find_longest_words(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            longest_words = []
            max_length = max(len(word) for word in words)
            for word in words:
                if len(word) == max_length:
                    longest_words.append(word)
            return longest_words
    except FileNotFoundError:
        return "File không tồn tại"

file_path = "D:/a.txt"
longest_words = find_longest_words(file_path)
if longest_words:
    print("Những từ dài nhất trong tệp là:", longest_words)
else:
    print("Không tìm thấy từ dài nào trong tệp.")
