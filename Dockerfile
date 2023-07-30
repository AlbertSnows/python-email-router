FROM python:latest

WORKDIR /app

COPY . /app

RUN python3 -m venv .venv
RUN . .venv/bin/activate
RUN pip install --upgrade pip
RUN pip install flask pyrsistent waitress jsonschema beautifulsoup4 requests python-dotenv

# RUN pip install dist/flaskr-1.0.0-py2.py3-none-any.whl
RUN chmod +x spin.sh

CMD ["./spin.sh"]