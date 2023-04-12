import os
from datetime import datetime

from atlassian import Confluence


CONFLUENCE_BASE_URL = os.getenv("INPUT_CONFLUENCE_BASE_URL")
CONFLUENCE_PARENT_PAGE = os.getenv("INPUT_CONFLUENCE_PARENT_PAGE")
CONFLUENCE_PAGE_TITLE = os.getenv("INPUT_CONFLUENCE_PAGE_TITLE")
CONFLUENCE_PAT = os.getenv("INPUT_CONFLUENCE_PAT")
CONFLUENCE_SPACE = os.getenv("INPUT_CONFLUENCE_SPACE")
CONFLUENCE_TEMPLATE = os.getenv("INPUT_CONFLUENCE_TEMPLATE")
CONFLUENCE_USERNAME = os.getenv("INPUT_CONFLUENCE_USERNAME")

CONFLUENCE_TEST_STATS = os.getenv("INPUT_TEST_STATS")
CONFLUENCE_TEST_OUTPUT = os.getenv("INPUT_TEST_OUTPUT")


CONFLUENCE = Confluence(
    url=CONFLUENCE_BASE_URL,
    username=CONFLUENCE_USERNAME,
    password=CONFLUENCE_PAT,
    cloud=True,
)

def publish_to_confluence(confluence_api, space):
    # Get the parent page
    parent_page = confluence_api.get_page_by_title(space, CONFLUENCE_PARENT_PAGE)
    parent_page_id = parent_page.get("id")

    test_date = datetime.now().strftime("%m-%d-%Y")
    report_page_title = f"{CONFLUENCE_PAGE_TITLE} - {test_date}"

    # Create the page
    CONFLUENCE.update_or_create(parent_page_id, report_page_title, CONFLUENCE_TEMPLATE, representation="storage")


# Do the things
try:
    publish_to_confluence(CONFLUENCE, CONFLUENCE_SPACE)
except Exception as e:
    print(f"Failed publishing to confluence due to:\n{e}")
