class SanPham:
    def __init__(self, ten_sp: str, gia_ban: float, giam_gia: float):

        self.__ten_sp = ten_sp
        self.__gia_ban = gia_ban
        self.__giam_gia = giam_gia

    def get_ten_sp(self):
        return self.__ten_sp

    def set_ten_sp(self, _ten_sp):
        self.__ten_sp = _ten_sp

    def get_gia_ban(self):
        return self.__gia_ban

    def set_gia_ban(self, _gia_ban):
        self.__gia_ban = _gia_ban

    def get_giam_gia(self):
        return self.__giam_gia

    def set_giam_gia(self, _giam_gia):
        self.__giam_gia = _giam_gia

    def thue_nk(self):
        return self.__gia_ban * 0.1

    def nhap_sp(self):
        self.__ten_sp = input("Nhập tên sản phẩm: ")
        self.__gia_ban = float(input("Nhập giá bán: "))
        self.__giam_gia = float(input("Nhập giảm giá: "))

    def xuat_tt_sp(self):
        print(
            f"Tên sản phẩm: {self.__ten_sp}, "
            f"giá bán: {self.__gia_ban}, "
            f"giảm giá: {self.__giam_gia}, "
            f"thuế nhập khẩu: {self.thue_nk()}"
        )

    def __str__(self):
        return (
            f"Tên sản phẩm: {self.__ten_sp}, "
            f"giá bán: {self.__gia_ban}, "
            f"giảm giá: {self.__giam_gia}, "
            f"thuế nhập khẩu: {self.thue_nk()}"
        )

    def thue_nk(self): return self.__gia_ban * 0.1
    def xuat_tt_sp(self):
        print(f"Tên sản phẩm: {self.__ten_sp}, giá bán: {self.__gia_ban}, "
              f"giảm giá: {self.__giam_gia}, thuế nhập khẩu: {self.thue_nk()}")
    def __str__(self):
        return (f"Tên sản phẩm: {self.__ten_sp}, giá bán: {self.__gia_ban}, "
                f"giảm giá: {self.__giam_gia}, thuế nhập khẩu: {self.thue_nk()}")