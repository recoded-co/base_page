from django.conf import settings
from django.contrib.sites.models import Site
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import translation
from base_page.forms import FeedbackForm
from base_page.models import Feedback

def set_language(request):

    next_page = request.REQUEST.get('next', None)
    if not next_page:
        next_page = request.META.get('HTTP_REFERER', None)
    if not next_page:
        next_page = '/'
    response = HttpResponseRedirect(next_page)

    if request.method == 'GET':

        lang_code = request.GET.get('lang', None)

        if lang_code and translation.check_for_language(lang_code):

            if hasattr(request, 'session'):
                request.session['django_language'] = lang_code
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)

    return response



def feedback(request):

    """
    This function handles the feedback form
    """
    if (request.method == 'GET'):
        form = FeedbackForm()
        next_page = request.GET.get('next', None)
        if next_page == None:
            next_page = request.META.get('HTTP_REFERER',
                                    '/')

        return render_to_response('feedback.html',
                                {'form': form,
                                 'site': Site.objects.get_current().id,
                                 'next': next_page},
                                context_instance=RequestContext(request))

    elif (request.method == 'POST'):
        form = FeedbackForm(request.POST)
        next_page = request.POST.get('next', '/')
        if form.is_valid():

            cleaned_data = form.cleaned_data
            cleaned_data['content'] = "%s \n url: %s \n user agent: %s" % (cleaned_data['content'],
                                                                           request.POST.get('next',
                                                                                            'unknown'),
                                                                           request.META.get('HTTP_USER_AGENT',
                                                                                            'unknown'))
            if request.user.is_authenticated():
                cleaned_data['content'] = "%s %s" % (cleaned_data['content'],
                                                     request.user.email)

            new_feedback = Feedback(content = cleaned_data['content'],
                                site = cleaned_data['site'])
            new_feedback.save()

            return HttpResponseRedirect(next_page)

        else:
            #return with error messages
            return render_to_response('feedback.html',
                                    {'form': form,
                                     'site': Site.objects.get_current().id,
                                     'next': next_page},
                                    context_instance=RequestContext(request))
        
        
def osmextra(request):
    """
    This function is to provide the extra javascript for admin openstreetmap
    """
    return render_to_response('OSMextra.js',
                              context_instance=RequestContext(request),
                              mimetype='text/javascript')
