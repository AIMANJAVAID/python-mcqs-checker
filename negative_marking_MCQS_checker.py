from pathlib import Path

key_file = Path(__file__).with_name("negative_answer_key.txt")
marking_file = Path(__file__).with_name("negative_marking.txt")

valid_options = ["a", "b", "c", "d",'..']

while True:
    try:
        if key_file.exists():
            print("\n1. Use saved answer key")
            print("2. Enter new answer key")

            choice = input("Choose (1/2): ").strip()

            if choice == "1":
                saved_key = key_file.read_text()
                answer_key = [
                    ans.strip()
                    for ans in saved_key.lower().split(",")
                ]

            elif choice == "2":
                user_input = input(
                    "Enter new answer key (comma-separated): "
                )
                answer_key = [
                    ans.strip()
                    for ans in user_input.lower().split(",")
                ]

            else:
                raise ValueError("Choose only 1 or 2!")

        else:
            choice = "2"
            user_input = input(
                "Enter answer key (comma-separated): "
            )
            answer_key = [
                ans.strip()
                for ans in user_input.lower().split(",")
            ]

        for ans in answer_key:
            if ans not in valid_options:
                raise ValueError(f"Invalid answer: {ans!r}")

        if choice == "1" and marking_file.exists():
            negative_marking = float(marking_file.read_text())

        else:
            while True:
                try:
                    negative_marking = float(
                        input("Enter negative marks per wrong answer: ")
                    )

                    if not 0 <= negative_marking <= 1:
                        raise ValueError(
                            "Enter a value between 0 and 1!"
                        )

                    break

                except ValueError as error:
                    print("Error:", error)

        if choice == "2":
            key_file.write_text(",".join(answer_key))
            marking_file.write_text(str(negative_marking))
            print("Answer key and marking scheme saved!")

        elif not marking_file.exists():
            marking_file.write_text(str(negative_marking))

        break

    except ValueError as error:
        print("Error:", error)

total_questions = len(answer_key)

while True:
    try:
        student_input = input(
            "\nEnter student answers (comma-separated): "
        )

        student_answers = [
            ans.strip()
            for ans in student_input.lower().split(",")
        ]
        if len(student_answers) != total_questions:
          raise ValueError(
        f"Expected {total_questions} answers, "
        f"but got {len(student_answers)}"
    )

        for ans in student_answers:
           if ans not in valid_options:
              raise ValueError(f"Invalid student answer: {ans!r}")
        

        break

    except ValueError as error:
        print("Error:", error)
correct = 0
wrong = 0
unattempted = 0

for i in range(total_questions):
    if student_answers[i] == "..":
        unattempted += 1

    elif student_answers[i] == answer_key[i]:
        correct += 1

    else:
        wrong += 1

print("\nAnswer key:", answer_key)
print("Total questions:", total_questions)
print("Negative marking per wrong answer:", negative_marking)

print("Correct answers:", correct)
print("Wrong answers:", wrong)
print("Unattempted questions:", unattempted)
total_marks = total_questions


deduction = wrong * negative_marking

calculated_marks = correct - deduction
obtained_marks = max(0, calculated_marks)

percentage = (obtained_marks / total_marks) * 100


print("Total marks:", total_marks)
print("Negative marks deducted:", deduction)
print("Obtained marks:", obtained_marks)
print(f"Percentage: {percentage:.2f}%")
