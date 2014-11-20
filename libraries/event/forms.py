from wtforms import StringField, validators, TextAreaField
from libraries.endemic.form import MyBaseForm as Form


class NewEvent(Form):
    date = StringField('Date',
                       [validators.DataRequired(),
                        validators.Length(min=1, max=35)])
    time = StringField('Time (local time for event)',
                       [validators.DataRequired(),
                        validators.Length(min=1, max=35)])
    location = StringField('Location',
                           [validators.DataRequired(),
                            validators.Length(min=1, max=100)])
    title = StringField('Title',
                        [validators.DataRequired(),
                         validators.Length(min=1, max=35)])
    description = TextAreaField('Give details on event',
                                [validators.Length(min=1, max=350)])
