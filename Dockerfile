#stage for packaging transfomers
FROM python:3-alpine AS packaging-image
RUN mkdir -p /usr/src/base
COPY util/python/transformers-2.0 /usr/src/base
WORKDIR /usr/src/base
RUN python setup.py bdist_wheel
RUN mkdir -p /usr/src/chembl
COPY transformers/chembl/python-flask-server /usr/src/chembl
WORKDIR /usr/src/chembl
RUN python setup.py bdist_wheel

#stage for installing transformers on server
FROM python:3-alpine AS runtime-image
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/data
RUN mkdir -p /usr/src/app/database
RUN mkdir -p /usr/src/app/info
#ADD https://translator.broadinstitute.org/db/ChEMBL.target.xref.sqlite /usr/src/app/data
#ADD https://translator.broadinstitute.org/db/ChEMBL.sqlite /usr/src/app/database
COPY util/python/transformers-2.0/config/BiolinkClassMap.txt /usr/src/app/data
COPY util/python/transformers-2.0/config/prefixMap.json /usr/src/app/data
COPY transformers/chembl/python-flask-server/info /usr/src/app/info
WORKDIR /usr/src/app
COPY --from=packaging-image /usr/src/base/dist .
COPY --from=packaging-image /usr/src/chembl/dist .
RUN pip3 install -I base_transformer-2.0.1-py3-none-any.whl
RUN pip3 install -I chembl_transformer-2.4.0-py3-none-any.whl
COPY transformers/chembl/python-flask-server/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8080
