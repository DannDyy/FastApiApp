from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from elasticsearch import Elasticsearch

router = APIRouter()

db = Elasticsearch(
    'https://552ae5cc2b68444b98f7ba59322c15f4.us-central1.gcp.cloud.es.io:443',
    api_key=('ZkdNMGlwTUJneUx3UFFVX1gzcjE6RHNwWHhiYnpRVU9VaVIzS3ZMMDRrZw==')
)

@router.get('/get/known')
def get_known_cve():
    index = 'cve'

    query = {
        'query': {
            'match': {
                'knownRansomwareCampaignUse': 'Known'
            }
        },
        'size': 10
    }

    response = db.search(index=index, body=query)
    hits = response.get('hits', {}).get('hits', [])

    known_vulnerabilities = [hit['_source'] for hit in hits]

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <h1>Known CVE Entries</h1>
    """
    
    for cve in known_vulnerabilities:
        html_content += f"""
        <p>
            <strong>cveID:</strong> {cve.get("cveID", "N/A")}<br>
            <strong>vendorProject:</strong> {cve.get("vendorProject", "N/A")}<br>
            <strong>product:</strong> {cve.get("product", "N/A")}<br>
            <strong>vulnerabilityName:</strong> {cve.get("vulnerabilityName", "N/A")}<br>
            <strong>dateAdded:</strong> {cve.get("dateAdded", "N/A")}<br>
            <strong>shortDescription:</strong> {cve.get("shortDescription", "N/A")}<br>
            <strong>requiredAction:</strong> {cve.get("requiredAction", "N/A")}<br>
            <strong>dueDate:</strong> {cve.get("dueDate", "N/A")}<br>
            <strong>knownRansomwareCampaignUse:</strong> {cve.get("knownRansomwareCampaignUse", "N/A")}<br>
            <strong>notes:</strong> {cve.get("notes", "N/A")}<br>
            <strong>cwes:</strong> {', '.join(cve.get("cwes", []))}<br>
        </p>
        <hr>
        """
    
    html_content += """
    </body>
    </html>
    """
    
    return HTMLResponse(content=html_content)