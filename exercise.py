class Course :
    def __init__ (self, id, name, credit, teacher, time, elective) :
        self.id = id
        self.name = name
        self.credit = credit
        self.teacher = teacher
        self.time = time
        self.elective = elective


c1 = Course('A1','English','3','John','7:00-9:00','選修')
print("課程代碼:",c1.id)
print("課程名稱:",c1.name)
print("學分數:",c1.credit)
print("任課老師:",c1.teacher)
print("上課時間:",c1.time)
print("必選修:",c1.elective)
