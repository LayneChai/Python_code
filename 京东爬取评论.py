# -*- coding:utf-8 -*-
# 这是一个爬取京东小米音箱综合评价前20的商品评论(包括 好评/中评/差评)的 Python 脚本。使用了快代理和66代理的ip代理池 防止触发反爬虫


import re
import time
import requests
import openpyxl
import pandas as pd
import random
headers={ #京东的header
    # refer为每次登陆后重新填写
    'referer':'https://item.jd.com/',
    # cookie为每次登陆后重新粘贴
    'cookie':''
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

# pat = re.compile('"rateContent":"(.*?)","fromMall"')  # 定义评价内容模式,"(?:vcontent|creationTime|commentId)"
pat = re.compile('"content":"(.*?)"')# 定义评价内容模式 匹配模式 包含客服回复，读取之后过滤掉
patPage = re.compile('"maxPage":(.*?),"productCommentSummary"')# 定义评价页数 匹配模式


def liuliuproxy():  #66代理ip池
    ip_list = []
    port_list = []
    for i in range(1, 20): #20代表的一共20个页面获取ip
        res1 = requests.get("http://www.66ip.cn/" + str(i) + ".html").text
        paip = re.compile('<td>([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})</td>')
        paport = re.compile('<td>([0-9]{2,5})</td>')
        ip_list.extend(paip.findall(res1))
        port_list.extend(paport.findall(res1))
    proxy_list = []
    for i in range(len(ip_list)):
        aa = {}
        aa['http'] = ip_list[i] + ":" + port_list[i]
        proxy_list.append(aa)
    print(proxy_list)
    return proxy_list
def kuaiproxy():  #快代理ip池
    #快代理在京东上爬评论太垃圾 所以还是调用66代理
    return liuliuproxy()
    # headersip = {# 快代理的header
    #     'cookie': 'channelid=0; sid=1651999961800159; _gcl_au=1.1.771854632.1652001492; _ga=GA1.2.496859659.1652001492; _gid=GA1.2.2024589242.1652001492; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1652001493; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1652001730',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    # }
    # ip_list = []
    # port_list = []
    # for i in range(1, 20): #20代表的一共20个页面获取ip
    #     res1 = requests.get("https://www.kuaidaili.com/free/inha/" + str(i), headers=headersip).text
    #     # print(res1)
    #     patip = re.compile('<td data-title="IP">(.*?)</td>')
    #     patport = re.compile('<td data-title="PORT">(.*?)</td>')
    #     ip_list.extend(patip.findall(res1))
    #     port_list.extend(patport.findall(res1))
    # proxy_list = []
    # for i in range(len(ip_list)):
    #     aa = {}
    #     aa['http'] = ip_list[i] + ":" + port_list[i]
    #     proxy_list.append(aa)
    # print(proxy_list)
    # return proxy_list

if __name__ == '__main__':
    proxy_list = liuliuproxy()
    res = []
    # print("#本次采取了综合评价前10的小米音箱好评 、 中评 、差评 的销售评价数据")
    URLS = [
        #第一个商品
        # 好评
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100019730040&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        # 中评
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100019730040&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        # 差评
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100019730040&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        # 第二个商品
        # 好评
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100021518293&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        # 中评
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100021518293&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        #差评
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100021518293&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        #第三类商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100004676756&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100004676756&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100004676756&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        # 第四个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=11733008484&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=11733008484&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=11733008484&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        #第五个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=50373333999&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=50373333999&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=50373333999&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        #第六个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=57145320768&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=57145320768&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=57145320768&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        # 第七个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10029443801633&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10029443801633&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10029443801633&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        # 第八个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100008509177&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100008509177&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100008509177&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        # 第九个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=33671032046&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=33671032046&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=33671032046&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        # 第10个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=67135496652&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=67135496652&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=67135496652&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        # 第11个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=1805623401&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=1805623401&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=1805623401&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        # 第12个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=57206232477&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=57206232477&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=57206232477&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        # 第13个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=41104872436&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=41104872436&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=41104872436&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        # 第14个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10026670314128&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10026670314128&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10026670314128&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        # 第15个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=61833762529&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=61833762529&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=61833762529&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        # 第16个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10025990928047&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10025990928047&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10025990928047&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        # 第17个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=63731109038&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=63731109038&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=63731109038&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        # 第18个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=50067819225&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=50067819225&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=50067819225&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        # 第19个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=57541235177&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=57541235177&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=57541235177&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        # 第20个商品
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=67155108401&score=3&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=67155108401&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',
        'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=67155108401&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1',

        ]
    index = 0 #根据index来选择代理池
    for i,URL1 in enumerate(URLS):
        res = []
        if i%10==0: #每隔10个链接换一下ip代理池
            proxy_list =kuaiproxy() if index % 2!=1 else liuliuproxy()
            index=index+1
        print(URL1)

        all = URL1.split("page=0")
        if len(all)<2:
            print("网址错误，请打开第一页评论后获取网址")
        else:
            all[0]+="page="
            urlParent = all[0]+"0"+all[1]
            t = random.randint(0, len(proxy_list) - 1)

            pageContent = requests.get(urlParent,headers=headers,proxies=proxy_list[t]).text
            print(pageContent)
            pageSize = int(patPage.findall(pageContent)[0])
            print("评论共有"+str(pageSize)+"页,爬取中....")
            # pageSize = max(pageSize,51);
            for j in range(0,pageSize):
                url1 = all[0]+str(j)+all[1]
                # tmp = requests.head(url1,headers=headers).text
                # print(tmp)
                t = random.randint(0, len(proxy_list) - 1)
                data = requests.get(url1,headers=headers,proxies=proxy_list[t]).text
                # 增加延时 控制速度每3秒一个页面   防止触发反爬虫
                time.sleep(3)
                res1 = pat.findall(data)
                res2=[]
                for res11 in res1:
                    if not res11.startswith('您没有填写内容') and  not res11.startswith('没有您的支持') and not res11.startswith('超级诚信好买家') and  not res11.startswith('很好很好的买家') and not res11.startswith('谢谢') and not res11.startswith('小店') and not res11.startswith('您好') and not res11.startswith('没有早一步') and not res11.startswith("每次的好评") and not res11.startswith("亲爱") and not res11.startswith("尊敬") and not res11.startswith("感谢") and not res11.startswith("再一次") and not res11.startswith("阳光温暖"):
                        res2.append(res11)
                res.extend(res2)
                print('第'+str(i)+'个网址的第'+str(j)+'页爬取完成')
                print(res2)
        if i % 3 == 0:
            # print(res)
            # 存储excel文件
            df = pd.DataFrame()
            df['购买音箱后好评'] = res
            df.to_excel('小爱同学好评'+str(i)+'.xlsx')
        elif i%3 ==1:
            # print(res)
            # 存储excel文件
            df = pd.DataFrame()
            df['购买音箱后中评'] = res
            df.to_excel('小爱同学中评' + str(i) + '.xlsx')
        else:
            # print(res)
            # 存储excel文件
            df = pd.DataFrame()
            df['购买音箱后差评'] = res
            df.to_excel('小爱同学差评' + str(i) + '.xlsx')
        # time.sleep(300)
    # 合并所有的好评excel 和 中评的excel 和 差评excel
