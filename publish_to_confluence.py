import os

from atlassian import Confluence


CONFLUENCE_BASE_URL = os.getenv("CONFLUENCE_BASE_URL")
CONFLUENCE_PAGE = os.getenv("CONFLUENCE_PAGE")
CONFLUENCE_PAT = os.getenv("CONFLUENCE_PAT")
CONFLUENCE_SPACE = os.getenv("CONFLUENCE_SPACE")
CONFLUENCE_TEMPLATE = os.getenv("CONFLUENCE_TEMPLATE")
CONFLUENCE_USERNAME = os.getenv("CONFLUENCE_USERNAME")


CONFLUENCE = Confluence(
    url=CONFLUENCE_BASE_URL,
    username=CONFLUENCE_USERNAME,
    password=CONFLUENCE_PAT,
    cloud=True,
)


def publish_to_confluence():
    print(f"The current environment:\n{os.environ}")


# Do the things
publish_to_confluence()
