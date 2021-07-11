import requests
from bs4 import BeautifulSoup
from lxml import etree

# urlstr = 'https://xj-sbr.prdasbbwla2.com/zh-cn/info-centre/sportsbook-info/results?opcode=HaoWin&tzoff=480&theme=Haowin'
#
#
#
# var = {
#      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                    "Chrome/91.0.4472.124 Safari/537.36 "
# }

# p = requests.get(urlstr, headers=var)
#
# with open("./haowin.html", 'w', encoding='utf-8') as fp:
#     fp.write(p.text)
# print(p.text)
# print('爬取数据结束')
# p.close()


# closefp = open('./haowin.html', 'r', encoding='utf-8')

parser = etree.HTMLParser(encoding='utf-8')
tree = etree.parse('haowin.html', parser=parser)

Eight_minutes_of_e_football = tree.xpath('//*[@id="cmp-100928"]/span[2]/text()')

number = tree.xpath('//*[@id="dt-cmp-100928"]/div')

Competition_time = tree.xpath('//*[@id="e-5082743"]/span/text()')
print(Eight_minutes_of_e_football)
print(Competition_time)
p = len(number)
print(p)
q = 1
while q < p:
    if q < p and (q % 2 != 0):
        Team_name1 = tree.xpath('//*[@id="dt-cmp-100928"]/div[' + str(q) + ']/div[2]/span[1]/text()')
        Team_name2 = tree.xpath('//*[@id="dt-cmp-100928"]/div[' + str(q) + ']/div[2]/span[3]/text()')
        ht = tree.xpath('//*[@id="dt-cmp-100928"]/div[' + str(q) + ']/div[3]/text()')
        ft = tree.xpath('//*[@id="dt-cmp-100928"]/div[' + str(q) + ']/div[4]/text()')
        print('------------------------------------------')
        print(Team_name1)
        print(Team_name2)
        print(ht)
        print(ft)
    q += 1


