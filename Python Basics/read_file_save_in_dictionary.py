def read_grades(gradefile):
    '''(file open for reading) -> dict of {float: list of str}

    Read the grades from gradefile and return a dictionary where
    each grade is a key and each value is the list of ids of students
    who earned that grade.

    Precondition: gradefile starts with a header that contatins
    no blank linse, then has blank line, and then lines
    containing a student number and a grade.
    '''

    # Skip over the header.
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()

    # Read the grades, accumulating them into a dict.

    grade_to_ids = {}
    line = gradefile.readline()

    while line != '':
        student_id = line[:4]
        grade = line[4:].strip()

        if grade not in grade_to_ids:
            grade_to_ids[grade] = [student_id]
        else:
            grade_to_ids[grade].append(student_id)

        line = gradefile.readline()

    return grade_to_ids


# File sample
* Assignment 1 grades
* Columns:
* id grade

0052  77.5
0072  37.5
0144  62.5
0162  72.5
0173  72.5
0190  55.0
.................
..................
..................
....................

