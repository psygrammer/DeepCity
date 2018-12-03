D_RLET_TYPE_CODE = {
                    '아파트':'A01',
                    '오피스텔':'A02',
                    '분양권':'B01',
                    '주택':'C03', 
                    '토지':'E03', 
                    '원룸':'C01',
                    '상가':'D02', 
                    '사무실':'D01', 
                    '공장':'E02', 
                    '재개발':'F01', 
                    '건물':'D03'
             }

D_TRADE_TYPE_CODE = {
                    '전체':'all',
                    '매매':'A1', 
                    '전세':'B1',
                    '월세':'B2', 
                    '단기임대':'B3'
              }
    
D_HSCP_TYPE_CODE = {
                    '아파트':'A01', 
                    '주상복합':'A03', 
                    '재건축':'A04'
             }
    
def get_search_api(cortar_no=None, page_no=None, text=None) :
    # rletTypeCd: 
    #      - A01=아파트, 
    #      - A02=오피스텔, 
    #      - B01=분양권, 
    #      - 주택=C03, 
    #      - 토지=E03, 
    #      - 원룸=C01, 
    #      - 상가=D02, 
    #      - 사무실=D01, 
    #      - 공장=E02, 
    #      - 재개발=F01, 
    #      - 건물=D03
    # tradeTypeCd (거래종류):
    #      - all=전체, 
    #      - A1=매매, 
    #      - B1=전세, 
    #      - B2=월세, 
    #      - B3=단기임대
    # hscpTypeCd (매물종류): 
    #      - 아파트=A01, 
    #      - 주상복합=A03, 
    #      - 재건축=A04 (복수 선택 가능)
    # cortarNo(법정동코드): 
    #      - (예: 1168010600 서울시, 강남구, 대치동)
    #      - 다음을 참조 - https://goo.gl/P6ni8Q
        
    root_url = "http://land.naver.com/article/articleList.nhn"
    args_types = {}
    
    args_types['rletTypeCd'] = D_RLET_TYPE_CD['아파트']
    args_types['tradeTypeCd'] = D_TRADE_TYPE_CODE['전체']
    args_types['hscpTypeCd'] = D_HSCP_TYPE_CODE['아파트'] + ":" + D_HSCP_TYPE_CODE['주상복합'] + ":" + D_HSCP_TYPE_CODE['재건축']
    args_types['cortarNo'] = str(cortar_no) #'1168010600'
    
    #print(args_types)
    
    args_str = [k+'='+v for k, v in args_types.items()] 
    #print(args_str)
    api_url = root_url + "?" + "&".join(args_str)
    #print(api_url)
    
    return api_url
    