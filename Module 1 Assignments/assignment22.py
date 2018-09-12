name="John"
institute="ABC Training Institute"
courses=("Python Programming","RDBMS","Web Technology","Software Engg.")
electives=("Business Intelligence","Big Data Analytics")
print(("Number of courses opted by %s are %d ")%(name,len(courses)))
print(("Courses opted by %s are")%(name))
for i in range(0,4):
    print(courses[i],end=" ")
'''courses.insert(5,electives[0])
courses.insert(6,electives[1])'''
print("")

'''Are you kidding me!!!! Tuples are immutable! First typecast as list change and then remake as tuple'''

courses=list(courses)
courses.append(electives[0])
courses.append(electives[1])
courses=tuple(courses)

print("Added elective with complete list are now shown")
for i in range(0,6):
    print(courses[i],end=" ")
