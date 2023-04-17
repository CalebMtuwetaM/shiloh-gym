from flask import Flask,render_template,flash,redirect,url_for
from forms import RegistrationForm,LoginForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)




@app.route('/')
def home():
  return render_template('home.html')


@app.route('/communities')
def communities():
  return render_template('communities.html')


@app.route('/morningclass')
def morningclass():
  return render_template('morningclass.html')

 
@app.route('/eveningclass')
def eveningclass():
  return render_template('eveningclass.html')


@app.route('/boxingclass')
def boxingclass():
  return render_template('boxingclass.html')


@app.route('/yogaclass')
def yogaclass():
  return render_template('yogaclass.html')


@app.route('/karateclass')
def karateclass():
  return render_template('karateclass.html')


@app.route('/saturdayclass')
def saturdayclass():
  return render_template('saturdayclass.html')


@app.route('/kidsclass')
def kidsclass():
  return render_template('kidsclass.html')
                         
app.config['SECRET_KEY'] = 'Shiloh-gym' # Set your secret key here
csrf = CSRFProtect(app)


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!","success")
        return redirect(url_for("home"))
    return render_template('register.html', title='Register', form=form)
    

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('communities'))
        else:
            flash('Login unsuccessful. Please check username and password','danger')
    return render_template("login.html",title="Login",form=form)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)