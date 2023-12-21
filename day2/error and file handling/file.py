with open('newfile.txt', mode = 'w') as file: #CREATE
    file.write("NEW FILE")

with open('newfile.txt', mode = 'a') as file: #ADD
    file.writelines(["\nline 2", "\nline 3"])

with open('newfile.txt', mode = 'r') as file: #READ
    print(file.read(3))

with open('newfile.txt', mode = 'r') as file: #READ
    lines = file.readlines()
    for line in lines:
        print(line)