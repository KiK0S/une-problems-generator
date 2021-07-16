FROM ubuntu:latest

RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8


RUN ls

RUN apt-get update && apt-get -y install software-properties-common && add-apt-repository universe
RUN apt-get -y install \
    texlive-base \
    latexmk 

RUN apt-get -y install \
	texlive-pictures \
	texlive-latex-extra \
	texlive-latex-recommended \
	texlive-lang-cyrillic \
	python3 \
	python3-pip

COPY . /opt/app
RUN chmod +x /opt/app/entrypoint.sh

ENTRYPOINT ["/opt/app/entrypoint.sh"]