if __name__ == "__main__":

    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name,scores = line[0],line[1:]
        scores = list(map(float,scores))
        student_marks[name] = scores

name = str(input())
marks = student_marks.get(name)
print("{0:.2f}".format(sum(marks)/(len(marks))))
