from wtforms import validators, TextAreaField
from libraries.endemic.form import MyBaseForm as Form


class Skill(Form):
    description = TextAreaField('Describe your experience with this skill',
                                [validators.Length(min=1, max=255)])
