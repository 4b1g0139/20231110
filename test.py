class Student :
    def __init__ (self, id ,name ,major) :
        self._id = id
        self._name = name
        self._major = major
s1 = Student('001','A','PYTHON')
print("學生姓名:",s1._name)
print("學生學號:",s1._id)
print("學生已選課程:",s1._major)
s2 = Student('002','B','PYTHON')
print("學生姓名:",s2._name)
print("學生學號:",s2._id)
print("學生已選課程:",s2._major)
s3 = Student('003','C','PYTHON')
print("學生姓名:",s3._name)
print("學生學號:",s3._id)
print("學生已選課程:",s3._major)
