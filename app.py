from flask import Flask,render_template,url_for,request,redirect
import requests
from flask_mysqldb import MySQL
from flask_socketio import SocketIO, send, emit
from flask_socketio import join_room, leave_room
from flask_socketio import SocketIO
from flask import session
import datetime
import json
from flask import jsonify
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory
import logging
import Checksum
import cgi
import base64
import random
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

UPLOAD_FOLDER = '/home/deepak/IDS/photo'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

user={}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        # print("____________+++++++++++++++++++++++++++++++++++++++++++====================================")
        if 'file' not in request.files:
            # pri/nt("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@= = "+request.url)
            # flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        # print("=======================================")
        # print(file.filename)
        if file.filename == '':
            # print("**************************************************************==================1")
            # flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # print("**************************************************************==================2")
            filename = secure_filename(file.filename)
            # print("**************************************************************==================2")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # print("**************************************************************==================2")
            # print(os.path)
            # print("**************************************************************==================2")
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
    # print('hihihih'+url_for('index'))
    return render_template('signup.html')


@app.route('/student/',methods=['POST'])
def signupforstudent():
    name=request.form['name']
    email=request.form['email']
    type=request.form['persontype']
    password1=request.form['password1']
    password2=request.form['password2']
    # print(name,email,type,password1,password2)
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
    # print(name,email,type,password1,password2)
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
    # print(" =))))))))))))))))))))))---------------=",session.id)
    email=request.form['email']
    password=request.form['password']
    a=email
    x,y=(a.split("@"))

    cur = mysql.connection.cursor()
    cur.execute("select ppassword from person where pemail= %s",(email,));
    query_string=cur.fetchall()
    str(query_string)
    # print(query_string," +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ",password)
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
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    cur = mysql.connection.cursor()
    cur.execute("select cpassword from club where cemail= %s",(email,));
    query_string=cur.fetchall()
    # cur = mysql.connection.cursor()
    # query_string=cur.execute("select password from person where pemail= %s",email);
    # print("hiehif = = "+str(query_string))
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

users={}

@app.route('/<type>/<username>/<email>/',methods=['POST','GET'])
def account(username,type,email):
    # handle_message(email)
    if (type=="student"):
        cur = mysql.connection.cursor()
        cur.execute("select `pname` from person where pemail=%s;",(email,));
        mysql.connection.commit();
        myresult = cur.fetchall()
        print("============================account==============================",myresult[0][0]);

    if (type=="club"):
        cur = mysql.connection.cursor()
        cur.execute("select `cname` from club where cemail=%s;",(email,));
        mysql.connection.commit();
        myresult = cur.fetchall()
        print("============================account==============================",myresult[0][0]);

    # users[email] = request.sid

    # users['b17039@student.iitmandi.ac.in']=request.id
    return render_template('account.html',username=username,type=type,email=email,name=myresult[0][0])

# @app.route('/user/<username>',methods=['POST','GET'])
# def create_post(username):
#     return render_template('account.html',username=username)


# @socketio.on('my_event')
# def handle_message(email,):
#     print(email," =))))))))))))))))))))))---------------=")
    # users[email] = request.sid

@app.route('/temp',methods=['POST'])
def create_posting():
    postere=request.form['article']
    email=request.form['authoremail']
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
                return redirect(url_for('account',username=author,type=authortype,email=email))

            if (authortype=="student"):
                cur.execute("INSERT INTO blog(pemail,cemail,dtype,post,time) VALUES(%s,%s,%s,%s,%s)",(author,"nss","daily_use_item",postere,str(now)));
                mysql.connection.commit();
                return redirect(url_for('account',username=author,type=authortype,email=email))
            else:
                if (authortype=="club"):
                    cur.execute("INSERT INTO blog(pemail,cemail,dtype,post,time) VALUES(%s,%s,%s,%s,%s)",("Alumuni",author,"club_requirement",postere,str(now)));
                    mysql.connection.commit();
                    return redirect(url_for('account',username=author,type=authortype,email=email))

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
                return redirect(url_for('account',username=author,type=authortype,email=email))
            if (authortype=="student"):
                cur.execute("INSERT INTO blog(pemail,cemail,dtype,post,time) VALUES(%s,%s,%s,%s,%s)",(author,"nss","daily_use_item",postere,str(now)));
                mysql.connection.commit();
                return redirect(url_for('account',username=author,type=authortype,email=email))
            else:
                if (authortype=="club"):
                    cur.execute("INSERT INTO blog(pemail,cemail,dtype,post,time) VALUES(%s,%s,%s,%s,%s)",("Alumuni",author,"club_requirement",postere,str(now)));
                    mysql.connection.commit();
                    return redirect(url_for('account',username=author,type=authortype,email=email))
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
            # print(os.path)
            # print(send_from_directory(app.config['UPLOAD_FOLDER'],filename))
            # print("**************************************************************==================2")
            return redirect(url_for('account',username=author,type=authortype,email=email))
    return redirect(url_for('account',username=author,type=authortype,email=email));

@socketio.on('update_post')
def update_post(data):
    room=users[data['me']]
    # print(room)
    # print("-====update_post===============================",data)
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

        if p["dtype"]=='daily_use_item':
            # print(p["dtype"])
            cur = mysql.connection.cursor()
            cur.execute("select count(recommended) from daily_use_item where recommended='YES' AND blog_id="+str(p['did'])+";");
            mysql.connection.commit();
            myresult = cur.fetchall()
            p['recommended']=myresult[0][0]
            cur.execute("select count(not_recommended) from daily_use_item where not_recommended='YES' AND blog_id="+str(p['did'])+";");
            mysql.connection.commit();
            myresult = cur.fetchall()
            p['not_recommended']=myresult[0][0]
            cur.execute("select count(comment) from daily_use_item where comment!='NULL' AND blog_id="+str(p['did'])+";");
            mysql.connection.commit();
            myresult = cur.fetchall()
            p['comment']=myresult[0][0]
            cur.execute("select recommended from daily_use_item where userid=%s AND blog_id=%s",(str(data['me']),str(p['did'])))
            mysql.connection.commit();
            myresult = cur.fetchall()
            # print(myresult)
            if len(myresult) == 0:
                p['recommendedcheck']='NULL'
            else:
                p['recommendedcheck']=myresult[0][0]

            cur.execute("select not_recommended from daily_use_item where userid=%s AND blog_id=%s",(str(data['me']),str(p['did'])))
            mysql.connection.commit();
            myresult = cur.fetchall()
            # print(myresult)
            if len(myresult) == 0:
                p['not_recommendedcheck']='NULL'
            else:
                p['not_recommendedcheck']=myresult[0][0]
            # p['not_recommendedcheck']=myresult[0][0]
            # print("@@@@@@@@@@@@@@@@@@@@@@@@@",p)
            # select count(not_recommended) from daily_use_item where not_recommended='YES' ;
            emit('update_post', p, room=room)
            # socketio.emit('update_post', p)
        if p["dtype"]=='social':
            # print(p["dtype"])
            cur = mysql.connection.cursor()
            cur.execute("select count(interested) from social_blog where interested='YES' AND blog_id="+str(p['did'])+";");
            mysql.connection.commit();
            myresult = cur.fetchall()
            p['interested']=myresult[0][0]
            cur.execute("select count(not_interested) from social_blog where not_interested='YES' AND blog_id="+str(p['did'])+";");
            mysql.connection.commit();
            myresult = cur.fetchall()
            p['not_interested']=myresult[0][0]
            cur.execute("select count(comment) from social_blog where comment!='NULL' AND blog_id="+str(p['did'])+";");
            mysql.connection.commit();
            myresult = cur.fetchall()
            p['comment']=myresult[0][0]
            cur.execute("select interested from social_blog where userid=%s AND blog_id=%s",(str(data['me']),str(p['did'])))
            mysql.connection.commit();
            myresult = cur.fetchall()
            # print(p['did'],"{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}",myresult)
            if len(myresult) == 0:
                p['interestedcheck']='NULL'
            else:
                p['interestedcheck']=myresult[0][0]
            # p['intestedcheck']=myresult[0][0]
            cur.execute("select not_interested from social_blog where userid=%s AND blog_id=%s",(str(data['me']),str(p['did'])))
            mysql.connection.commit();
            myresult = cur.fetchall()
            if len(myresult) == 0:
                p['not_interestedcheck']='NULL'
            else:
                p['not_interestedcheck']=myresult[0][0]
            # print(myresult)
            # p['not_intestedcheck']=myresult[0][0]
            # print("@@@@@@@@@@@@@@@@@@@@@@@@@",p)
            # select count(not_recommended) from daily_use_item where not_recommended='YES' ;
            emit('update_post', p, room=room)
            # socketio.emit('update_post', p)

        if p["dtype"]=='club_requirement':
            # print(p["dtype"])
            cur = mysql.connection.cursor()
            cur.execute("select count(upvote) from club_requirement where upvote='YES' AND blog_id="+str(p['did'])+";");
            mysql.connection.commit();
            myresult = cur.fetchall()
            p['upvote']=myresult[0][0]
            cur.execute("select sum(amount_donated) from club_requirement where blog_id="+str(p['did'])+";");
            mysql.connection.commit();
            myresult = cur.fetchall()
            p['total_amount_donated']=myresult[0][0]
            cur.execute("select count(comment) from club_requirement where comment!='NULL' AND blog_id="+str(p['did'])+";");
            mysql.connection.commit();
            myresult = cur.fetchall()
            p['comment']=myresult[0][0]
            cur.execute("select upvote from club_requirement where userid=%s AND blog_id=%s",(str(data['me']),str(p['did'])))
            mysql.connection.commit();
            myresult = cur.fetchall()
            # print(myresult)
            if len(myresult) == 0:
                p['upvotecheck']='NULL'
            else:
                p['upvotecheck']=myresult[0][0]
            # p['upvotecheck']=myresult[0][0]
            # cur.execute("select not_recommended from club_requirement where userid=%s AND blog_id=%s",(str(data['me']),str(p['did'])))
            # mysql.connection.commit();
            # myresult = cur.fetchall()
            # print(myresult)
            # p['not_recommendedcheck']=myresult[0][0]
            # print("@@@@@@@@@@@@@@@@@@@@@@@@@",p)
            # select count(not_recommended) from daily_use_item where not_recommended='YES' ;
            emit('update_post', p, room=room)
            # socketio.emit('update_post', p)

@socketio.on('online')
def online(data):
    # print("=======================online============================================ ",data['me'])
    # print(online_users)
    socketio.emit('online', online_users)
    # for i in users.keys():
    #     if data['me']!=i:
    #         print(i)

        # emit('online', p, room=room)

@socketio.on('logout')
def logout(data):
    print('=logout==================',users)
    del users[data['me']]
    del online_users[data['me']]
    # print('=after logout==================',users)
    # return render_template('signup.html')

    # return 'arhul, World!'
# @app.route('/a/b/logout',methods=['POST'])
# def logout():
#     print('==============================================================logout'+url_for('index'))
#     return render_template('signup.html')


@socketio.on('chat')
def chat(data):
    # print("==-=-=======-=---------chat---------================= ",data['from'])
    # cur = mysql.connection.cursor()
    # # cur.execute('CREATE TABLE IF NOT EXISTS blog(author varchar(100),post varchar(100),time varchar(100));')
    # cur.execute("select json_object('pname',`pname`,'pemail',`pemail`) from person where online=1;");
    # # cur.execute("select json_object('did',`did`,'pemail',`pemail`,'cemail',`cemail`,'dtype',`dtype`,'time',`time`,'post',`post`,'filename',`filename`) from blog;");
    # mysql.connection.commit();
    # myresult = cur.fetchall()
    # room = session.get(data['to'])
    room=users[data['to']]
    # print(room)
    emit('chat', data, room=room)

    # users[data['to']].emit('chat',data)



# io=socket(server);
online_users={}
@socketio.on('makeroom')
def makeroom(data):
    # print(data['name'],"==fghbjnkml,============= ",data['me'])
    users[data['me']] = request.sid
    online_users[data['me']] = data['name']
    # room = session.get(data['me'])
    # print("room ============================ ",room)
    # join_room(room)
    # print(data['me']," =))))))))))))))))))))))---------------=",request.sid)
    # users[data['me']] = request.sid
    # print("vorvm")
	# data.email=NAME;
	# console.log('Connection Made by '+NAME)
	# # var session='UPDATE user SET SessionID=? where Name=?';
	# # con.query(session,[data.email,NAME])
	# if(data.name!==''):
    #     users[data.email]=socket

@app.route('/payment/<blog_id>/<customerid>/<customername>',methods=['GET'])
def paymentform(customerid,customername,blog_id):
    print(customerid,customername,blog_id)
    return render_template('payment/payment_details.html',customerid=customerid,customername=customername,blog_id=blog_id)




MERCHANT_ID = 'fADQZI57666205989648'
MERCHANT_KEY='nMQZuvux1QzS4Hrf'
paymentemail={}
paymentblog={}
# MERCHANT_KEY = 'notmade'
@app.route('/shop/',methods=['POST'])
def shop():
    name=request.form['name']
    email=request.form['email']
    blog_id=request.form['blog_id']
    amount=request.form['amount']
    orderid=str(random.randint(1,2000))
    paymentemail[orderid]=email
    paymentblog[orderid]=blog_id
    # password1=request.form['password1']
    # password2=request.form['password2']
    # print(name,email,paytmno,amount)
    deepak_dict = {

                'MID': MERCHANT_ID,
                'ORDER_ID':orderid ,
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://localhost:5000/shop/handlerequest/',

        }
    deepak_dict['CHECKSUMHASH'] = Checksum.generate_checksum(deepak_dict, MERCHANT_KEY)
    return render_template('payment/paytm.html', deepak_dict=deepak_dict)

@app.route('/shop/handlerequest/',methods=['POST'])
def shop_handlerequest():
    # print(request.form)
    data = request.form.to_dict()
    check=0
    for i in data.keys():
        # print(i)
        if i=='CHECKSUMHASH':
            check=1

    if 'GATEWAYNAME' in data:
        if data['GATEWAYNAME'] == 'WALLET':
            data['BANKNAME'] = 'null';  #If Gateway is user's paytm wallet setting bankname to null

    if check==1:
        verify = Checksum.verify_checksum(data, MERCHANT_KEY, data['CHECKSUMHASH']) # returns true or false based on calculations
    else:
        verify=False

    # print(verify)

    if verify:
        if data['RESPCODE'] == '01':
            # print(paymentblog[data['ORDERID']],"++++++++++++ORDERSUCCESSFUL++++++++++++++++++++++++",paymentemail[data['ORDERID']])
            cur = mysql.connection.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS club_requirement(blog_id varchar(100) NOT NULL,userid varchar(100),upvote varchar(10),comment varchar(100),time varchar(100),amount_donated FLOAT(8,5) DEFAULT 0,transaction_id varchar(100),primary key (blog_id, userid));')
            # cur.execute("INSERT INTO club_requirement(blog_id,userid,amount_donated,transaction_id,time) VALUES(%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE "+data['key']+" = %s , time=%s",(data['blog_id'],data['author'],data['value'],str(datetime.datetime.now()),data['value'],str(datetime.datetime.now())));
            cur.execute("INSERT INTO club_requirement(blog_id,userid,amount_donated,transaction_id,time) VALUES(%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE amount_donated=amount_donated+"+data['TXNAMOUNT']+",transaction_id=%s ,time=%s",(paymentblog[data['ORDERID']],paymentemail[data['ORDERID']],data['TXNAMOUNT'],data['TXNID'],str(datetime.datetime.now()),data['TXNID'],str(datetime.datetime.now())));
            # cur.execute("update club_requirement SET amount_donated=amount_donated+"+data['TXNAMOUNT']+" where blog_id LIKE %s AND userid LIKE %s",[paymentblog[data['ORDERID']],paymentemail[data['ORDERID']]])
            # UPDATE pollData SET option2 = option2 + 1
            mysql.connection.commit()
            print("order successful"),data['TXNAMOUNT']
        else:
            print("order unsuccessful because"+data['RESPMSG'])
    else:
        print("order unsuccessful because"+data['RESPMSG'])
    return render_template('payment/paytm_response.html',response=data)


@socketio.on('chat')
def chat(data):
    # print("==-=-=======-=---------chat---------================= ",data['from'])
    # cur = mysql.connection.cursor()
    # # cur.execute('CREATE TABLE IF NOT EXISTS blog(author varchar(100),post varchar(100),time varchar(100));')
    # cur.execute("select json_object('pname',`pname`,'pemail',`pemail`) from person where online=1;");
    # # cur.execute("select json_object('did',`did`,'pemail',`pemail`,'cemail',`cemail`,'dtype',`dtype`,'time',`time`,'post',`post`,'filename',`filename`) from blog;");
    # mysql.connection.commit();
    # myresult = cur.fetchall()
    # room = session.get(data['to'])
    room=users[data['to']]
    # print(room)
    emit('chat', data, room=room)

    # users[data['to']].emit('chat',data)



# io=socket(server);


@socketio.on('insert_in_daily_use_item')
def insert_in_daily_use_item(data):
    # print("==========inserting in daily_use_item==================")
    cur = mysql.connection.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS daily_use_item(blog_id varchar(100) NOT NULL,userid varchar(100),recommended varchar(10),not_recommended varchar(10),comment varchar(100),time varchar(100),primary key (blog_id, userid));')
    cur.execute("INSERT INTO daily_use_item(blog_id,userid,"+data['key']+",time) VALUES(%s,%s,%s,%s) ON DUPLICATE KEY UPDATE "+data['key']+" = %s , time=%s",(data['blog_id'],data['author'],data['value'],str(datetime.datetime.now()),data['value'],str(datetime.datetime.now())));
    mysql.connection.commit()

@socketio.on('insert_in_social_blog')
def insert_in_social_blog(data):
    # print("==========inserting in daily_use_item==================")
    cur = mysql.connection.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS social_blog(blog_id varchar(100) NOT NULL,userid varchar(100),interested varchar(10),not_interested varchar(10),comment varchar(100),time varchar(100),primary key (blog_id, userid));')
    cur.execute("INSERT INTO social_blog(blog_id,userid,"+data['key']+",time) VALUES(%s,%s,%s,%s) ON DUPLICATE KEY UPDATE "+data['key']+" = %s , time=%s",(data['blog_id'],data['author'],data['value'],str(datetime.datetime.now()),data['value'],str(datetime.datetime.now())));
    mysql.connection.commit()

@socketio.on('insert_in_club_requirement')
def insert_in_club_requirement(data):
    # print("==========inserting in daily_use_item==================")
    cur = mysql.connection.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS club_requirement(blog_id varchar(100) NOT NULL,userid varchar(100),upvote varchar(10),comment varchar(100),time varchar(100),amount_donated int DEFAULT 0,transaction_id varchar(100),primary key (blog_id, userid));')
    cur.execute("INSERT INTO club_requirement(blog_id,userid,"+data['key']+",time) VALUES(%s,%s,%s,%s) ON DUPLICATE KEY UPDATE "+data['key']+" = %s , time=%s",(data['blog_id'],data['author'],data['value'],str(datetime.datetime.now()),data['value'],str(datetime.datetime.now())));
    mysql.connection.commit()


@socketio.on('show_me_comment')
def show_me_comment(data):

    # print("==========show me comment==================")
    room=users[data['user']]
    cur = mysql.connection.cursor()
    # cur.execute('CREATE TABLE IF NOT EXISTS blog(author varchar(100),post varchar(100),time varchar(100));')
    cur.execute("select json_object('userid',`userid`,'comment',`comment`) from "+data['key']+" where blog_id="+str(data['blog_id'])+";");
    mysql.connection.commit();
    myresult = cur.fetchall()
    s1 = json.dumps(myresult)
    m1=json.loads((s1));
    m1.reverse()
    for x in m1:
        # print(x[0]['post'])
        p = json.loads(x[0]);
        x,y=(p['userid'].split("@"))
        p['userid']=x
        p['comment_id']=data['comment_id']
        # print(p)
        emit('show_me_comment', p, room=room)
    # print(m1)

    # cur = mysql.connection.cursor()
    # cur.execute('CREATE TABLE IF NOT EXISTS club_requirement(blog_id varchar(100) NOT NULL,userid varchar(100),upvote varchar(10),comment varchar(100),time varchar(100),amount_donated int DEFAULT 0,transaction_id varchar(100),primary key (blog_id, userid));')
    # cur.execute("INSERT INTO club_requirement(blog_id,userid,"+data['key']+",time) VALUES(%s,%s,%s,%s) ON DUPLICATE KEY UPDATE "+data['key']+" = %s , time=%s",(data['blog_id'],data['author'],data['value'],str(datetime.datetime.now()),data['value'],str(datetime.datetime.now())));
    # mysql.connection.commit()

# @socketio.on('show_me_comment')
# def show_me_comment(data):
#
#     print("==========show me comment==================",data)
#     room=users[data['user']]
#     cur = mysql.connection.cursor()
#     # cur.execute('CREATE TABLE IF NOT EXISTS blog(author varchar(100),post varchar(100),time varchar(100));')
#     cursor.execute(" drop trigger if exists delete_post_trigger")
#     cur.execute("CREATE TRIGGER delete_post_trigger BEFORE DELETE ON  FOR EACH ROW BEGIN IF (select COUNT(*) from MYTABLE) = 12 THEN SET NEW.COL2 = 10; END IF; END");
#     mysql.connection.commit();
#     myresult = cur.fetchall()
#     s1 = json.dumps(myresult)
#     m1=json.loads((s1));
#     m1.reverse()
#     for x in m1:
#         # print(x[0]['post'])
#         p = json.loads(x[0]);
#         x,y=(p['userid'].split("@"))
#         p['userid']=x
#         p['comment_id']=data['comment_id']
#         print(p)
#         emit('show_me_comment', p, room=room)
#     # print(m1)
