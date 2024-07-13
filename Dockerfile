FROM debian:bookworm

RUN apt-get update && apt-get install --yes docker.io

COPY inner /inner
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
