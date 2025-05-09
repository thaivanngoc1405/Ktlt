print("Thai Van Ngoc")
print("MSSV: 235752020710016")
print("#####################")
def longest_words(sequence):
    words = sequence.split()
    max_length = max(len(word) for word in words)
    longest = [word for word in words if len(word) == max_length]
    return longest

input_sequence = input("Nhập dãy các từ từ bàn phím: ")
longest = longest_words(input_sequence)

print("Từ dài nhất trong dãy là:", longest)
