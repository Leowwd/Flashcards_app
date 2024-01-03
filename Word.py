import json
import random

flashcards = []

def load_flashcards():
    global flashcards
    try:
        with open('flashcards.json', 'r') as file:
            flashcards = json.load(file)
    except FileNotFoundError:
        flashcards = []

def save_flashcards():
    with open('flashcards.json', 'w') as file:
        json.dump(flashcards, file)

def add_flashcard():
    question = input("Enter the vocabulary: ")
    if {"question": question} not in flashcards and question.isalpha():
        flashcards.append({"question": question})
        print("Flashcard added successfully!\n")
    else:
        print("repetition\n")

def view_flashcards():
    if not flashcards:
        print("No flashcards available.")
    else:
        for idx, card in enumerate(flashcards, start=1):
            print(f"Card {idx}:")
            print("Question:", card['question'])
            print()

def sample():
    if not flashcards:
        print("No flashcards available for the quiz.")
        return

    num_questions = int(input("Enter the number of questions for the quiz: "))
    if num_questions <= 0 or num_questions > len(flashcards):
        print("Invalid number of questions.")
        return

    quiz_flashcards = random.sample(flashcards, num_questions)

    for idx, card in enumerate(quiz_flashcards, start=1):
        print(f"{idx}. {card['question']}", end=" ")
    print()

def main():
    load_flashcards()
    while True:
        print("Menu:")
        print("1. Add Flashcard")
        print("2. View Flashcards")
        print("3. Ramdom Samples")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_flashcard()
        elif choice == '2':
            view_flashcards()
        elif choice == '3':
            sample()
        elif choice == '4':
            save_flashcards()
            print("Flashcards saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    