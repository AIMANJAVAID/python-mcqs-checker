
from pathlib import Path

key_file = Path(__file__).with_name("answer_key.txt")
valid_options = ["a", "b", "c", "d"]

while True:
    try:
        if key_file.exists():
            print("\n1. Use saved answer key")
            print("2. Update answer key")

            choice = input("Choose option (1/2): ").strip()

            if choice == "1":
                saved_key = key_file.read_text().strip()
                answer_key = [
                    answer.strip()
                    for answer in saved_key.lower().split(",")
                ]

            elif choice == "2":
                user_input = input(
                    "Enter new answer key (comma-separated): "
                )
                answer_key = [
                    answer.strip()
                    for answer in user_input.lower().split(",")
                ]

            else:
                raise ValueError("Choose only 1 or 2!")

        else:
            user_input = input(
                "Enter answer key (comma-separated): "
            )
            answer_key = [
                answer.strip()
                for answer in user_input.lower().split(",")
            ]

        if not answer_key or not any(answer_key):
            raise ValueError("Answer key cannot be empty!")

        for answer in answer_key:
            if answer not in valid_options:
                raise ValueError(f"Invalid answer: {answer!r}")

        if not key_file.exists() or choice == "2":
            key_file.write_text(",".join(answer_key))
            print("Answer key saved successfully!")

        break

    except ValueError as error:
        print("Error:", error)

total_questions = len(answer_key)
print("Total questions:", total_questions)
print("Answer key:", answer_key)


while True:
    try:
        student_input = input("Enter student answers (comma-separated): ")

        if not student_input.strip():
            raise ValueError("Student answers cannot be empty!")

        student_answers = [
            answer.strip()
            for answer in student_input.lower().split(",")
        ]

        if len(student_answers) != total_questions:
            raise ValueError(
                f"Expected {total_questions} answers, "
                f"but received {len(student_answers)}!"
            )

        for answer in student_answers:
            if answer not in valid_options and answer != "..":
                raise ValueError(f"Invalid student answer: {answer!r}")

        break
    except ValueError as error:
        print("Error:", error)

print("Student answers accepted successfully!")
print("Student answers:", student_answers)


correct_answers = []
wrong_answers = []
unattempted_questions = []

for i in range(total_questions):
    if student_answers[i] == "..":
        unattempted_questions.append(i + 1)

    elif student_answers[i] == answer_key[i]:
        correct_answers.append(i + 1)

    else:
        wrong_answers.append(i + 1)

print("Correct question numbers:", correct_answers)
print("Wrong question numbers:", wrong_answers)
print("Unattempted question numbers:", unattempted_questions)

correct_count = len(correct_answers)
wrong_count = len(wrong_answers)
unattempted_count = len(unattempted_questions)

total_marks = correct_count * 1

print("Correct answers:", correct_count)
print("Wrong answers:", wrong_count)
print("Unattempted answers:", unattempted_count)
print("Total marks:", total_marks, "/", total_questions)

percentage = (total_marks / total_questions) * 100
print(f"Student Percentage: {percentage:.2f}%")



        