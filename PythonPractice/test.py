#practice work quiz

#setting counter to count correct answers
count = 0

#introductory message
print('''
Welcome to my first Gemini quiz!

I will ask five questions to start,
and I'll give you a score at the end.

''')

#first question input/output
print("Q1: How many refined markets are there?")
q1 = input()
if q1 == "12" or q1.lower() == "twelve":
    print("Correct! There are 12 refined markets.")
    count += 1
else:
    print("Incorrect, there are 12 refined markets.")
print()

#second question input/output
print("Q2: How many gallons is the average ULSD load?")

q2 = input()
if q2 == "7800":
    print("Correct! ULSD loads are approx. 7800 gallons.")
    count += 1
else:
    print("Incorrect, ULSD loads are approx. 7800 gallons.")
print()

#third question input/output
print("Q3: What does DEF stand for?")

q3 = input()
if q3.lower() == "diesel exhaust fluid":
    print("Correct!  Great job.")
    count += 1
else:
    print("Incorrect, DEF stands for diesel exhaust fluid.")
print()

#fourth question input/output
print("How many gallons is the average Unleaded load?")

q4 = input()
if q4 == "8800":
    print("Yes, Unleaded loads usually run around 8800 gallons!")
    count += 1
else:
    print("Incorrect, unleaded loads are approx. 8800 gallons.")
print()

#fifth question input/output
print("Q5: What is the Gemini Logistics phone number?")

q5 = input()
if q5 == "1-888-439-5087" or q5 == "1.888.439.5087" or q5 == "888-439-5087" or q5 == "888.439.5087" or q5 == "18884395087" or q5 == "8884395087":
    print("Correct, the number is 1-888-439-5087.")
    count += 1
else:
    print("Incorrect, the number is 1-888-439-5087")
print()

#score calculation
score = int((count / 5) * 100)

if score >= 80:
    print("Nice job, you scored", score)
elif score >=60:
    print("Good try, you scored", score)
else:
    print("Keep studying, you'll get it down.  You scored", score)
