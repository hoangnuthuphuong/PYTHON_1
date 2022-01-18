from test1 import QuanLySinhVien

# khởi tạo một đối tượng QuanLySinhVien để quản lý sinh viên
dssv = QuanLySinhVien()
while (1 == 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN C#")
    print("*************************MENU**************************")
    print("**  1. Them sinh vien.                               **")
    print("**  2. Cap nhat thong tin sinh vien.                 **")
    print("**  3. Xoa sinh vien.                                **")
    print("**  4. Tim kiem sinh vien theo ten.                  **")
    print("**  5. Sap xep sinh vien theo ten.                   **")
    print("**  6. Hien thi danh sach giang vien                 **")
    print("**  7. Hien thi danh sach sinh vien.                 **")
    print("**  0. Thoat                                         **")
    print("*******************************************************")

    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("\n1. Them sinh vien.")
        dssv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
    elif (key == 2):
        if (dssv.soLuongSinhVien() > 0):
            print("\n2. Cap nhat thong tin sinh vien. ")
            print("\nNhap ID: ")
            ID = int(input())
            dssv.updateSinhVien(ID)
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 3):
        print("\n3. Xoa sinh vien.")
        muonxoa = []  # Khởi tạo một mảng chứa kết quả cần tìm
        name = input("Nhap ten sinh vien: ")  # Là chuỗi con bạn cần tìm, ví dụ 'abc'
        for name in dssv:  # Duyệt từng phần tử trong mảng
            if muonxoa in dssv:  # Xét xem chuỗi có nằm trong phần tử này hay không?
                print(sorted(set(dssv), key=dssv.index))



    elif (key == 4):
        print("\n4. Tim kiem sinh vien theo ten.")
        print("\nNhap ten de tim kiem: ")
        name = input()
        if (name == 1):
            if (dssv.soLuongSinhVien() > 0):
                print("\n4. Tim kiem sinh vien theo ten.")
                print("\nNhap ten de tim kiem: ")
                name = input()
                searchResult = dssv.findByName(name)
                dssv.showSinhVien(searchResult)
            else:
                print("\nKhong tim thay trong danh sach")
        else:
            print("\nKhong tim thay trong danh sach")




    elif (key == 5):
        if (dssv.soLuongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo ten.")
            dssv.sortByName()
            dssv.showSinhVien(dssv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong!")


    elif (key == 6):
        if (dssv.soLuongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ID.")
            dssv.sortByName()
            dssv.showSinhVien(dssv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 7):
        if (dssv.soLuongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien.")
            dssv.showSinhVien(dssv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong 7!")

    elif (key == 0):

        print("\nBan da chon thoat chuong trinh!")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")
