institute="ABC Training Institue"
java_course={"John","Jack","Jill","Joe"}
python_course={"Jake","John","Eric","Jill"}
print("Number of students enrolled in python course are",len(python_course))
print("Number of students enrolled in Java course only are",len(java_course-python_course))
print("Number of students enrolled in Python course only are",len(python_course-java_course))
print("Number of students enrolled in both Java and Python course are",len(java_course&python_course))
print("Number of students enrolled in either Java or Python but not in both course are",len((python_course|java_course)-python_course&java_course))
print("Number of students enrolled in either Java or Python courses are",len(python_course&java_course))
