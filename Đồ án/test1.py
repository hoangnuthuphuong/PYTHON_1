from Pythontest import Student


class QuanLySinhVien:
    dssv = []

    def nhapSinhVien(self):
        # Khởi tạo một sinh viên mới
        name = input("Nhap ten sinh vien: ")
        phone = int(input("Nhap so dien thoai sinh vien: "))
        email = input("nhap email: ")
        studentID = input("nhap ID sinh vien")
        chuyennganh = str(input("nhap chuyen nganh: "))
        hanhkiem = str(input("nhap hanh kiem: "))


        # Nhập dữ liệu cho sinh viên
        stu = (Student(name,phone,email, studentID, chuyennganh, hanhkiem))
        self.dssv.append(stu)


    # Hàm hiển thị danh sách sinh viên ra màn hình 
    def showSinhVien(self, dssv):
        # hien thi tieu de cot
        print("{:<8} {:<18} {:<8}{:<8} {:<8} {:<8}"
              .format("ID", "Name", "phone", "email", "chuyen nganh", "hanh kiem"))
        # hien thi danh sach sinh vien
        if (dssv.__len__() > 0):
            for stu in dssv:
                print("{:<8} {:<18} {:<8}{:<8} {:<8} {:<8}"
                      .format(stu._studentID, stu._name, stu._phone, stu._mail, stu._chuyennganh, stu._hanhkiem))
        print("\n")
    # Hàm trả về danh sách sinh viên
    def getListSinhVien(self):
        return self.dssv







