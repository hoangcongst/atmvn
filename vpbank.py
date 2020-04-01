import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
params = {
    'view_name': 'chi_nhanh_atm',
    'view_display_id': 'page',
    'view_args': '',
    'view_path': 'locations',
    'view_base_path': 'locations',
    'view_dom_id': '70c3a5a09598a7e7def17e05e63a382b',
    'pager_element': '0',
}

for page in range(0, 31):
    params['page'] = str(page)
    res = requests.post('https://www.vpbank.com.vn/views/ajax', params).json()
    res = res[2]['data']
    f = open('raw-vpbank/vpbank' + str(page) + '.html', 'w')
    f.write(res)
    f.close()
