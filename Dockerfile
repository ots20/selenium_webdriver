FROM joyzoursky/python-chromedriver:3.8

COPY . /docker_selenium_webdriver

WORKDIR /docker_selenium_webdriver

RUN pip3 install pipenv