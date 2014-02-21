import tweepy

class CustomStreamListener(tweepy.StreamListener):      
    def __init__(self, api_arg):
    	self.count = 0
    	self.api = api_arg

    def on_status(self, status):   
        print 'Post number : ' + str(self.count)
        self.count = self.count + 1 
        try:
            if (not status.favorited) and (status.lang.strip()=='en'):
                self.api.create_favorite(status.id)                
        except Exception, e:
            print e        
        
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True

class StreamOperations:        
    def keywordChange(self, auth):    	
    	print 'disconnecting'
        sapi.disconnect()            
        self.startStreaming(auth)

    def startStreaming(self, auth):
    	api = tweepy.API(auth)
    	listenerObj = CustomStreamListener(api)
        sapi = tweepy.streaming.Stream(auth, listenerObj)
        sapi.filter(track=['#ecommerce,#socialcommerce'])