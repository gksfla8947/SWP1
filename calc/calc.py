from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    add = 0
    mul = 0
    msg = ''
    if '' not in [a, b]:
        a, b = int(a), int(b)
        add = (a+b)
        mul = (a*b)
        msg = "Calculation has done"
    else:
        add = 0
        mul = 0
        msg = "Please enter the number"
    response_body = html % {
            'add' : add,
            'mul' : mul,
            'msg' : msg,
            }

    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
        ])
    return [response_body]

