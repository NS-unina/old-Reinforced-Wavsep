FROM maven:3.8.4-jdk-11

COPY src/ /root/src
COPY pom.xml /root/

RUN cd /root/ && mvn package

FROM tomcat:7.0.63-jre8
COPY --from=0 /root/target/wavsep-enhancement-1.0-SNAPSHOT /usr/local/tomcat/webapps/wavsep

CMD ["/usr/local/tomcat/bin/catalina.sh","run"]
