import requests
from pprint import pprint


def recommendation(title):
    url = 'https://api.themoviedb.org/3/'
    path = 'search/movie'
    params = {
        'api_key' : 'd167ae542dc3068ed1ff2d9023caff95',   
        'query' : title
    }
    response = requests.get(url+path, params).json()

#    print(f'{title}', response)
    if response.get('total_pages') == 0:
        return None
    path = 'movie/{}/recommendations'.format(response.get('results')[0].get('id'))
    params = {
        'api_key' : 'd167ae542dc3068ed1ff2d9023caff95',   
        'language': 'ko-KR'
    }
    response = requests.get(url+path, params).json()
    res = []
    for i in response.get('results'):
        res.append(i.get('title'))

    return res


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    print(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
