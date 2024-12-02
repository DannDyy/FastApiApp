from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from datetime import datetime
import json

router = APIRouter()

@router.get("/get/new")
def get_new_cve():
    with open("resourses/known_exploited_vulnerabilities.json") as file:
        data = json.load(file)
    new_cve = sorted(data["vulnerabilities"], key=lambda x: datetime.strptime(x["dateAdded"], "%Y-%m-%d"), reverse=True) [:10]

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <h1>New CVE Entries</h1>
    """
    
    for cve in new_cve:
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