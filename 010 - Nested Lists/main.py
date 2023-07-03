if __name__ == "__main__":
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    scores_list = [x[1] for x in records]
    
    unique_scores = set(scores_list)
    unique_scores = list(unique_scores)

    unique_scores.sort()
    unique_scores.remove(min(unique_scores))
    
    min_score = min(unique_scores)

    min_students = [x[0] for x in records if x[1] == min_score]
    min_students.sort()
    
    for min_student in min_students:
        print(min_student)
