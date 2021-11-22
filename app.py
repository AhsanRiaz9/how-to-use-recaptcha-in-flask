from flask import *
from flask_recaptcha import ReCaptcha

app = Flask(__name__)
app.config['RECAPTCHA_SITE_KEY'] = 'your public key for re-captcha'
app.config['RECAPTCHA_SECRET_KEY'] = 'your secret key for re-captcha'
app.config['RECAPTCHA_OPTIONS']= {'theme':'white'}
app.config['RECAPTCHA_USE_SSL']= False

recaptcha = ReCaptcha(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = '' # Create empty message
    if request.method == 'POST': # Check to see if flask.request.method is POST
        if recaptcha.verify(): # Use verify() method to see if ReCaptcha is filled out
            message = 'Thanks for filling out the form!' # Send success message
        else:
            message = 'Please fill out the ReCaptcha!' # Send error message
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()
