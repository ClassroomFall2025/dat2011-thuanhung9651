def y1():
    print("→ [Y1] Nhập danh sách nhân viên từ bàn phím và LƯU VÀO FILE.")

def y2():
    print("→ [Y2] Đọc nhân viên từ FILE và XUẤT danh sách ra màn hình.")

def y3():
    print("→ [Y3] Tìm và hiển thị nhân viên THEO MÃ nhập từ bàn phím.")

def y4():
    print("→ [Y4] Xóa nhân viên theo MÃ và CẬP NHẬT FILE dữ liệu.")

def y5():
    print("→ [Y5] Cập nhật thông tin nhân viên theo MÃ và GHI THAY ĐỔI VÀO FILE.")

def y6():
    print("→ [Y6] Tìm các nhân viên THEO KHOẢNG LƯƠNG nhập từ bàn phím.")

def y7():
    print("→ [Y7] Sắp xếp nhân viên THEO HỌ VÀ TÊN.")

def y8():
    print("→ [Y8] Sắp xếp nhân viên THEO THU NHẬP.")

def y9():
    print("→ [Y9] Xuất 5 nhân viên CÓ THU NHẬP CAO NHẤT.")

def menu_quan_ly_nhan_vien():
    while True:
        print("\n===== MENU QUẢN LÝ NHÂN VIÊN (GIAI ĐOẠN 1) =====")
        print("1. Y1 - Nhập DS NV và lưu file")
        print("2. Y2 - Đọc NV từ file và xuất")
        print("3. Y3 - Tìm NV theo mã")
        print("4. Y4 - Xóa NV theo mã (cập nhật file)")
        print("5. Y5 - Cập nhật NV theo mã (ghi file)")
        print("6. Y6 - Tìm NV theo khoảng lương")
        print("7. Y7 - Sắp xếp theo Họ và Tên")
        print("8. Y8 - Sắp xếp theo Thu nhập")
        print("9. Y9 - Top 5 NV thu nhập cao")
        print("0. Thoát")
        print("================================================")

        chon = input("Nhập lựa chọn (0-9): ").strip()

        match chon:
            case "1": y1()
            case "2": y2()
            case "3": y3()
            case "4": y4()
            case "5": y5()
            case "6": y6()
            case "7": y7()
            case "8": y8()
            case "9": y9()
            case "0":
                print("Tạm biệt!")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
if __name__ == "__main__":
    menu_quan_ly_nhan_vien()
