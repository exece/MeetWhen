from flask import Blueprint, render_template, request, redirect, url_for, session
from app.forms import JoinForm
from .forms import JoinForm, InputTypeForm, CalanderForm, WeekForm
import uuid


main = Blueprint('main', __name__)

# title should auto fill if it has been filled in once
@main.route('/', methods=['GET', 'POST'])
def createEvent():
    input_type = 0
    input_type_form = InputTypeForm()

    form_cal = CalanderForm()
    form_week = WeekForm()

    # if calander form is submitted
    if form_cal.submit.data and form_cal.validate():
        session['event_title'] = form_cal.event_title.data
        session['event_date'] = form_cal.date.data
        return redirect(url_for('main.scheduleEvent', page_id = uuid.uuid4()))

    # if week form is submitted
    if form_week.submit.data and form_week.validate():
        session['event_title'] = form_week.event_title.data
        session['event_days'] = form_week.days.data
        return redirect(url_for('main.scheduleEvent', page_id = uuid.uuid4()))

    # input type form
    if input_type_form.calander.data and input_type_form.validate():
        form_week.event_title.data = form_cal.event_title.data  # not doing anything
        
        input_type = 0
    
    elif input_type_form.week.data and input_type_form.validate():
        form_week.event_title.data = form_cal.event_title.data # not doing anything

        input_type = 1
    
    return render_template('create-event.html', input_type_form=input_type_form, form_cal=form_cal,
                           form_week=form_week, input_type=input_type)


@main.route('/join', methods=['GET'])
def joinEvent():
    form = JoinForm()

    return render_template('join-event.html', form=form)


@main.route('/<page_id>', methods=['GET'])
def scheduleEvent(page_id):
    event_title = session['event_title']
    # should use session to pass data between routes without revealing it in url
    return render_template('schedule-event.html', event_title=event_title)
