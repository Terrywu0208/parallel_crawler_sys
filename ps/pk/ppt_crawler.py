import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def get_articles_info(start_date=None):
    articles = []
    index_url = "https://www.ptt.cc/bbs/index.html"
    headers = {"content-type": 'text/html; charset=UTF-8',
               "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    
    response = requests.get(index_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 取得看板名稱
    for item in soup.select(".board-name"):
        board = item.text.strip()
        board_url = f"https://www.ptt.cc/bbs/{board}/index.html"
        response = requests.get(board_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 看板的所有文章資訊
        for item in soup.select(".r-ent"):
            title_elem = item.select_one(".title a")
            if not title_elem:
                continue
            
            # 取得文章標題
            title = title_elem.text.strip()
            author_elem = item.select_one(".author")
            if not author_elem:
                continue
            
            # 取得文章作者
            author = author_elem.text.strip()
            date_elem = item.select_one(".date")
            if not date_elem:
                continue
            
            # 取得文章日期
            date_str = date_elem.text.strip()
            date = datetime.strptime(date_str, "%m/%d")
            
            if start_date and date < start_date:
                continue  # 如果文章日期早於起始日期，則跳過
            
            articles.append({
                "board": board,
                "title": title,
                "author": author,
                "date": date_str
            })
    
    result_df = pd.DataFrame(articles)
    return result_df
# if __name__ == "__main__":
#     start_date_str = "3/16"
#     start_date = datetime.strptime(start_date_str, "%m/%d")
#     articles = get_articles_info(start_date=start_date)
