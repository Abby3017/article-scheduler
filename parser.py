# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r') as contacts_file:
        for contact in contacts_file:
            names.append(contact.split()[0])
            emails.append(contact.split()[1])
    return names, emails

def read_template(filename):
    with open(filename, 'r') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def scrape():
    base_url = "http://www.onlykollywood.com/category/news/page/"
    lst_article = []
    for page in range(1,3):
        url = base_url+str(page)+"/"
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        all_articles = soup.find_all('article', class_="item-list")
        for article in all_articles:
            article_dict = {}
            title = article.find("a")
            date = article.find("span", class_="tie-date")
            article_dict['title']=title.string
            article_dict['date']=date.string
            lst_article.append(article_dict)
    return (lst_article)

def export_dict_list_to_csv(data, filename):
    with open(filename, 'w') as f:
        headers = sorted([k for k, v in data[0].items()])
        csv_data = [headers]
        for d in data:
            csv_data.append([d[h] for h in headers])
        writer = csv.writer(f)
        writer.writerows(csv_data)

def import_list_from_csv(filename):
    lst_article = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ar_dict = {}
            ar_dict['title']=row['title']
            ar_dict['date']=row['date']
            lst_article.append(ar_dict)
    return lst_article


if __name__ == "__main__":
    filename = 'article_list.csv'
    articles = scrape()
    stored_articles = import_list_from_csv(filename)
    pairs = zip(articles,stored_articles)
    result = any(x!=y for x, y in pairs)
    # result = [(x,y) for x, y in pairs if x != y]  to get dict of new articles r[0][0]['title]
    # print (result, len(articles), len(stored_articles))  #false both same
    if result or len(stored_articles) == 0:
        export_dict_list_to_csv(articles,filename)
        names, emails = get_contacts('contact.txt')
        message_template = read_template('message.txt')
        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        s.starttls()
        s.login('emailid','password') # enter your outlook email id and passwd
        for name, email in zip(names, emails):
            msg = MIMEMultipart()
            message = message_template.substitute(PERSON_NAME=name.title())
            msg['FROM']='abby37kumar@outlook.com'
            msg['TO'] = email
            msg['Subject'] = 'News from onkollywood'
            msg.attach(MIMEText(message,'plain'))
            s.send_message(msg)
            del msg
    else:
        pass


"""
tag to look for
<div class="post-listing">
    <article class="item-list item_1">
        <h2 class="post-title">
            <a title="Title of post">Title of post</a>
            <p class="post-meta">
                <span class="tie-date">
                    Date
                </span>
            </p>
"""
