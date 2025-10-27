#bài 4
import sinhvienpoly as svpl

class QuanLySinhVien:
    def __init__(self):
        self.dssv = []

    def nhap_dssv(self):
        while True:
            ho_ten_sv = input("Nhập họ tên sinh viên: ")
            nganh_hoc = input("Nhập ngành học sinh viên (it/biz/exit): ")

            if nganh_hoc.lower() == "it":
                java = float(input("Điểm Java: "))
                html = float(input("Điểm HTML: "))
                css = float(input("Điểm CSS: "))
                sv = svpl.SinhVienIT(ho_ten_sv, nganh_hoc, java, html, css)
                self.dssv.append(sv)

            elif nganh_hoc.lower() == "biz":
                marketing = float(input("Điểm Marketing: "))
                sales = float(input("Điểm Sales: "))
                sv = svpl.SinhVienBiz(ho_ten_sv, nganh_hoc, marketing, sales)
                self.dssv.append(sv)

            elif nganh_hoc.lower() == "exit":
                print("\nKết thúc nhập thông tin sinh viên !!!\n")
                break
            else:
                print("Nhập sai, vui lòng nhập lại!\n")

        return self.dssv

    def xuat_dssv(self):
        if not self.dssv:
            print("Danh sách sinh viên rỗng !!!")
        else:
            print(f"{'Tên sinh viên':20} {'Ngành học':10} {'Điểm':10} {'Học lực':10}")
            for sv in self.dssv:
                sv.xuat_tt()   


    def xuat_dssv_gioi(self):
        print("\n--- DANH SÁCH SINH VIÊN GIỎI ---")
        gioi = [sv for sv in self.dssv if sv.get_hoc_luc() == "Giỏi"]
        if not gioi:
            print("Không có sinh viên giỏi.")
        else:
            print(f"{'Họ Tên':20} {'Ngành':10} {'Điểm':10} {'Học lực':10}")
            print("-" * 55)
            for sv in gioi:
                sv.xuat_tt()

    def sap_xep_dssv(self):
        if not self.dssv:
            print("Danh sách sinh viên rỗng, không thể sắp xếp!")
            return
        self.dssv.sort(key=lambda sv: sv.get_diem(), reverse=True)
        print("\nĐã sắp xếp danh sách sinh viên theo điểm (cao → thấp):")
        self.xuat_dssv()
