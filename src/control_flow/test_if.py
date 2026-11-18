"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    elif number % 2 == 0:
        conclusion = 'Number is even'
    elif number < 10:
        conclusion = 'Number is a single digit'
    else:
        conclusion = 'Number bigger than or equal to one'    
    

    assert conclusion == 'Number bigger than or equal to one'


def test_nested_if_statement():
    """Test nested conditional statements"""
    age = 20
    has_license = True
    status = "Ineligible"

    if age >= 18:
        if has_license:
            status = "Eligible to drive"
        else:
            status = "Needs a license"
    else:
        status = "Underage"

    assert status == "Eligible to drive"


def test_multiple_elif_branches():
    """Test conditional statement with multiple elif branches"""
    scores = [95, 85, 72, 65, 40]
    grades = []

    for score in scores:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades.append(grade)

    assert grades == ["A", "B", "C", "D", "F"]