print("Python Programming Course Marksheet")
marks={"John":86.5,"Jack":91.2,"Jill":84.5,"Harry":72.1,"Joe":80.5}
for k in marks:
    print(("Name of the student is %s and has scored %0.2f marks")%(k,marks[k]))
import operator
sorted_marks = sorted (marks.items(),key=operator.itemgetter(1))
for k in range(0,2):
    print("Highest Marks at",k+1,"position are",sorted_marks[len(marks)-1-k])
sum=0
for k in marks:
    sum=sum+marks[k]
average=sum/len(marks)
print("Average score of the class is",average)
    
