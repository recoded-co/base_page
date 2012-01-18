from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import translation

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

def test(request, template_name):
    """
    This view is made only for testing the templates
    """
    return render_to_response('%s.html' % template_name,
                              context_instance = RequestContext(request))