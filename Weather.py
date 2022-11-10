import requests
import bs4

adrr = 'https://yandex.ru/pogoda'
i = 0
response = requests.get(adrr)
tt = bs4.BeautifulSoup(response.text, 'html.parser')
for ii in tt.select('.forecast-briefly__day'):
    if i > 0 and i < 8:
        week_tag = ii.select_one('.forecast-briefly__name')
        week = week_tag.text
        date_tag = ii.select_one('.forecast-briefly__date')
        date = date_tag.text
        temp_1_tag = ii.select_one('.forecast-briefly__temp_day')
        temp_1 = temp_1_tag.text
        temp_2_tag = ii.select_one('.forecast-briefly__temp_night')
        temp_2 = temp_2_tag.text
        cond_tag = ii.select_one('.forecast-briefly__condition')
        cond = cond_tag.text
        print(f'{week} {date}   {temp_1}/{temp_2}   {cond}')
    i += 1