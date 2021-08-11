text ="Click Open link on the dialog shown by your browser"
#print(text)
browser=text[44:51]
#nbrowser=text[-7:0]
#print(nbrowser)
print(browser)
link=text[11:15]
print(link)
print("Converting all string to uppercase")
upper=text.upper()
print(upper)
print("Converting all string to lowercase")
print(upper.lower())
print("converting Click to upper")
remain=text[5:]

click=text[0:5]
uclick=click.upper()

aa= uclick + remain
print(aa)


print ("open and browser in upper case")
open=text[6:10]
f1=text[0:5]
f2=text[11:43]
uopen=open.upper()
ubrowser=browser.upper()
#print(ubrowser)
#print(uopen)

newt = f1 + uopen + f2 + ubrowser
print(newt)

print ("reverse")
print(text[::-1])



print("numbers only")  


num="1,2,3,4,5,6,7,8,9"
newnum =num.replace(',',"")
print(newnum)

#e







#print("addition")
a = newnum[0]
b= newnum[4]
ia=int(a)
ib=int(b)
add = ia+ib
print(add)

#print ("mult")
o=newnum[1]
p=newnum[7]
io=int(o)
ip=int(p)
mult = io*ip
print(mult)

print("new")
print(text[15:5:-1])




