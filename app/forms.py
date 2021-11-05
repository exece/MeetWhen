from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, widgets, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
from wtforms.fields.html5 import DateField as html_date_field, TimeField as html_time_field


class InputTypeForm(FlaskForm):
    calander = SubmitField('Calander')
    week = SubmitField('Week')


class CalanderForm(FlaskForm):
    event_title = StringField('Event Title', [InputRequired()])
    # create funcitonality for multiple dates?
    date = html_date_field('Selected Dates', validators=[InputRequired()])
    submit = SubmitField('Create')


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class WeekForm(FlaskForm):
    days_of_week = [('sun', 'Sunday'), ('mon', 'Monday'), ('tue', 'Tuesday'), (
        'wen', 'Wenesday'), ('thur', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday')]
    event_title = StringField('Event Title', [InputRequired()])
    days = SelectMultipleField('Days', choices=days_of_week, validators=[InputRequired()])
    submit = SubmitField('Create')


class JoinForm(FlaskForm):
    event_code = StringField('Event Code', [InputRequired()])
    submit = SubmitField('Join')
