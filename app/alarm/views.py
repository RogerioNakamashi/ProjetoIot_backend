import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from app import db, app
from app.alarm.models import Alarm
alarmsList = Blueprint('alarmsList', __name__)
 
@alarmsList.route('/')
def default():
    return "start"
@alarmsList.route('/home')
def home():
    return "Alarms home."
 
 
class AlarmView(MethodView):
 
    def get(self, id=None, page=1):
        if not id:
            alarms = Alarm.query.paginate(page, 10).items
            res = {}
            for alarm in alarms:
                res[alarm.id] = {
                    'name': alarm.name,
                    'time': alarm.time,
                }
        else:
            alarm = Alarm.query.filter_by(id=id).first()
            if not alarm:
                abort(404)
            res = {
                'name': alarm.name,
                'time': alarm.time,
            }
        return jsonify(res)
 
    def post(self):
        name = request.form.get('name')
        time = request.form.get('time')
        alarm = Alarm(name, time)
        db.session.add(alarm)
        db.session.commit()
        return jsonify({alarm.id: {
            'name': alarm.name,
            'time': alarm.time,
        }})
 
    def put(self, id):
        alarm = Alarm.query.filter_by(id=id)\
            .update({\
            'name': (request.form.get('name')),\
            'time': (request.form.get('time'))})
        db.session.commit()
        alarm = Alarm.query.filter_by(id=id).first()
        return jsonify({alarm.id: {
            'name': alarm.name,
            'time': alarm.time,
        }})
 

 
    def delete(self, id):
        # Delete the record for the provided id.
        return
 
 
Alarm_view =  AlarmView.as_view('Alarm_view')
app.add_url_rule(
    '/alarms/', view_func=Alarm_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/alarms/<int:id>', view_func=Alarm_view, methods=['GET', 'PUT']
)