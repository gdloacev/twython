from twython import Twython, TwythonAuthError, TwythonError

app_key = 'xiHlth8bVMiFmxGt741g'
app_secret = 'pnSyIx7awxtB3BRCArdfZ5neebAAokzhmPQgzerqlU'

t = Twython(app_key, app_secret)

auth_props = t.get_authentication_tokens(callback_url='http://localhost.com/login_twitter.html')

oauth_token = '90926098-ha8yQlvDrtI92odzBcVlBehmxGpZdrOQqLOJAFs4E'
oauth_token_secret = '2n8hPIA9yF6J20G9ZjWAcDLAnKarvSYbYyjV8EDw'
oauth_verifier = ''

try:
    t = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
    followers = t.get_followers_ids()

    for follower_id in followers['ids']:
        print follower_id

    tweets = t.get_home_timeline()

    for tweet in tweets:
        print 'Name: %s \n' % (tweet['user']['name'].encode('utf-8'))
        print 'Tweet: %s \n' % (tweet['text'].encode('utf-8'))

    mentions = t.get_mentions_timeline()

    for mention in mentions:
        print 'Name: %s \n' % (mention['user']['name'].encode('utf-8'))
        print 'Mention: %s \n' % (mention['text'].encode('utf-8'))

except TwythonAuthError as e:
    print e
except TwythonError as er:
    print er
