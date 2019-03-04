# Ques:  Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
# https://www.hackerrank.com/challenges/nested-list/problem

def get_minNames(listMin, nestList ):
    minList = []
    secMin = float('inf')
    for l in nestList:
        if l[1] <= secMin and l[1] != listMin:
            secMin = l[1]

    for l in nestList:
        if l[1] == secMin:
            minList.append(l[0])

    return minList

if __name__ =='__main__':
    nestList = []
    listMin = float('inf')
    for i in range(int(input())):
        name = input()
        score = float(input())
        nestList.append([name, score])
        if score < listMin:
            listMin = score

    minNames = get_minNames(listMin, nestList)
    minNames.sort()
    for i in minNames:
        print(i)
