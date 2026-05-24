# regular expression

# import re

# count = 0

# pattern = re.compile("function")

# text = """The `print()` function print() function is very useful in Python because the print() function helps programmers display output output clearly on the screen screen while debugging programs."""

# matcher = pattern.finditer(text)

# for i in matcher:
#     count += 1
#     print(i.start(), "...", i.end(), "...", i.group())

# print("The number of occurrence:", count)

# import re

# count = 0

# matcher =re.finditer("Hi","HiHiHiHi")

# for i in matcher:
#     count += 1
#     print(i.start(), "...", i.end(), "...", i.group())

# print("The number of occurrence:", count)


# import re
# obj = input("enter any charecter")
# objmatch=re.finditer(obj,"a7b @k9zz")
# #print(objmatch)
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())


# import re
# a=input("enter string to perform match operation")
# mtch=re.match(a,"python is very important language")
# print(mtch)
# if mtch!=None:
#     print("match founf at begining level")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("there is no matching at beging level")


# import re
# a=input("enter string to perform match operation:")
# mtch=re.fullmatch(a,"pythonisvery ")
# print(mtch)
# if mtch!=None:
#     print("match found")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("Full match not found")

# write program to check wherther the given mail valid gmail or not

# import re
# s=input("Enter Mail id:")
# m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
# if m!=None:
#     print("Valid E-mail ID")
# else:
#     print("Invalid E-Mail id")

# import re
# mo=input("Enter Mobile id:")
# obj=re.fullmatch("[0-5]\d{9}",mo)
# if obj!=None:
#     print("Valid Mobile No")
# else:
#     print("Invalid Mobile No")

# import re

# mo = input("Enter Mobile No: ")

# obj = re.fullmatch("[6-9]\d{9}", mo)

# if obj != None:
#     print("Valid Mobile Number")


# else:#search() function
# import re
# a=input("Enter string to perform matvh operation:")
# mtch=re.search(a,"python sss dynamic lann")
# print(mtch)
# if mtch!=None:
#     print(mtch.start()," ",mtch.end()," ",mtch.group())
# else:
#     print("there is no matching anywhere")


#findall() function
# import re
# mtch = re.findall('[0-9a-z]',"abch3hdk5bhk7zQ$&*")
# print(mtch)
                           
# import re
# mtch = re.findall('[A-Z]',"abch3hdk5bhk7zQ$&*")
# print(mtch)

#sub()mfunction
# import re
# obj=re.sub('[a-zA-Z]',' ','2345  ABCD habf deff')
# print(obj)

# import re
# obj=re.sub('[a-z]',' ','2345  ABCD habf deff')
# print(obj)

# import re
# obj=re.subn('[0-7]','@','ab3gd6nk17')
# print(obj)
# print("the string is=",obj[0])
# print("the number of replacement is=",obj[1])


import re

f1 = open(r"C:\Dsa\datafile.txt", "r")
f2 = open(r"C:\Dsa\output.txt", "w")

a = input("Enter string to perform match operation: ")

data = f1.read()

objmatch = re.finditer(a, data)

for match in objmatch:
    result = f"{match.start()} ... {match.end()} ... {match.group()}"

    print(result)
    f2.write(result + "\n")

f1.close()
f2.close()