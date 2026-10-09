def predict_result(internal_marks, attendance):
    if internal_marks >= 40 and attendance >= 75:
        return "PASS"
    return "FAIL"


if __name__ == "__main__":
    marks = 70
    attendance = 85

    result = predict_result(marks, attendance)
    print("Internal Marks:", marks)
    print("Attendance:", attendance)
    print("Predicted Result:", result)
