class Person:
    name: str
    age: int
    gender: str
    phone: str
    email: str

    def __init__(self, name, age, gender, phone, email) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.email = email

    def setName(self, name: str) -> None:
        self.name = name

    def setAge(self, age: int) -> None:
        self.age = age

    def setGender(self, gender: str) -> None:
        self.gender = gender

    def setPhone(self, phone: str) -> None:
        self.phone = phone

    def setEmail(self, email: str) -> None:
        self.email = email

    def getName(self) -> str:
        return self.name

    def getGender(self) -> str:
        return self.gender

    def getPhone(self) -> str:
        return self.phone

    def getEmail(self) -> str:
        return self.email

    def outputPerson(self) -> str:
        result = "Ho ten: " + self.name + "Gioi tinh: " + self.gender + "; sdt: " + self.phone + "; email: " + self.email
        return result

class Hoc_phan:
    tenhocphan: str
    sotinchi: int

    def __init__(self, tenhocphan: str, sotinchi: int) -> None:
        super().__init__()
        self.tenhocphan = tenhocphan
        self.sotinchi = sotinchi

    def setTenhocphan(self, name) -> None:
        self.tenhocphan = name

    def setSotinchi(self, credit) -> None:
        self.sotinchi = credit

    def getTenhocphan(self) -> str:
        return self.tenhocphan

    def getSotinchi(self) -> int:
        return self.sotinchi

    def outputHocphan(self) -> str:
        result = "Ten hoc phan: " + self.tenhocphan + "; so tin chi: " + str(self.sotinchi)
        return result

class Student(Person):
    stuID: str
    dshp: list[Hoc_phan]

    def __init__(self, name: str, phone: str, email: str, studentID: str, gpa: float) -> None:
        Person.__init__(self, name, phone, email)
        self.studentID = studentID
        self.gpa = gpa
        self.dshp = []



    def setStudentID(self, id: str) ->None:
        self.studentID = id

    def setGPA(self, gpa: float) -> None:
        self.gpa = gpa

    def setDSHP(self, dshp: list[Course]) -> None:
        self.dshp = dshp

    def addCourse(self, hocphan: Course) -> None:
        self.dshp.append(hocphan)

    def getStudentID(self) -> str:
        return self.studentID

    def getGPA(self) -> float:
        return self.gpa

    def getDSHP(self) -> list[Course]:
        return self.dshp

    def outputStudentInfo(self) -> str:
        result = self.outputPersonInfo() + "; ma so SV: " + self.studentID + "; DTB: " + str(self.gpa) + "\n"
        for hocphan in self.dshp:
            result += "\t" + hocphan.outputCourseInfo() + "\n"
        return result

print(hello)