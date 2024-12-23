while True:

    midterm_exam = int(input("enter your midterm exam grade :"))
    final_exam = int (input ("enter your final exam grade :"))
    average = ((midterm_exam * 40)/100 + (final_exam * 60)/100)
    if  average >= 50:
        print(average, "SUCCESSFUL")
        break
    else:
        print("FAILED!!")   

