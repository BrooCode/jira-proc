from fastapi import FastAPI, Request, Form
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import io
import jira_api as jira
# import size as detect_size

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/jira_api")
async def form_post(request: Request):
        jira.create_issue()
        return "Issue Created"