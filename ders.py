days = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]
lessons = ["A", "B", "C", "D", "E", "F", "G"]
teachers = ["X", "Y", "Z"]
schedule = {}
teacher_lessons = {
    "X": ["A", "B"],
    "Y": ["C", "D"],
    "Z": ["F", "G"]
}
for day in days:
    schedule[day] = {}
    lesson_count = 0
    while lesson_count < 3:
        for teacher in teachers:
            for lesson in teacher_lessons[teacher]:
                if lesson_count >= 3:
                    break
                if day in schedule and lesson in schedule[day].values():
                    continue
                if teacher in schedule[day]:
                    continue
                schedule[day][lesson_count] = {
                    "teacher": teacher,
                    "lesson": lesson
                }
                lesson_count += 1
print(schedule)
