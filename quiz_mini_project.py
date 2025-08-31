
import random

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [
    Question("What is the largest state in India?\n(a) Mumbai\n(b) Telangana\n(c) Rajasthan\n(d) Andhra Pradesh\n", "c"),
    Question("Which programming language is mostly used in data science?\n(a) Python and R\n(b) Java and C++\n(c) JavaScript and C#\n(d) None of Above\n", "a"),
    Question("Who is the founder of Python?\n(a) Dennis Ritchie\n(b) James Gosling\n(c) Guido van Rossum\n(d) Andres\n", "c"),
    Question("What is the world's largest country?\n(a) India\n(b) China\n(c) Africa\n(d) Russia\n", "d"),
    Question("What is the capital of India?\n(a) Delhi\n(b) Mumbai\n(c) Hyderabad\n(d) Chennai\n", "a"),
]

def run_quiz(questions):
    name = input("Enter your name: ")
    print(f"\nWelcome to the quiz, {name}! 🎉\n")

    score = 0
    random.shuffle(questions)

    for q in questions:
        answer = input(q.prompt).strip().lower()
        if answer == q.answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {q.answer}\n")

    total = len(questions)
    percent = (score / total) * 100

    print(f"🎯 {name}, your final score is {score}/{total}")
    print(f"📊 percentage: {percent:.2f}%")

    if percent >= 50:
        print("🎉 ✅ passed! Well done!")
    else:
        print("😢 ❌ Failed. Keep practicing")

while True:
    run_quiz(questions)
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("👋 Thanks for playing! Goodbye!")
        break
