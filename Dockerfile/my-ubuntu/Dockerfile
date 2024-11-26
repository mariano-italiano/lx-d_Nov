FROM ubuntu:22.04
RUN apt-get update -y && \
	apt-get upgrade -y && \
	apt-get install --no-install-recommends net-tools nginx -y && \
	rm -rf /var/lib/apt/lists/* && \
	mkdir /my-app && \
	systemctl enable --now nginx

WORKDIR /my-app

EXPOSE 80
ENTRYPOINT ["/bin/bash"] 
CMD ["-c", "tail -f /dev/null"]
