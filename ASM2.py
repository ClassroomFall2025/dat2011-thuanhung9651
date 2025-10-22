#ASM Giai doan 1: Quan ly nhan vien
# def y1():
#     print("→ [Y1] Nhập danh sách nhân viên từ bàn phím và LƯU VÀO FILE")

# def y2():
#     print("→ [Y2] Đọc nhân viên từ FILE và XUẤT danh sách ra màn hình")

# def y3():
#     print("→ [Y3] Tìm và hiển thị nhân viên THEO MÃ nhập từ bàn phím")

# def y4():
#     print("→ [Y4] Xóa nhân viên theo MÃ và CẬP NHẬT FILE dữ liệu")

# def y5():
#     print("→ [Y5] Cập nhật thông tin nhân viên theo MÃ và GHI THAY ĐỔI VÀO FILE")

# def y6():
#     print("→ [Y6] Tìm các nhân viên THEO KHOẢNG LƯƠNG nhập từ bàn phím")

# def y7():
#     print("→ [Y7] Sắp xếp nhân viên THEO HỌ VÀ TÊN")

# def y8():
#     print("→ [Y8] Sắp xếp nhân viên THEO THU NHẬP")

# def y9():
#     print("→ [Y9] Xuất 5 nhân viên CÓ THU NHẬP CAO NHẤT")

# def menu_quan_ly_nhan_vien():
#     while True:
#         print("\nMENU QUẢN LÝ NHÂN VIÊN (GIAI ĐOẠN 1)")
#         print("1. Y1 - Nhập DS NV và lưu file")
#         print("2. Y2 - Đọc NV từ file và xuất")
#         print("3. Y3 - Tìm NV theo mã")
#         print("4. Y4 - Xóa NV theo mã (cập nhật file)")
#         print("5. Y5 - Cập nhật NV theo mã (ghi file)")
#         print("6. Y6 - Tìm NV theo khoảng lương")
#         print("7. Y7 - Sắp xếp theo Họ và Tên")
#         print("8. Y8 - Sắp xếp theo Thu nhập")
#         print("9. Y9 - Top 5 NV thu nhập cao")
#         print("0. Thoát")
    
#         chon = input("Nhập lựa chọn (0-9): ").strip()

#         match chon:
#             case "1": y1()
#             case "2": y2()
#             case "3": y3()
#             case "4": y4()
#             case "5": y5()
#             case "6": y6()
#             case "7": y7()
#             case "8": y8()
#             case "9": y9()
#             case "0":
#                 print("Tạm biệt!")
#                 break
#             case _:
#                 print("Lựa chọn không hợp lệ, vui lòng nhập lại")


#ASM Giai doan 2: May tinh


from dataclasses import dataclass
from typing import List, Optional, Dict, Type
import csv, os

FILE_CSV = "nhanvien.csv"
HEADERS = ["Loai", "Ma", "HoTen", "Luong", "DoanhSo", "HoaHong", "TrachNhiem", "ThuNhap"]


@dataclass
class NhanVien:
    ma: str
    ho_ten: str
    luong: float  

    def getThuNhap(self) -> float:
        return float(self.luong)

    def loai(self) -> str:
        return "HanhChinh"

    # serialize to dict for CSV
    def to_row(self) -> Dict[str, str]:
        return {
            "Loai": self.loai(),
            "Ma": self.ma,
            "HoTen": self.ho_ten,
            "Luong": f"{self.luong}",
            "DoanhSo": "",
            "HoaHong": "",
            "TrachNhiem": "",
            "ThuNhap": f"{self.getThuNhap()}",
        }

@dataclass
class TiepThi(NhanVien):
    doanh_so: float
    hoa_hong: float  

    def getThuNhap(self) -> float:
        return float(self.luong) + float(self.doanh_so) * float(self.hoa_hong)

    def loai(self) -> str:
        return "TiepThi"

    def to_row(self) -> Dict[str, str]:
        return {
            "Loai": self.loai(),
            "Ma": self.ma,
            "HoTen": self.ho_ten,
            "Luong": f"{self.luong}",
            "DoanhSo": f"{self.doanh_so}",
            "HoaHong": f"{self.hoa_hong}",
            "TrachNhiem": "",
            "ThuNhap": f"{self.getThuNhap()}",
        }

@dataclass
class TruongPhong(NhanVien):
    trach_nhiem: float 

    def getThuNhap(self) -> float:
        return float(self.luong) + float(self.trach_nhiem)

    def loai(self) -> str:
        return "TruongPhong"

    def to_row(self) -> Dict[str, str]:
        return {
            "Loai": self.loai(),
            "Ma": self.ma,
            "HoTen": self.ho_ten,
            "Luong": f"{self.luong}",
            "DoanhSo": "",
            "HoaHong": "",
            "TrachNhiem": f"{self.trach_nhiem}",
            "ThuNhap": f"{self.getThuNhap()}",
        }

TYPE_MAP: Dict[str, Type[NhanVien]] = {
    "HanhChinh": NhanVien,
    "TiepThi": TiepThi,
    "TruongPhong": TruongPhong,
}


def ensure_file():
    if not os.path.exists(FILE_CSV):
        with open(FILE_CSV, "w", encoding="utf-8-sig", newline="") as f:
            csv.DictWriter(f, fieldnames=HEADERS).writeheader()

def read_all() -> List[NhanVien]:
    ensure_file()
    ds: List[NhanVien] = []
    with open(FILE_CSV, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            loai = r.get("Loai", "HanhChinh")
            try:
                if loai == "HanhChinh":
                    ds.append(NhanVien(
                        ma=r["Ma"].strip(),
                        ho_ten=r["HoTen"].strip(),
                        luong=float(r["Luong"] or 0),
                    ))
                elif loai == "TiepThi":
                    ds.append(TiepThi(
                        ma=r["Ma"].strip(),
                        ho_ten=r["HoTen"].strip(),
                        luong=float(r["Luong"] or 0),
                        doanh_so=float(r["DoanhSo"] or 0),
                        hoa_hong=float(r["HoaHong"] or 0),
                    ))
                elif loai == "TruongPhong":
                    ds.append(TruongPhong(
                        ma=r["Ma"].strip(),
                        ho_ten=r["HoTen"].strip(),
                        luong=float(r["Luong"] or 0),
                        trach_nhiem=float(r["TrachNhiem"] or 0),
                    ))
            except Exception:
                
                continue
    return ds

def write_all(ds: List[NhanVien]) -> None:
    with open(FILE_CSV, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        for nv in ds:
            writer.writerow(nv.to_row())

def append_many(ds_new: List[NhanVien]) -> None:
    ds = read_all()
    ds.extend(ds_new)
    write_all(ds)

# -------------------- VIEW helpers --------------------
def input_float(prompt: str, allow_blank: bool=False, default: Optional[float]=None) -> Optional[float]:
    while True:
        s = input(prompt).strip()
        if allow_blank and s == "": return default
        try:
            return float(s)
        except ValueError:
            print("→ Vui lòng nhập số hợp lệ.")

def print_table(ds: List[NhanVien], title: Optional[str] = None):
    if title: print("\n" + title)
    if not ds:
        print("(Không có dữ liệu)")
        return
    print(f"{'Ma':<10} {'Loai':<12} {'HoTen':<28} {'Luong':>12} {'PhuTro/DS*HH':>16} {'ThuNhap':>12}")
    print("-"*95)
    for nv in ds:
        if isinstance(nv, TiepThi):
            pt = f"{nv.doanh_so:.2f}*{nv.hoa_hong:.2f}"
        elif isinstance(nv, TruongPhong):
            pt = f"+{nv.trach_nhiem:.2f}"
        else:
            pt = "-"
        print(f"{nv.ma:<10} {nv.loai():<12} {nv.ho_ten:<28} {nv.luong:>12.2f} {pt:>16} {nv.getThuNhap():>12.2f}")


def _split_name(hoten: str):
    parts = hoten.strip().split()
    if not parts: return ("","")
    return (parts[-1].lower(), " ".join(parts[:-1]).lower())

def find_by_ma(ds: List[NhanVien], ma: str) -> Optional[int]:
    for i, nv in enumerate(ds):
        if nv.ma.lower() == ma.lower():
            return i
    return None

def nhap_nv_tu_ban_phim() -> NhanVien:
    print("Chọn loại NV: 1) Hành chính  2) Tiếp thị  3) Trưởng phòng")
    loai = input("Nhập lựa chọn (1/2/3): ").strip()
    ma = input("Mã NV: ").strip()
    ho_ten = input("Họ tên: ").strip()
    luong = input_float("Lương cơ bản: ")

    if loai == "2":
        doanh_so = input_float("Doanh số: ")
        hoa_hong = input_float("Hoa hồng (vd 0.05 = 5%): ")
        return TiepThi(ma, ho_ten, luong, doanh_so, hoa_hong)
    elif loai == "3":
        trach_nhiem = input_float("Phụ cấp trách nhiệm: ")
        return TruongPhong(ma, ho_ten, luong, trach_nhiem)
    else:
        return NhanVien(ma, ho_ten, luong)


def y1():
    print("→ [Y1] Nhập DS NV từ bàn phím và LƯU VÀO FILE (append).")
    n = int(input("Nhập số lượng NV cần thêm: ").strip())
    ds_new: List[NhanVien] = []
    for i in range(1, n+1):
        print(f"--- NV {i} ---")
        ds_new.append(nhap_nv_tu_ban_phim())
    append_many(ds_new)
    print("→ Đã lưu vào file", FILE_CSV)

def y2():
    print("→ [Y2] Đọc từ file và XUẤT danh sách")
    print_table(read_all(), "DANH SÁCH NHÂN VIÊN")

def y3():
    print("→ [Y3] Tìm NV theo MÃ")
    key = input("Nhập mã cần tìm: ").strip()
    ds = read_all()
    idx = find_by_ma(ds, key)
    if idx is None:
        print("→ Không tìm thấy.")
    else:
        print_table([ds[idx]], f"KẾT QUẢ TÌM THEO MÃ = {key}")

def y4():
    print("→ [Y4] Xoá NV theo MÃ (cập nhật file)")
    key = input("Nhập mã cần xoá: ").strip()
    ds = read_all()
    idx = find_by_ma(ds, key)
    if idx is None:
        print("→ Không tìm thấy.")
    else:
        ds.pop(idx)
        write_all(ds)
        print("→ Đã xoá và cập nhật file.")

def y5():
    print("→ [Y5] Cập nhật NV theo MÃ và ghi thay đổi vào file")
    key = input("Nhập mã cần cập nhật: ").strip()
    ds = read_all()
    idx = find_by_ma(ds, key)
    if idx is None:
        print("→ Không tìm thấy.")
        return

    nv = ds[idx]
    print("Nhấn Enter để giữ nguyên.")
    ho_ten = input(f"Họ tên [{nv.ho_ten}]: ").strip() or nv.ho_ten
    luong = input_float(f"Lương [{nv.luong}]: ", allow_blank=True, default=nv.luong)

    # Cho phép đổi loại nếu muốn
    print(f"Loại hiện tại: {nv.loai()}  → đổi loại?  (Enter bỏ qua)")
    ch = input("1) Hành chính  2) Tiếp thị  3) Trưởng phòng: ").strip()

    if ch == "2":
        if isinstance(nv, TiepThi):
            ds[idx] = TiepThi(nv.ma, ho_ten, luong,
                              input_float(f"Doanh số [{nv.doanh_so}]: ", True, nv.doanh_so),
                              input_float(f"Hoa hồng [{nv.hoa_hong}]: ", True, nv.hoa_hong))
        else:
            doanh_so = input_float("Doanh số: ")
            hoa_hong = input_float("Hoa hồng: ")
            ds[idx] = TiepThi(nv.ma, ho_ten, luong, doanh_so, hoa_hong)

    elif ch == "3":
        if isinstance(nv, TruongPhong):
            ds[idx] = TruongPhong(nv.ma, ho_ten, luong,
                                  input_float(f"Trách nhiệm [{nv.trach_nhiem}]: ", True, nv.trach_nhiem))
        else:
            trach_nhiem = input_float("Trách nhiệm: ")
            ds[idx] = TruongPhong(nv.ma, ho_ten, luong, trach_nhiem)

    else:
        
        if isinstance(nv, TiepThi):
            ds[idx] = TiepThi(nv.ma, ho_ten, luong,
                              input_float(f"Doanh số [{nv.doanh_so}]: ", True, nv.doanh_so),
                              input_float(f"Hoa hồng [{nv.hoa_hong}]: ", True, nv.hoa_hong))
        elif isinstance(nv, TruongPhong):
            ds[idx] = TruongPhong(nv.ma, ho_ten, luong,
                                  input_float(f"Trách nhiệm [{nv.trach_nhiem}]: ", True, nv.trach_nhiem))
        else:
            ds[idx] = NhanVien(nv.ma, ho_ten, luong)

    write_all(ds)
    print("→ Đã cập nhật và ghi file.")

def y6():
    print("→ [Y6] Tìm NV theo KHOẢNG LƯƠNG (theo lương cơ bản)")
    mn = input_float("Lương MIN: ")
    mx = input_float("Lương MAX: ")
    if mn > mx: mn, mx = mx, mn
    ds = read_all()
    kq = [nv for nv in ds if mn <= nv.luong <= mx]
    print_table(kq, f"NHÂN VIÊN CÓ LƯƠNG TRONG [{mn} .. {mx}]")

def y7():
    print("→ [Y7] Sắp xếp theo họ và tên (ưu tiên Tên rồi Họ)")
    ds = read_all()
    ds_sorted = sorted(ds, key=lambda nv: _split_name(nv.ho_ten))
    print_table(ds_sorted, "DANH SÁCH SAU KHI SẮP XẾP THEO HỌ & TÊN")

def y8():
    print("→ [Y8] Sắp xếp theo THU NHẬP (giảm dần)")
    ds = read_all()
    ds_sorted = sorted(ds, key=lambda nv: nv.getThuNhap(), reverse=True)
    print_table(ds_sorted, "DANH SÁCH THEO THU NHẬP ↓")

def y9():
    print("→ [Y9] Top 5 nhân viên có THU NHẬP cao nhất")
    ds = read_all()
    top5 = sorted(ds, key=lambda nv: nv.getThuNhap(), reverse=True)[:5]
    print_table(top5, "TOP 5 THU NHẬP CAO NHẤT")


def menu_quan_ly_nhan_vien():
    while True:
        print("\nMENU QUẢN LÝ NHÂN VIÊN (GĐ1+2)")
        print("1. Y1 - Nhập DS NV và lưu file")
        print("2. Y2 - Đọc NV từ file và xuất")
        print("3. Y3 - Tìm NV theo mã")
        print("4. Y4 - Xóa NV theo mã (cập nhật file)")
        print("5. Y5 - Cập nhật NV theo mã (ghi file)")
        print("6. Y6 - Tìm NV theo khoảng lương (lương cơ bản)")
        print("7. Y7 - Sắp xếp theo họ và tên")
        print("8. Y8 - Sắp xếp theo thu nhập")
        print("9. Y9 - Top 5 NV thu nhập cao")
        print("0. Thoát")
        chon = input("Nhập lựa chọn (0-9): ").strip()

        if   chon == "1": y1()
        elif chon == "2": y2()
        elif chon == "3": y3()
        elif chon == "4": y4()
        elif chon == "5": y5()
        elif chon == "6": y6()
        elif chon == "7": y7()
        elif chon == "8": y8()
        elif chon == "9": y9()
        elif chon == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")


if __name__ == "__main__":
    ensure_file()
    menu_quan_ly_nhan_vien()
