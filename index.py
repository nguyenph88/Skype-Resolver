# Standard libraries
# source venv/bin/activate
import os
import time, string
from collections import deque
from itertools import product
from string import ascii_lowercase, digits
from flask import Flask, stream_with_context, request, Response, url_for

app = Flask(__name__)

def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    return rv

@app.route('/')
def index():
    ip = request.remote_addr
    style = url_for('static', filename='css/style.css')
    return Response(stream_template('index.html', client_ip=ip, style_static = style))

'''
@app.route('/', methods=['POST'])
def get_data():
    # Read from the from input
    skype_id = request.form['skypeid']

    def get_ids():
        for iid in id_list:
            yield checker.check(iid), iid
            time.sleep(.1)  # delay to make the data split out slower
    
    return Response(stream_template('result.html', data=get_ids(), combination=combinations, gen_time=gen_times))
'''
# It is the main call for the application
# DO NOT CHANGE
if __name__ == '__main__':
	app.run()
