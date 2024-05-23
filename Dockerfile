#stage for packaging transfomers
FROM python:3-alpine AS packaging-image
RUN mkdir -p /usr/src/trapi
COPY trapi/gelinea/python-flask-server /usr/src/trapi
WORKDIR /usr/src/trapi
RUN python setup.py bdist_wheel
#stage for installing transformers on server
FROM python:3-alpine AS runtime-image
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY --from=packaging-image /usr/src/trapi/dist .
RUN pip3 install -I gelinea_trapi-1.4.0.0-py3-none-any.whl
COPY trapi/python-flask-server .
COPY trapi/python-flask-server/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["nohup","gunicorn", "-w","128","-b","0.0.0.0:8080","openapi_server.__main__:app","--timeout","1800"]
