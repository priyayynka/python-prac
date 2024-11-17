letter = '''Dear, <|NAME|>

Greetings from Priyanka Industries.

We are happy to tell you that, You are selected! We are hoping to see you working with us soon.
Have a cheerful day!

Thank you.

Regards,
Priyanka Shinde
(CEO & director of Priyanka Industries)

Date: <|DATE|>'''

name = input("Enter your name\n")
date = input("Enter today's date\n")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)

print(letter)