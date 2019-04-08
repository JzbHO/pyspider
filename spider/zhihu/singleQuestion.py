from bs4 import BeautifulSoup
from urllib import request, parse
import time
import urllib
import http.cookiejar
from xlwt import *
import json
import re


urlCollection = {'https://www.zhihu.com/api/v4/questions/304927212/answers'}
beginUrl = 'https://www.zhihu.com/api/v4/questions/304927212/answers'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/73.0.3683.86 Mobile Safari/537.36',
    'Cookie':'_zap=04b90d85-62c6-4170-af47-1c73387c915a; d_c0="AIAkFxIUaA6PTpze7O6t5TVD-rbf3Sw0QgA=|1540282751"; __gads=ID=b8c9efb415b5bb86:T=1541413856:S=ALNI_Mb0QPjzZC5D2D4pqssQwV50dzcNwQ; _xsrf=NQgP0v87vtliRIqBdM7yIMhmlrlPXU4Y; z_c0="2|1:0|10:1551448587|4:z_c0|92:Mi4xdXl2V0FnQUFBQUFBZ0NRWEVoUm9EaVlBQUFCZ0FsVk5DNGhtWFFBcmpTd2FZbHNRSFZ5TnpRZFRvaXNQVjhRQUJn|f12357fbc0048aa4d1ca6cf82313072eaee612233f5ea4188243fb5ff44c3268"; tst=r; __utmz=51854390.1552476597.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/creator/analytics/work/answers; __utmv=51854390.100-1|2=registration_date=20160406=1^3=entry_date=20160406=1; __utma=51854390.126240704.1552476597.1552476597.1552477021.2; tgw_l7_route=7bacb9af7224ed68945ce419f4dea76d; q_c1=81c4f527e7c94544ad009bb634575015|1554688740000|1540282755000',
    ':authority': 'www.zhihu.com'
}


offset = 0
limit = 5

postdata = urllib.parse.urlencode({'offset':offset,'limit':limit,'include':"data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics"})
postdata = postdata.encode('utf-8')

request = urllib.request.Request(url = beginUrl,data = postdata,headers = headers,method = 'GET')
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')

#res = urllib.request.urlopen(beginUrl, postdata, headers)

#

#line = res.read().decode('utf-8')
print(html)


