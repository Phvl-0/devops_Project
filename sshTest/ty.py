class Student:
    def __init__(self, name_param, grade_param):
        self.name = name_param
        
        if 1<= grade_param <=12:
            self.grade = grade_param
        else:
            print(f"Grade:{grade_param} is out of range for (1 - 12), setting to 1 for now.")
            self.grade = 1
        self.grade = grade_param
        self.courses = []
    
    def enroll(self, course_name):
        self.courses.append(course_name)
        print(f"{self.name} has enrolled in {course_name}")

    def get_courses(self):
        return self.courses

    def grade_level_up(self): 
        self.grade += 1
        print(f"Congratulations {self.name}! You are now in grade {self.grade}!")

    def get_info(self):
        
        if not self.courses:
            courses_disp="[Not courses enrolled yet] "
        else:
            courses_disp = f"[{', '.join(self.courses)}]"
        info_str = f"Name: {self.name}\nGrade:{self.grade}\nCourses: {courses_disp}"
        return info_str    
        
print("===============Creating Students=======================")
studA = Student("Gwen Stacy", 6)
studB = Student("Miles Morales", 5)
studC = Student("Milla Gates", 7)

print("\n========Enrollin Students in Courses==================")
studA.enroll("English")
studA.enroll("Math")
studA.enroll("History")
studA.enroll("Geography")
studA.enroll("Arts")
studC.enroll("Music")
studC.enroll("Business")
studB.enroll("IT")
studB.enroll("Computer Sci.")
studB.enroll("Medicine")

print("\n=====================Checking Students Courses ==================================")
sA = studA.get_courses()
print(f"Gwen's courses : {sA}")
sB = studB.get_courses()
print(f"Miles's courses: {sB}")
sC = studC.get_courses()
print(f"Milla's courses: {sC}")

print("\n ==================Students Leveling Up===============================================")
studA.grade_level_up()
studB.grade_level_up()


print("\n=====================Getting Full Stud Info================================================")
print("\n"+studA.get_info())
print("\n"+studB.get_info())
print("\n"+studC.get_info())


studD = Student("Kyle Wyatt", 10)
print("\n"+studD.get_info())