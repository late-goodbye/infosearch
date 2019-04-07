import requests
from lxml import html
from lxml.etree import XPathEvalError
from uuid import uuid4
import urllib


from task_1.database_handler import DatabaseHandler


class Parser(object):

    def __init__(self, config, database_handler: DatabaseHandler):
        self.config = config
        self.database_handler = database_handler

    def download_articles(self):
        page_links = self.gather_page_links()
        article_links = self.gather_article_links(page_links)
        self.gather_articles(article_links)

    def gather_page_links(self):
        main_page = requests.get(
            self.config.host_url + self.config.articles_suburl)
        tree = html.fromstring(main_page.content)
        page_links = tree.xpath(self.config.page_link_selector)
        return page_links

    def gather_article_links(self, page_links: list):
        article_links = []
        for link in page_links:
            page = requests.get(self.config.host_url + link)
            tree = html.fromstring(page.content)
            article_links += tree.xpath(self.config.article_link_selector)
        return article_links

    def gather_articles(self, article_links: list):
        for link in article_links:
            article = requests.get(link)
            tree = html.fromstring(article.content)

            title = tree.xpath(self.config.article_title_selector)[0]
            try:
                keywords = ';'.join(tree.xpath(self.config.article_keywords_selector))
            except XPathEvalError as e:
                print('Article {} has no tags'.format(title))
                keywords = ''
            content = '\n'.join(tree.xpath(self.config.article_content_selector))
            url = link
            id = uuid4().hex
            student_id = self.config.article_student_id

            article = (id, title, keywords, content, url, student_id)

            print('Article with id {} has been added.'.format(self.database_handler.add_article(article)))
