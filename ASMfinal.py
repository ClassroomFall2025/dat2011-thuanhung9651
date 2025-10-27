
import csv
CSV_FILE = "nhanvien.csv"



class NhanVien:
    def __init__(self, ma, ho_ten, luong):
        self.ma = ma
        self.ho_ten = ho_ten
        self.luong = float(luong)

    def get_thu_nhap(self):
        return self.luong

    def loai(self):
        return "HanhChinh"


class TiepThi(NhanVien):
    def __init__(self, ma, ho_ten, luong, doanh_so, hoa_hong):
        super().__init__(ma, ho_ten, luong)
        self.doanh_so = float(doanh_so)
        self.hoa_hong = float(hoa_hong)   # ví dụ 0.05 = 5%

    def get_thu_nhap(self):
        return self.luong + self.doanh_so * self.hoa_hong

    def loai(self):
        return "TiepThi"


class TruongPhong(NhanVien):
    def __init__(self, ma, ho_ten, luong, trach_nhiem):
        super().__init__(ma, ho_ten, luong)
        self.trach_nhiem = float(trach_nhiem)

    def get_thu_nhap(self):
        return self.luong + self.trach_nhiem

    def loai(self):
        return "TruongPhong"




class QuanLyNhanVien:
    def __init__(self):
        self.ds = []  

    
    def xuat_ds(self, ds=None):
        ds = ds if ds is not None else self.ds
        if not ds:
            print("Danh sách rỗng.")
            return
        print(f"{'Mã':10} | {'Họ tên':25} | {'Lương':>12} | {'Thu nhập':>12} | Loại")
        print("-" * 75)
        for nv in ds:
            print(f"{nv.ma:10} | {nv.ho_ten:25} | {nv.luong:12,.0f} | {nv.get_thu_nhap():12,.0f} | {nv.loai()}")

   
    def them_nv(self, nv):
        # chống trùng mã
        for x in self.ds:
            if x.ma == nv.ma:
                raise ValueError("Mã nhân viên đã tồn tại.")
        self.ds.append(nv)

    
    def luu_file(self, path=CSV_FILE):
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["Loai","Ma","HoTen","Luong","DoanhSo","HoaHong","TrachNhiem","ThuNhap"])
            for nv in self.ds:
                if isinstance(nv, TiepThi):
                    w.writerow([nv.loai(), nv.ma, nv.ho_ten, nv.luong, nv.doanh_so, nv.hoa_hong, "", nv.get_thu_nhap()])
                elif isinstance(nv, TruongPhong):
                    w.writerow([nv.loai(), nv.ma, nv.ho_ten, nv.luong, "", "", nv.trach_nhiem, nv.get_thu_nhap()])
                else:
                    w.writerow([nv.loai(), nv.ma, nv.ho_ten, nv.luong, "", "", "", nv.get_thu_nhap()])
        print("✔ Đã lưu vào", path)

    # Y2
    def doc_file(self, path=CSV_FILE):
        self.ds.clear()
        try:
            with open(path, "r", encoding="utf-8") as f:
                r = csv.DictReader(f)
                for row in r:
                    loai = row.get("Loai","HanhChinh")
                    ma = row.get("Ma","")
                    ho_ten = row.get("HoTen","")
                    luong = float(row.get("Luong") or 0)
                    if loai == "TiepThi":
                        ds = float(row.get("DoanhSo") or 0)
                        hh = float(row.get("HoaHong") or 0)
                        self.ds.append(TiepThi(ma, ho_ten, luong, ds, hh))
                    elif loai == "TruongPhong":
                        tn = float(row.get("TrachNhiem") or 0)
                        self.ds.append(TruongPhong(ma, ho_ten, luong, tn))
                    else:
                        self.ds.append(NhanVien(ma, ho_ten, luong))
            print(" Đã đọc dữ liệu từ", path)
        except FileNotFoundError:
            print(" Chưa có file dữ liệu.")

    # ------- TÌM / XÓA / CẬP NHẬT -------
    # Y3
    def tim_theo_ma(self, ma):
        for nv in self.ds:
            if nv.ma == ma:
                return nv
        return None

    # Y4
    def xoa_theo_ma(self, ma, path=CSV_FILE):
        nv = self.tim_theo_ma(ma)
        if nv:
            self.ds.remove(nv)
            self.luu_file(path)  # cập nhật file sau xóa
            print("✔ Đã xóa và cập nhật file.")
            return True
        print(" Không tìm thấy mã.")
        return False

    # Y5
    def cap_nhat_va_ghi(self, ma, path=CSV_FILE,
                         ho_ten=None, luong=None,
                         doanh_so=None, hoa_hong=None,
                         trach_nhiem=None):
        nv = self.tim_theo_ma(ma)
        if not nv:
            print(" Không tìm thấy mã.")
            return False

        if ho_ten not in (None, ""): nv.ho_ten = ho_ten
        if luong is not None: nv.luong = float(luong)

        if isinstance(nv, TiepThi):
            if doanh_so is not None: nv.doanh_so = float(doanh_so)
            if hoa_hong is not None: nv.hoa_hong = float(hoa_hong)
        if isinstance(nv, TruongPhong):
            if trach_nhiem is not None: nv.trach_nhiem = float(trach_nhiem)

        self.luu_file(path)
        print("✔ Đã cập nhật và ghi file.")
        return True

    def tim_theo_khoang_luong(self, luong_min, luong_max):
        return [nv for nv in self.ds if luong_min <= nv.luong <= luong_max]

    def _key_ten(self, nv):
        parts = nv.ho_ten.strip().split()
        return (parts[-1] + " " + " ".join(parts[:-1])).lower()

    def sap_xep_theo_ten(self):
        self.ds.sort(key=self._key_ten)

    def sap_xep_theo_thu_nhap(self, giam_dan=True):
        self.ds.sort(key=lambda x: x.get_thu_nhap(), reverse=giam_dan)

    def top5_thu_nhap(self):
        return sorted(self.ds, key=lambda x: x.get_thu_nhap(), reverse=True)[:5]




def nhap_so_thuc(thong_diep, allow_zero=True, min_val=None, max_val=None):
    while True:
        try:
            x = float(input(thong_diep))
            if not allow_zero and x == 0:
                print("  -> Giá trị phải khác 0.")
                continue
            if min_val is not None and x < min_val:
                print(f"  -> Phải >= {min_val}."); continue
            if max_val is not None and x > max_val:
                print(f"  -> Phải <= {max_val}."); continue
            return x
        except ValueError:
            print("  -> Vui lòng nhập số hợp lệ.")

def nhap_nv_tu_ban_phim():
    print("\n-- Nhập nhân viên --")
    loai = input("Loại (1-Hành chính, 2-Tiếp thị, 3-Trưởng phòng): ").strip()
    ma = input("Mã (không để trống): ").strip()
    if not ma:
        print("  -> Mã không được rỗng."); return None
    ho_ten = input("Họ tên (không để trống): ").strip()
    if not ho_ten:
        print("  -> Họ tên không được rỗng."); return None
    luong = nhap_so_thuc("Lương (>=0): ", min_val=0)

    if loai == "2":
        doanh_so = nhap_so_thuc("Doanh số (>=0): ", min_val=0)
        hoa_hong = nhap_so_thuc("Hoa hồng (0..1): ", min_val=0, max_val=1)
        return TiepThi(ma, ho_ten, luong, doanh_so, hoa_hong)
    elif loai == "3":
        trach_nhiem = nhap_so_thuc("Trách nhiệm (>=0): ", min_val=0)
        return TruongPhong(ma, ho_ten, luong, trach_nhiem)
    else:
        return NhanVien(ma, ho_ten, luong)




def menu():
    ql = QuanLyNhanVien()
    while True:
        print("\n===== MENU QUẢN LÝ NHÂN VIÊN =====")
        print("1. [Y1] Nhập danh sách và LƯU vào file")
        print("2. [Y2] Đọc từ file và XUẤT danh sách")
        print("3. [Y3] Tìm & hiển thị theo MÃ")
        print("4. [Y4] Xóa theo MÃ (và cập nhật file)")
        print("5. [Y5] Cập nhật theo MÃ (và ghi file)")
        print("6. [Y6] Tìm theo KHOẢNG LƯƠNG")
        print("7. [Y7] Sắp xếp theo HỌ & TÊN")
        print("8. [Y8] Sắp xếp theo THU NHẬP (giảm dần)")
        print("9. [Y9] Xuất TOP 5 thu nhập cao nhất")
        print("0. Thoát")
        chon = input("Chọn: ").strip()

        if chon == "1":
            try:
                n = int(input("Số lượng cần nhập: "))
            except ValueError:
                print("  -> Vui lòng nhập số nguyên."); continue
            for _ in range(n):
                nv = nhap_nv_tu_ban_phim()
                if nv: 
                    try:
                        ql.them_nv(nv)
                    except ValueError as e:
                        print("  ->", e)
            ql.luu_file(CSV_FILE)

        elif chon == "2":
            ql.doc_file(CSV_FILE)
            ql.xuat_ds()

        elif chon == "3":
            ma = input("Nhập MÃ cần tìm: ").strip()
            nv = ql.tim_theo_ma(ma)
            if nv: ql.xuat_ds([nv])
            else: print("Không tìm thấy.")

        elif chon == "4":
            ma = input("Nhập MÃ cần xóa: ").strip()
            ql.xoa_theo_ma(ma, CSV_FILE)

        elif chon == "5":
            ma = input("MÃ cần cập nhật: ").strip()
            print("Bỏ trống nếu không đổi.")
            ten = input("Tên mới: ").strip()
            luong_raw = input("Lương mới: ").strip()
            luong = float(luong_raw) if luong_raw else None

            ds = input("Doanh số mới (TT): ").strip()
            hh = input("Hoa hồng mới 0..1 (TT): ").strip()
            tn = input("Trách nhiệm mới (TP): ").strip()

            # kiểm tra hoa hồng nếu có
            hh_val = float(hh) if hh else None
            if hh and not (0 <= hh_val <= 1):
                print("  -> Hoa hồng phải trong khoảng 0..1."); continue

            ql.cap_nhat_va_ghi(
                ma, CSV_FILE,
                ho_ten=ten if ten else None,
                luong=luong,
                doanh_so=float(ds) if ds else None,
                hoa_hong=hh_val,
                trach_nhiem=float(tn) if tn else None
            )

        elif chon == "6":
            mn = nhap_so_thuc("Lương min: ")
            mx = nhap_so_thuc("Lương max: ")
            if mn > mx: 
                mn, mx = mx, mn
            ql.xuat_ds(ql.tim_theo_khoang_luong(mn, mx))

        elif chon == "7":
            ql.sap_xep_theo_ten(); ql.xuat_ds()

        elif chon == "8":
            ql.sap_xep_theo_thu_nhap(True); ql.xuat_ds()

        elif chon == "9":
            ql.xuat_ds(ql.top5_thu_nhap())

        elif chon == "0":
            print("Tạm biệt!"); break
        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    menu()
