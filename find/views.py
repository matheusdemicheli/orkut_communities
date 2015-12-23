from multiprocessing.pool import ThreadPool

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from endless_pagination.decorators import page_template

from find.models import Community


def home(request):
    """
    Home view.
    """
    return render_to_response('home.html', {'results': []},
                              context_instance=RequestContext(request))

def search(database, term):
    """
    Make a search in specific database.
    """
    manager = Community.objects.db_manager(database)
    return manager.filter(name__icontains=term)


@page_template('results.html')
def results(request, term,
            input_changed=False, template='home.html', extra_context=None):
    """
    Return the search's results.
    """
    db = 'db_%s'
    letters = '#abcdefghijklmnopqrstuvxyz'
    letters = 'ac'
    
    threads = []
    pool = ThreadPool(processes=26)
    results = Community.objects.none()

    for letter in letters:
        database = db % letter
        thread = pool.apply_async(search, (database, term,))
        threads.append(thread)

    for thread in threads:
        results |= thread.get()

    context = {
        'results': results,
        'loading_more_results': request.GET.get('page', None),
    }

    if extra_context is not None:
        context.update(extra_context)

    return render_to_response('results.html', context,
                              context_instance=RequestContext(request))

def help(request):
    """
    Help View.
    """
    return render_to_response('help.html', {})
