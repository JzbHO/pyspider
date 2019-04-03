
from bs4 import BeautifulSoup
from urllib import request, parse
import time
import http.cookiejar
from xlwt import *

# response = urllib.request.urlopen('https://www.baidu.com/')
#
# print(response.getcode())
#
# cont = response.read()
#
# print(cont)


#请求提交数据和请求头
# data = {'a': '1'}
# data = parse.urlencode(data).encode('utf-8')
# headers = {'User-Agent': 'Mozilla/5.0'}

# cookie = http.cookiejar.CookieJar()
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
#
# response = opener.open('https://www.douban.com/')
# for item in cookie:
#     print('Name = '+item.name)
#     print('Value = '+item.value)

dict1 = {"a":1}
dict1['aaa']=2
for d , x in dict1.items():
    print(d+str(x))



ws = Workbook(encoding='utf-8')
w = ws.add_sheet("评论数据")
w.write(0,0,"评论日期")
w.write(0,1,"评论数量")


#agent 存在问题，因此抓取不到数据
urlCollection = {'https://movie.douban.com/subject/4840388/comments'}


# url = "https://movie.douban.com/subject/4840388/comments"
# print(url)
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Cookie': 'bid=7uzaaRDIPag; douban-fav-remind=1; _vwo_uuid_v2=D67ADE5CB4AC75F187A1B7A3ECB1911ED|8397e10994edfd7a6a4b36235429dc08; ll="108120"; gr_user_id=b2e45264-e31a-4ea6-b609-d425f2141922; __yadk_uid=lLLIb0FkMXok2KnekkHwsOrTpfAZDoYw; viewed="25779298_26383653_4817744_5912334_1017157_26656350_1961913_27179953_27170483_30365801"; __utmc=30149280; __utmc=223695111; push_doumail_num=0; _ga=GA1.2.1259078594.1543152693; _gid=GA1.2.1988960070.1554283868; __utmv=30149280.17320; push_noty_num=0; dbcl2="173203890:TsXyaJN4SMI"; ck=G_uN; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1554288028%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fredir%3Dhttps%253A%252F%252Fmovie.douban.com%252F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1259078594.1543152693.1554283452.1554288028.30; __utmb=30149280.0.10.1554288028; __utmz=30149280.1554288028.30.28.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utma=223695111.1773724212.1544459933.1554283506.1554288028.8; __utmb=223695111.0.10.1554288028; __utmz=223695111.1554288028.8.7.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; _pk_id.100001.4cf6=c677784fadd8c8d1.1544459934.8.1554288036.1554283518.'

}
# response = request.urlopen(req)
# content = response.read().decode('utf-8')
# print(content)




# headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36',
#            'Cookie': 'bid=7uzaaRDIPag; douban-fav-remind=1; _vwo_uuid_v2=D67ADE5CB4AC75F187A1B7A3ECB1911ED|8397e10994edfd7a6a4b36235429dc08; ll="108120"; gr_user_id=b2e45264-e31a-4ea6-b609-d425f2141922; __yadk_uid=lLLIb0FkMXok2KnekkHwsOrTpfAZDoYw; viewed="25779298_26383653_4817744_5912334_1017157_26656350_1961913_27179953_27170483_30365801"; __utmc=30149280; __utmc=223695111; push_doumail_num=0; _ga=GA1.2.1259078594.1543152693; _gid=GA1.2.1988960070.1554283868; __utmv=30149280.17320; push_noty_num=0; dbcl2="173203890:TsXyaJN4SMI"; ck=G_uN; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1554288028%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fredir%3Dhttps%253A%252F%252Fmovie.douban.com%252F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1259078594.1543152693.1554283452.1554288028.30; __utmb=30149280.0.10.1554288028; __utmz=30149280.1554288028.30.28.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utma=223695111.1773724212.1544459933.1554283506.1554288028.8; __utmb=223695111.0.10.1554288028; __utmz=223695111.1554288028.8.7.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; _pk_id.100001.4cf6=c677784fadd8c8d1.1544459934.8.1554288036.1554283518.'
#            }




dict = {}

while(urlCollection.__len__()!=0):
    tempUrl = urlCollection.pop()
    print(tempUrl)
    req = request.Request(tempUrl, headers=headers)

    page = request.urlopen(req).read()



    soup = BeautifulSoup(page.decode('utf-8'), 'html.parser')

    comments = soup.find_all("span", class_="comment-time")

    print(comments.__len__())
    for comment in comments:
        date=comment.get_text()
        print(date)
        if(date in dict):
            dict[date] += 1
        else:
            dict[date] = 1

    links = soup.select('.next')

    try:
        if (links.__len__()>0):
            for link in links:
                if(link['href']):
                    urlCollection.add("https://movie.douban.com/subject/4840388/comments"+link['href'])
    except :
        break


linecount=1
for d,x in  dict.items():
    print(d+str(x))
    w.write(linecount,0,d)
    w.write(linecount,1,str(x))
    linecount+=1

ws.save("测试数据20191.xls")

