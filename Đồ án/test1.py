import pickle
from Pythontest import Person, KetQuaHocTap, MonHoc, Student, Lecturer


class QuanLySinhVien:

    def __init__(self) -> None:
        super().__init__()
        self.student_list = []

    def inputStudent(self, sv: Student) -> None:
        self.student_list.append(sv)

    def getSLStudent(self) -> int:
        return self.student_list.__len__()

    def getDSSV(self) -> list:
        return self.student_list

    # Ham sap xep sinh vien theo thu tu tang dan cua ten
    def SapxepSVTheoTen(self):
        for i in range(len(self.student_list)):
            for j in range(i + 1, len(self.student_list)):  # [i+1, len)
                if (self.student_list[i].name < self.student_list[j].name):
                    self.student_list[i], self.student_list[j] = self.student_list[j], self.student_list[i]
        return self.student_list

    # Ham tim kiem sinh vien theo MSSV
    def TimKiemSVTheoMS(self, mssv):
        if (self.getSLStudent() > 0):
            for sv in self.student_list:
                if (sv.student_code == mssv):
                    return sv

    # Ham xoa sinh vien theo MMSV
    def XoaSVTheoMS(self, mssv):
        sv = self.TimKiemSVTheoMS(mssv)
        if (sv != None):
            self.student_list.remove(sv)
            return True
        else:
            return False

    # Ham xuat sinh vien ra console
    def XuatSV(self, dssv):
        for sv in dssv:
            print(sv.outputTTStudent())

    def InVaoFileSV(self, dssv):
        with open("Student.txt", "wb+") as f:
            for i in dssv:
                pickle.dump(i.outputTTStudent(), f)

    def DocFile(self,tenfile, x, name):
        with  open(tenfile, "rb+") as sf:
            for i in range(x):
                print(name, "thu", i + 1, ":")
                print(pickle.load(sf))

class QuanLyMonHoc:
    def __init__(self) -> None:
        super().__init__()
        self.subject_list = []
        self.score_list = []

    # Ham tinh diem trung binh cho sinh vien
    def tinhDTB(self, mh:MonHoc):
        gpa = (mh.score.point_process + mh.score.test_point + mh.score.test_score) / 3
        mh.score.gpa = round(gpa, 3)

    # Ham xep loai hoc luc cho sinh vien
    def XepLoaiHocLuc(self, mh:MonHoc):
        if (mh.score.gpa >= 8.5):
            mh.score.classification = "A"
        elif (mh.score.gpa >= 8):
            mh.score.classification = "B+"
        elif (mh.score.gpa >= 7):
            mh.score.classification = "B"
        elif (mh.score.gpa >= 6.5):
            mh.score.classification = "C+"
        elif (mh.score.gpa >= 5.5):
            mh.score.classification = "C"
        elif (mh.score.gpa >= 5):
            mh.score.classification = "D+"
        elif (mh.score.gpa >= 4):
            mh.score.classification = "D"
        else:
            mh.score.classification = "F"

    # Nhap mon hoc
    def inputMonHoc(self, mh:MonHoc) -> None:
        self.subject_list.append(mh)

    def getSLMonHoc(self) -> int:
        return self.subject_list.__len__()

    def getDSMH(self) -> list:
        return self.subject_list

class QuanLyGiangVien:

    def __init__(self) -> None:
        super().__init__()
        self.lecture_list = []

    def inputLecturer(self, gv: Lecturer):
        self.lecture_list.append(gv)

    def getSLLecturer(self) -> int:
        return self.lecture_list.__len__()

    def getDSGV(self) -> list:
        return self.lecture_list

    # Ham sap xep giang vien theo thu tu tang dan cua ten
    def SapxepGVTheoTen(self):
        for i in range(len(self.lecture_list)):
            for j in range(i + 1, len(self.lecture_list)):  # [i+1, len)
                if (self.lecture_list[i].name < self.lecture_list[j].name):
                    self.lecture_list[i], self.lecture_list[j] = self.lecture_list[j], self.lecture_list[i]
        return self.lecture_list

    # Ham tim kiem giang vien theo MSGV
    def TimKiemGVTheoMS(self, msgv):
        if (self.getSLLecturer() > 0):
            for gv in self.lecture_list:
                if (gv.lecture_code == msgv):
                    return gv

    # Ham xoa giang vien theo MMGV
    def XoaGVTheoMS(self, msgv):
        gv = self.TimKiemGVTheoMS(msgv)
        if (gv != None):
            self.lecture_list.remove(gv)
            return True
        else:
            return False

    # Ham xuat giang vien ra console
    def XuatGV(self, dsgv):
        for gv in dsgv:
            print(gv.outputTTLecturer())

    def InVaoFileGV(self, dsgv):
        with open("Lecturer.txt", "wb+") as f:
            for i in dsgv:
                pickle.dump(i.outputTTLecturer(), f)

    def DocFile(self, tenfile, x, name):
        with  open(tenfile, "rb+") as sf:
            for i in range(x):
                print(name, "thu", i + 1, ":")
                print(pickle.load(sf))