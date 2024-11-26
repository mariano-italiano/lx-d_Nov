FROM centos:7

LABEL "Author"="Marcin K."

RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-* && \
	sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-* && \
	yum repolist && \
	yum install httpd -y && \
	yum clean all

COPY index.html /var/www/html/
ENTRYPOINT ["/usr/sbin/httpd"]

CMD ["-D", "FOREGROUND"]

