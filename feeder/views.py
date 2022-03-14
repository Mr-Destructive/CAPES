from django.views.generic import ListView
from feeder.models import Article
from django.core.management import call_command

class FeedFetch(ListView):
    model = Article
    template_name = "fetch.html"
    
    def get_context_data(self, **kwargs):
        call_command('fetch_articles')
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.filter().order_by("pub_date")[:12]
        return context
