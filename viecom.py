#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import requests

fRunned = open("demofile2.txt", "r")
lines = fRunned.readlines()
listRunned = []
for line in lines:
    listRunned.append(int(line[:3]))

listTinh = {467: "Hà Nội",
            466: "Hồ Chí Minh",
            502: "An Giang ",
            460: "Bà Rịa - Vũng Tàu",
            508: "Bạc Liêu",
            509: "Bắc Giang",
            507: "Bắc Ninh",
            506: "Bến Tre",
            459: "Bình Dương",
            480: "Bình Định",
            505: "Bình Phước",
            504: "Bình Thuận",
            503: "Cà Mau",
            471: "Cần Thơ",
            489: "Đà Nẵng",
            501: "Đắk Lắk",
            485: "Đồng Nai",
            500: "Đồng Tháp",
            499: "Gia Lai",
            498: "Hà Nam",
            497: "Hà Tĩnh",
            496: "Hải Dương",
            487: "Hải Phòng",
            482: "Hưng Yên",
            481: "Kiên Giang",
            494: "Kon Tum",
            486: "Khánh Hoà",
            492: "Lạng Sơn",
            491: "Lào Cai",
            493: "Lâm Đồng",
            490: "Long An",
            488: "Nam Định",
            484: "Ninh Bình",
            483: "Ninh Thuận",
            463: "Nghệ An",
            479: "Phú Thọ",
            478: "Phú Yên",
            477: "Quảng Bình",
            476: "Quảng Nam",
            474: "Quảng Ninh",
            475: "Quảng Ngãi",
            473: "Quảng Trị",
            472: "Sóc Trăng",
            470: "Tây Ninh",
            465: "Tiền Giang",
            457: "Tuyên Quang",
            469: "Thái Bình",
            468: "Thái Nguyên",
            458: "Thanh Hóa",
            495: "Thừa Thiên - Huế",
            464: "Trà Vinh",
            462: "Vĩnh Long",
            461: "Vĩnh Phúc"}

for tinh in listTinh.keys():
    try:
        f = open("demofile2.txt", "a")
        print tinh
        if tinh in listRunned:
            continue
        listChiNhanh = 'https://portal.vietcombank.com.vn/UserControls/TVPortal.MangLuoiDiemGiaoDich/Action.ashx?Action=getQuanHuyenByTinhThanh&t=' + str(
            tinh) + '&url=/content/Network/Lists/QuanHuyen'
        res = requests.get(listChiNhanh, verify=False)
        listQuan = json.loads(res.json()['Title'])
        num = 0
        for quan in listQuan:
            print quan
            resQuan = requests.get(
                'https://portal.vietcombank.com.vn/UserControls/TVPortal.MangLuoiDiemGiaoDich/Actionnew.ashx?s=&x1=0&y1=0&urlmangluoi=/content/Network/Lists/DiemATM&Action=getdsatm&loai=2&t='
                + str(
                    tinh) + '&c=0&checkidmap=0&q=' + str(quan['ID']) + '&urlqh=/content/Network/Lists/QuanHuyen&urltt=/content/Network/Lists/TinhThanhPho', verify=False)
            listAtm = json.loads(resQuan.json()['Title'])
            num += len(listAtm)
        f.write(str(tinh) + ' ' + listTinh[tinh] + ' ' + str(num) + '\n')
        f.close()
    except BaseException as e:
        print e

