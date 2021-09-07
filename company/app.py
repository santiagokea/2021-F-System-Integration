from bottle import run, get, view

##############################
@get("/")
@view("index.html")
def do():
  return dict(company_name = "SUPER")

##############################
run(host="127.0.0.1", port=4444, debug=True, reloader=True, server="paste")




