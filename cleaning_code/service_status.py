"""
Download from http://www.mta.info/status/serviceStatus.txt
"""
import json
import xmltodict

# the xml file is available at http://www.mta.info/status/serviceStatus.txt
s = open("serviceStatus.txt").read()
# we convert it to a dictionary
d = xmltodict.parse(s)
# and then dump the subway section into a JSON file to visualise
json.dump(d['service']['subway']['line'], open("../visualisations/data/service_status.json",'w'))
