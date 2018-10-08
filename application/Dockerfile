FROM centos:7

COPY ["./requirements.txt", "/tmp/"]
COPY ["./entrypoint.sh", "/"]
COPY ["./APP", "/srv/www/application"]

RUN yum -y upgrade && yum -y install openssl yum-utils epel-release https://centos7.iuscommunity.org/ius-release.rpm \
    && yum -y install python36u \
    && /etc/pki/tls/certs/make-dummy-cert /etc/ssl/certs/dummy-cert.crt \
    && python3.6 -m venv /srv/www/environment \
    && source /srv/www/environment/bin/activate \
    && /srv/www/environment/bin/pip install --upgrade pip -r /tmp/requirements.txt \
    && mkdir -p /srv/www/application /var/log/gunicorn

ENTRYPOINT /bin/sh /entrypoint.sh
