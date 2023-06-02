import argparse
import re
import requests


class UrlAnalyzer:
    def __init__(self, url=None):
        if url:
            self.url = url
        else:
            self.url = self.user_input()
        self.link_analyzer = LinkAnalyzer()

    @staticmethod
    def user_input():
        parser = argparse.ArgumentParser()
        parser.add_argument('-url', type=str, help='Please set url for parsing')
        args = parser.parse_args()
        if args.url:
            return args.url
        else:
            url = input('Please set url for parsing: ')
            return url

    def __str__(self):
        return self.url


class LinkAnalyzer:
    def __init__(self):
        self.valid_links = []
        self.broken_links = []

    def parse_and_save_links(self, url):
        links = self.get_links_from_url(url)
        self.check_links(links)
        self.save_links(self.valid_links, "valid_links.txt")
        self.save_links(self.broken_links, "broken_links.txt")

    def get_links_from_url(self, url):
        if not url.startswith('http'):
            url = 'http://' + url
        response = requests.get(url)
        if response.status_code != 200:
            return []

        base_url = response.url
        html_content = response.text
        links = re.findall('<a\s+(?:[^>]*?\s+)?href="([^"]*)"', html_content)
        absolute_links = [self.construct_absolute_link(base_url, link) for link in links]
        return absolute_links

    def construct_absolute_link(self, base_url, link):
        if link.startswith('/'):
            return base_url + link
        else:
            return base_url + '/' + link

    def check_link(self, link):
        response = requests.get(link)
        return response.status_code == 200

    def check_links(self, links):
        for link in links:
            if self.check_link(link):
                self.valid_links.append(link)
            else:
                self.broken_links.append(link)

    def save_links(self, links, filename):
        with open(filename, 'w') as file:
            for link in links:
                file.write(link + '\n')


if __name__ == "__main__":
    url = UrlAnalyzer()
    link_analyzer = url.link_analyzer
    link_analyzer.parse_and_save_links(url.url)