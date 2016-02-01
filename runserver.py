import cherrypy
import os
from pprint import pprint
from kafka import SimpleProducer
from kafka import KafkaClient


class Sap(object):
	@cherrypy.expose
	def index(self):
		print "===========\nROOT server\n==========="
		print "Pathinfo: \t" + cherrypy.request.path_info
		M = cherrypy.request.method 
		print "Method: \t" + M 
		#print "Reguest params: ", cherrypy.request.params
		#auto_on = cherrypy.request.process_request_body 
		#print "Process ON: \t" + str(auto_on)
		#print "Reguest metods: ", cherrypy.request.methods_with_bodies 
		#print "Reguest headers: "  
		pprint (cherrypy.request.headers)
		return Page


# This method runs if POST request is on the "/ppost" URL 
# Content-type must be text/plain or app/json 

	@cherrypy.expose
	def ppost(self):
		print "===========\nPOST reciever\n==========="
		print "Pathinfo: \t" + cherrypy.request.path_info
		M = cherrypy.request.method 
		print "Method: \t" + M 
		#print "Request params: ", cherrypy.request.params
		auto_on = cherrypy.request.process_request_body 
		print "Process ON: \t" + str(auto_on)
		headers = cherrypy.request.headers 
		pprint (headers)
		#print "Content-type: ", headers.get("Content-Type")
		#print "metods: ", cherrypy.request.methods_with_bodies 
		#print "Reguest params: ", cherrypy.request.params
		if (M == "POST"):
		#if (M == "POST") and (True):
			print "Recieved POST... "  
			LN = cherrypy.request.headers.get("Content-Length") 
			print "Body length: " + str(LN)
			data = cherrypy.request.body.read(LN) 
			print "Body string: " + data
			producer.send_messages("test", data)	# Send to topic "test"
		return "exiting /ppost"


#NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
#   Main  
#NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

cur_dir = os.path.dirname(__file__)
conf1 = os.path.join(cur_dir,  "server.conf")
#print "\nUsing config file: ", conf1

index_file = os.path.join(cur_dir,  "index.html")
with open(index_file, 'r') as f:
	Page = f.read() 

kafka_client = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka_client)		# Kafka Producer

cherrypy.quickstart(Sap(), "/", conf1)
