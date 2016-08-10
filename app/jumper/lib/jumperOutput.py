import json

errors = []
response = None

def setResponse(data):
  global response
  response = data


def setError(code, text, id = 0):
  global errors
  errors.append({"code": str(code), "text": text, "id": id})

def output():
  global errors, response
  out = ""
  statusTxt = "200 OK"

  if(len(errors) == 0):
    if(isinstance(response, str) or isinstance(response, int)):
      out = {"value" : response}
    else:
      out = response
  else:
    out = {"errors" : errors }
    if(getConfig("sendErrorHTMLCodes")):
      statusTxt = errors[0]["code"] + " " + errors[0]["text"] 

  print("Content-Type: application/json;charset=utf-8") 
  print("Status: " + statusTxt )
  print()
  print(json.dumps(out))
