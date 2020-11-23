import pytest

from autoscraper import AutoScraper

url = 'https://stackoverflow.com/questions/2081586/web-scraping-with-python'
wanted_list = ["How to call an external command?"]


@pytest.mark.asyncio
async def test_async_autoscraper():
    scraper = AutoScraper()
    scraper.use_async = True
    result = scraper.build(url, wanted_list)
    print(result)


if __name__ == '__main__':
    import asyncio

    asyncio.run(test_async_autoscraper())
