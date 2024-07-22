from socket import *
import re


def request_parser(line):
    p = re.compile(r'(data\d*)=(value\d*)')
    return p.findall(line)



def create_server():
    server_socket = socket(AF_INET, SOCK_STREAM)

    try:
        server_socket.bind(('localhost', 9000))
        server_socket.listen(5)
        while True:
            (client_socket, adress) = server_socket.accept()

            rd = client_socket.recv(5000).decode()
            pieces = rd.split('\n')
            if (len(pieces) > 0 ): print(pieces[0])

            data = 'HTTP/1.1 200 OK\r\n'
            data += 'Content-Type: text/html; charset=utf-8\r\n'
            data += '\r\n'
            data_list = ''
            parse_data = request_parser(pieces[0])
            for request_data in parse_data:
                data_list += f'<li>{request_data[1]}</li>'
            data += f'<html><body><h1>Hello world!</h1><ol>{data_list}<ol></body></html>\r\n\r\n'
            print(data)
            client_socket.sendall(data.encode())
            client_socket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print('\nShutting down...\n')
    except Exception as exc:
        print('Error:\n')
        print(exc)

    server_socket.close()

print('Acces http://localhost:9000')
create_server()