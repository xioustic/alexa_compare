import sys
import json

from pyquery import PyQuery as pq
from utils import jsonPretty

def getSiteRank(hostname):
  # TODO: Normalize hostname first
  d = pq('http://www.alexa.com/siteinfo/'+hostname)
  retval = {}
  retval['hostname'] = hostname

  retval['global_rank'] = d("#rank-panel-content .span-col.last span[data-cat='globalRank'] .metrics-data").text()
  retval['top_country_rank'] = d("#rank-panel-content .span-col.last span[data-cat='countryRank'] .metrics-data").text()
  retval['top_country'] = d("#rank-panel-content .span-col.last span[data-cat='countryRank'] .metrics-title > a").text()

  # normalize to standard integers
  for key in ['global_rank', 'top_country_rank']:

    retval[key] = retval[key].replace(',','')

    # empty string for a rank indicates lack of a ranking
    if retval[key] == "":
      retval[key] = 0
    else:
      try:
        retval[key] = int(retval[key])
      except:
        print >> sys.stderr, "Failed to parse", key, "for", hostname, "with value of", retval[key]

  return retval

def getSiteRanks(*hostnames):
  if type(hostnames[0]) is list:
    hostnames = hostnames[0]
  
  return [getSiteRank(x) for x in hostnames]

def printHelp():
  print """Retrieves and displays Alexa rankings for a hostname.

  Usage: alexa_compare.py [Flags]... [Hostname]...

  Flags:
    --help | display this help information
    --json | output to json"""
  
if __name__ == "__main__":
  if len(sys.argv) in [0,1]:
    printHelp()
    sys.exit()

  results = []
  dojson = False
  for argument in sys.argv[1:]:
    if argument == 'json':
      dojson = True
    else:
      results.append(getSiteRank(argument))

  # sort on global rank in descending order; lower is better
  results = sorted(results, key=lambda x: x['global_rank'], reverse=False)
      
  # TODO: Implement non-json output
  print jsonPretty(results)