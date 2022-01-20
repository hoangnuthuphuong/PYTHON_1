import pickle
from Pythontest import Person, KetQuaHocTap, MonHoc, Student, Lecturer
from test1 import QuanLySinhVien, QuanLyGiangVien
from test2 import Hoc_phan

def NhapN(name):
    n = "Nhap so " + str(name)
    x = int(input(n))
    while (x <= 0):
        print("Nhập sai, xin nhập lại!")
        x = int(input("Nhập số lượng: "))
    return x


def main():

    qlsv = QuanLySinhVien()
    qlgv = QuanLyGiangVien()
    #Su dung doi tuong cua lop Hoc_phan de nhap du lieu
    View = Hoc_phan()

    while True:
        print("\nCHUONG TRINH QUAN LY SINH VIEN *******")
        print("1. Them sinh vien.                     *")
        print("2. Xoa sinh vien boi ID.               *")
        print("3. Tim kiem sinh vien theo ID.         *")
        print("4. Sap xep sinh vien theo ten.         *")
        print("5. In danh sach sinh vien vao file.    *")
        print("6. Xuat danh sach sinh vien.           *")
        print("              *****                     ")
        print("8. Them giang vien.                    *")
        print("9. Xuat giang vien ra console.         *")
        print("10. Sap xep giang vien theo ten.       *")
        print("11. Xoa giang vien boi ID.             *")
        print("12. Tim kiem giang vien theo ten.      *")
        print("13. Sap xep giang vien theo ten.       *")
        print("14. In danh sach sinh vien vao file.   *")
        print("15. Xuat danh sach sinh vien tu file.  *")
        print("0. Thoat                               *")
        print("****************************************")

        key = int(input("Nhap tuy chon: "))
        if (key == 1):
            for i in range(NhapN("Sinh Vien: ")):
                print("Nhap thong tin sinh vien thu", i + 1)
                qlsv.inputStudent(View.NhapDuLieuSV())
                print("Them sinh vien thanh cong!\n")
        elif (key == 2):
            if (qlsv.getSLStudent() > 0):
                ID = input("Nhap mssv: ")
                if (qlsv.XoaSVTheoMS(ID)):
                    print("\nSinh vien co mssv = ", ID, " da bi xoa.")
                else:
                    print("\nSinh vien co mssv = ", ID, " khong ton tai.")
            else:
                print("\nKhong co sinh vien nao trong danh sach!")
        elif (key == 3):
            if (qlsv.getSLStudent() > 0):
                name = input("Nhap ID de tim kiem: ")
                searchResult = qlsv.TimKiemSVTheoMS(name)
                print(searchResult.outputTTStudent())
            else:
                print("\nKhong co sinh vien nao trong danh sach! ")
        elif (key == 4):
            if (qlsv.getSLStudent() > 0):
                print("\nSap xep sinh vien theo ten.")
                qlsv.SapxepSVTheoTen()
                qlsv.XuatSV(qlsv.getDSSV())
            else:
                print("\nKhong co sinh vien nao trong danh sach!")

        elif (key == 5):
            if (qlsv.getSLStudent() > 0):
                print("\nIn danh sach sinh vien vao file.")
                qlsv.InVaoFileSV(qlsv.getDSSV())
            else:
                print("\nKhong co sinh vien nao trong danh sach!")
        elif (key == 6):
            if (qlsv.getSLStudent() > 0):
                print("\nXuat danh sach sinh vien .")
                qlsv.DocFile("Student.txt", qlsv.getSLStudent(), "Sinh vien ")
            else:
                print("\nKhong co sinh vien nao trong danh sach!")
        elif (key == 8):
            for i in range(NhapN("Giang Vien: ")):
                print("Nhap thong tin giang vien thu", i + 1)
                qlgv.inputLecturer(View.NhapDuLieuGV())
                print("Them giang vien thanh cong!\n")
        elif (key == 9):
            if (qlgv.getSLLecturer() > 0):
                print("\n7. Xuat danh sach giang vien ra console.")
                qlgv.XuatGV(qlgv.getDSGV())
            else:
                print("\nKhong co giang vien nao trong danh sach!")
        elif (key == 10):
            if (qlgv.getSLLecturer() > 0):
                print("\n6. Sap xep giang vien theo ten.")
                qlgv.SapxepGVTheoTen()
                qlgv.XuatGV(qlgv.getDSGV())
            else:
                print("\nKhong co giang vien nao trong danh sach!")
        elif (key == 11):
            if (qlgv.getSLLecturer() > 0):
                ID = input("Nhap msgv: ")
                if (qlgv.XoaGVTheoMS(ID)):
                    print("\nGiang vien co mssv = ", ID, " da bi xoa.")
                else:
                    print("\nGiang vien co mssv = ", ID, " khong ton tai.")
            else:
                print("\nKhong co giang vien nao trong danh sach!")
        elif (key == 12):
            if (qlgv.getSLLecturer() > 0):
                name = input("Nhap ten de tim kiem: ")
                searchResult = qlgv.TimKiemGVTheoMS(name)
                print(searchResult.outputTTLecturer())
            else:
                print("\nKhong co giang vien nao trong danh sach! ")
        elif (key == 13):
            if (qlgv.getSLLecturer() > 0):
                print("\n6. Sap xep giang vien theo ten.")
                qlgv.SapxepGVTheoTen()
                qlgv.XuatGV(qlgv.getDSGV())
            else:
                print("\nKhong co giang vien nao trong danh sach!")
        elif (key == 14):
            if (qlgv.getSLLecturer() > 0):
                print("\n7. In danh sach giang vien vao file.")
                qlgv.InVaoFileGV(qlgv.getDSGV())
            else:
                print("\nKhong co giang vien nao trong danh sach!")
        elif (key == 15):
            if (qlgv.getSLLecturer() > 0):
                print("\n7. Xuat danh sach giang vien.")
                qlsv.DocFile("Lecturer.txt", qlgv.getSLLecturer(), "Giang vien ")
            else:
                print("\nKhong co giang vien nao trong danh sach!")
        elif (key == 0):
            print("\nBan da chon thoat chuong trinh!")
            break
        else:
            print("\nKhong co chuc nang nay!")
            print("\nHay chon chuc nang trong hop menu.")

if __name__ == '__main__':
    main()