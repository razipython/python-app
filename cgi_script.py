import http.server
import socketserver
import cgi
import cgitb

cgitb.enable()



print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
print("Hello, world!")

form = cgi.FieldStorage()
if "name" not in form or "addr" not in form:
    print("<H1>Error</H1>")
    print("Please fill in the name and addr fields.")

print("<p>name:", form["name"].value)
print("<p>addr:", form["addr"].value)


