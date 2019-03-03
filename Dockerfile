FROM python:3.5

ENV firstname Nicolas
ENV lastname Chariglione
ENV exo_name biggest

COPY ./moulinette/rendus ./rendus
COPY ./moulinette/run_moulinette.sh .
COPY ./moulinette/resources ./sandbox
RUN chmod +x run_moulinette.sh

CMD "./run_moulinette.sh" $firstname $lastname $exo_name
