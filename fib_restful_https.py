#!/usr/bin/python

import web


from web.wsgiserver import CherryPyWSGIServer
CherryPyWSGIServer.ssl_certificate = "my-server.crt"
CherryPyWSGIServer.ssl_private_key = "my-server.key"

urls=(
    '/fib','list_usage',
    '/fib/(.*)','get_number'
)
app = web.application(urls,globals(),True)


class list_usage:
    def GET(self):
        output = 'Fibonacci service usage is as below example: \n http://0.0.0.0:8080/fib/n \n n should be a integer \n http://0.0.0.0:8080/fib/5 '
        return output

class get_number:
    def GET(self,number):
        try:
            output = fib_list(int(number))
        except Exception as e:
            return e
        return output


def fib_list(n):
    if n < 0:
        return 'Error, must be greater than or equal to 0 and must be a integer'
    if type(n) is not int:
        return 'Error, n must be integer'
    lst = []
    if n == 0 or n == 1:
        lst = [0]
        #lst = ' '.join(lst)
        return lst
    if n ==2 :
        lst = [0,1]
        #lst = ' '.join(lst)
        return lst
    if n > 2 :
        lst = [0,1]
        while len(lst) < n:
            lst.append(lst[-1] + lst [-2])
        #lst = ' '.join(lst)
        return lst

if __name__ == '__main__':

    app.run()

