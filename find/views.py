from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from endless_pagination.decorators import page_template
from find.models import Community
from django.db.models import Q

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
    #terms = term.split(" ")
    #results = Community.objects.all()

    # More than 2 terms for search is very slow.
    #if len(terms) > 2:
        # Garanted at least two terms consectives.
        #filter_terms = Q(name__icontains='%s %s' % (terms[0], terms[1]))
    #filter_terms = Q()
    #for separeted_term in terms:
        #filter_terms |= Q(name__icontains=separeted_term)
    #else:
    #    filter_terms = Q(name__icontains=term)

    db = 'db_%s'
    letters = 'abcdefghijklmnopqrstuvxyz'
    first_letter = term[0].lower()
    index = letters.find(first_letter)
    if index < 0:
        db = db % '#'
    else:
        db = db % letters[index]

    from IPython import embed; embed()
    Community.objects._db = db

    results = Community.objects.filter(name__istartswith=term)

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
