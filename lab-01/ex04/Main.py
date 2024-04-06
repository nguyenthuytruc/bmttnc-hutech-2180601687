from QuanLiSinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1==1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("******************************MENU***************************")
    print(" 1.Them sinh vien.")
    print(" 2.Cap nhat thong tin sinh vien boi ID")
    print("3.Xoa sinh vien boi ID")
    print("4.Tim kiem sinh vien theo ten")
    print("5.Sap xep sinh vien theo DTB")
    print("6.Sap xep sinh vien theo ten chuyen nganh")
    print("7.Hien thi danh sach sinh vien")
    print("0. Thoat")
    print("***************************************")
    key = int(input("Nhap tuy chon: "))
    if(key == 1):
        print("\n1. Them sinh vien")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh công!")
    elif(key == 2):
        if (qlsv.soLuongSinhVien()> 0):
            print("\n2. Cap nhat thong tin sinhvien") 
            print("Nhap ID:") 
            ID = int(input()) 
            qlsv.updateSinhVien(ID)
        else:
            print("\n Danh sach dinh vien trong!")
    elif (key == 3):
        if qlsv.soLuongSinhVien() > 0:
            print("\n3. Xóa sinh viên bởi ID")
            print("Nhập ID:")
            ID = int(input())
            if qlsv.deleteById(ID):
                print("Sinh vien co ID = ", ID,"da bi xoa.")
            else:
                print("\nSinh vien co id =", ID, "KHONG OTN TAI")
        else:
            print("\nSach sach sinh vien trong!") 
    elif (key == 4):
        if (qlsv.soLuongSinhVien()>0):
            print("\n4 Tim kiem sinh vien theo ten")
            print("\nNhap ten de tim kiem:")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\n Sach sach sinh vien trong!")
    elif (key == 5):
        if(qlsv.soLuongSinhVien()>0):
            print("\n5, sap xep sinh vien theo diem trung binh .")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSach sinh vien trong!") 
    elif (key == 6):
        if(qlsv.soLuongSinhVien()>0):
            print("\n6. Sap xep sinhvien theo ten")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Sach sinh vien trong!") 
    elif (key == 7):
        if(qlsv.soLuongSinhVien()>0):    
            print("\n7. Hien thi danh sach sih vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 0):
        print("\nBan da chon thoat chuong tỉnh!") 
        break
    else:
        print("\nKhong co chuc nang nay") 
        print("\nHay cho chuc nang trong menu.")                                    