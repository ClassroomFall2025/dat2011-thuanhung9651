
#xếp học lực
class SinhVienPoly:
    def __init__(self, ten_sinh_vien, nganh_hoc):
        self.ten_sinh_vien = ten_sinh_vien
        self.nganh_hoc = nganh_hoc
    def get_diem(self):
        pass
    def get_hoc_luc(self):
        if self.get_diem() >= 9 and self.get_diem() <=10:
            return "xuất sắc"
        elif self.get_diem() >=8:
            return "giỏi"
        elif self.get_diem() >= 7:
            return "khá"
        elif self.get_diem() >=5:
            return "trung bình"
        else:
            return "chưa đạt"
    #Xuất 
    def xuat_tt(self):
        print(f"{self.ten_sinh_vien:<20} {self.nganh_hoc:<10} {self.get_diem():<10} {self.get_hoc_luc():10}")
    def __str__(self):
        return f"{self.ten_sinh_vien:<20} {self.nganh_hoc:<10} {self.get_diem():<10} {self.get_hoc_luc():10}"

#bài 3
class SinhVienIT(SinhVienPoly):
    def __init__(self, ten_sinh_vien, nganh_hoc, java, html, css):
        super().__init__(ten_sinh_vien, nganh_hoc)
        self.java = java
        self.html = html
        self.css = css
    def get_diem(self):
        return (self.java*2 + self.html + self.css)/4
    
class SinhVienBiz(SinhVienPoly):
    def __init__(self, ten_sinh_vien, nganh_hoc, marketing, sales):
        super().__init__(ten_sinh_vien, nganh_hoc)
        self.marketing = marketing
        self.sales = sales
    def get_diem(self):
        return (self.marketing *2 + self.sales)/3
