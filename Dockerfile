FROM maven  AS build
COPY . /app
WORKDIR /app
RUN mvn package 

FROM tomcat
COPY --from=build /app/target/wavsep-enhancement-1.0-SNAPSHOT.war /usr/local/tomcat/webapps/wavsep.war
