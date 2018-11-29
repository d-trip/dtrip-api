FROM python:3.6.4

ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

ADD . /app

CMD ["gunicorn", "run:app", "-b", "0.0.0.0:5000", \
    "--workers=4", \
    "--timeout=30", \
    "--log-level=debug"]
