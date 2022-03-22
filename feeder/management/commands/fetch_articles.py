from django.core.management.base import BaseCommand
from dateutil import parser
import feedparser
import ssl

from feeder.models import Article
from feeder.models import FeedLink 

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

'''
feedlist = [ 
        "https://dev.to/feed/", 
        "https://www.techrepublic.com/rssfeeds/articles/", 
        "https://medium.com/feed/better-programming",
        "https://cdn.hackernoon.com/feed"]
'''


def save_new_article():

    feedlist = FeedLink.objects.values_list('rss_link', flat=True) 
    for feed in feedlist:
        feed = feedparser.parse(feed)
        article_title = feed.channel.title

        for item in feed.entries:
            if not Article.objects.filter(puid=item.guid).exists():
                article = Article(
                    title=item.title,
                    description=item.description,
                    pub_date=parser.parse(item.published),
                    link=item.link,
                    publication_name=article_title,
                    puid=item.guid,
                )
                article.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        save_new_article()
