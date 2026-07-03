print("=" * 50)
print("      WELCOME TO KBC")
print("=" * 50)

name = input("Enter your name: ")

print(f"\nHello, {name}! Let's start the game.")
print("-" * 50)

# -------------------------------
# Questions
# -------------------------------

questions = [
    {
        "question": "1. What is the capital of India?",
        "options": [
            "A. Delhi",
            "B. Mumbai",
            "C. Kolkata",
            "D. Chennai"
        ],
        "answer": "A"
    },
    {
        "question": "2. Which programming language is most popular for AI?",
        "options": [
            "A. Java",
            "B. Python",
            "C. C",
            "D. HTML"
        ],
        "answer": "B"
    },
    {
        "question": "3. Who developed Python?",
        "options": [
            "A. Dennis Ritchie",
            "B. Elon Musk",
            "C. Guido van Rossum",
            "D. James Gosling"
        ],
        "answer": "C"
    },
    {
        "question": "4. Which planet is known as the Red Planet?",
        "options": [
            "A. Earth",
            "B. Venus",
            "C. Mars",
            "D. Jupiter"
        ],
        "answer": "C"
    },
    {
        "question": "5. How many days are there in a leap year?",
        "options": [
            "A. 364",
            "B. 365",
            "C. 366",
            "D. 367"
        ],
        "answer": "C"
    }
]

# -------------------------------
# Prize Money
# -------------------------------

prize_money = [
    1000,
    5000,
    10000,
    50000,
    100000
]

current_prize = 0

# -------------------------------
# Game Loop
# -------------------------------

for i in range(len(questions)):

    print("\n" + "=" * 50)
    print(f"Question for ₹{prize_money[i]}")
    print("=" * 50)

    print(questions[i]["question"])

    for option in questions[i]["options"]:
        print(option)

    while True:
        answer = input("\nEnter your answer (A/B/C/D): ").upper()

        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid choice! Please enter A, B, C or D.")

    if answer == questions[i]["answer"]:
        current_prize = prize_money[i]
        print("\n✅ Correct Answer!")
        print(f"🎉 Congratulations! You won ₹{current_prize}")
    else:
        print("\n❌ Wrong Answer!")
        print(f"The correct answer was: {questions[i]['answer']}")
        print("\nGAME OVER!")
        break

# -------------------------------
# Final Result
# -------------------------------

print("\n" + "=" * 50)
print("            GAME FINISHED")
print("=" * 50)

print(f"Player Name : {name}")
print(f"Winning Amount : ₹{current_prize}")

if current_prize == prize_money[-1]:
    print("\n🏆 CONGRATULATIONS!")
    print("🎊 You have won the KBC Game!")
else:
    print("\n😊 Thank you for playing!")

print("=" * 50)