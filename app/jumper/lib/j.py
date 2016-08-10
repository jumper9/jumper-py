
import jumperDb
import jumperCommon
import jumperOutput



### COMMON SECTION ###
def getConfig(p):
  return jumperCommon.getConfig(p)

def getParam(p):
  return jumperCommon.getParam(p)

def getParams():
  return jumperCommon.getParams()
  
def setParams():
  return jumperCommon.setParams()
  
def strToken(str, pos, div):
  return jumperCommon.strToken(str, pos, div)

def router():
  return jumperCommon.router()

def output():
  return jumperCommon.output()  
### COMMON SECTION END ###
 

### DB SECTION ###
def dbConnect():
  jumperDb.connect()
  
def dbRes(sql, queryParams = {}):
  jumperDb.debug(sql)
  return jumperDb.res(sql, queryParams)

def dbFirstRow(sql, queryParams = {}):
  jumperDb.debug(sql)
  return jumperDb.firstRow(sql, queryParams)

def dbFullRes(sql, queryParams = {}):
  jumperDb.debug(sql)
  return jumperDb.fullRes(sql, queryParams)

def query(sql, queryParams = {}):
  jumperDb.debug(sql)
  return jumperDb.query(sql, queryParams)
  
def dbDebug(on = True):
  jumperDb.sqlDebug(on)
### DB SECTION END ###



### OUTPUT SECTION ###
def setResponse(data):
  return jumperOutput.setResponse(data)

def setError(code, text, id = 0):
  return jumperOutput.setError(code, text, id)

def output():
  return jumperOutput.output()
### OUTPUT SECTION END ###



dbConnect()
setParams()
router()
output()