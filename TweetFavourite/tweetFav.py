from flask import Flask, render_template, request, session
from stream import StreamOperations

import tweepy

app = Flask('TwitterBot')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

streamChangerObj = StreamOperations()

@app.route('/index')
def indexPage():
    return '''<html>
                <body>
                    <form action="/startbot" method="post" enctype="multipart/form-data">
                        <input type="textbox" name="hashtags">Enter hashtags
                        <input type="submit" value="Submit">
                    </form>
                </body>
            </html>''' 
    

@app.route('/startbot',methods=['GET','POST'])
def streamData():     
    consumer_key = "4T61yy5gA1df0Zx05ClTJw"
    consumer_secret = "co7HSpQ3HqvHZX3lqUiYEMDES48WVJIyCfyuNab8"
    # access_key = "420078732-IXAtLJjOcxD7UlCHxGrgqes971uRyBRLRdh8kNNN"
    # access_secret = "nvthoZJq2dGlD5iiQhiN0cCDonHh6nMIMpJWv8eelUswU" 

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_key, access_secret)        
    # streamChangerObj.startStreaming(auth)

    verifier = request.args.get('oauth_verifier')
    print 'verifier received from twitter callback: '
    print verifier

    if(verifier):            
        auth.set_request_token(session['request_token_key'], session['request_token_secret'])
        try:
            auth.get_access_token(verifier)
        except tweepy.TweepError:
            print 'Error! Failed to get access token.'
                        
        print 'hashtags stored in session:'
        print session['hashtags']
        streamChangerObj.startStreaming(auth, session['hashtags'])
        return '''Twitter Bot started...'''
    else:                                
        auth_url = auth.get_authorization_url()
        session['request_token_key'] = auth.request_token.key
        session['request_token_secret'] = auth.request_token.secret
        print 'hashtags received from user:'
        print request.form.get('hashtags')                        
        session['hashtags'] = request.form.get('hashtags')
        return render_template('redirect.html',redirect_url=auth_url)                

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True, threaded = True, port = 80)