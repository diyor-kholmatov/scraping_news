#news by preferens botscraping1
import json
#import requests
from bs4 import BeautifulSoup
import aiohttp
import asyncio
from fake_useragent import UserAgent

async def get_first_news2():
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    async with aiohttp.ClientSession() as session:
        response = await session.get(url="https://www.sport-express.ru/news/", headers=headers)
        soup = BeautifulSoup(await response.text(), 'lxml')

        articles_cards = soup.find_all("div", class_="se-news-list-page__item")
        news1_dict = {}

        for article in articles_cards:
            article_title = article.find("div", class_="se-material__title se-material__title--size-middle").text.strip()


            article_times = article.get("se-news-list-page__item-left")



            links = article.find(class_="se-material__title se-material__title--size-middle").find_all("a")
            #print(links)
            for link in links:
                LINK_HRED = link.get("href")
                #print(LINK_HRED)
            #print(f"{article_title} | {LINK_HRED} | {article_times}")

            article_id = LINK_HRED[-7:]
            news1_dict[article_id] = {
                "article_title": article_title,
                "article_url": LINK_HRED,
            }
    with open("news_dict1.json", "w", encoding='utf-8') as file:
        json.dump(news1_dict, file, indent=4, ensure_ascii=False)

"""async def check_news_update1():
    with open("news_dict1.json", encoding='utf-8') as file:
        news1_dict = json.load(file)

    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    async with aiohttp.ClientSession() as session:
        response = await session.get(url = "https://www.sport-express.ru/news/", headers=headers)
        soup = BeautifulSoup(await response.text(), 'lxml')

        articles_cards = soup.find_all("div", class_="se-news-list-page__item")

        fresh_news1_dict = {}
        for article in articles_cards:
            links = article.find(class_="se-material__title se-material__title--size-middle").find_all("a")
            for link in links:
                LINK_HRED = link.get("href")

            article_id = LINK_HRED[-7:]

            if article_id in news1_dict:
                continue
            else:
                article_title = article.find("div",class_="se-material__title se-material__title--size-middle").text.strip()
                article_id = LINK_HRED[-7:]

                news1_dict[article_id] = {
                    "article_title": article_title,
                    "article_url": LINK_HRED,
                }

                fresh_news1_dict[article_id] = {
                    "article_title": article_title,
                    "article_url": LINK_HRED,
                }

        with open("news_dict1.json", "w", encoding='utf-8') as file:
                json.dump(news1_dict, file, indent=4, ensure_ascii=False)

        return fresh_news1_dict
"""
def main():
    return get_first_news2()


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(get_first_news2())
if __name__ == '__main__':
    asyncio.run(main())
