import csv
import os
import datetime
import shutil
from typing import List, Dict, Any
FILENAME = "taikhoan.csv"
BACKUP_DIR = "backup"
TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"

class TaiKhoan:
    """Đại diện cho một tài khoản ngân hàng."""
    def __init__(self, soTaiKhoan: str, ten: str, loai: str, soDu: float):
        self.soTaiKhoan = soTaiKhoan
        self.ten = ten
        self.loai = loai.upper()
        self.soDu = soDu

    @staticmethod
    def taoTaiKhoan():
        """Tạo một đối tượng TaiKhoan mới từ input người dùng."""
        print("\n--- TẠO TÀI KHOẢN MỚI ---")
        
        soTaiKhoan = input("Nhập Số Tài Khoản (ví dụ: 12345): ").strip()
        ten = input("Nhập Tên Chủ Tài Khoản: ").strip()
        
        while True:
            loai = input("Nhập Loại Tài Khoản ('T' - Tiết kiệm, 'C' - Thường): ").strip().upper()
            if loai in ['T', 'C']:
                break
            print("Lỗi: Loại tài khoản phải là 'T' hoặc 'C'.")
            
        while True:
            try:
                soDu = float(input("Nhập Số Dư Ban Đầu: "))
                if soDu >= 0:
                    break
                print("Lỗi: Số dư ban đầu không được âm.")
            except ValueError:
                print("Lỗi: Số dư phải là một số.")

        return TaiKhoan(soTaiKhoan, ten, loai, soDu)

    def hienThiTaiKhoan(self):
        """Hiển thị chi tiết tài khoản."""
        loai_tk = "Tiết kiệm" if self.loai == 'T' else "Thường"
        print(f"| {self.soTaiKhoan:<15} | {self.ten:<30} | {loai_tk:<10} | {self.soDu:15,.2f} VND |")

    def guiTien(self, soTien: float):
        """Thêm số tiền vào số dư."""
        if soTien > 0:
            self.soDu += soTien
            print(f"-> Gửi thành công {soTien:,.2f} VND. Số dư mới: {self.soDu:,.2f} VND.")
        else:
            print("Lỗi: Số tiền gửi phải lớn hơn 0.")

    def rutTien(self, soTien: float):
        """Trừ số tiền khỏi số dư (có kiểm tra)."""
        if soTien <= 0:
            print("Lỗi: Số tiền rút phải lớn hơn 0.")
            return False
            
        if self.soDu >= soTien:
            self.soDu -= soTien
            print(f"-> Rút thành công {soTien:,.2f} VND. Số dư mới: {self.soDu:,.2f} VND.")
            return True
        else:
            print(f"Lỗi: Số dư không đủ ({self.soDu:,.2f} VND). Không thể rút {soTien:,.2f} VND.")
            return False

    def toDict(self) -> Dict[str, Any]:
        """Chuyển đổi đối tượng TaiKhoan thành dictionary."""
        return {
            "soTaiKhoan": self.soTaiKhoan,
            "ten": self.ten,
            "loai": self.loai,
            "soDu": self.soDu
        }

    @staticmethod
    def fromDict(data: Dict[str, Any]):
        """Tạo đối tượng TaiKhoan từ dictionary."""
        return TaiKhoan(
            soTaiKhoan=data['soTaiKhoan'],
            ten=data['ten'],
            loai=data['loai'],
            soDu=float(data['soDu'])
        )



def docTaiKhoanTuCSV() -> List[TaiKhoan]:
    """Đọc dữ liệu tài khoản từ file CSV."""
    danhSachTK: List[TaiKhoan] = []
    if not os.path.exists(FILENAME): return danhSachTK
    try:
        with open(FILENAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                danhSachTK.append(TaiKhoan.fromDict(row))
        return danhSachTK
    except Exception as e:
        print(f"Lỗi khi đọc file CSV: {e}")
        return []

def ghiTaiKhoanVaoCSV(danhSach: List[TaiKhoan]):
    """Ghi danh sách các đối tượng TaiKhoan vào file CSV."""
    try:
        with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['soTaiKhoan', 'ten', 'loai', 'soDu']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for tk in danhSach:
                writer.writerow(tk.toDict())
        print(f"-> Đã cập nhật thành công dữ liệu vào file {FILENAME}.")
    except Exception as e:
        print(f"Lỗi khi ghi file CSV: {e}")



def timTaiKhoan(danhSach: List[TaiKhoan], soTK: str) -> TaiKhoan | None:
    """Hàm tiện ích để tìm kiếm tài khoản theo số tài khoản."""
    for tk in danhSach:
        if tk.soTaiKhoan == soTK:
            return tk
    return None

def hienThiBang(danhSach: List[TaiKhoan]):
    """Hiển thị danh sách tài khoản dưới dạng bảng."""
    if not danhSach:
        print("\n*** Danh sách tài khoản rỗng. ***")
        return

    print("\n" + "="*70)
    print(f"| {'SỐ TÀI KHOẢN':<15} | {'TÊN CHỦ TÀI KHOẢN':<30} | {'LOẠI':<10} | {'SỐ DƯ (VND)':<15} |")
    print("="*70)
    for tk in danhSach:
        tk.hienThiTaiKhoan()
    print("="*70)
    print(f"Tổng số tài khoản: {len(danhSach)}")


def chucNang1_TaoTaiKhoan(danhSach: List[TaiKhoan]):
    """1. TẠO TÀI KHOẢN MỚI"""
    while True:
        try:
            tk_moi = TaiKhoan.taoTaiKhoan()
            if timTaiKhoan(danhSach, tk_moi.soTaiKhoan):
                print(f"Lỗi: Số Tài Khoản '{tk_moi.soTaiKhoan}' đã tồn tại.")
            else:
                danhSach.append(tk_moi)
                ghiTaiKhoanVaoCSV(danhSach)
                break
        except Exception as e:
            print(f"Lỗi xảy ra khi tạo tài khoản: {e}")
            break


def chucNang2_GuiTien(danhSach: List[TaiKhoan]):
    """2. GỬI TIỀN"""
    print("\n--- GỬI TIỀN ---")
    soTK = input("Nhập Số Tài Khoản cần gửi tiền: ").strip()
    tk = timTaiKhoan(danhSach, soTK)
    
    if tk:
        try:
            soTien = float(input("Nhập Số Tiền cần gửi: "))
            tk.guiTien(soTien)
            ghiTaiKhoanVaoCSV(danhSach)
        except ValueError:
            print("Lỗi: Số tiền không hợp lệ.")
    else:
        print(f"Lỗi: Không tìm thấy Tài Khoản với số '{soTK}'.")


def chucNang3_RutTien(danhSach: List[TaiKhoan]):
    """3. RÚT TIỀN"""
    print("\n--- RÚT TIỀN ---")
    soTK = input("Nhập Số Tài Khoản cần rút tiền: ").strip()
    tk = timTaiKhoan(danhSach, soTK)
    
    if tk:
        try:
            soTien = float(input("Nhập Số Tiền cần rút: "))
            if tk.rutTien(soTien):
                ghiTaiKhoanVaoCSV(danhSach)
        except ValueError:
            print("Lỗi: Số tiền không hợp lệ.")
    else:
        print(f"Lỗi: Không tìm thấy Tài Khoản với số '{soTK}'.")


def chucNang4_KiemTraSoDu(danhSach: List[TaiKhoan]):
    """4. KIỂM TRA SỐ DƯ"""
    print("\n--- KIỂM TRA SỐ DƯ ---")
    soTK = input("Nhập Số Tài Khoản cần kiểm tra: ").strip()
    tk = timTaiKhoan(danhSach, soTK)
    
    if tk:
        print("\n--- THÔNG TIN CHI TIẾT ---")
        hienThiBang([tk])
    else:
        print(f"Lỗi: Không tìm thấy Tài Khoản với số '{soTK}'.")


def chucNang6_DongTaiKhoan(danhSach: List[TaiKhoan]):
    """6. ĐÓNG (XÓA) TÀI KHOẢN"""
    print("\n--- ĐÓNG (XÓA) TÀI KHOẢN ---")
    soTK = input("Nhập Số Tài Khoản muốn đóng: ").strip()
    
    index_to_delete = -1
    for i, tk in enumerate(danhSach):
        if tk.soTaiKhoan == soTK:
            index_to_delete = i
            break
            
    if index_to_delete != -1:
        tk_bi_xoa = danhSach.pop(index_to_delete)
        ghiTaiKhoanVaoCSV(danhSach)
        print(f"-> Đã đóng và xóa Tài Khoản '{tk_bi_xoa.ten}' ({soTK}) thành công.")
    else:
        print(f"Lỗi: Không tìm thấy Tài Khoản với số '{soTK}'.")


def chucNang7_ChinhSuaTaiKhoan(danhSach: List[TaiKhoan]):
    """7. CHỈNH SỬA TÀI KHOẢN"""
    print("\n--- CHỈNH SỬA TÀI KHOẢN ---")
    soTK = input("Nhập Số Tài Khoản muốn chỉnh sửa: ").strip()
    tk = timTaiKhoan(danhSach, soTK)

    if tk:
        print("Tài khoản hiện tại:")
        hienThiBang([tk])
        
        ten_moi = input(f"Nhập Tên mới (Enter để giữ nguyên: '{tk.ten}'): ").strip()
        if ten_moi:
            tk.ten = ten_moi
            
        while True:
            loai_moi = input(f"Nhập Loại mới ('T'/'C', Enter để giữ nguyên: '{tk.loai}'): ").strip().upper()
            if not loai_moi:
                break
            if loai_moi in ['T', 'C']:
                tk.loai = loai_moi
                break
            print("Lỗi: Loại tài khoản phải là 'T' hoặc 'C'.")
            
        while True:
            soDu_moi_str = input(f"Nhập Số dư mới (Enter để giữ nguyên: {tk.soDu:,.2f}): ").strip()
            if not soDu_moi_str:
                break
            try:
                soDu_moi = float(soDu_moi_str)
                if soDu_moi >= 0:
                    tk.soDu = soDu_moi
                    break
                print("Lỗi: Số dư không được âm.")
            except ValueError:
                print("Lỗi: Số dư phải là một số.")
                
        ghiTaiKhoanVaoCSV(danhSach)
        print("\n-> Cập nhật tài khoản thành công.")
        
    else:
        print(f"Lỗi: Không tìm thấy Tài Khoản với số '{soTK}'.")


def chucNang8_TimKiemTheoTen(danhSach: List[TaiKhoan]):
    """8. TÌM KIẾM THEO TÊN"""
    print("\n--- TÌM KIẾM THEO TÊN ---")
    tu_khoa = input("Nhập từ khóa Tên cần tìm kiếm: ").strip().lower()
    
    ket_qua = []
    for tk in danhSach:
        if tu_khoa in tk.ten.lower():
            ket_qua.append(tk)
            
    if ket_qua:
        print(f"\n-> Tìm thấy {len(ket_qua)} tài khoản chứa từ khóa '{tu_khoa}':")
        hienThiBang(ket_qua)
    else:
        print(f"-> Không tìm thấy tài khoản nào có tên chứa từ khóa '{tu_khoa}'.")


def chucNang9_XuatBaoCao(danhSach: List[TaiKhoan]):
    """9. XUẤT BÁO CÁO"""
    print("\n--- XUẤT BÁO CÁO THỐNG KÊ ---")
    
    tong_tai_khoan = len(danhSach)
    tong_so_du = sum(tk.soDu for tk in danhSach)
    
    so_tk_tiet_kiem = sum(1 for tk in danhSach if tk.loai == 'T')
    so_tk_thuong = tong_tai_khoan - so_tk_tiet_kiem
    
    bao_cao_content = f"""
==================================================
        BÁO CÁO THỐNG KÊ HỆ THỐNG TÀI KHOẢN
==================================================
Thời gian báo cáo: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

1. TỔNG QUAN
- Tổng số Tài Khoản trong hệ thống: {tong_tai_khoan}
- Tổng Số Dư tích lũy: {tong_so_du:,.2f} VND

2. PHÂN LOẠI TÀI KHOẢN
- Tài Khoản Tiết kiệm ('T'): {so_tk_tiet_kiem} tài khoản
- Tài Khoản Thường ('C'):    {so_tk_thuong} tài khoản
==================================================
"""
    
    timestamp = datetime.datetime.now().strftime(TIMESTAMP_FORMAT)
    report_filename = f"bao_cao_{timestamp}.txt"
    
    try:
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write(bao_cao_content)
        print(f"-> Đã xuất báo cáo thành công vào file: {report_filename}")
    except Exception as e:
        print(f"Lỗi khi xuất báo cáo: {e}")


def chucNang10_SaoLuuDuLieu():
    """10. SAO LƯU DỮ LIỆU"""
    print("\n--- SAO LƯU DỮ LIỆU ---")
    
    if not os.path.exists(FILENAME):
        print(f"Lỗi: Không tìm thấy file nguồn '{FILENAME}' để sao lưu.")
        return

    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        print(f"Đã tạo thư mục sao lưu: {BACKUP_DIR}/")

    timestamp = datetime.datetime.now().strftime(TIMESTAMP_FORMAT)
    backup_filename = f"taikhoan_backup_{timestamp}.csv"
    backup_filepath = os.path.join(BACKUP_DIR, backup_filename)
    
    try:
        shutil.copyfile(FILENAME, backup_filepath)
        print(f"-> Sao lưu thành công file '{FILENAME}' vào: {backup_filepath}")
    except Exception as e:
        print(f"Lỗi khi sao lưu: {e}")


def chucNang11_KhoiPhucDuLieu(danhSach):
    """11. KHÔI PHỤC DỮ LIỆU"""
    print("\n--- KHÔI PHỤC DỮ LIỆU ---")
    
    if not os.path.exists(BACKUP_DIR) or not os.listdir(BACKUP_DIR):
        print(f"Lỗi: Không tìm thấy thư mục sao lưu hoặc thư mục trống: {BACKUP_DIR}/")
        return

    print("Danh sách các file sao lưu khả dụng:")
    backup_files = [f for f in os.listdir(BACKUP_DIR) if f.endswith('.csv') and f.startswith('taikhoan_backup_')]
    
    if not backup_files:
        print("Không tìm thấy file sao lưu nào.")
        return danhSach # Trả về danh sách hiện tại
        
    for i, f in enumerate(backup_files):
        print(f"{i+1}. {f}")
        
    while True:
        try:
            chon = input("Chọn số thứ tự file muốn khôi phục (hoặc '0' để Hủy): ")
            if chon == '0':
                print("Hủy khôi phục.")
                return danhSach
                
            index = int(chon) - 1
            if 0 <= index < len(backup_files):
                selected_file = backup_files[index]
                source_filepath = os.path.join(BACKUP_DIR, selected_file)
                
                shutil.copyfile(source_filepath, FILENAME)
                print(f"-> Khôi phục thành công '{selected_file}' thành file '{FILENAME}' chính.")
                # Tải lại danh sách tài khoản sau khi khôi phục
                return docTaiKhoanTuCSV()
                
            else:
                print("Lựa chọn không hợp lệ.")
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")
        except Exception as e:
            print(f"Lỗi khi khôi phục: {e}")
            return danhSach



def main():
    # Tải dữ liệu ban đầu
    danhSachTaiKhoan: List[TaiKhoan] = docTaiKhoanTuCSV()
    print("----------------------------------------------------------------------")
    print(f"Đã tải {len(danhSachTaiKhoan)} tài khoản từ file '{FILENAME}'.")
    print("----------------------------------------------------------------------")

    while True:
        print("\n====================== MENU QUẢN LÝ TÀI KHOẢN ======================")
        print("1. TẠO TÀI KHOẢN MỚI")
        print("2. GỬI TIỀN")
        print("3. RÚT TIỀN")
        print("4. KIỂM TRA SỐ DƯ")
        print("5. DANH SÁCH TẤT CẢ TK")
        print("6. ĐÓNG (XÓA) TÀI KHOẢN")
        print("7. CHỈNH SỬA TÀI KHOẢN")
        print("8. TÌM KIẾM THEO TÊN")
        print("9. XUẤT BÁO CÁO")
        print("10. SAO LƯU DỮ LIỆU")
        print("11. KHÔI PHỤC DỮ LIỆU")
        print("12. THOÁT")
        print("======================================================================")
        
        chon = input("Nhập lựa chọn của bạn (1-12): ").strip()

        try:
            if chon == '1':
                chucNang1_TaoTaiKhoan(danhSachTaiKhoan)
            elif chon == '2':
                chucNang2_GuiTien(danhSachTaiKhoan)
            elif chon == '3':
                chucNang3_RutTien(danhSachTaiKhoan)
            elif chon == '4':
                chucNang4_KiemTraSoDu(danhSachTaiKhoan)
            elif chon == '5':
                hienThiBang(danhSachTaiKhoan)
            elif chon == '6':
                chucNang6_DongTaiKhoan(danhSachTaiKhoan)
            elif chon == '7':
                chucNang7_ChinhSuaTaiKhoan(danhSachTaiKhoan)
            elif chon == '8':
                chucNang8_TimKiemTheoTen(danhSachTaiKhoan)
            elif chon == '9':
                chucNang9_XuatBaoCao(danhSachTaiKhoan)
            elif chon == '10':
                chucNang10_SaoLuuDuLieu()
            elif chon == '11':
                # Chức năng 11 cần cập nhật danh sách sau khi khôi phục
                danhSachTaiKhoan = chucNang11_KhoiPhucDuLieu(danhSachTaiKhoan)
            elif chon == '12':
                print("\nCảm ơn bạn đã sử dụng Hệ thống Quản lý Tài Khoản. Tạm biệt!")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 12.")
        
        except Exception as e:
            print(f"Đã xảy ra lỗi không mong muốn: {e}")

if __name__ == "__main__":
    main()
