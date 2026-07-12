# The lists must correspond.
Student = ["Amir" ,"Mohammad" ,"Moein" ,"Mobin" ,"Amirhosein" ,"Mina" ,"Narges" ,"Elnaz"]
scores = [2 ,3 ,4 ,5 ,4 ,3 ,7 ,3]

for i in range(len(Student)):
    # It prints the names of the students and their scores in front of them.
    print(Student[i] , scores[i] * "*" , sep= "")
