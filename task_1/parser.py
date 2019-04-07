import requests
from lxml import html


class Parser(object):

    def __init__(self, config):
        self.config = config
        page_links = self.gather_page_links()
        article_links = self.gather_article_links(page_links)

    def gather_page_links(self):
        main_page = requests.get(
            self.config.host_url + self.config.articles_suburl)
        tree = html.fromstring(main_page.content)
        page_links = tree.xpath(self.config.page_link_selector)
        return page_links

    def gather_article_links(self, page_links):
        article_links = []
        for page_link in page_links:
            page = requests.get(self.config.host_url + page_link)
            tree = html.fromstring(page.content)
            article_links += tree.xpath(self.config.article_link_selector)
        return article_links