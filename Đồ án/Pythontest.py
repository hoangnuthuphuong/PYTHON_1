class Person:

    def __init__(self, ten: str, mail: str, sdt: str, gioitinh: str):
        super().__init__()
        self.name = ten
        self.mail = mail
        self.phone = sdt
        self.gender = gioitinh


    def setName(self, ten: str):
        self.name = ten

    def setPhone(self, sdt: str):
        self.phone = sdt

    def setEmail(self, email: str):
        self.email = email

    def setGender(self, gioitinh: str):
        self.gender = gioitinh

    def getName(self) -> str:
        return self.name

    def getPhone(self) -> str:
        return self.phone

    def getEmail(self) -> str:
        return self.email

    def getGender(self) -> str:
        return self.gender

    def outputPerson(self) -> str:
        result = "Ten: " + self.name + "; Gioi tinh: " + self.gender + "; Dia chi mail: " + self.mail + "; So dien thoai: " + self.phone
        return result


class KetQuaHocTap:

    def __init__(self, diem_qua_trinh: float, diem_kiem_tra: float, diem_thi: float, tb: float, xep_loai: str):
        self.point_process = diem_qua_trinh
        self.test_point = diem_kiem_tra
        self.test_score = diem_thi
        self.gpa = tb
        self.classification = xep_loai

    #setter
    def setPointProcess(self, diem_qua_trinh: float):
        self.point_process = diem_qua_trinh

    def setTestPoint(self, diem_kiem_tra: float):
        self.test_point = diem_kiem_tra

    def setTestScore(self, diem_thi: float):
        self.test_score = diem_thi

    def setGPA(self, tb: float):
        self.gpa = tb

    def setClassification(self, xep_loai: str):
        self.classification = xep_loai

    def getPointProcess(self) -> float:
        return self.point_process

    def getTestPoint(self) -> float:
        return self.test_point

    def getTestScore(self) -> float:
        return self.test_score

    def getGPA(self) -> float:
        return self.gpa

    def getClassification(self) -> str:
        return self.classification

    def outputKetQua(self) -> str:
        result = "Diem qua trinh: " + str(self.point_process) + "; Diem kiem tra: " + str(
            self.test_point) + "; Diem thi: " + str(self.test_score) + "; Diem trung binh: " + str(self.gpa) + "; Xep loai: " + self.classification + "\n"
        return result


class MonHoc:

    def __init__(self, ma_mon_hoc: str, ten_mon_hoc: str, tin_chi: int, thanh_tien: float, diem_qua_trinh: float, diem_kiem_tra: float, diem_thi: float, tb: float, xep_loai: str):
        self.ma_mon_hoc = ma_mon_hoc
        self.ten_mon_hoc = ten_mon_hoc
        self.credits = tin_chi
        self.moneys = thanh_tien
        # self.score = obj KetQuaHocTap self.score.
        # self.score = ketqua (ketqua = 1 doi tuong) ketqua.point_process ketqua.test_point
        self.score = KetQuaHocTap(diem_qua_trinh, diem_kiem_tra, diem_thi, tb, xep_loai)

    def setSubjectCode(self, ma_mon_hoc: str):
        self.subject_code = ma_mon_hoc

    def setSubjectName(self, ten_mon_hoc: str):
        self.subject_name = ten_mon_hoc

    def setCredits(self, tin_chi: int):
        self.credits = tin_chi

    def setMoney(self, thanh_tien: float):
        self.moneys = thanh_tien

    def setScore(self, diem: KetQuaHocTap):
        self.score = diem

    def getSubjectCode(self) -> str:
        return self.subject_code

    def getSubjectName(self) -> str:
        return self.subject_name

    def getCredits(self) -> int:
        return self.credits

    def getMoney(self) -> float:
        return self.moneys

    def getScore(self) -> KetQuaHocTap:
        return self.score

    def outputTTMonHoc(self) -> str:
        result = "\nMa mon hoc: " + self.ma_mon_hoc + "; Ten mon hoc: " + self.ten_mon_hoc + "; So tin chi: " + str(self.credits) + "; Thanh tien: " + str(
            self.moneys) + "\n"
        result += self.score.outputKetQua()
        return result


class Student(Person):

    def __init__(self, ten: str, mail: str, sdt: str, gioitinh: str, mssv: str, monhoc: MonHoc):
        Person.__init__(self, ten, mail, sdt, gioitinh)
        self.student_code = mssv
        self.subject = monhoc  # monhoc = MonHoc()

    def setstudent_code(self, mssv: str):
        self.student_code = mssv

    def setSubject(self, monhoc: MonHoc):
        self.subject = monhoc

    def getStudentCode(self) -> str:
        return self.student_code

    def getSubject(self):
        return self.subject

    def outputTTStudent(self) -> str:
        result = self.outputPerson() + "; Ma so SV: " + self.student_code + "Mon hoc: " + self.subject.outputTTMonHoc()
        return result


class Lecturer(Person):

    def __init__(self, ten: str, mail: str, sdt: str, gioitinh: str, msgv: str, luong: float, monhoc: MonHoc):
        Person.__init__(self, ten, mail, sdt, gioitinh)
        self.lecture_code = msgv
        self.salary = luong
        self.subject = monhoc

    def setLectureCode(self, msgv: str):
        self.lecture_code = msgv

    def setSalary(self, luong: float):
        self.salary = luong

    def setSubject(self, monhoc: MonHoc):
        self.subject = monhoc

    def getLectureCode(self):
        return self.lecture_code

    def getSalary(self) -> float:
        return self.salary

    def getSubject(self) -> MonHoc:
        return self.subject

    def outputTTLecturer(self) -> str:
        result = self.outputPerson() + "; Ma so GV: " + self.lecture_code + "; Luong: " + str(self.salary) + "Mon hoc: " + self.subject.outputTTMonHoc()
        return result