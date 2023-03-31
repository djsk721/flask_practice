from flask import Flask, render_template, url_for, redirect
from authlib.integrations.flask_client import OAuth
import os
from config import config


app = Flask(__name__)
app.secret_key = os.urandom(12)

oauth = OAuth(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/google/')
def google():
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=config['GOOGLE_CLIENT_ID'],
        client_secret=config['GOOGLE_CLIENT_SECRET'],
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    redirect_uri = url_for('google_auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    # DB에 저장 token['userinfo'] 이용하여
    print(token['userinfo'])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)