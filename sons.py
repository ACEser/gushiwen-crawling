import requests
from bs4 import BeautifulSoup

def get_poetry_phrases(keyword):
    base_url = "https://so.gushiwen.cn/mingjus/default.aspx"
    params = {
        'page': 1,  # 初始化为第一页
        'tstr': keyword
    }
    
    params2 = {
        'page': 1,  # 初始化为第一页
        'astr': keyword,  # 使用新的参数'astr'来传递关键词
        'tstr': ''  # 根据新的URL格式，保持'tstr'为空
    }  
    while True:
        response = requests.get(base_url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找包含名句的<div>标签
        poems = soup.find_all('div', class_='cont', style=True)
        
        # 如果当前页没有名句，则终止循环
        if not poems:
            break

        # 遍历所有找到的名句，并提取文本
        for poem in poems:
            phrase = poem.find('a', target="_blank").get_text(strip=True)
            source = poem.find_all('a', target="_blank")[1].get_text(strip=True)
            print(f"{phrase} —— {source}")

        # 检查是否有下一页的链接
        next_page_link = soup.find('a', class_='amore', text='下一页')
        if next_page_link and 'href' in next_page_link.attrs:
            params['page'] += 1  # 准备访问下一页
        else:
            break  # 没有下一页，结束循环

# 测试函数
get_poetry_phrases("春天")

# 名句列表
list = ['春天', '夏天', '秋天', '冬天', '爱国', '写雪', '思念', '爱情', '思乡', '离别', '月亮', '梅花', '励志', '荷花', '写雨', '友情', '感恩', '写风', '西湖', '读书', '菊花', '长江', '黄河', '竹子', '哲理', '泰山', '边塞', '柳树', '写鸟', '桃花', '老师', '母亲', '伤感', '田园', '写云', '庐山', '山水', '星星', '荀子', '孟子', '论语', '墨子', '老子', '史记', '中庸', '礼记', '尚书', '晋书', '左传', '论衡', '管子', '说苑', '列子', '国语', '节日', '春节', '元宵节', '寒食节', '清明节', '端午节', '七夕节', '中秋节', '重阳节', '韩非子', '菜根谭', '红楼梦', '弟子规', '战国策', '后汉书', '淮南子', '商君书', '水浒传', '西游记', '格言联璧', '围炉夜话', '增广贤文', '吕氏春秋', '文心雕龙', '醒世恒言', '警世通言', '幼学琼林', '小窗幽记', '三国演义', '贞观政要']
