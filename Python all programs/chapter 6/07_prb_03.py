coomment = input ("enter the text")


if("make a lot of money"):
    spam =True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("Subscribe" in text):
    spam = True
elif("please" in text):
    spam = True
else:
    spam = False
if(spam):
    print("This is spam")
else:
      print("This is not  spam")