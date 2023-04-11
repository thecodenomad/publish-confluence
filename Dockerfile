FROM python:3.11.3-alpine3.17

# Add Python Requirements
RUN pip install atlassian-python-api \
                bs4                  \
                lxml                 \
                jinja2

# Do the things
COPY publish_to_confluence.py /publish_to_confluence.py

ENTRYPOINT [ "python3", "/publish_to_confluence.py" ]
