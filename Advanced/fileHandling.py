file = open("./my/data.txt", "r")
content = file.read()
print(content)
file.close()


print("________________________________")

file = open("./my/data.txt", "r")
for line in file:
    print(line)
file.close()

file = open("./my/data.txt", "a")
file.write("New Line Added\n")
file.close()








