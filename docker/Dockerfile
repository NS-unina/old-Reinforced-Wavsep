FROM maven:3.8.4-jdk-11

RUN git clone https://github.com/NS-unina/wavsep-enhancement.git
RUN cd wavsep-enhancement && mvn package

FROM tomcat:7.0.63-jre8
COPY --from=0 /wavsep-enhancement/target/wavsep-enhancement-1.0-SNAPSHOT.war /usr/local/tomcat/webapps/wavsep.war

CMD ["/usr/local/tomcat/bin/catalina.sh","run"]