import requests, json, uuid

def DumpFriendlist(id:str, token:str, cursor=None):
    r    = requests.Session()
    var  = {"friends_paginating_at_stream_use_customized_batch":False,"profile_image_size":60,"friends_paginating_first":20,"profile_id":id,"paginationPK":id,"friends_paginating_after_cursor":cursor}
    data = {'access_token':token,'method':'post','pretty':False,'format':'json','server_timestamps':True,'locale':'user','purpose':'fetch','fb_api_req_friendly_name':'FriendListContentQuery_At_Connection_Pagination_User_friends_paginating','fb_api_caller_class':'ConnectionManager','client_doc_id':'24605340972600723188569773708','fb_api_client_context':json.dumps({"load_next_page_counter":1,"client_connection_size":20}),'variables':json.dumps(var),'fb_api_analytics_tags':["At_Connection","GraphServices"],'client_trace_id':str(uuid.uuid4())}
    pos  = r.post('https://graph.facebook.com/graphql', data=data).json()
    try:
        for i in pos['data']['node']['friends']['edges']:
            try:
                id, name = i['node']['id'], i['node']['name']
                print('{}|{}'.format(id, name))
            except Exception: continue
        if pos['data']['node']['friends']['page_info']['has_next_page']:
            next_cursor = pos['data']['node']['friends']['page_info']['end_cursor']
            DumpFriendlist(id=id, token=token, cursor=next_cursor)
    except Exception: print(pos)

id    = '100047167328313' #--> Account ID
token = 'EAAAAU....'      #--> Access Token (EAAU from b-graph login)

DumpFriendlist(id=id, token=token)