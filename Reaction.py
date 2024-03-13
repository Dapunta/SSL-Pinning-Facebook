import requests, random, json, uuid, time, base64

def Reaction(actor_id:str, post_id:str, react:str, token:str):
    r    = requests.Session()
    var  = {"input":{"feedback_referrer":"native_newsfeed","tracking":[None],"feedback_id":str(base64.b64encode(('feedback:{}'.format(post_id)).encode('utf-8')).decode('utf-8')),"client_mutation_id":str(uuid.uuid4()),"nectar_module":"newsfeed_ufi","feedback_source":"native_newsfeed","attribution_id_v2":"NewsFeedFragment,native_newsfeed,cold_start,1710331848.276,264071715,4748854339,,","feedback_reaction_id":react,"actor_id":actor_id,"action_timestamp":str(time.time())[:10]}}
    data = {'access_token':token,'method':'post','pretty':False,'format':'json','server_timestamps':True,'locale':'id_ID','fb_api_req_friendly_name':'ViewerReactionsMutation','fb_api_caller_class':'graphservice','client_doc_id':'2857784093518205785115255697','variables':json.dumps(var),'fb_api_analytics_tags':["GraphServices"],'client_trace_id':str(uuid.uuid4())}
    pos  = r.post('https://graph.facebook.com/graphql', data=data).json()
    try:
        if react in str(pos): print('React Success!')
        else: print('React Failed!')
    except Exception: print('React Failed!')

actor_id = '61555299014636'  #--> Your Logged Profile ID
post_id  = '434488795714662' #--> Post ID Target You Want To React, You Can Scrap In Web "share_fbid":"733442355639178"
react    = random.choice([   #--> Type Of Reaction
    '1635855486666999', # Like
    '1678524932434102', # Love
    '115940658764963',  # Haha
    '478547315650144',  # Wow
    '613557422527858',  # Care
    '908563459236466',  # Sad
    '444813342392137']) # Angry
token = 'EAAAAU....'         #--> Access Token (EAAU from b-graph login)

Reaction(actor_id=actor_id, post_id=post_id, react=react, token=token)