from DrissionPage import Chromium
import json

def get_bbc_news():
    browser = Chromium()
    tab1 = browser.latest_tab
    url = 'https://www.bbc.com/news'
    tab1.get(url)
    data = []    #数据保存器

    # 抓取Most read
    links = tab1.eles('css:[data-testid*="illinois-grid-10"] [data-testid="internal-link"]')    #用css后代选择路径穿透，避免嵌套循环
    for link in links:
        title = link.ele('@data-testid=card-headline')
        url = link.attr('href')
        data.append({'title': title.text,
                     'url': url})    #数据添加到data

    #抓取文章内容
    try:    #异常处理，防止中断
        for i,item in enumerate(data):    #使用 enumerate 自动生成索引 n (从 0 开始) 和元素 item
            if i == 10:
                break
            tab2 = browser.new_tab()    #创建新标签页
            tab2.get(item['url'])
            contacts = tab2.eles('css:[data-component="layout-block"] p')    #css路径穿透法
            item['contact'] = "\n\n".join([x.text for x in contacts if x.text.strip()])    #.join()高效的将数据添加到data 列表推导式 隐式布尔值判断 .strip()删除空白
            tab2.close()   #关闭标签页
            print(f'正在抓取第{i+1}篇，共{len(data)}篇。。。\n链接{item['url']}\n标题{item['title']}')
    except Exception as e:
        print(e)
    finally:
        browser.quit()
        print("浏览器已彻底关闭，内存已释放。")

    # #保存为json文件
    # with open('bbc_news.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)

    return data

    print('Successfully saved as a JSON file!')
