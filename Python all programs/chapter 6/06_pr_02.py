sub1 = int(input("enter first subject marks"))
sub2 = int(input("enter second subject marks"))
sub3 = int(input("enter third subject marks"))

if(sub1 <33 or sub2 <33 or sub3<33 ):
    print("You are fail😫")

elif(sub1+sub2+sub3)/3 <40:
    print("YOu are fail due to total percentage is less than 40%")
else:
    print(" YOU are passed 🤩")

