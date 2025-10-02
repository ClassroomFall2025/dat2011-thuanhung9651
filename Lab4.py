#tính tiền nước
def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500 , 8800, 12000, 14000)
    if so_nuoc <=10:
        tien_nuoc= so_nuoc * gia_ban_nuoc [0]
    elif so_nuoc <=20:
        tien_nuoc= 10 * gia_ban_nuoc[0] + (so_nuoc - 10) * gia_ban_nuoc[1]
    elif so_nuoc <=30:
        tien_nuoc=10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_nuoc - 20) * gia_ban_nuoc[2] 
    else:
        tien_nuoc=10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (so_nuoc -30 ) * gia_ban_nuoc[3]
    return tien_nuoc  

#tính nguyên liệu làm bánh
def tinh_nguyen_lieu(sl_bdx, sl_btc, sl_bd):
    banh_dau_xanh = {"Đường" :0.04, "Đậu" :0.07}
    banh_thap_cam = {"Đường" :0.06, "Đậu" :0}
    banh_deo = {"Đường" :0.05, "Đậu" :0.02}
    nguyen_lieu = {}
    duong_hop_banh = sl_bdx * banh_dau_xanh["Đường"] + sl_btc * banh_thap_cam["Đường"] + sl_bd * banh_deo["Đường"]
    dau_hop_banh = sl_bdx * banh_dau_xanh["Đậu"] + sl_btc * banh_thap_cam["Đậu"] + sl_bd * banh_deo["Đậu"]
    nguyen_lieu["Đường"] = duong_hop_banh
    nguyen_lieu["Đậu"] = dau_hop_banh
    return nguyen_lieu