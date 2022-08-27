import requests
from pprint import pprint
import json


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.
    url = 'https://api.themoviedb.org/3/'
    path = 'search/movie'
    params = {
        'api_key' : 'd167ae542dc3068ed1ff2d9023caff95',   
        'query' : title
    }
    response = requests.get(url+path, params).json()
    if response.get('total_pages') == 0:
        return None

    m_id = response.get('results')[0].get('id')
    
    path = f'movie/{m_id}/credits'
#    del(params['query'])                    # 삭제 안해도 되지 않을까?
    response2 = requests.get(url+path, params).json()

    cast = []
    crew = []
    for i in response2.get('cast'):
        if i.get('cast_id') < 10:
            cast.append(i.get('name'))
    for i in response2.get('crew'):
        if i.get('department') == 'Directing':
            crew.append(i.get('name'))
    result = {
        'cast' : cast,
        'crew' : crew
    }

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
