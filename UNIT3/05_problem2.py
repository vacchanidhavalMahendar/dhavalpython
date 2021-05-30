letter = '''Dear <|NAME|>,
you are selected!

Date:<|DATE|>
'''
name = input("Enter your Name\n")
date = input("Enter your Name\n")
letter= letter.replace("<|NAME|>",name)
letter =letter.replace("<|DATE|>",date)
print(letter)
