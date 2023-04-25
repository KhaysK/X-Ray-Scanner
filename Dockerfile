FROM python:3.9-slim-buster

WORKDIR /app


COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r requirements.txt


RUN apt-get update && apt-get install -y curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y yarn

COPY . /app

RUN cd client && yarn install && yarn build

RUN export FLASK_APP=server.py && export FLASK_DEBUG=1 && flask db upgrade

EXPOSE 5000

CMD ["/bin/bash", "starter.sh"]