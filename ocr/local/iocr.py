'''
Author: feng
Date: 2021-07-15 16:27:22
LastEditors: mukangt
LastEditTime: 2021-08-04 15:10:47
Description: 
'''
import re
import fitz

PAT_CODE = '[0]{1}[0-9]{11}'
PAT_NUMBER = '^[0-9]{8}$'
PAT_DATE = '[0-9]{4}\D+[0-9]{2}\D+[0-9]{2}\D?'
PAT_CHECKCODE = '[0-9]{5}\s*[0-9]{5}\s*[0-9]{5}\s*[0-9]{5}\s*'

INVOICE_NUM = 1
TAX_NUM = '9132050508781783X7'


def ocr(filename, args=None):

    with fitz.open(filename) as doc:
        text = ""
        for page in doc:
            text += page.getText()
    text = text.split('\n')

    data = {}
    for item in text:
        if ("服务费" in item):
            data['发票种类'] = '增值税电子发票'
            data['发票种类代码'] = '10'
        elif ("通行费" in item):
            data['发票种类'] = '增值税电子普通发票（通行费）'
            data['发票种类代码'] = '18'
        elif ("成品油" in item):
            data['发票种类'] = '增值税电子发票'
            data['发票种类代码'] = '10'

        for pat in [PAT_CODE, PAT_NUMBER, PAT_DATE, PAT_CHECKCODE]:

            match = re.match(pat, item, flags=0)

            if match and pat == PAT_CODE:
                data['发票代码'] = match.string

            if match and pat == PAT_NUMBER:
                data['发票号码'] = match.string

            if match and pat == PAT_DATE:
                if len(match.string) == 11:
                    date = match.string.replace('年', '/').replace('月',
                                                                  '/').replace(
                                                                      '日', '')
                else:
                    date = "/".join(match.string.split())

                data['开票日期'] = date

            if match and pat == PAT_CHECKCODE:
                data['校验码'] = match.string.replace(' ', '')
                data['校验码后六位'] = match.string.replace(' ', '')[-6:]

        data['购方税号'] = TAX_NUM

        data['发票页码'] = 1

    return data


if __name__ == '__main__':
    print(ocr("1.pdf"))