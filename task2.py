class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()  # Will store subjects assigned to this teacher


def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)  # Subjects that still need to be assigned
    selected_teachers = []  # Teachers who are part of the schedule

    while remaining_subjects:
        # Find the teacher who can cover the most remaining subjects
        best_teacher = None
        max_coverage = 0

        for teacher in teachers:
            # Skip teachers who are already selected
            if teacher in selected_teachers:
                continue

            # Calculate how many uncovered subjects this teacher can teach
            coverage = len(teacher.can_teach_subjects.intersection(remaining_subjects))

            # Update best teacher if this one covers more subjects or is younger in case of a tie
            if coverage > 0:
                if (
                    best_teacher is None
                    or coverage > max_coverage
                    or (coverage == max_coverage and teacher.age < best_teacher.age)
                ):
                    best_teacher = teacher
                    max_coverage = coverage

        # If no teacher can cover any remaining subjects, return None (impossible to cover all)
        if not best_teacher:
            return None

        # Assign uncovered subjects to this teacher
        assigned_subjects = best_teacher.can_teach_subjects.intersection(
            remaining_subjects
        )
        best_teacher.assigned_subjects = assigned_subjects

        # Remove the newly covered subjects from the remaining set
        remaining_subjects -= assigned_subjects

        # Add the teacher to our schedule
        selected_teachers.append(best_teacher)

    return selected_teachers


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}

    # Створення списку викладачів
    teachers = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
