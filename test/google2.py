from googleapiclient.discovery import build
import pprint


from googleapiclient.discovery import build

#my_api_key = "AIbaSyAEY6egFSPeadgK7oS/54iQ_ejl24s4Ggc" #The API_KEY you acquired
#my_cse_id = "012345678910111213141:abcdef10g2h" #The search-engine-ID you created
my_api_key = "AIzaSyAQwvxsjirV3fXxQ_oCClvg5wct0Vyzq8A"
my_cse_id = "a641dd528fa274bc3"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']


results = google_search('宁德时代的股价', my_api_key, my_cse_id, num=10)
for result in results:
    print(result)


    #"https://www.googleapis.com/customsearch/v1?key=AIzaSyAQwvxsjirV3fXxQ_oCClvg5wct0Vyzq8A&q=002624&cx=a641dd528fa274bc3&start={1}&num={10}"
    #"https://www.googleapis.com/customsearch/v1?key=AIzaSyAQwvxsjirV3fXxQ_oCClvg5wct0Vyzq8A&q=%E5%AE%81%E5%BE%B7%E6%97%B6%E4%BB%A3%E7%9A%84%E8%82%A1%E4%BB%B7&cx=a641dd528fa274bc3&start=1&num=10&lr=zh&tbm=nws"