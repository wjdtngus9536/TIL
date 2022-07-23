# 'https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>'
import requests
from pprint import pprint

def popular_count():
    url = 'https://api.themoviedb.org/3/'
    path = 'movie/popular' # /movie/{movie_id} : 변수처럼 써라
    params={
        'api_key' : 'd167ae542dc3068ed1ff2d9023caff95',
        'language': 'ko-KR'
    }

    response = requests.get(url+path, params = params).json()
    
    return len(response['results'])
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
