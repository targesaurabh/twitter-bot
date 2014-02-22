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
        print 'Encountered error with status code:', status_code
        return True

    def on_timeout(self):
        print 'Timeout...'
        return True

class StreamOperations:
    streamCollection = dict()            
    def keywordChange(self, auth):    	
    	print 'disconnecting'
        sapi.disconnect()            
        self.startStreaming(auth)

    def startStreaming(self, auth, keywords):            
        if(auth.access_token.key in StreamOperations.streamCollection):
            StreamOperations.streamCollection[auth.access_token.key].disconnect()
            print 'disconnected'

    	api = tweepy.API(auth)
    	listenerObj = CustomStreamListener(api)        
        sapi = tweepy.streaming.Stream(auth, listenerObj) 
        StreamOperations.streamCollection[auth.access_token.key] = sapi
        print StreamOperations.streamCollection
        print 'stream started.....'        
        sapi.filter(track=[keywords])        