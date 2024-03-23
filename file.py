"""f=open("D:\\python\\funny.txt","w")
f.write("i love my india")
f.close()
f=open("D:\\python\\funny.txt","a")
f.write("\n i love you")
f.write("\n please marry me")
f.close()


f=open("D:\\python\\funny.txt","r")
print(f.read())
f.close()

f=open("D:\\python\\funny.txt","r")
print(f.read())
f.close()
f= open("D:\\python\\funny.txt","r")
for line in f:
    tokens=line.split(" ")
f_out=open("D:\\python\\funny01.txt","w")        
f_out.write("wordcount:"+str(len(tokens))+line)
f.close()
f_out.close()




def file_read(fname):
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                content_list = f.readlines()
                print(content_list)

file_read("D:\\python\\funny.txt")


with open("D:\\python\\funny01.txt","r") as f:
    content_list=f.readlines()
    print(content_list)


max(words, key=len)
    array=[]
    for line in f:
        array.append(line)
    print(array)


def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    #return [word for word in words if len(word) == max_len]
    return  max(words, key=len)
print(longest_word("D:\\python\\funny.txt"))"""

with open("D:\\python\\funny.txt","r") as f:
    n=0
    for line in f:
        tokens=line.split(" ")
        n+=len(tokens)
print(n)        
        





























