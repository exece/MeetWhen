from flask import Blueprint, render_template, request, redirect,url_for

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def createEvent():
    return render_template('create-event.html')


@main.route('/<ID>', methods=['GET'])
def scheduleEvent():
    return render_template('schedule-event.html')

