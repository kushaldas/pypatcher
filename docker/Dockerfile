FROM fedora
MAINTAINER kushal <kushal@fedoraproject.org>

RUN yum -y install yum-utils mercurial
RUN yum-builddep python3 -y
RUN yum groupinstall "Development Tools" -y


ADD ./start.sh /start.sh
RUN chmod 755 /start.sh
