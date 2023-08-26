FROM python:3.11-bookworm
SHELL ["/bin/bash", "-c"] 
WORKDIR /app
COPY Pipfile Pipfile.lock ./
ENV PIPENV_VENV_IN_PROJECT=1
RUN python3 -m pip install pipenv
RUN pipenv install
COPY . .
CMD source .venv/bin/activate && uwsgi --ini ./uwsgi.ini