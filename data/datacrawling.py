from urllib.request import urlopen
from bs4 import BeautifulSoup

kind = ["이름 : ", "태그 : ", "위치 : ", "영업 시간 : ", "전화 : "]
for i in range(1, 380):
    resNum = str(i).zfill(4)
    html = urlopen(
        "https://www.koreapas.com/m/sofo.php?back=1&Num=a_nam_"+resNum)
    htmlCode = BeautifulSoup(html, "html.parser")

    for data in htmlCode.find_all("div", "background-img"):
        if not htmlCode.find_all("img", src="https://www.koreapas.com/bbs/diskn/sticker/124.png") and not '폐업' in data.text:
            introLine = '#' + resNum +'\n' + kind[0] + data.text.strip() + '\n' + kind[1]
            for data in htmlCode.find_all("span", style="display:inline-block;padding:2px 5px;color:#2b52e3;font-weight:bold;cursor:pointer"):
                introLine += data.text.strip() + ' '
            introLine += '\n'
            for i, data in zip(range(2, 5), htmlCode.find_all("span", style="color:#111;font-size:14px;")):
                introLine += kind[i]+data.text.strip() +'\n'
            print(introLine)