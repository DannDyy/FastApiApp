# FastApiApp
UndDef HomeWork4 Python course - FastApi app
--------------------------------------------------------------------------------------------
Some explanations:
I use the datetime module to work with dates and times.
In the app, datetime.now() is used to get the current date-time that helps filter and sort vulnerabilities based on their dateAdded field.
*in \get\all i set 20 days, because within 5 days there is no cve to display. It can be easily changed, so i left it like that
New cve sorted in descending order (reverse=True) and return the top 10 (and i made it by datetime again)
Filter for vulnerabilities that have value "Known" for the knownRansomwareCampaignUse field is just a list comprehension that checks this specific field.
--------------------------------------------------------------------------------------------
All pages of app are displayed using html.
Html content styles cve data into tags with param <strong> for the field names, and <br> for line breaks.
The content is then returned as a response using HTMLResponse (it is inside fastapi lib already)
*also, there is a prety noraml cat on info page, so don`t be scared ^_^
