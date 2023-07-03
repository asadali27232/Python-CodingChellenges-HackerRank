if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        input_string = input()
        input_string = input_string.split(' ')
        
        name = input_string[0]
        scores = list(map(float, input_string[1:]))
        
        student_marks[name] = scores
        
    query_name = input()
    query_marks = student_marks[query_name]
    
    sum_marks = 0
    for marks in query_marks:
        sum_marks += marks
    
    print("{:.2f}".format(sum_marks/len(query_marks)))