st1=input("Entr the first string")
st2=input("Enter the second string")
if(len(st1)==len(st2)):
    if(sorted(st1)==sorted(st2)):
        print("Anagram")
    else:
        print("Not an anagram")


