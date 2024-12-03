from elasticsearch import Elasticsearch

def create_cve_index():
    es_url = 'https://552ae5cc2b68444b98f7ba59322c15f4.us-central1.gcp.cloud.es.io:443'
    es_token = 'ZkdNMGlwTUJneUx3UFFVX1gzcjE6RHNwWHhiYnpRVU9VaVIzS3ZMMDRrZw=='

    client = Elasticsearch(es_url, api_key=es_token)
    
    if client.indices.exists(index='cve'):
        print('Index cve already exists!')
        return
    
    try:
        response = client.indices.create(index='cve')
        if response.get('acknowledged', False):
            print('Index cve created!')
    except Exception as e:
        print('Creation failed!', str(e))

if __name__ == '__main__':
    create_cve_index()