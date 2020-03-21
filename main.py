from bs4 import BeautifulSoup 
import requests,os,shutil,time
headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Encoding': 'gzip',
        "Referer": "https://www.mzitu.com/101553"
    }
def getLi(url):
    r = requests.get(url,headers=headers)
    html = r.text
    soup = BeautifulSoup(html,"html.parser")
    pinsObj=soup.find('ul',id='pins')
    ls=[]
    for i in pinsObj.find_all('li'):
        lss=[]
        lss.append(i.find("span").find("a").get_text())
        lss.append(i.find("a").get("href"))
        ls.append(lss)
    return ls

def getLiUrl(url):
    r=requests.get(url)
    r=requests.get(url,headers=headers)
    html = r.text
    soup = BeautifulSoup(html,"html.parser")
    imgLen=soup.find("div",class_="pagenavi").find_all("span")[-2].get_text()
    ls=[]
    ls.append(url)
    for i in range(1,int(imgLen)):
        ls.append(url+"/"+str(i+1))
    return ls

def li(url):
    r=requests.get(url)
    r=requests.get(url,headers=headers)
    html = r.text
    soup = BeautifulSoup(html,"html.parser")
    main=soup.find_all("div",class_="main-image")
    time.sleep(0.5)
    s=main[0].find("p").find("a").find("img").get("src")
    return s
    #索引0是下一张地址 索引1是当前图片地址

def download(url,name,i):
    r = requests.get(url,headers=headers,stream=True)
    img=os.getcwd()+r"\images\\"+name+"\\"+i+".jpg"
    with open(img, 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)

if __name__ == "__main__":
    if os.path.exists(os.getcwd()+r"\images\\"):
        shutil.rmtree(os.getcwd()+r"\images\\")
    urlLs=["https://www.mzitu.com/","https://www.mzitu.com/hot/","https://www.mzitu.com/best/"]
    while True:
        n = input("1最新 2最火 3推荐 请输入要下载的类型：")
        if n == "1" or n == "2" or n == "3":
            print("正在获取图片……请勿关闭")
            ulLs = getLi(urlLs[eval(n) - 1])
            for i in ulLs:
                print("正在获取{}".format(i[0]))
                os.makedirs(os.getcwd() + r"\images\\" + i[0])
                liLs = getLiUrl(i[1])
                count = 1
                for a in liLs:
                    imgurl = li(a)
                    download(imgurl, i[0], str(count))
                    count += 1
        else:
            print("请输入正确的数！")
        
