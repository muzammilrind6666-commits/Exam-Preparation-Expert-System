
# ==========================================
# EXAM PREPARATION EXPERT SYSTEM
# Artificial Intelligence Project
# ==========================================

print("=" * 45)
print("      EXAM PREPARATION EXPERT SYSTEM")
print("=" * 45)

print("\nPlease enter your preparation details.\n")

name = input("Enter your name: ")
days = int(input("Days remaining until exam: "))
syllabus = float(input("Syllabus completed (0-100%): "))
hours = float(input("Daily study hours: "))
difficulty = input("Subject difficulty (easy/medium/hard): ").lower()
practice = int(input("Practice questions solved: "))

print("\n" + "=" * 45)
print("          EXPERT SYSTEM REPORT")
print("=" * 45)

print("Student Name:", name)

# Validate the input
if (days < 0 or not 0 <= syllabus <= 100
        or hours < 0 or practice < 0
        or difficulty not in ["easy", "medium", "hard"]):
    print("Invalid input! Please enter correct values.")

else:
    # Knowledge Base and Inference Engine

    print("\nPreparation Analysis:")

    # Rule 1: Preparation level
    if syllabus >= 80 and practice >= 20:
        level = "Well Prepared"
    elif syllabus >= 50:
        level = "Moderately Prepared"
    else:
        level = "Needs More Preparation"

    print("Preparation Level:", level)

    # Rule 2: Time management
    if days <= 2:
        print("Priority: Focus on revision and key topics.")
    elif days <= 7:
        print("Priority: Complete important topics and practice.")
    else:
        print("Priority: Follow a balanced study timetable.")

    # Rule 3: Syllabus advice
    if syllabus < 40:
        print("Advice: Cover essential topics first.")
    elif syllabus < 80:
        print("Advice: Finish the remaining syllabus.")
    else:
        print("Advice: Revise completed topics.")

    # Rule 4: Study hours
    if hours < 2:
        print("Study Advice: Increase focused study time.")
    elif hours <= 5:
        print("Study Advice: Maintain your study routine.")
    else:
        print("Study Advice: Take regular breaks to avoid fatigue.")

    # Rule 5: Subject difficulty
    if difficulty == "hard":
        print("Subject Advice: Break difficult topics into small parts.")
    elif difficulty == "medium":
        print("Subject Advice: Revise concepts and solve examples.")
    else:
        print("Subject Advice: Practice questions to strengthen basics.")

    # Rule 6: Practice questions
    if practice < 10:
        print("Practice Advice: Solve more questions and past papers.")
    else:
        print("Practice Advice: Review mistakes and practice mock tests.")

    # Final reminder
    print("\nFinal Recommendation:")
    if days <= 2 and syllabus < 50:
        print("Focus on the most important topics and stay calm.")
    elif syllabus >= 80 and practice >= 20:
        print("You have a good preparation base. Keep revising!")
    else:
        print("Follow a daily plan and track your progress.")

print("\n" + "=" * 45)
print("       Thank you for using the system!")
print("=" * 45)
