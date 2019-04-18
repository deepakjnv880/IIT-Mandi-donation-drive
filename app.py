from flask import Flask,render_template,url_for,request,redirect
from flask_mysqldb import MySQL
from flask_socketio import SocketIO, send, emit
# from flask_socketio import SocketIO
import datetime
import json
from flask import jsonify
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

UPLOAD_FOLDER = '/home/deepak/IDS/photo'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        print("____________+++++++++++++++++++++++++++++++++++++++++++====================================")
        if 'file' not in request.files:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@= = "+request.url)
            # flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        print("=======================================")
        print(file.filename)
        if file.filename == '':
            print("**************************************************************==================1")
            # flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print("**************************************************************==================2")
            filename = secure_filename(file.filename)
            print("**************************************************************==================2")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("**************************************************************==================2")
            print(os.path)
            print("**************************************************************==================2")
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
from flask_socketio import SocketIO

# app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
#
if __name__ == '__main__':
    socketio.run(app)


# app = Flask(__name__)
# app = Flask(__name__)
mysql = MySQL()
con=mysql.connection
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = "******"
app.config['MYSQL_DB'] = "IDS"
# cur = mysql.connection.cursor()
# cur.execute('CREATE DATABASE IF NOT EXISTS DBName;')
# app.config['MYSQL_DB'] = "DBName"
# mysql.init_app(app)
# cur = mysql.connection.cursor()
# # cur.config[.cursor()
# cur.execute('CREATE TABLE IF NOT EXISTS deepak(hi int);')
# app.config['MYSQL_DATABASE_DB'] = 'EmpData'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/',methods=['POST','GET'])
def index():
    print('hihihih'+url_for('index'))
    return render_template('signup.html')

    # return 'arhul, World!'
# @app.route('/a/b/logout',methods=['POST'])
# def logout():
#     print('==============================================================logout'+url_for('index'))
#     return render_template('signup.html')

@app.route('/student/',methods=['POST'])
def signupforstudent():
    name=request.form['name']
    email=request.form['email']
    type=request.form['persontype']
    password1=request.form['password1']
    password2=request.form['password2']
    print(name,email,type,password1,password2)
    # print('hihihih2'+url_for('create_account'))
    cur = mysql.connection.cursor()
    # cur.execute('CREATE DATABASE IF NOT EXISTS DBName;')
    # app.config['MYSQL_DB'] = "DBName"
    # mysql.init_app(app)
    # cur = mysql.connection.cursor()
    # cur.config[.cursor()
    if password1!=password2:
        return redirect(url_for('index'))
    else:
        try:
            a=email
            x,y=(a.split("@"))
            cur.execute('CREATE TABLE IF NOT EXISTS person(pname varchar(100),ptype varchar(100),pemail varchar(100),ppassword varchar(100),online int,PRIMARY KEY (pemail));')
            cur.execute("INSERT INTO person VALUES(%s,%s,%s,%s,%s)",(name,type,email,password1,1));
            mysql.connection.commit();
            return redirect(url_for('account',username=x,type="student",email=email))
        except Exception as e:
            return redirect(url_for('index'))

@app.route('/student/club',methods=['POST'])
def signupforclub():
    name=request.form['name']
    email=request.form['email']
    type=request.form['clubtype']
    password1=request.form['password1']
    password2=request.form['password2']
    print(name,email,type,password1,password2)
    # print('hihihih2'+url_for('create_account'))
    cur = mysql.connection.cursor()
    # cur.execute('CREATE DATABASE IF NOT EXISTS DBName;')
    # app.config['MYSQL_DB'] = "DBName"
    # mysql.init_app(app)
    # cur = mysql.connection.cursor()
    # cur.config[.cursor()
    if password1!=password2:
        return redirect(url_for('index'))
    else:
        try:
            a=email
            x,y=(a.split("@"))
            cur.execute('CREATE TABLE IF NOT EXISTS club(cname varchar(100),cemail varchar(100),ctype varchar(100),cpassword varchar(100),online int,PRIMARY KEY (cemail));')
            print("____________________________________________________________________________________")
            cur.execute("INSERT INTO club VALUES(%s,%s,%s,%s,%s)",(name,email,type,password1,1));
            mysql.connection.commit();
            return redirect(url_for('account',username=x,type="club",email=email))
        except Exception as e:
            return redirect(url_for('index'))


@app.route('/test3',methods=['POST'])
def signinstudent():
    email=request.form['email']
    password=request.form['password']
    a=email
    x,y=(a.split("@"))

    cur = mysql.connection.cursor()
    cur.execute("select ppassword from person where pemail= %s",(email,));
    query_string=cur.fetchall()
    str(query_string)
    print(query_string," +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ",password)
    # con.commit()
    if (query_string[0][0])!=password:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('account',username=x,type="student",email=email))

@app.route('/test4',methods=['POST'])
def signinclub():
    email=request.form['email']
    password=request.form['password']
    a=email
    x,y=(a.split("@"))
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    cur = mysql.connection.cursor()
    cur.execute("select cpassword from club where cemail= %s",(email,));
    query_string=cur.fetchall()
    # cur = mysql.connection.cursor()
    # query_string=cur.execute("select password from person where pemail= %s",email);
    print("hiehif = = "+str(query_string))
    str(query_string)
    # con.commit()
    if str(query_string[0][0])!=password:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('account',username=x,type="club",email=email))
    # try:
    #     cur.execute("select password from user where username VALUES(%s)",(username))
    #     return 'succesfull'
    # except Exception as e:
        # return 'not succesfuull'
        # return redirect(url_for('index'))

@app.route('/<type>/<username>/<email>/',methods=['POST','GET'])
def account(username,type,email):
    # handle_message(email)
    # print(" =))))))))))))))))))))))---------------=")
    # users[email] = request.sid
    return render_template('account.html',username=username,type=type,email=email)

# @app.route('/user/<username>',methods=['POST','GET'])
# def create_post(username):
#     return render_template('account.html',username=username)


@socketio.on('my_event')
def handle_message(email,):
    print(email," =))))))))))))))))))))))---------------=")
    # users[email] = request.sid

@app.route('/temp',methods=['POST','GET'])
def create_posting():
    postere=request.form['article']
    author=request.form['author']
    authortype=request.form['authortype']
    now = datetime.datetime.now()

    # print('- =- =-= -= '+str(data['post'])+' - == -++ '+str(data['author'])+str(now))
    cur = mysql.connection.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS blog(did int NOT NULL AUTO_INCREMENT PRIMARY KEY,pemail varchar(100),cemail varchar(100),dtype varchar(100),post varchar(100),time varchar(100),filename varchar(100));')
    # postere=request.form['article']
    print(author,authortype)


    if request.method == 'POST':
        # check if the post request has the file part
        # print("____________+++++++++++++++++++++++++++++++++++++++++++====================================")
        if 'file' not in request.files:
            # print("dsdf@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@= = "+request.url)
            # flash('No file part')
            if (author=="nss"):
                cur.execute("INSERT INTO blog(pemail,cemail,dtype,post,time) VALUES(%s,%s,%s,%s,%s)",("anyone",author,"social",postere,str(now)));
                mysql.connection.commit();
                return redirect(url_for('account',username=author,type=authortype))

            if (authortype=="student"):
                cur.execute("INSERT INTO blog(pemail,cemail,dtype,post,time) VALUES(%s,%s,%s,%s,%s)",(author,"nss","daily_use_item",postere,str(now)));
                mysql.connection.commit();
                return redirect(url_for('account',username=author,type=authortype))
            else:
                if (authortype=="club"):
                    cur.execute("INSERT INTO blog(pemail,cemail,dtype,post,time) VALUES(%s,%s,%s,%s,%s)",("Alumuni",author,"club_requirement",postere,str(now)));
                    mysql.connection.commit();
                    return redirect(url_for('account',username=author,type=authortype))

        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        # print("=======================================")
        print(file.filename)
        if file.filename == '':
            # print("**************************************************************==================1")
            if (author=="nss"):
                cur.execute("INSERT INTO blog(pemail,cemail,dtype,post,time) VALUES(%s,%s,%s,%s,%s)",("anyone",author,"social",postere,str(now)));
                mysql.connection.commit();
                return redirect(url_for('account',username=author,type=authortype))
            if (authortype=="student"):
                cur.execute("INSERT INTO blog(pemail,cemail,dtype,post,time) VALUES(%s,%s,%s,%s,%s)",(author,"nss","daily_use_item",postere,str(now)));
                mysql.connection.commit();
                return redirect(url_for('account',username=author,type=authortype))
            else:
                if (authortype=="club"):
                    cur.execute("INSERT INTO blog(pemail,cemail,dtype,post,time) VALUES(%s,%s,%s,%s,%s)",("Alumuni",author,"club_requirement",postere,str(now)));
                    mysql.connection.commit();
                    return redirect(url_for('account',username=author,type=authortype))
            # cur.execute("INSERT INTO blog(author,post,time) VALUES(%s,%s,%s)",(author,postere,str(now)));
            # mysql.connection.commit();
            # flash('No selected file')
            # return redirect(url_for('account',username=author))
        if file and allowed_file(file.filename):
            a=file.filename
            a=str(a);
            a=a.replace(" ", "_")
            # print("see filename =======")
            # print(a)
            if (author=="nss"):
                cur.execute("INSERT INTO blog(pemail,cemail,dtype,post,time,filename) VALUES(%s,%s,%s,%s,%s,%s)",("anyone",author,"social",postere,str(now),[a]));
                mysql.connection.commit();
            else:
                if (authortype=="student"):
                    cur.execute("INSERT INTO blog(pemail,cemail,dtype,post,time,filename) VALUES(%s,%s,%s,%s,%s,%s)",(author,"nss","daily_use_item",postere,str(now),[a]));
                    mysql.connection.commit();
                else:
                    if (authortype=="club"):
                        cur.execute("INSERT INTO blog(pemail,cemail,dtype,post,time,filename) VALUES(%s,%s,%s,%s,%s,%s)",("Alumuni",author,"club_requirement",postere,str(now),[a]));
                        mysql.connection.commit();
                    # return redirect(url_for('account',username=author,type=authortype))
            # cur.execute("INSERT INTO blog(author,post,time,filename) VALUES(%s,%s,%s,%s)",(author,postere,str(now),[a]));#file.filename is not converting to string from byte
            # mysql.connection.commit();
            # print("**************************************************************==================2")
            filename = secure_filename(file.filename)
            # print("**************************************************************==================2")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # print("**************************************************************==================2")
            print(os.path)
            # print(send_from_directory(app.config['UPLOAD_FOLDER'],filename))
            # print("**************************************************************==================2")
            return redirect(url_for('account',username=author,type=authortype))
    return redirect(url_for('account',username=author,type=authortype));

@socketio.on('update_post')
def update_post():
    print("svybnmo,xposd v bnmodicdomvomeov")
    # now = datetime.datetime.now()
    # print('- =- =-= -= '+str(data['post'])+' - == -++ '+str(data['author'])+str(now))
    cur = mysql.connection.cursor()
    # cur.execute('CREATE TABLE IF NOT EXISTS blog(author varchar(100),post varchar(100),time varchar(100));')
    cur.execute("select json_object('did',`did`,'pemail',`pemail`,'cemail',`cemail`,'dtype',`dtype`,'time',`time`,'post',`post`,'filename',`filename`) from blog;");
    mysql.connection.commit();
    myresult = cur.fetchall()
    # print("========================================================================================")
    # print(myresult)
    # print("========================================================================================")
    s1 = json.dumps(myresult)
    # print(s1)
    # print("========================================================================================")
    m1=json.loads((s1));
    # print(m1)

    # print("========================================================================================")
    # print(m1)
    m1.reverse()
    for x in m1:
        # print(x[0]['post'])
        p = json.loads(x[0]);
        # print(p["post"])
        socketio.emit('update_post', p)

@socketio.on('online')
def online():
    # print("=======================online============================================")
    cur = mysql.connection.cursor()
    # cur.execute('CREATE TABLE IF NOT EXISTS blog(author varchar(100),post varchar(100),time varchar(100));')
    cur.execute("select json_object('pname',`pname`,'pemail',`pemail`) from person where online=1;");
    # cur.execute("select json_object('did',`did`,'pemail',`pemail`,'cemail',`cemail`,'dtype',`dtype`,'time',`time`,'post',`post`,'filename',`filename`) from blog;");
    mysql.connection.commit();
    myresult = cur.fetchall()
    # print("========================================================================================")
    # print(myresult)
    # print("========================================================================================")
    s1 = json.dumps(myresult)
    # print(s1)
    # print("========================================================================================")
    m1=json.loads((s1));
    # print(m1)

    # print("========================================================================================")
    # print(m1)
    m1.reverse()
    for x in m1:
        # print(x[0]['post'])
        p = json.loads(x[0]);
        p['type'] = 'person'
        # print(p["post"])
        socketio.emit('online', p)

    # print("=======================online============================================")
    cur = mysql.connection.cursor()
    # cur.execute('CREATE TABLE IF NOT EXISTS blog(author varchar(100),post varchar(100),time varchar(100));')
    cur.execute("select json_object('cname',`cname`,'cemail',`cemail`) from club where online=1;");
    # cur.execute("select json_object('did',`did`,'pemail',`pemail`,'cemail',`cemail`,'dtype',`dtype`,'time',`time`,'post',`post`,'filename',`filename`) from blog;");
    mysql.connection.commit();
    myresult = cur.fetchall()
    # print("========================================================================================")
    # print(myresult)
    # print("========================================================================================")
    s1 = json.dumps(myresult)
    # print(s1)
    # print("========================================================================================")
    m1=json.loads((s1));
    # print(m1)

    # print("========================================================================================")
    # print(m1)
    m1.reverse()
    for x in m1:
        # print(x[0]['post'])
        p = json.loads(x[0]);
        p['type'] = 'club'
        # print(p["post"])
        socketio.emit('online', p)

users={}
# users['b17039@student.iitmandi.ac.in']=socketio

@socketio.on('chat')
def chat(data):
    print("==-=-=======-=------------------================= ",data['to'])
    emit('chat', data['to'], room=users[data['to']])

    # users[data['to']].emit('chat',data)



# io=socket(server);

# @socketio.on('connect')
# def connect(data):
#     print(data['me']," =))))))))))))))))))))))---------------=",request.sid)
#     users[data['me']] = request.sid
    # print("vorvm")
	# data.email=NAME;
	# console.log('Connection Made by '+NAME)
	# # var session='UPDATE user SET SessionID=? where Name=?';
	# # con.query(session,[data.email,NAME])
	# if(data.name!==''):
    #     users[data.email]=socket
