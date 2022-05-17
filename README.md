<p align="center">
  <img src="/wavsep-logo.jpeg?raw=true"/>
</p>

# Reinforced-Wavsep
A reinforced version of the Wavsep evaluation platform.

• Added ≃ 80 GET/POST new cases:

	- Reflected XSS
	- Blind Sql Injection
	- Obfuscation Sql Injection
	- Union Sql Injection
	- XML External Entity
	- Path Traversal
	- OS Command Injection

• Homepage and pages restyling.

• Added jar libraries for use with mysql 8.0.22 and to execute new XSS and SQLI scenarios (e.g. sectooladdict.jar).

• Solved some bugs.

# WAVSEP - The Web Application Vulnerability Scanner Evaluation Project

WAVSEP is vulnerable web application designed to help assessing the features, quality and accuracy of web application vulnerability scanners.
This evaluation platform contains a collection of unique vulnerable web pages that can be used to test the various properties of web application scanners.

## Installation

(1) Download & Install OpenJdk (suggested >= 11.x).<br/>
(2) Download & install Apache Tomcat (suggested >= 8.x).<br/>
(3) Download & install MySQL Community Server 8.0.22 (sudo apt install mysql-server).<br/>
(3) Copy the wavsep.war file into the tomcat webapps directory.<br/>
(4) Restart the application server.<br/>
<br/>
Example of installation with new setup (January 2021):<br/>
<br/>
(1) JDK:
```bash
sudo apt install openjdk-11-jdk
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
java --version
```
(2) Apache Tomcat:
```bash
mkdir /opt/tomcat
cd /opt/tomcat
wget http://apache.spinellicreations.com/tomcat/tomcat-8/v8.5.32/bin/apache-tomcat-8.5.32.tar.gz
tar xvzf apache-tomcat-8.5.32.tar.gz
export CATALINA_HOME=/opt/tomcat/apache-tomcat-8.5.32
~/.bashrc
$CATALINA_HOME/bin/startup.sh
```
(3) MySQL Community Server:
```bash
sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation (During installation select 'N', 0, enter root password, 'Y')
systemctl status mysql.service
```
(4) Copy the wavsep.war file into the tomcat webapps directory (with git):
```bash
cd /opt/tomcat/webapps/
mv /path/to/wavsep.war/ .
```
(5) Restart the application server:
```bash
$CATALINA_HOME/bin/startup.sh

or

cd/opt/tomcat/bin/
./startup.sh
```
## Usage

Although some of the test cases are vulnerable to additional exposures, the purpose of each test case is to evaluate the detection accuracy of one type of exposure, and thus, “out of scope” exposures should be ignored when evaluating the accuracy of vulnerability scanners.

**Note:** To use SQLI labs correctly there is a .jsp page whose purpose is to create and populate the necessary database tables. To do this, visit the URL "**/wavsep/wavsep-install/install.jsp**", and follow instructions.

## Contributing
Copyright © 2020, Luigi Urbano, Università degli Studi di Napoli Federico II<br/>
Copyright © 2014, Shay Chen<br/>

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
