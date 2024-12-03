from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get('/info', response_class=HTMLResponse)
def info():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                padding: 10px;
                text-align: center;
            }
            h1 {
                color: #9b59b6;
            }
            p {
                font-size: 18px;
            }
            .image-container {
                margin-top: 15px;
                text-align: center;
            }
            img {
                max-width: 100%;
                height: auto;
                display: block;
                margin: 0 auto;
            }
        </style>
    </head>
    <body>
        <h1>Hello, my name is Danylo!</h1>
        <p>This is my FastAPI App, it can help you with viewing NIST CVE reports via Elasstic Search DB.</p>
        <p>To navigate, change the URL!</p>
        <p>Available endpoints: /get/all, /get/known, /get/new, /get/query, /init_db</p>

        <div class="image-container">
            <img src="https://maximum.fm/uploads/media_news/2021/01/5ffadd48c7391685703632.jpg?w=1200&h=675&il&q=90&output=jpg" alt="Image">
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)