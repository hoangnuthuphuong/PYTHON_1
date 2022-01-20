from Pythontest import MonHoc, Student, Lecturer

class Hoc_phan:

    def NhapDuLieuMH():
        sbj_code = input("Ma mon hoc: ")
        sbj_name = input("Ten mon hoc: ")
        credit = input("So tin chi: ")
        money = float(input("Thanh tien: "))
        point_process = float(input("Nhap diem qua trinh: "))
        test_point = float(input("Nhap diem kiem tra: "))
        test_score = float(input("Nhap diem thi: "))
        gpa = (point_process + test_point + test_score) / 3
        if (gpa >= 8.5):
            classification = "A"
        elif (gpa >= 8):
            classification = "B+"
        elif (gpa >= 7):
            classification = "B"
        elif (gpa >= 6.5):
            classification = "C+"
        elif (gpa >= 5.5):
            classification = "C"
        elif (gpa >= 5):
            classification = "D+"
        elif (gpa >= 4):
            classification = "D"
        else:
            classification = "F"
        mh = MonHoc(sbj_code, sbj_name, credit, money, point_process, test_point, test_score, gpa, classification)
        return mh

    def NhapDuLieuSV(self) -> Student:
        name = input("Ho ten: ")
        sdt = input("So dien thoai: ")
        email = input("Dia chi email: ")
        gender = input("Nhap gioi tinh: ")
        st_code = input("Nhap ma so sinh vien:")
        subject = Hoc_phan.NhapDuLieuMH()
        sv = Student(name, sdt, email, gender, st_code, subject)
        return sv

    def NhapDuLieuGV(self) -> Lecturer:
        name = input("Ho ten: ")
        sdt = input("So dien thoai: ")
        email = input("Dia chi email: ")
        gender = input("Nhap gioi tinh: ")
        lt_code = input("Ma so sinh vien: ")
        salary = float(input("Nhap luong: "))
        subject = Hoc_phan.NhapDuLieuMH()
        gv = Lecturer(name, sdt, email, gender, lt_code, salary, subject)
        return gv