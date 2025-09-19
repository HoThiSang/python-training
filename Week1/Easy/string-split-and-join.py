def split_and_join(line):
    words = line.split(" ")
    return "-".join(words)

line = input()
print(split_and_join(line))  