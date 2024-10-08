import requests

from bs4 import BeautifulSoup

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

content = ''

def extract_news(url):
    print('Extracting news from ' + url)
    cnt = ''
    cnt += '<b> HN Top Stories: </b>\n' + '<br>' + '-' * 50 + '<br>\n<br>'
    response = requests.get(url)

    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    #print(soup.find_all('span', attrs={'class': 'titleline'})[0])
    for i,tag in enumerate(soup.select('span.titleline a')):
        cnt += ((str(i+1)+' :: '+tag.text + f" <a href={tag.attrs['href']}> [link]</a>" + "\n" + '<br>') if tag.text != 'More' else '')
        #print(cnt)
        #print(tag.prettify)

    return cnt

#cnt = extract_news('https://news.ycombinator.com')
# content += cnt
# content += '<br>-------------<br>'
# content += '<br><br>\nEnd of Message'
# print(content)
