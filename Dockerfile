FROM python:3.10.4

COPY ./tapp /home/app
WORKDIR /home/app
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
