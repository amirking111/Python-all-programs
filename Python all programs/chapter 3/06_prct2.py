letter = '''Dear: <|NAME|>
Greetings From Microsoft , I am Happy to tell You about your selection
You are Selected!
Have a great Day!
Thanks and regards,
Amir khan
Date: <|DATE|>
'''

name = input("Enter Your Name\n")
date = input("Enter Date\n")  
lettter = letter.replace("<|NAME|>", name)
letter=letter.replace("<|DATE|>", date)

print(letter)