#text inspector 📈

info=input("enter your sentence: ")

cha=len(info)
low=info.strip().lower()
acount=info.count('a')
numcount=sum(c.isdigit() for c in info)
morp=info.replace(" ","-")

print("text analysis report: ")

print(f''' length of sentence is, '{cha}'
lowercase sentence is, '{low}'
"a" letter count is, '{acount}'
morphed sentence is, '{morp}'
number count is, '{numcount}' ''')
print("-----------------end of analysis 👩🏻‍💻 -----------------------------")
