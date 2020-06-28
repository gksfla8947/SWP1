from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    add = 0
    mul = 0
    msg = ''
    try:
        a, b = int(a), int(b)
        add = (a+b)
        mul = (a*b)
        msg = "Calculation has done"
    except ValueError:
        if a.isdigit():
            msg = "Please enter the correct number in b"
        elif b.isdigit():
            msg = "Please enter the correct number in a"
        else:
            msg = "Please enter the correct number in a and b"
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

