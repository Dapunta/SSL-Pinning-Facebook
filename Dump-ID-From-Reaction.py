import requests, json, uuid, base64

def DumpReaction(post_id:str, token:str, cursor=None):
    r    = requests.Session()
    var  = {"reactors_connection_at_stream_use_customized_batch":False,"reactors_connection_first":25,"fetch_invite_all_qe":False,"orderby":["is_viewer","is_viewer_friend","is_creator"],"top_story_prefetch_size":0,"profile_pic_media_type":"image/x-auto","fetch_invitable_reactor_count":True,"should_prefetch_top_story":False,"reactors_profile_image_size":40,"feedback_id":str(base64.b64encode(('feedback:{}'.format(post_id)).encode('utf-8')).decode('utf-8')),"paginationPK":str(base64.b64encode(('feedback:{}'.format(post_id)).encode('utf-8')).decode('utf-8')),"reactors_connection_after_cursor":cursor}
    data = {'access_token':token,'method':'post','pretty':False,'format':'json','server_timestamps':True,'locale':'user','purpose':'fetch','fb_api_req_friendly_name':'FeedbackReactorsGraphService_At_Connection_Pagination_Feedback_reactors_connection','fb_api_caller_class':'ConnectionManager','client_doc_id':'14962755647493038689879967568','fb_api_client_context':json.dumps({"load_next_page_counter":1,"client_connection_size":25}),'variables':json.dumps(var),'fb_api_analytics_tags':["At_Connection","GraphServices"],'client_trace_id':str(uuid.uuid4())}
    pos  = r.post('https://graph.facebook.com/graphql', data=data).json()
    try:
        for i in pos['data']['node']['reactors']['edges']:
            try:
                id, name = i['node']['id'], i['node']['name']
                print('{}|{}'.format(id, name))
            except Exception: continue
        if pos['data']['node']['reactors']['page_info']['has_next_page']:
            next_cursor = pos['data']['node']['reactors']['page_info']['end_cursor']
            DumpReaction(post_id=post_id, token=token, cursor=next_cursor)
    except Exception: print(pos)

post_id = '733442355639178'  #--> Post ID, You Can Scrap In Web "share_fbid":"733442355639178"
token   = 'EAAAAU....'       #--> Access Token (EAAU from b-graph login)

DumpReaction(post_id=post_id, token=token)