FROM tomcat
COPY target/wavsep-enhancement-1.0-SNAPSHOT.war /usr/local/tomcat/webapps/wavsep.war
COPY extra/wavsep-ext.war /usr/local/tomcat/webapps/wavsep-ext.war
