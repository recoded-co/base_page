"""
Django forms 
"""
from django.forms import ModelForm
from base_page.models import Feedback

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