from flask import Flask, render_template, request, session
from stream import StreamOperations

import tweepy

app = Flask('TwitterBot')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

streamChangerObj = StreamOperations()

@app.route('/index',methods=['GET'])
def streamData():  
    consumer_key = "4T61yy5gA1df0Zx05ClTJw"
    consumer_secret = "co7HSpQ3HqvHZX3lqUiYEMDES48WVJIyCfyuNab8"
    # access_key = "420078732-IXAtLJjOcxD7UlCHxGrgqes971uRyBRLRdh8kNNN"
    # access_secret = "nvthoZJq2dGlD5iiQhiN0cCDonHh6nMIMpJWv8eelUswU" 

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_key, access_secret)        
    # streamChangerObj.startStreaming(auth)

    verifier = request.args.get('oauth_verifier')
    print verifier

    if(not verifier):        
        auth.set_request_token(session['request_token_key'], session['request_token_secret'])
        try:
            auth.get_access_token(verifier)
        except tweepy.TweepError:
            print 'Error! Failed to get access token.'
        streamChangerObj.startStreaming(auth)
    else:                        
        auth_url = auth.get_authorization_url()
        session['request_token_key'] = auth.request_token.key
        session['request_token_secret'] = auth.request_token.secret
        return render_template('redirect.html',redirect_url=auth_url)                

if __name__ == '__main__':
    app.run(debug='true')