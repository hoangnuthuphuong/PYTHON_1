from test1 import QuanLySinhVien

# khởi tạo một đối tượng QuanLySinhVien để quản lý sinh viên
dssv = QuanLySinhVien()
while (1 == 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN C#")
    print("*************************MENU**************************")
    print("**  1. Them sinh vien.                               **")
    print("**  2. eiwuriweiweyfiweyiweyrfyewryu      ewgfeee    **")
    print("**  3. Hien thi danh sach sinh vien.                 **")
    print("*******************************************************")

    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("\n1. Them sinh vien.")
        dssv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
    elif (key == 2):
        print("\n7. Hien thi danh sach sinh vien.")
        dssv.showSinhVien(dssv.getListSinhVien())
