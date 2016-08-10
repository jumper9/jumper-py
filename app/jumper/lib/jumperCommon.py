import json
import cgi
import os
import sys

params = {}
 

### COMMON SECTION ###
def getConfig(p):
  if(p in config.c):
    return config.c[p]
  else:
    return False

def getParam(p):
  try:
    return params[p.lower()]
  except:
    return ""

def getParams(): 
  return params
  
  
def setParams():
  ## Order from most important: GET, POST, PAYLOAD 
  # Payload
  try:
    fields = json.loads(sys.stdin.read()) 
    for i in fields.keys():
      params[i.lower()] = fields[i]
  except:
    pass

  # GET & POST
  fields = cgi.FieldStorage()
  for i in fields.keys():
    params[i.lower()] = fields[i].value
  
def strToken(str, pos, div):
  out = ""
  s = str.split(div)
  if(pos > 0 and len(s) >= pos):
    out = s[pos - 1]
  elif(pos < 0):
    pos = len(s) + pos
    if(pos >= 0): 
      out = s[pos]
  return out
### COMMON SECTION END ###

def router():
  _requestMethod = os.environ['REQUEST_METHOD'].lower() 
  _url = os.environ['SCRIPT_URL'].split('/')
  _met = ""

  if(len(_url)>=4):
    _pkg = _url[1]
    _obj = _url[2]
    _met = _url[3]
  elif(len(_url)==3):
    _pkg = _url[1]
    _obj = _url[2] 
  else:
    _pkg = "default"
    _obj = _url[1]

  if(_met==""):
    _met = _requestMethod
  #print ("Method:",_met)

  if(os.path.isfile("../"+_pkg+"/services/"+_obj+".py")): 
    #try:
      sys.path.append("../"+_pkg+"/services")
      m = __import__ (_obj)
      func = getattr(m, _met)
      func()


    #except AttributeError:
    #  print("OBJECT FOUND:" + _pkg + "/" + _obj)
    #  print("METHOD NOT FOUND:" + _met)

  else:
    print("OBJECT NOT FOUND:" + _pkg + "/" + _obj)
