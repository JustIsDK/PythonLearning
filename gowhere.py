# 教育机构: 享学课堂
# 讲   师:  海伦
# 日   期:  2022/8/4
import random
import time
import requests
import parsel
import csv

csv_qne = open('去哪儿.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.writer(csv_qne)
csv_writer.writerow(['地点', '短评', '出发时间', '天数','人均费用','人物','玩法','浏览量','详情页'])
for page in range(1, 201):
    url = f'https://travel.qunar.com/travelbook/list.htm?page={page}&order=hot_heat'

    response = requests.get(url)
    html_data = response.text
    selector = parsel.Selector(html_data)

    url_list = selector.css('body > div.qn_mainbox > div > div.left_bar > ul > li > h2 > a::attr(href)').getall()
    for detail_url in url_list:
        detail_id = detail_url.replace('/youji/', '')
        detail_url = 'https://travel.qunar.com/travelbook/note/' + detail_id

    response_1 = requests.get(detail_url)

    data_html_1 = response_1.text

    selector_1 = parsel.Selector(data_html_1)
    title = selector_1.css('.b_crumb_cont *:nth-child(3)::text').get()

    comment = selector_1.css('.title.white::text').get()

    count = selector_1.css('.view_count::text').get()

    date = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.when > p > span.data::text').get()

    days = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.howlong > p > span.data::text').get()

    money = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.howmuch > p > span.data::text').get()

    character = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.who > p > span.data::text').get()

    play_list = selector_1.css('#js_mainleft > div.b_foreword > ul > li.f_item.how > p > span.data span::text').getall()
    play = ' '.join(play_list)
    print(title, comment, date, days, money, character, play, count, detail_url)
    csv_writer.writerow([title, comment, date, days, money, character, play, count, detail_url])
    time.sleep(random.randint(3, 5))
csv_qne.close()
