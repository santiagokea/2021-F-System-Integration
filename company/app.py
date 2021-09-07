from bottle import run, get, view, post

##############################
@get("/")
@view("index.html")
def do():
  return dict(company_name = "SUPER")

##############################
@post("/get-name-by-cpr")
def do():
  # Connect to db
  # Excecute a SQL/Document query
  return "Santiago"

##############################
run(host="127.0.0.1", port=5555, debug=True, reloader=True, server="paste")




