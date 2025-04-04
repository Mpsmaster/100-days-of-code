# absolute path
with open(r"C:\Users\Marco\Desktop\data.txt", "w") as file:
    file.write("Hello, world!\n")
# relative path
with open("../../../data.txt", "r") as file:
    content = file.read()
    print(content)    
