import requests, re, json, uuid

def DumpSearchName(search:str, token:str, cursor=None):
    r    = requests.Session()
    var  = {"end_cursor":cursor,"image_high_width":540,"enable_bloks":True,"scale":"1","image_large_aspect_height":282,"entered_query_text":"","disable_story_menu_actions":False,"nt_context":{"styles_id":"e6c6f61b7a86cdf3fa2eaaffa982fbd1","using_white_navbar":True,"pixel_ratio":1,"is_push_on":True,"bloks_version":"c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec"},"product_item_image_size":152,"profile_image_size":94,"search_query_arguments":{"family_device_id":str(uuid.uuid4())},"image_medium_width":270,"bsid":str(uuid.uuid4()),"callsite":"android:user_search","image_large_aspect_width":540,"bqf":"keywords_users({})".format(search),"enable_at_stream":True,"filters_enabled":False,"supported_experiences":["FAST_FILTERS","FILTERS","FILTERS_AS_SEE_MORE","INSTANT_FILTERS","MARKETPLACE_ON_GLOBAL","MIXED_MEDIA","NATIVE_TEMPLATES","NT_ENABLED_FOR_TAB","NT_SPLIT_VIEWS","PHOTO_STREAM_VIEWER","SEARCH_INTERCEPT","SEARCH_SNIPPETS_ICONS_ENABLED","USAGE_COLOR_SERP","commerce_groups_search","keyword_only"],"ui_theme_name":"APOLLO_FULL_BLEED","default_image_scale":1,"tsid":str(uuid.uuid4()),"request_index":0,"query_source":"unknown","image_low_width":180,"inline_comments_location":"search"}
    data = {'access_token':token,'method':'post','pretty':False,'format':'json','server_timestamps':True,'locale':'id_ID','fb_api_req_friendly_name':'SearchResultsGraphQL-pagination_query','fb_api_caller_class':'graphservice','client_doc_id':'395907910716207519270483411726','variables':json.dumps(var),'fb_api_analytics_tags':["pagination_query","GraphServices"],'client_trace_id':str(uuid.uuid4())}
    pos  = r.post('https://graph.facebook.com/graphql', data=data).text.replace('\\','')
    try:
        mat = r'"strong_id__":\".*?\","id":"(.*?)","profile_picture":.*?,"name":"(.*?)",'
        gex = re.findall(mat, str(pos))
        for i in gex:
            try:
                id, name = i[0], i[1]
                print('{}|{}'.format(id, name))
            except Exception: continue
        if re.search(r'"has_next_page":(.*?)}',str(pos)).group(1) == 'true':
            next_cursor = re.search(r'"end_cursor":"(.*?)"',str(pos)).group(1)
            DumpSearchName(search=search, token=token, cursor=next_cursor)
    except Exception: print(pos)

search = 'Andika'     #--> Name You Want To Search
token  = 'EAAAAU....' #--> Access Token (EAAU from b-graph login)

DumpSearchName(search=search, token=token)