# https://www.hackerrank.com/challenges/finding-the-percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    scores = list(student_marks[query_name])
    avg = sum(scores) / len(scores)
    print("%.2f" % avg)
