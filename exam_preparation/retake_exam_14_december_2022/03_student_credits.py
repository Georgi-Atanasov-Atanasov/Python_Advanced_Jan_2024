def students_credits(*args):
    total_credits = 0
    courses = {}
    result = ""
    for data in args:
        course_name, credits, max_test_points, diyan_points = data.split("-")
        achieved_credits = (int(diyan_points) / int(max_test_points)) * int(credits)
        total_credits += achieved_credits
        courses[course_name] = achieved_credits

    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n"
    sorted_dict = dict(sorted(courses.items(), key=lambda x: -x[1]))
    for course_name, credits in sorted_dict.items():
        result += f"{course_name} - {credits:.1f}" + "\n"
    return result


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
