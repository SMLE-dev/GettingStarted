
print("Welcome to quiz app...")

score = 0
total = 0
questions = 5

while True:
    if str(input("What's the meaning of CPU? ")).lower()== "central processing unit":
        print("Correct!")
        score += 1
        print(score)
    else:
        print("Incorrect!")
    if str(input("What's the meaning of RAM? ")).lower() =="random access memory":
        print("Correct!")
        score += 1
        print(score)
    else:
        print("Incorrect!")
    if str(input("What's the capital of Kenya? ")).capitalize() =="Nairobi":
        print("Correct!")
        score += 1
        print(score)
    else:
        print("Incorrect!")
    if str(input("What's the capital of Nigeria? ")).capitalize() =="Lagos":
        print("Correct!")
        score += 1
        print(score)
    else:
        print("Incorrect!")
    if str(input("Who's the founder of Amazon? ")).strip().lower() =="jeff bezos":
        print("Correct!")
        score += 1
        print(score)
    else:
        print("Incorrect!")

        total = score * 100 / 5
        print(f"You managed to get {total}% correct")

    if input("Would you like to retake questions?(y / n) ") == "n":
        break
    else:
        continue