import requests, json, uuid

def DumpMemberGroup(group_id:str, token:str, cursor=None):
    r    = requests.Session()
    var  = {"group_member_profiles_connection_at_stream_use_customized_batch":False,"group_member_profiles_connection_first":15,"paginationPK":group_id,"profile_image_size":64,"group_id":group_id,"group_member_profiles_connection_after_cursor":cursor}
    data = {'access_token':token,'method':'post','pretty':False,'format':'json','server_timestamps':True,'locale':'user','purpose':'fetch','fb_api_req_friendly_name':'FetchGroupMemberListRecentlyJoined_At_Connection_Pagination_Group_group_member_profiles_connection','fb_api_caller_class':'ConnectionManager','client_doc_id':'37182335416736319549125275009','fb_api_client_context':json.dumps({"load_next_page_counter":1,"client_connection_size":15}),'variables':json.dumps(var),'fb_api_analytics_tags':["At_Connection","GraphServices"],'client_trace_id':str(uuid.uuid4())}
    pos  = r.post('https://graph.facebook.com/graphql', data=data).json()
    try:
        for i in pos['data']['node']['group_member_profiles']['edges']:
            try:
                id, name = i['node']['id'], i['node']['name']
                print('{}|{}'.format(id, name))
            except Exception: continue
        if pos['data']['node']['group_member_profiles']['page_info']['has_next_page']:
            next_cursor = pos['data']['node']['group_member_profiles']['page_info']['end_cursor']
            DumpMemberGroup(group_id=group_id, token=token, cursor=next_cursor)
    except Exception: print(pos)

group_id = '804848814300940' #--> Group ID
token    = 'EAAAAU....'      #--> Access Token (EAAU from b-graph login)

DumpMemberGroup(group_id=group_id, token=token)