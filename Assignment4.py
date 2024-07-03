def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

str = "Introduction to Python"
char_count = count_characters(str)
print(char_count)
