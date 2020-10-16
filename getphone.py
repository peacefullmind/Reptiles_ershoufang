import requests
import re

headers = {
    'Referer': 'https://uutool.cn/phone-generate/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
}

params = (
    ('v', '2'),
)

response = requests.get('https://uutool.cn/assets/js/tools/phone_generate.min.js', headers=headers, params=params).text
print(response)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://uutool.cn/assets/js/tools/phone_generate.min.js?v=2', headers=headers)
re_result='areaArr:(.*?)segmentArr:'
re_data=re.findall(re_result,response,re.S)

print(re_data)