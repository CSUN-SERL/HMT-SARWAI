#Author : Sam Mouradian
#Date : 10/7/2017
#Description : Neulog Sensor Data Collection Functions

"""This module is comprised of functions that are intended to be called by
   theclient_device_interface. The functions in this module make API calls to
   the Neulog API which sends back relevant data regarding the heartrate and gsr sensors.

   The localhost port number may differ from computer to computer, and so it is a
   requirement, and my recoomendation, to download and run the Neulog Sensors API.
   Upon doing so, the application window will list the localhost port number.
   Then you may modify the below API calls to include the correct localhost port number.
"""


import urllib2
from urllib2 import Request, URLError
import json

localhost_port_num = '22002'
server_status_req = Request('http://localhost:22002/NeuLogAPI?GetSeverStatus')
gsr_value_req = Request('http://localhost:22002/NeuLogAPI?GetSensorValue:[GSR],[1]')
pulse_value_req = Request('http://localhost:22002/NeuLogAPI?GetSensorValue:[Pulse],[1]')

def get_localhost_port():
    """Get localhost port number from User.
    """
    localhost_port = input("Please Enter Localhost Port Number (i.e '22002') ")
    global localhost_port_num
    localhost_port_num = localhost_port
    print(localhost_port_num)
    

def get_server_version(object = server_status_req):
    """ Checks to see if the server is ready
        to recieve requests.
    """
    try:
        response = urllib2.urlopen(object).read()
        server_connect = json.loads(response)
        print server_connect['GetSeverStatus']
    except URLError, e:
        print 'Error: No Response From Server.'

def get_gsr_value(object = gsr_value_req):
    """ Captures Operators Current GSR Reading.
        Returns Parsed JSON containing GSR Value.
    """
    try:
        response = urllib2.urlopen(object).read()
        gsr_value = json.loads(response)
        print gsr_value['GetSensorValue'][0]
    except URLError, e:
        print 'Error: No GSR Value.'

def get_pulse_value(object = pulse_value_req):
    """ Captures Operators Current Pulse.
        Returns Parsed JSON Containing Pulse.
    """
    try:
        response = urllib2.urlopen(object).read()
        pulse_value = json.loads(response)
        print pulse_value['GetSensorValue'][0]
    except URLError, e:
        print 'Error: No Heartrate Value.'

def main():

    get_localhost_port()
    get_server_version()
    get_gsr_value()
    get_pulse_value()

if __name__ == '__main__':
    main()
