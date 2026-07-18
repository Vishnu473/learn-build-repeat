from random import randint

def student_marks_Analyzer(student_list:list,pass_score:int,max_score:int):
    print("List: ",student_list)
    print("Number of students: ",len(student_list))
    print("Total marks: ",sum(student_list))
    print("Average: ",sum(student_list)/len(student_list))
    print("Highest mark: ", max(student_list))
    print("Lowest mark: ", min(student_list))
    print("Sorted Ascending: ", sorted(student_list))
    print("Sorted Descending: ", sorted(student_list,reverse=True))

    for index,mark in enumerate(student_list):
        print(f"Student_{index} => {mark}")
    
    print("Everyone Passed: ",all(mark >= pass_score for mark in student_list))
    print(f"Anyone > {max_score*(0.30)}: {any(i>(max_score*0.3) for i in student_list)}")


def userInput_try():
    marks_list = []
    max_score = int(input("Test is for how many marks: "))
    pass_score = int(input("Enter pass score: "))    
    while True:
        marks = input(f'Enter the marks out of {max_score}, press any non-integer to continue.')
        try:
            if int(marks) <= 60:
                marks_list.append(int(marks))
            else:
                raise ValueError(
    f"Marks cannot exceed {max_score}"
)
                break
        except: #used exception to get out of the while loop(Not valid, but used)
            break
        continue
    return marks_list,pass_score,max_score

def userInput_range():
    marks = []
    max_score = int(input("Test is for how many marks: "))
    pass_score = int(input("Enter pass score: "))
    marks_list_len = input("Enter the number of students to enter marks:")
    try:
        if type(int(marks_list_len)).__name__ == 'int':
            for index,_ in enumerate(range(int(marks_list_len))):
                mark = input(f"Enter the student_{index+1} marks: ")
                if int(mark):
                    marks.append(int(mark))
    except:
        print("Exiting as entered non-integer, Try again")
    return marks,pass_score,max_score

if __name__ == "__main__":
    # from two approaches, the program randomly chooses one
    get_input = randint(1,2)
    print(get_input)
    if get_input == 1:
        marks,pass_score, max_score = userInput_try()
        student_marks_Analyzer(marks,pass_score, max_score)
    else:
        marks,pass_score, max_score = userInput_range()
        student_marks_Analyzer(marks,pass_score, max_score)
    