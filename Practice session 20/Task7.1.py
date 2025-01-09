file=open(r"C:\Users\divya aghi\PycharmProjects\Python_SDET\Practice session 20\input.txt","r")
content=file.read()
lines=content.count("\n")+1
words=len(content.split())
count=0
print(lines)
print(words)
for i in content:
    if i.isalpha():
        count+=1
print("No of characters are:",count)

