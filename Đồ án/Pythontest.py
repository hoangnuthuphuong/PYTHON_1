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
    stuID: str
    chuyennganh: str
    hanhkiem: str
    dshp: list[Hoc_phan]

    def __init__(self, name: str, age: int, gender: str, phone: int, email: str, stuID, chuyennganh, hanhkiem ) -> None:
        Person.__init__(self, name, age, gender, phone, email)
        self.stuID = stuID
        self.chuyennganh = chuyennganh
        self.hanhkiem = hanhkiem
        self.dshp = []


    def getDSHP(self) -> list[Hoc_phan]:
        return self.dshp

    def outputStudent(self) -> str:
        result = self.outputPerson() + "; ma so SV: " + self.stuID + "; Chuyen nganh: " + self.chuyennganh + "; Hanh kiem: " + self.hanhkiem + "\n"
        return result


class Lecturer(Person):
    lecID: str
    dshp: list[Hoc_phan]

    def __init__(self, gender: str, name: str, phone: int, email: str, lecID: str, trinhdo: str, luong: str) -> None:
        Person.__init__(self, name, gender, phone, email)
        self.lecID = lecID
        self.trinhdo = trinhdo
        self.luong = luong
        self.dshp = []

    def setLecturerID(self, id: str) ->None:
        self.lecturerID = id

    def getLuong(self, luong: str) -> None:
        self.luong = luong

    def addHocphan(self, hocphan: Hoc_phan) -> None:
        self.dshp.append(hocphan)

    def getLecturerID(self) -> str:
        return self.lecturerID

    def getTrinhdo(self) -> str:
        return self.trinhdo

    def getDSHP(self) -> list[Hoc_phan]:
        return self.dshp

    def outputLecturer(self) -> str:
        result = self.outputPerson() + "; ma so : " + self.lecID + "; Trinh do: " + self.trinhdo + "\n"
        for hocphan in self.dshp:
            result += "\t" + hocphan.outputHocphan() + "\n"
        return result

