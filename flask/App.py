from flask import Flask, render_template,request,url_for,redirect,flash
from flask_mysqldb import MySQL



app= Flask(__name__)
#mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

app.secret_key='mysecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_contact',methods=['POST'])
def add_contact():
    if request.method=='POST':
        fullname= request.form['fullname']
        phone= request.form['phone']
        email= request.form['email']
        print(fullname)
        print(phone)
        print(email)

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname,phone,email) VALUES (%s,%s,%s)',(fullname,phone,email))
        mysql.connection.commit()

        flash('contacto agregado!!')
        return redirect(url_for('index'))



@app.route('/edit')
def edit_contact():
    return 'edit contact'

@app.route('/delet')
def delete_contact():
    return 'delete contact'



if __name__== '__main__':
    app.run(port=3000,debug=True)
