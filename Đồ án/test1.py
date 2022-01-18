from Pythontest import Student


class QuanLySinhVien:
    listSinhVien = []

    def nhapSinhVien(self):
            # Khởi tạo một sinh viên mới
            name = input("Nhap ten sinh vien: ")
            phone = int(input("Nhap so dien thoai sinh vien: "))
            email = input("nhap email: ")
            stuID = input("nhap ID sinh vien")
            chuyennganh = str(input("nhap chuyen nganh: "))
            hanhkiem = str(input("nhap hanh kiem: "))

            # Nhập dữ liệu cho sinh viên

            def  __init__() -> object:
                stu = (Student(name, phone, email, stuID, chuyennganh, hanhkiem))
                self.dssv.append(stu)


    # Hàm hiển thị danh sách sinh viên ra màn hình
    def showSinhVien(self, dssv):
        def __init__(self):
            # hien thi tieu de cot
            print("{:<8} {:<18} {:<8}{:<8} {:<8} {:<8}"
                  .format("ID", "Name", "phone", "email", "chuyen nganh", "hanh kiem"))
            # hien thi danh sach sinh vien
            def   __init__() -> object:

                if (dssv.__len__() > 0):
                    for stu in dssv:
                       print("{:<8} {:<18} {:<8}{:<8} {:<8} {:<8}".format(stu._studentID, stu._name, stu._phone, stu._mail,
                                                                       stu._chuyennganh, stu._hanhkiem))
                print("\n")
            # Hàm trả về danh sách sinh viên



    def getListSinhVien(self):
            return self.dssv



    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()


    # Hàm tìm kiếm sinh viên theo tên
    # Trả về một danh sách sinh viên
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV



    def updateSinhVien(self, ID):
        # Tìm kiếm sinh viên trong danh sách listSinhVien
        stu: Student = self.findByID(ID)
        # Nếu sinh viên tồn tại thì cập nhập thông tin sinh viên
        if (stu != None):
            # nhập thông tin sinh viên
            name = input("Nhap ten sinh vien: ")
            phone = int(input("Nhap so dien thoai sinh vien: "))
            email = input("nhap email: ")
            studentID = input("nhap ID sinh vien")
            chuyennganh = str(input("nhap chuyen nganh: "))
            hanhkiem = str(input("nhap hanh kiem: "))
            # cập nhật thông tin sinh viên
            stu._name = name
            stu._phone = phone
            stu._email = email
            stu._studentID = studentID
            stu._chuyennganh = chuyennganh
            stu._hanhkiem = hanhkiem
        else:
            print("Sinh vien co ID = {} khong ton tai.".format(ID))

    # Hàm xóa sinh viên theo ten
    muonxoa = []  # Khởi tạo một mảng chứa kết quả cần tìm
    name = input("Nhap ten sinh vien: ")  # Là chuỗi con bạn cần tìm, ví dụ 'abc'
    for name in listSinhVien:  # Duyệt từng phần tử trong mảng
        if muonxoa in listSinhVien:  # Xét xem chuỗi có nằm trong phần tử này hay không?
            print(sorted(set(listSinhVien), key=listSinhVien.index))


    # Trả về một danh sách sinh viên
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV


    # Hàm sắp xếp danh sach sinh vien theo tên tăng dần
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    def getListSinhVien(self):
        return self.listSinhVien



