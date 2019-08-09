from wtforms_alchemy import ModelForm

from models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
