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


@page_template('results.html')
def results(request, term,
            input_changed=False, template='home.html', extra_context=None):
    """
    Return the search's results.
    """
    results = Community.objects.filter(name__icontains=term)

    context = {
        'results': results,
        'term': term,
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