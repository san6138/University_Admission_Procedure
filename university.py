from functools import partial
maxstud = int(input())
file = open('applicants.txt', 'r')
students = file.read().split('\n')
file.close()
def sorti(x,a,b):
    num = -((float(x.split()[a]) + float(x.split()[b]))/2)
    num1 = -float(x.split()[6])
    return (num, x.split(" ", 1)[0]) if num < num1 else (num1, x.split(" ", 1)[0])
def sortin(x, a):
    num = -float(x.split()[a])
    num1 = -float(x.split()[6])
    return (num,  x.split(" ", 1)[0]) if num < num1 else (num1, x.split(" ", 1)[0])
phy = sorted(students, key=partial(sorti, a=2, b=4))
chem = sorted(students, key=partial(sortin, a=3))
math = sorted(students, key=partial(sortin, a=4))
comp = sorted(students, key=partial(sorti, a=5, b=4))
chem1 = sorted(students, key=partial(sorti, a=2, b=3))
phylist = []
mathlist = []
biolist = []
chelist = []
englist = []
file.close()

list = [math, phy, chem, comp, chem1]
list1 = ['Mathematics', 'Physics', 'Chemistry', 'Engineering', 'Biotech']
list2 = [mathlist, phylist, chelist, englist, biolist]
list3 = [4,2,3,5,3]
def mathpriorities(n):
    for i,k,h,l in zip(list,list1, list2, list3):
        for student in i:
            studetails = student.split()
            if studetails[n] == k and len(h) < maxstud and (student in students):
                if i in (chem, math):
                    h.append(' '.join([studetails[0], studetails[1], str(-sortin(student, l)[0])]))
                if i == phy:
                    h.append(' '.join([studetails[0], studetails[1], str(-sorti(student, 2, 4)[0])]))
                if i == chem1:
                    h.append(' '.join([studetails[0], studetails[1], str(-sorti(student, 2, 3)[0])]))
                if i == comp:
                    h.append(' '.join([studetails[0], studetails[1], str(-sorti(student, 5, 4)[0])]))
                students.remove(student)


for p in range(7, 10):
    mathpriorities(p)

for i in (mathlist, biolist, englist, chelist, phylist):
     i.sort(key=lambda x: (-float(x.split()[2]), x.split()[0]))
for i, k in zip(list1, [mathlist, phylist, chelist, englist, biolist]):
#['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
    file = open(i +'.txt', 'w')
    for j in k:
        file.write(j + '\n')
    file.close()

print("Biotech")
print(*biolist, sep='\n')
print("\nchemistry")
print(*chelist, sep='\n')
print("\nEngineering")
print(*englist, sep='\n')
print("\nMathematics")
print(*mathlist, sep='\n')
print("\nPhysics")
print(*phylist, sep='\n')




