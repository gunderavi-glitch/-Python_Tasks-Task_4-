# problem 16 : Nested Lists

# link : https://www.hackerrank.com/challenges/nested-list/problem

# code:

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    unique_scores = sorted(set([student[1] for student in students]))
    second_lowest_score = unique_scores[1]
    
    target_students = [student[0] for student in students if student[1] == second_lowest_score]
    
    for student_name in sorted(target_students):
        print(student_name)
