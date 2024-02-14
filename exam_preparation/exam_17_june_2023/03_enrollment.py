def gather_credits(needed_number_of_credits, *args):
    courses = {}
    total_credits = 0
    for course_name, course_credits in args:
        if total_credits >= needed_number_of_credits:
            break

        if course_name not in courses:
            courses[course_name] = int(course_credits)
            total_credits += course_credits

    if total_credits >= needed_number_of_credits:
        return (f"Enrollment finished! Maximum credits: {total_credits}.\n"
                f"Courses: {', '.join(sorted(courses))}")

    return (f"You need to enroll in more courses! You have to gather {needed_number_of_credits - total_credits} credits more.")


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

