from fastapi import APIRouter, Query
from fastapi.responses import HTMLResponse
import json

router = APIRouter()

@router.get("/get/query")
def get_query_cve(query: str = Query(...)):
    with open("resourses\\known_exploited_vulnerabilities.json", "r", encoding="utf-8") as file:
        data = json.load(file).get("vulnerabilities", [])
        
    query_lower_case = query.lower()
    result = [cve for cve in data
              if any(query_lower_case in cve.get(field, "").lower() for field in ["shortDescription", "vulnerabilityName"])]
    
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <h1>Query Results for: {query}</h1>
        <p><strong>Matches found:</strong> {matches}</p>
    """.format(query=query, matches=len(result))

    if result:
        for cve in result:
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
    else:
        html_content += "<p>No results found matching your query.</p>"

    html_content += """
    </body>
    </html>
    """
    
    return HTMLResponse(content=html_content)