FROM python:3

WORKDIR /

COPY bot.py requirements.txt /

RUN pip3 install -r /requirements.txt

CMD [ "python3", "-u", "/bot.py" ]