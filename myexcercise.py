import sys
file=open(sys.argv[1],'r')
information={}
for info in file:
    lst=info.split(":")
    student=lst[0]
    information[student]=(lst[1].split(","))
list=sys.argv[2].split(",")
try:
    for j in sys.argv[2].split(","):
        department=information[j][1]
        university=information[j][0]
        print("name:",j,"university:",university,"department:",department)
except KeyError:
    print("no record exists for",j)
