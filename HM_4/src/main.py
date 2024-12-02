from fastapi import FastAPI
from end_points import info, get_all, get_known, get_new, get_query

app = FastAPI()

app.include_router(info.router)
app.include_router(get_all.router)
app.include_router(get_known.router)
app.include_router(get_new.router)
app.include_router(get_query.router)