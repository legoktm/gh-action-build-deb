ARG DISTRO=debian:unstable
FROM $DISTRO

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y && \
 apt-get install build-essential debhelper devscripts equivs \
 software-properties-common -y

COPY inner.sh /inner.sh

ENTRYPOINT ["/inner.sh"]
