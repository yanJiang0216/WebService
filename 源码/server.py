from flask import Flask
from flask import render_template,request
import sqlite3
number_user=0
cx = sqlite3.connect("./data.db",check_same_thread = False)
cu=cx.cursor() 
app=Flask(__name__)
@app.route('/')#route关联URL和函数
def index():
    return render_template('homepage.html')
#@app.route('/<path>')#route关联URL和函数
#def anypage(path):
#    try:
#        page=render_template(path)
#        return page
#    except Exception as e:
#        return render_template('404.html')
@app.route('/login.html',methods=['GET', 'POST'])#route关联URL和函数
def getuser():
    kwargs = {}
    kwargs['username'] = request.form.get('username',type=str,default=None)
    kwargs['userpwd'] = request.form.get('userpwd',type=str,default=None)
    return render_template('login.html',**kwargs)
@app.route('/register.html',methods=['GET', 'POST'])#route关联URL和函数
def getNewuser():
    kwargs = {}
    kwargs['username'] = request.form.get('username',type=str,default=None)
    kwargs['userpwd'] = request.form.get('userpwd',type=str,default=None)
    kwargs['telphone'] = request.form.get('telphone',type=str,default=None)
    cu.execute("insert into  user values(?,?,?,?)",(++number_user,kwargs['username'],kwargs['userpwd'],kwargs['telphone']))
    return render_template('register.html',**kwargs)
@app.route('/reserve.html',methods=['GET','POST'])
def getcar():
    kwargs = {}
    kwargs['start']=request.form.get('startstation',type=str,default=None)
    kwargs['terminus']=request.form.get('endstation',type=str,default=None)
    if(kwargs['start'] and kwargs['terminus']):
        cu.execute("SELECT * from car where start=? AND terminus=?",(kwargs['start'],kwargs['terminus']))
        itemlist = cu.fetchall()
        kwargs['id'] = itemlist[0][0]
        kwargs['fares'] = itemlist[0][3]
        kwargs['surplus'] = itemlist[0][4]
    return render_template('reserve.html',**kwargs)
@app.route('/refund.html',methods=['GET','POST'])
def getUserTickets():
    kwargs= {}
    kwargs['start']=request.form.get('startstation',type=str,default=None)
    kwargs['terminus']=request.form.get('endstation',type=str,default=None)
    if(kwargs['start'] and kwargs['terminus']):
        cu.execute("SELECT * from car where start=? AND terminus=?",(kwargs['start'],kwargs['terminus']))
        itemlist = cu.fetchall()
        kwargs['id'] = itemlist[0][0]
        kwargs['fares'] = itemlist[0][3]
        kwargs['surplus'] = itemlist[0][4]
    return render_template('refund.html',**kwargs)
@app.route('/alfter_reserve.html',methods=['GET','POST'])
def getResult():
    return render_template('alfter_reserve.html')
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')
app.run(port=9000,debug = True)