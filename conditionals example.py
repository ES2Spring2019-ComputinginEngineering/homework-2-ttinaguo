def getGrade(score):
    if (score >= 90):
        grade = "A"
    elif (score >= 80):
        grade = "B"
    elif (score >= 70):
        grade = "C"
    elif (score >= 60):
        grade = "D"
    else:
        grade = "F"
    return grade

print("103 -->", getGrade(103))
print(" 88 -->", getGrade(88))
print(" 70 -->", getGrade(70))
print(" 88 -->", getGrade(61))