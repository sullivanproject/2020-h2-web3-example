import requests
import xmltodict
import json
from pprint import pprint

def get_corona_data(startCreateDt, endCreateDt):
    url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"
    params = {
        'serviceKey':'3orEATyZglGF61/gMb9YFa9bNrX72kHX/fxAq+bR17uawigH5YY8v5sr6cNNN6X/cLBtXzPIZN7M7lmwcfH7GQ==',
        'pageNo':'1',
        'numOfRows':10,
        'startCreateDt': startCreateDt , # '20200701',
        'endCreateDt':  endCreateDt , # '20200701',
    }

    res = requests.get(url, params=params)
    # print(res.url)
    # print(res.text)

    # xml to dict
    dict_data = xmltodict.parse(res.text)
    # print(dict_data)

    # dict to json
    json_data = json.dumps(dict_data)
    # print(json_data, type(json_data))

    # json to dict
    dict_data = json.loads(json_data)
    # print(dict_data, type(dict_data))
    # pprint(dict_data['response']['body']['items']['item'])

    # totalCount로 제대로 데이터가 가져와졌는지 확인하기
    totalCount = dict_data['response']['body']['totalCount']
    # print(totalCount)
    if totalCount == "0" :
        return False

    # 지역 정보를 담은 리스트
    area_data = dict_data['response']['body']['items']['item']
    area_data.reverse()
    # print(area_data)

    return area_data

if __name__ == "__main__":
    data = get_corona_data('20200630','20200630')
    print(data)
