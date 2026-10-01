#text inspector 📈

info=input("enter your password: ")

cha=len(info)
low=info.strip().lower()
acount=info.count('a')
numcount=sum(c.isdigit() for c in info)
morp=info.replace(" ","-")

print("text analysis report: ")

print(f''' length of password is, '{cha}'
in lowercase password is, '{low}'
"a" letter count is, '{acount}'
morphed password is, '{morp}'
number count is, '{numcount}' ''')
print("-----------------end of analysis 👩🏻‍💻 -----------------------------")
