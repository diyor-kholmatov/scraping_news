#news by preferens botscraping
import json
from datetime import datetime
import time
#import requests
from bs4 import BeautifulSoup
import aiohttp
import asyncio
from fake_useragent import UserAgent

async def get_first_news():
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    async with aiohttp.ClientSession() as session:
        response = await session.get(url="https://808.media/topics/news/", headers=headers)
        soup = BeautifulSoup(await response.text(), 'lxml')


        articles_cards = soup.find_all("div", class_="feed_row row row-no-gutters")
        news_dict = {}
        for article in articles_cards:
            article_title = article.find(class_="entry_title").text.strip()
            article_desc = article.find("p").text.strip()
            article_url = article.select_one("a")['href']

            article_date_time = article.find("time").get("datetime")
            date_from_iso = datetime.fromisoformat(article_date_time)
            date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
            article_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timetuple())

            #print(f"{article_title} | {article_url} | {article_date_time} | {article_desc}")
            article_id = article_url[18:-1]

            news_dict[article_id] = {
                "article_date_timestamp": article_date_timestamp,
                "article_title": article_title,
                "article_url": article_url,
                "article_desc": article_desc
            }
    with open("news_dict.json", "w", encoding='utf-8') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)



"""async def check_news_update():
    with open("news_dict.json", encoding='utf-8') as file:
        news_dict = json.load(file)
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }

    async with aiohttp.ClientSession() as session:
        response = await session.get(url="https://808.media/topics/news/", headers=headers)
        soup = BeautifulSoup(await response.text(), 'lxml')
        articles_cards = soup.find_all("div", class_="feed_row row row-no-gutters")

        fresh_news = {}
        for article in articles_cards:
            article_url = article.select_one("a")['href']
            article_id = article_url[18:-1]

            if article_id in news_dict:
                continue
            else:
                article_title = article.find(class_="entry_title").text.strip()
                article_desc = article.find("p").text.strip()

                article_date_time = article.find("time").get("datetime")
                date_from_iso = datetime.fromisoformat(article_date_time)
                date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
                article_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timetuple())


                news_dict[article_id] = {
                    "article_date_timestamp": article_date_timestamp,
                    "article_title": article_title,
                    "article_url": article_url,
                    "article_desc": article_desc
                }

                fresh_news[article_id] = {
                    "article_date_timestamp": article_date_timestamp,
                    "article_title": article_title,
                    "article_url": article_url,
                    "article_desc": article_desc
                }
    print(fresh_news)
    with open("news_dict.json", "w", encoding='utf-8') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)
    return fresh_news
"""


async def main():
    await get_first_news()
    #print(check_news_update())
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(get_first_news())
if __name__ == '__main__':
    asyncio.run(main())
