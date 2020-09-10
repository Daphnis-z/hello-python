import random

from elasticsearch import Elasticsearch

from hello import log_util


def gene_goods_id(num):
    str_num = str(num)
    zero_num = 3 - len(str_num)
    
    for i in range(0, zero_num):
        str_num = '0' + str_num
    return str_num


def insert_data():
    """
    C: insert data to es
    """

    # "goods_id": {
    #     "type": "keyword"
    # },
    # "name": {
    #     "type": "keyword"
    # },
    # "price": {
    #     "type": "double"
    # }
    for i in range(1, 21):
        goods_id = gene_goods_id(i)
        doc = {
            'goods_id': goods_id,
            'name': '努比亚Z' + str(i),
            "price": random.randint(1000, 3000)
        }
        result = es_client.index(index='demo-data-202008', body=doc)
        log.info('insert result: {}'.format(result))


def query_data():
    """
    R: query data from es
    """
    body = {
        'query': {
            'match_all': {}
        }
    }

    scroll = '5m'
    size = 10
    query_result = es_client.search(index='demo-data-all', scroll=scroll, size=10, body=body)
    all_data = query_result.get("hits").get("hits")
    if all_data:
        scroll_id = query_result["_scroll_id"]
        data_count = query_result["hits"]["total"]['value']
        for i in range(int(data_count / size)):
            res = es_client.scroll(scroll_id=scroll_id, scroll=scroll)
            all_data = all_data + res["hits"]["hits"]

        es_client.clear_scroll(scroll_id=scroll_id)

    num = 1
    for doc in all_data:
        log.info('{}: {}'.format(num, doc['_source']))
        num += 1


def update_data():
    """
    U: update es data
    """
    body = {
        "script": {
            "source": "ctx._source['price']=3699.00"
        },
        "query": {
            "bool": {
                "must": [{"match": {"goods_id": "010"}}]
            }
        }
    }

    result = es_client.update_by_query(index='demo-data-202008', body=body)
    log.info(result)


def delete_data():
    """
    D: delete es data
    """
    body = {
        "query": {
            "bool": {
                "must": [{"match": {"goods_id": "014"}}]
            }
        }
    }

    result = es_client.delete_by_query(index='demo-data-202008', body=body)
    log.info(result)


if __name__ == '__main__':
    log = log_util.get_logger('es-crud')
    log.info('It is some es operators ..')

    es_client = Elasticsearch('192.168.227.200', port=9200)

    # insert_data()
    # query_data()
    # delete_data()
    update_data()
