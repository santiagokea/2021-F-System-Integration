from bottle import run, get, post, request
import time
import requests
##############################


# Show letter X in the terminal every second
while True:
  r = requests.get("http://127.0.0.1:4444")
  print(r.text)
  time.sleep(1)


##############################
@get("/")
def do():
  return "SERVER ONE"

##############################
@post("/signin")
def do():
  # How do we get the form data
  the_name = request.forms.get("name")
  email = request.forms.get("email")
  print(the_name)
  return f"Hi {the_name}, your email is {email}"
##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True )

