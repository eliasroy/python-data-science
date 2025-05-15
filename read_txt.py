#read file
with open('cuento.txt','r')as file:
    for lines in file:
        print(lines.strip())

#read all lines on the list
"""with open('cuento.txt','r') as file:
    lines=file.readlines()
    print(lines)"""

#add line to end
"""with open('cuento.txt','a') as file:
    file.write("\n by elias pro")"""

#rewrite to file

"""with open('cuento.txt','w') as file:
    file.write("HELLO WORLD")"""

