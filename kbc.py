
count = 0

dict = {
    "Q1. What is the capital of India?": {
        "options": ["A. New Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
        "answer": "a"
    },
    "Q2. Which planet is known as the Red Planet?": {
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "b"
    },
    "Q3. Who is known as the Father of the Nation in India?": {
        "options": ["A. Jawaharlal Nehru", "B. Subhas Chandra Bose",
                    "C. Mahatma Gandhi", "D. Bhagat Singh"],
        "answer": "c"
    },
    "Q4. Which is the largest ocean in the world?": {
        "options": ["A. Atlantic Ocean", "B. Indian Ocean",
                    "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "d"
    },
    "Q5. How many colours are there in a rainbow?": {
        "options": ["A. 7", "B. 5", "C. 6", "D. 8"],
        "answer": "a"
    }
}

for question in dict:
    print(question)

    for option in dict[question]["options"]:
        print(option)

    ans = input("Select option (a/b/c/d): ").lower()

    if ans == dict[question]["answer"]:
        print("Correct answer!")
        count += 100
    else:
        print("Incorrect!")

    print("\n----------------------")

print("Total points:", count, "/ 500")
