from bs4 import BeautifulSoup
from urllib import request, parse
import time
import urllib
import http.cookiejar
from xlwt import *
import json
import re
ws = Workbook(encoding='utf-8')


# agent 存在问题，因此抓取不到数据
urlCollection = {
'https://goods.kaola.com/product/2260540.html?kpm=MTAwMg==.Nzg2Ng==.MTMwMjE1.MQ==@@djEuMTAwMi4xMDAyX3BfMjI2MDU0MC5fLmxlZ29f'}

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/73.0.3683.86 Mobile Safari/537.36',
    'Cookie': 'davisit=24; usertrack=CrHtiFvm9LxkO3jQAzkvAg==; kaola_user_key=1953e336-8975-4c1b-84f2-1dfa10d10ead; __kaola_usertrack=20181111124444731477; _da_ntes_uid=20181111124444731477; _ntes_nnid=86691e8447e6f115707a4dd97cc07a92,1541911485794; __da_ntes_utma=2525167.578633789.1553311600.1553311600.1553311600.1; davisit=1; __da_ntes_utmz=2525167.1553311600.1.1.utmcsr%3Dweex.kaola.com%7Cutmccn%3D(prom)%7Cutmcmd%3Dprom%7Cutmpclid%3Dklzkheader%3D1%26noklfooter%3D1%26tag%3D__ta_zhuanke_03%26__da_dad3e203_592c1e770e033c80%26__da_dad3e203_592c1e770e033c80%26unionId%3Dzhuanke_700045446%26euid%3D%2522%2522%26mid%3D%2522%2522%26from_zk%3D1; __da_ntes_utmfc=utmcsr%3Dweex.kaola.com%7Cutmccn%3D(prom)%7Cutmcmd%3Dprom%7Cutmpclid%3Dklzkheader%3D1%26noklfooter%3D1%26tag%3D__ta_zhuanke_03%26__da_dad3e203_592c1e770e033c80%26__da_dad3e203_592c1e770e033c80%26unionId%3Dzhuanke_700045446%26euid%3D%2522%2522%26mid%3D%2522%2522%26from_zk%3D1; _klhtxd_=31; JSESSIONID-WKL-8IO=6wG5okMHD2GzkIbzpw85%2Fa5v7DrcURcOMC4rPXPvegIEB9laOtoEuYVYQa4Mwu%5CeMQBEjWrNLY8054hW2YJNw6twl5p9rjb3J5Iw3ROcHR%2FWLYsSqto2gH%2BSkXDl%5Cpxk3k1jxc%5CSAmrDyIOs7y4BO9j%2B3HIZ3AM%2BMQoLWCkSeBH5NqpI%3A1554648872867; KAOLA_NEW_USER_COOKIE=yes; _ga=GA1.2.1564144905.1554562474; _gid=GA1.2.842631349.1554562474; _jzqx=1.1554562480.1554562480.1.jzqsr=kaola%2Ecom|jzqct=/.-; _jzqckmp=1; P_INFO=ojk_rulfmz29f8073e8ca12bd878cc073f11b690e0@wx.163.com|1554562493|0|kaola|00&99|null#0|null|kaola|ojk_rulfmz29f8073e8ca12bd878cc073f11b690e0@wx.163.com; KAOLA_ACC=ojk_rulfmz29f8073e8ca12bd878cc073f11b690e0@wx.163.com; _ntes_nuid=de44a2db8d4f17d3d50b99bb9e9f2357; NETEASE_WDA_UID="ojk_rulfmz29f8073e8ca12bd878cc073f11b690e0@wx.163.com#|#1531071783960"; __da_ntes_utmb=2525167.1.10.1554562492; hb_MA-930E-151AE827FE90_source=buy.kaola.com; WM_TID=Ayvi0zsELtdFUEUQQUJ9hvoPGCKKc9M8; _ga=GA1.3.1564144905.1554562474; _gid=GA1.3.842631349.1554562474; __da_ntes_utma=2525167.578633789.1553311600.1553311600.1553311600.1; __da_ntes_utmb=2525167.2.10.1554562492; __da_ntes_utmz=2525167.1553311600.1.1.utmcsr%3Dweex.kaola.com%7Cutmccn%3D(prom)%7Cutmcmd%3Dprom%7Cutmpclid%3Dklzkheader%3D1%26noklfooter%3D1%26tag%3D__ta_zhuanke_03%26__da_dad3e203_592c1e770e033c80%26__da_dad3e203_592c1e770e033c80%26unionId%3Dzhuanke_700045446%26euid%3D%2522%2522%26mid%3D%2522%2522%26from_zk%3D1; hb_MA-AE38-1FCC6CD7201B_source=goods.kaola.com; _gat=1; _qzjc=1; _jzqa=1.2358534182298819600.1554562480.1554562480.1554564640.2; _jzqc=1; NTES_KAOLA_ADDRESS_CONTROL=420000|420100|420102|1; _dc_gtm_UA-60320154-1=1; _dc_gtm_UA-60320154-1=1; _qzja=1.352731545.1554562779637.1554562779638.1554564640035.1554564656704.1554564670852..0.0.10.2; _qzjb=1.1554562779637.10.0.0.0; _qzjto=10.2.0; _jzqb=1.7.10.1554564640.1; NTES_KAOLA_RV=2260540_1554564670926_0'
}
dict = {}
timedict = {}
pageNo = 1
pageSize = 20

goodIds = ['2260540', '2062796']
#commentLimit = [1690, 2457]
commentLimit = [1000, 1000]
index = 0

for goodIs in goodIds:
    limit = commentLimit[index]
    while(limit>0):
            #成功获取response
        postdata = urllib.parse.urlencode({'goodsId':goodIs,'pageSize':pageSize,'pageNo':pageNo})

        postdata = postdata.encode('utf-8')
        res = urllib.request.urlopen('https://goods.kaola.com/commentAjax/comment_list_new.json',postdata)

        line = res.read().decode('utf-8')
        matchObj = re.match(r'(.*)"commentType":1,"createTime":(\d*)', line, re.M|re.I)

        p = re.compile(r'"commentType":1,"createTime":\d*')
        newline = str(p.findall(line))
        newp = re.compile(r'\d{2,}')
        timelists = newp.findall(newline)

        for timelist in timelists:
            commentTime = int(timelist) / 1000
            timeArray = time.localtime(commentTime)
            otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
            if(otherStyleTime in timedict):
                timedict[otherStyleTime] += 1
            else:
                timedict[otherStyleTime] = 1
            print(otherStyleTime)
        limit-=1
        pageNo+=1

    linecount = 1
    w = ws.add_sheet("商品"+str(index))
    w.write(0, 0, "评论日期")
    w.write(0, 1, "评论数量")
    for d, x in timedict.items():
        w.write(linecount, 0, d)
        w.write(linecount, 1, x)
        linecount += 1

    timedict={}

    index+=1


ws.save("测试数据20191.xls")
