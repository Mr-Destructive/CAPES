from django.core.management.base import BaseCommand
import feedparser
from dateutil import parser

from feeder.models import Article
from feeder.models import FeedLink 

'''
feedlist = [ 
        "https://dev.to/feed/", 
        "https://www.techrepublic.com/rssfeeds/articles/", 
        "https://medium.com/feed/better-programming",
        "https://cdn.hackernoon.com/feed"]
'''

feedlist = FeedLink.objects.values_list('rss_link', flat=True) 

def save_new_article(feedlist):

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
        save_new_article(feedlist)
