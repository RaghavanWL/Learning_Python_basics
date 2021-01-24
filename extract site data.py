from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):

    print()
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)
    print()

    try:
        video_source = article.find('iframe', class_='youtube-player')['src']
        video_id = video_source.split("/")[4].split("?")[0]
        yt_link = f'https://youtube.com/watch?v={video_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)
    print("______________________________________________________________________________________")

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
