
Web server and application is based on CherryPy Framework (Linux)

Requirements:

 - Python 2.7
 - CherryPy
 - Kafka Server (requires Java. If not installed, download and install 
JDK from Oracle official download site)


INSTALLATION (Fedora 21, x86)
===========================
(for later Fedora version, use "dnf" command instead of "yum")

1. Install python (2.7.8 is used in this example) and python dev package:
	> sudo yum install python
	> sudo yum install python-devel

2. CherryPy Framework
	> hg clone https://bitbucket.org/cherrypy/cherrypy
	> cd cherrypy
	> sudo python setup.py install

    Test if CherryPy works (press Ctrl-C to close server)
	> python -m cherrypy.tutorial.tut01_helloworld

3. Kafka: donwload Server binaries and extract:
	> tar -xzf kafka_2.10-0.8.2.2.tgz

    Install Python Kafka Client:
	> git clone https://github.com/dpkp/kafka-python
	> cd kafka-python
	> sudo python setup.py install


TEST: Kafka Server; Webserver + client App 
======================

1. Run Kafka Server from your Kafka folder:
	> bin/zookeeper-server-start.sh config/zookeeper.properties
 	> bin/kafka-server-start.sh config/server.properties
	> bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

2. Run dummy consumer to see messages on Kafka (Ctrl-C to stop):
	> bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic test --from-beginning

   To stop the Server run:
	> bin/kafka-server-stop.sh
 	> bin/zookeeper-server-stop.sh

3. Run CherryPy app (Kafka client included) from "mysite" directory:
	> python runserver.py

   This will host "index.html" and /static directory.
   POST Requests are sent to /ppost URL and will be delivered to Kafka Server
   Contet-Type must be "text/plain" or "application/json" (NOT "x-form")




About CherryPy:
=========

Benefits for developer: 
- simple readable syntax
- easy webserver and app configuration
- a lot of helper functions (e.g. serve static files)
- provides rich request-level features, session pool
- can be integrated with standalone apps
- integrates well with Nginx server
- lightweight test webserver is included, fast and reliable
- good documented
- used in various real projects for data mining (Netflix)

Other comparable Python-related server solutions:
- Django, Flask, Gunicorn

Other servers which work with Python extensions (CGI/WSGI): 
- uWSGI, Nginx, Apache 