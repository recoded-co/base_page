from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import translation
from forms import FeedbackForm

def set_language(request):
    next = request.REQUEST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
    response = http.HttpResponseRedirect(next)
    if request.method == 'GET':
        lang_code = request.GET.get('language', None)
        if lang_code and check_for_language(lang_code):
            if hasattr(request, 'session'):
                request.session['django_language'] = lang_code
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
            translation.activate(lang_code)
    return response

def feedback(request):
    
    """
    This function handles the feedback form
    """
    if (request.method == 'GET'):
        form = FeedbackForm();
        next = request.GET.get('next', '/')
        return render_to_response('feedback.html',
                                {'form': form,
                                 'next': next},
                                context_instance=RequestContext(request))
            
    elif (request.method == 'POST'):
        form = FeedbackForm(request.POST)
        
        if form.is_valid():
            
            cleaned_data = form.cleaned_data
            cleaned_data['content'] = "%s %s" % (cleaned_data['content'],
                                                 request.META.get('HTTP_USER_AGENT',
                                                                  'unknown'))
            if request.user.is_authenticated():
                cleaned_data['content'] = "%s %s" % (cleaned_data['content'],
                                                     request.user.email)
            
            feedback = Feedback(content = cleaned_data['content'])
            feedback.save()
            
            next = cleaned_data['next']       
            return HttpResponseRedirect(next)
            

def test(request, template_name):
    """
    This view is made only for testing the templates
    """
    return render_to_response('%s.html' % template_name,
                              context_instance = RequestContext(request))