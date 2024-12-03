from fastapi import APIRouter
from elasticsearch import Elasticsearch
import json

router = APIRouter()

@router.get('/init_db')
def init_db():
    INDEX = 'cve'

    db = Elasticsearch(
        'https://552ae5cc2b68444b98f7ba59322c15f4.us-central1.gcp.cloud.es.io:443',
        api_key='ZkdNMGlwTUJneUx3UFFVX1gzcjE6RHNwWHhiYnpRVU9VaVIzS3ZMMDRrZw=='
    )

    if not db.indices.exists(index=INDEX):
        db.indices.create(index=INDEX)

    with open('resourses\known_exploited_vulnerabilities.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    vulnerabilities = data.get('vulnerabilities', [])

    if db.count(index=INDEX)['count'] != len(vulnerabilities):
        db.delete_by_query(index=INDEX, body={'query': {'match_all': {}}})
        for id, cve in enumerate(vulnerabilities, start=1):
            db.index(index=INDEX, id=f'cve-{id}', document=cve)
        return "Database successfully updated!"

    return "Database already has last update!"