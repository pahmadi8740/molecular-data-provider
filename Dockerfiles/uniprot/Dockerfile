#stage for packaging transfomers
FROM python:3-alpine AS packaging-image
RUN mkdir -p /usr/src/base
COPY util/python/transformers-2.0 /usr/src/base
WORKDIR /usr/src/base
RUN python setup.py bdist_wheel
RUN mkdir -p /usr/src/uniprot
COPY transformers/uniprot/python-flask-server /usr/src/uniprot
WORKDIR /usr/src/uniprot
RUN python setup.py bdist_wheel

#stage for installing transformers on server
FROM python:3-alpine AS runtime-image
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/data
RUN mkdir -p /usr/src/app/info
COPY transformers/uniprot/python-flask-server/info /usr/src/app/info
WORKDIR /usr/src/app/data
COPY util/python/transformers-2.0/config/BiolinkClassMap.txt /usr/src/app/data
COPY util/python/transformers-2.0/config/prefixMap.json /usr/src/app/data
ADD https://translator.broadinstitute.org/db/UniProt.sqlite /usr/src/app/data
WORKDIR /usr/src/app
COPY --from=packaging-image /usr/src/base/dist .
COPY --from=packaging-image /usr/src/uniprot/dist .
RUN pip3 install -I base_transformer-2.0.1-py3-none-any.whl
RUN pip3 install -I uniprot_transformer-2.4.0-py3-none-any.whl
COPY transformers/uniprot/python-flask-server/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["nohup","gunicorn", "-w","16","-b","0.0.0.0:8080","openapi_server.__main__:app","--timeout","1800"]
