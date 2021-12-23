class Person:
    name: str
    age: int
    gender: str
    phone: int
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

    def setPhone(self, phone: int) -> None:
        self.phone = phone

    def setEmail(self, email: str) -> None:
        self.email = email

    def getName(self) -> str:
        return self.name

    def getGender(self) -> str:
        return self.gender

    def getPhone(self) -> int:
        return self.phone

    def getEmail(self) -> str:
        return self.email

    def outputPerson(self) -> str:
        result = "Ho ten: " + self.name + "Gioi tinh: " + self.gender + "; sdt: " + str(self.phone) + "; email: " + self.email
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
    studentID: str
    dshp: list[Hoc_phan]

    def __init__(self, name: str, phone: int, email: str, studentID: str, chuyennganh: str, hanhkiem: str) -> None:
        Person.__init__(self, name, phone, email)
        self.studentID = studentID
        self.chuyennganh = chuyennganh
        self.hanhkiem = hanhkiem
        self.dshp = []


    def setStudentID(self, id: str) ->None:
        self.studentID = id

    def getChuyennganh(self, chuyennganh: str) -> None:
        self.chuyennganh = chuyennganh

    def setDSHP(self, dshp: list[Hoc_phan]) -> None:
        self.dshp = dshp

    def addHocphan(self, hocphan: Hoc_phan) -> None:
        self.dshp.append(hocphan)

    def getStudentID(self) -> str:
        return self.studentID

    def getHanhkiem(self) -> str:
        return self.hanhkiem

    def getDSHP(self) -> list[Hoc_phan]:
        return self.dshp

    def outputStudent(self) -> str:
        result = self.outputPerson() + "; ma so SV: " + self.studentID + "; Chuyen nganh: " + self.chuyennganh + "; Hanh kiem: " + self.hanhkiem + "\n"
        for hocphan in self.dshp:
            result += "\t" + hocphan.outputHocphan() + "\n"
        return result
