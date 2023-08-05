from flask import Flask, redirect, request, jsonify
import facebook

# Facebook app credentials
app_id = 'YOUR_APP_ID'
app_secret = 'YOUR_APP_SECRET'
authorization_base_url = 'https://www.facebook.com/v18.0/dialog/oauth'
token_url = 'https://graph.facebook.com/v18.0/oauth/access_token'
redirect_uri = 'http://localhost:5000/callback'  # Update with your own redirect URI

app = Flask(__name__)


# Facebook app credentials


@app.route('/')
def index():
    return 'Login with Facebook'


@app.route('/login-facebook')
def login():
    auth_url = facebook.Auth(app_id, app_secret, redirect_uri).get_auth_url()

    return redirect(auth_url)


@app.route('/callback')
def callback():
    global access_token
    code = request.args.get('code')
    access_token = facebook.Auth(app_id, app_secret, redirect_uri).get_access_token_from_code(code)
    # Retrieve user's name and ID
    graph = facebook.GraphAPI(access_token['access_token'])
    me = graph.get_object('me',)
    print(graph)
    id = me['id']
    name = me['name']
    return  name



if __name__ == '__main__':
    app.run(debug=True)
