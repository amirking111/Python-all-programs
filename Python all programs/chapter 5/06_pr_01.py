myDict = {
    "pankha" : "fan" ,
    "dabba"  : "box",
    "vastu"  : "item"
 }
print("options are" , myDict.keys())
a =input("enter the hindi  worrd\n")
# print("the meaning of your word is:" , myDict[a])

# #below line will not throw an error if the key is not present
# in the distionry
print("the meaning of your word is:" , myDict.get(a))
