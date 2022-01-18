from test1 import QuanLySinhVien
from Pythontest import Student

dssv = QuanLySinhVien()
ds = []

while (1 == 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*************************MENU**************************")
    print("**  1. Thêm sinh viên.                               **")
    print("**  2. Cập nhật thông tin sinh viên.                 **")
    print("**  3. Xóa sinh viên.                                **")
    print("**  4. Tìm kiếm sinh viên theo tên.                  **")
    print("**  5. Sắp xếp sinh viên theo tên.                   **")
    print("**  6. Hiển thị số sinh viên trong danh sách.        **")
    print("**  7. Tra cứu thông tin sinh viên.                  **")
    print("**  8. Hiển thị danh sách sinh viên.                 **")
    print("**  0. Thoát                                         **")
    print("*******************************************************")

    key = int(input("nhập tuy chọn: "))
    if (key == 1):
        print("\n1. Thêm sinh viên.")
        name = input("nhập tên sinh viên: ")
        phone = int(input("nhập số điện thoại: "))
        email = input("nhập email: ")
        stuID = input("nhập ID sinh viên: ")
        chuyennganh = str(input("nhập chuyên ngành: "))
        hanhkiem = str(input("nhập hạnh kiểm: "))


        def __init__() -> object:
           stu = (Student(name, phone, email, stuID, chuyennganh, hanhkiem))
           ds.append(stu)
        print("\nThêm sinh viên thành công!")


    elif (key == 2):
        if (dssv.soLuongSinhVien() > 0):
            print("\n2. Cập nhật thông tin sinh viên. ")
            print("\nNhập ID: ")
            ID = int(input())
            dssv.updateSinhVien(ID)
        else:
            print("\nDanh sách sinh viên trống!")


    elif (key == 3):
        name = input("Nhập Id Sinh viên cần xóa :  ")
        for i in ds:
            if i.get_name() == name:
                assert isinstance(i, object)
                ds.remove(i)
                print("Bạn đã xóa sinh viên thành công ")
                continue
            print("đã xóa")
        else:
                print("không có sinh viên trong danh sách")



    elif (key == 4):
        print("\n4. Tim kiem sinh vien theo ten.")
        print("\nNhap ten de tim kiem: ")
        name = input()
        if (name == 1):
            if (dssv.soLuongSinhVien() > 0):
                print("\n4. Tìm kiếm sinh viên.")
                print("\nNhập tên sinh viên muốn tìm kiếm: ")
                name = input()
                searchResult = dssv.findByName(name)
                dssv.showSinhVien(searchResult)
            else:
                print("\nKhông tìm thấy trong danh sách")
        else:
            print("\nKhông tìm thấy sinh viên trong danh sách")


    elif (key == 5):
        if (dssv.soLuongSinhVien() > 0):
            print("\n5. Sắp xếp sinh viên theo tên.")
            dssv.sortByName()
            dssv.showSinhVien(dssv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống!")

    elif key == 6:
        print(f"\nHiện có {len(ds)} Sinh Viên \n")


    elif key == 7:
        if len(ds) == 0:
            print("\n hiện không có sinh viên . Bạn vui lòng thêm sinh viên vào danh sách !")
        else:
            print(f"\nHiện có {len(ds)} Sinh viên ")
            for i in ds:
                i.show_info()

    elif (key == 8):
        if (dssv.soLuongSinhVien() > 0):
            print("\n6. Hiển thị danh sách sinh viên.")
            dssv.showSinhVien(dssv.getListSinhVien())
        else:
            print("\nDanh sách sinh viên trống!")

    elif (key == 0):

        print("\nBạn đã thoát chương trình!")
        break
    else:
        print("\nKhông có chức năng này!")
        print("\nHãy chọn chức năng có trong menu.")


