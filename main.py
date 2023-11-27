import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from logging.handlers import TimedRotatingFileHandler
from routes.endpoints.concurrency.concurrency import concurrency_api
from routes.endpoints.guidancehub.guidancehub import guidancehub_api
import config

# from git import Repo

# logs formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def setup_logger(name, log_file, level=logging.INFO):
    handler = TimedRotatingFileHandler(f"{log_file}", when='midnight')
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


# Information Logger
info_logger = setup_logger('info_logger', 'logs/info_logger/info_logger.log')

tags_metadata = [
    {
        "name": "main",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "loan",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

# # Provide the path to the repository
# repo_path = "/Users/fdsap-rommel/Projects/API/PythonTemplate"
#
# # Open the repository
# repo = Repo(repo_path)
#
# # Get the HEAD commit
project_version = "v1.0.0"
# head_commit = repo.head.commit
# for commit in repo.iter_commits():
#     message = commit.message
#     loc = message.find("Version")
#     project_version = message[(loc+8):-1]
#     break

# Retrieve the commit ID
# commit_id = head_commit.hexsha
commit_id = "v1.0.0"

app = FastAPI(
    title="Template",
    description=f"Rommel Lagurin Python Template. Version - {commit_id}",
    version=f"{project_version}"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
async def startup():
    await config.database.connect()


@app.on_event("shutdown")
async def shutdown():
    print("shutdown")
    await config.database.disconnect()


app.include_router(guidancehub_api)



