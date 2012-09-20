"""
Django forms 
"""
from django.forms import ModelForm
from base_page.models import Feedback
from geonition_utils.widgets import ColorInput

class FeedbackForm(ModelForm):
    """
    This form is used to validate and send
    feedback email from user to administrator
    """
    
    class Meta:
        """
        This is a modelform for the Feedback model
        """
        model = Feedback
        

#admin forms
class OrganizationSetting(ModelForm):
    
    class Meta:
        widgets = {
            'background_color': ColorInput(),
            'text_color': ColorInput()
        }