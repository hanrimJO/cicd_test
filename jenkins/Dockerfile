FROM jenkins/jenkins:lts
USER root
RUN apt-get update && apt-get install -y make && apt-get autoclean && apt-get clean && apt-get autoremove
RUN apt-get install -y curl
RUN curl -fsSL https://get.docker.com/ | sh
RUN usermod -aG docker jenkins
RUN curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose
RUN apt-get update
USER jenkins