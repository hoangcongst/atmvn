#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
locations = []
for page in range(0, 31):
    f = open('raw-vpbank/vpbank' + str(page) + '.html', 'r')

    content = f.read()
    nameAtm = re.findall("""<span class="field-content">(.*?)<span class="location-type">(.*?)</span></span>""",
                         content)
    locationsRe = re.findall("""<div class="field-content">(.*?)</div>""", content)

    for i in range(0, len(locationsRe)):
        locations.append({'name': nameAtm[i][0], 'type': nameAtm[i][1], 'location': locationsRe[i]})
    f.close()

final = {

}


def getCity(location):
    locationsRe = re.findall("([^,]*$)", location)
    return locationsRe[0].replace("Tỉnh", "").replace("tỉnh", "").replace("TP", "")\
        .replace("Tp", "").replace("Thành phố", "").replace("thành phố", "") \
        .replace("HN", "Hà Nội").replace("HCM", "Hồ Chí Minh").replace("BN", "Bắc Ninh").replace(".", "").strip()

total = 0
for location in locations:
    if 'ATM' not in location['type']:
        continue
    total += 1
    city = getCity(location['location'])
    if city in final:
        final[city] += 1
    else:
        final[city] = 1

print total
print final

f = open('vpbankfinal.txt', 'w')
f.write('TOTAL: ' + str(total) + '\n')
for key in final.keys():
    f.write(key + '  ' + str(final[key]) + '\n')
f.close()