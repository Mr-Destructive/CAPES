from django.views.generic import ListView, CreateView
from feeder.models import Article, FeedLink
from feeder.forms import AddFeedForm
from django.core.management import call_command
from .scraper import findfeed
from django.http import HttpResponse
import feedparser

class FeedFetch(ListView):
    model = Article
    template_name = "fetch.html"
    
    def get_context_data(self, **kwargs):
        call_command('fetch_articles')
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.filter().order_by("pub_date")[:15]
        return context

class FeedView(ListView):
    model = Article
    template_name = 'fetch.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.filter().order_by("pub_date")[:15]
        return context

class FeedListView(ListView):
    model = FeedLink
    template_name = 'pub_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["publications"] = FeedLink.objects.all()
        return context

class PublicationFeedView(ListView):
    model = Article
    template_name = 'fetch.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["articles"] = Article.objects.filter(publication_name="DEV Community")[:10]
        context["articles"] = Article.objects.filter(publication_name=self.kwargs['pub_name'])[:10]
        return context

class AddFeed(CreateView):
    model = FeedLink
    form_class = AddFeedForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.rss_link = findfeed(str(form.instance.link))
        if not form.instance.rss_link:
            return HttpResponse("The RSS feed cannot be found for the publication")
        feed = feedparser.parse(form.instance.rss_link)
        form.instance.name = feed.feed.title
        return super(AddFeed, self).form_valid(form)
    
