## News Web Crawler

This Python script is designed to crawl the UDN news website for articles published after a specified date. The script uses the requests and BeautifulSoup libraries to scrape the website and parse the HTML, and then outputs the results as a CSV file.

### Installation

To run this script, you will need to install the following libraries:

- requests
- BeautifulSoup
- pandas

You can install these libraries using pip:

```
pip install requests
pip install beautifulsoup4
pip install pandas

```

### Usage

To use this script, simply run it in a Python environment. The script will crawl the UDN news website for articles published after a specified date, and output the results as a CSV file named "result.csv".

You can change the start date of the search by modifying the `start_t` variable in the main function. The date should be in the format `datetime(year, month, day)`.

### Output

The script outputs a CSV file with the following columns:

- `title`: The title of the article.
- `desc`: A brief description of the article.
- `time`: The publication time of the article, in the format `YYYYMMDDHHMM`.
- `cate`: The category of the article.

### Notes

The script currently only crawls the first page of search results. To crawl additional pages, you will need to modify the `page` variable in the `news_crawler` function.

The script also uses a delay of 3 seconds between requests to prevent overloading the server. If you need to crawl a large number of pages, you may need to increase this delay.