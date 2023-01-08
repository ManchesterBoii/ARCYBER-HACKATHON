from flask import Flask, render_template

flask_app = Flask(__name__)
from BarGraph import run


@flask_app.route('/')
def index():
    return render_template('home.html')



@flask_app.route('/datavis1')
def vis1():
    return render_template('logins_from_outside_rcc-c.csv_profile_1601518044.html')



@flask_app.route('/datavis2')
def vis2():
    return render_template('proxy_hackathon_sample.csv_profile_1601168659.html')



@flask_app.route('/datavis3')
def vis3():
    return render_template('winevents_hackathon_sample.csv_profile_1601166777.html')



@flask_app.route('/datavis4')
def vis4():
    return render_template('dns_hackathon_sample.csv_profile_1601166383.html')


@flask_app.route('/datavis5')
def vis5():
    run()
    return render_template('BarGraph.html')

@flask_app.route('/datavis6')
def vis6():
    return render_template('abl-networkanomaly-datausage.cyberspace_weekly.csv_profile_1601520238.html')

@flask_app.route('/datavis7')
def vis7():
    return render_template('[oq]_vils_sysmon_1wk.csv_profile_1601236131.html')

@flask_app.route('/datavis8')
def vis8():
    return render_template('[oq]_reverse_proxy_command_injection_(non-army.csv_profile_1601166591.html')





