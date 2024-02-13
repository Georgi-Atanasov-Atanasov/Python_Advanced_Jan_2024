def softuni_students(*args, **kwargs):
    valid_students = {}
    invalid_students = []
    for course_id, username in args:
        if course_id in kwargs:
            valid_students[username] = kwargs[course_id]
        else:
            invalid_students.append(username)

    result = ""
    if valid_students:
        for student_name, course_name in sorted(valid_students.items()):
            result += f"*** A student with the username {student_name} has successfully finished the course {course_name}!\n"
    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"
    return result

print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))


