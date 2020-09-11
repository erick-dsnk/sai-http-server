import socket
import sys
import threading
from selenium import webdriver
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler



class Server:
    def __init__(self, host='127.0.0.1', port=8000):
        self.host = host
        self.port = port
        self.content_dir = 'web'
        self.status_codes = {
            100: 'Continue',
            101: 'Switching Protocols',
            102: 'Processing',
            103: 'Early Hints',

            200: 'OK',
            201: 'Created',
            202: 'Accepted',
            203: 'Non-Authoritative Information',
            204: 'No Content',
            205: 'Reset Content',
            206: 'Partial Content',
            207: 'Multi-Status',
            208: 'Already Reported',
            226: 'IM Used',
            
            300: 'Multiple Choices',
            301: 'Moved Permanently',
            302: 'Found',
            303: 'See Other',
            304: 'Not Modified',
            305: 'Use Proxy',
            306: 'Switch Proxy',
            307: 'Temporary Redirect',
            308: 'Permanent Redirect',

            400: 'Bad Request',
            401: 'Unauthorized',
            402: 'Payment Required',
            403: 'Forbidded',
            404: 'Not Found',
            405: 'Method Not Allowed',
            406: 'Not Acceptable',
            407: 'Proxy Authentication Required',
            408: 'Request Timeout',
            409: 'Conflict',
            410: 'Gone',
            411: 'Length Required',
            412: 'Precondition Failed',
            413: 'Payload Too Large',
            414: 'URI Too Long',
            415: 'Unsupported Media Type',
            416: 'Range Not Satisfiable',
            417: 'Expectation Failed',
            418: "I'm a cup of coffee :3",
            421: 'Misdirected Request',
            422: 'Unprocessable Entity',
            423: 'Locked',
            424: 'Failed Dependency',
            425: 'Too Early',
            426: 'Upgrade Required',
            428: 'Precondition Required',
            429: 'Too Many Requests',
            431: 'Request Header Fields Too Large',
            451: 'Unavailable For Legal Reasons',

            500: 'Internal Server Error',
            501: 'Not Implemented',
            502: 'Bad Gateway',
            503: 'Service Unavailable',
            504: 'Gateway Timeout',
            505: 'HTTP Version Not Supported',
            506: 'Variant Also Negotiates',
            507: 'Insufficient Storage',
            508: 'Loop Detected',
            510: 'Not Extended',
            511: 'Network Authentication Required'
        }
        self.headers = {
            'Server': 'Sai',
            'Content-Type': 'text/html',
            'Connection': 'keep-alive'
        }
        self.driver = webdriver.Chrome()
        
        event_handler = PatternMatchingEventHandler(
            patterns="*",
            ignore_patterns="",
            ignore_directories=False,
            case_sensitive=True
        )

        event_handler.on_any_event = self.on_file_event

        self.observer = Observer()

        self.observer.schedule(
            event_handler=event_handler,
            path="./web",
            recursive=True
        )


    def on_file_event(self, event):
        print(f"Detected a change at {event.src_path}. Refreshing web page.")
        
        self.driver.refresh()

    
    def start(self):
        self.sv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            print(f"Starting server on {self.host}:{self.port}")

            self.sv.bind((self.host, self.port))

            print(f"Successfully started server on {self.host}:{self.port}")

            print("\nDISCLAIMER: Due to limitations of the Selenium package and the way the code is set up, you will have to manually type in the server address. We're looking into solving the problem!\n")

            self.listen()
        
        except Exception as e:
            print("Failed to start server")

            self.shutdown()

    def listen(self):
        self.sv.listen(5)

        self.observer.start()

        while True:
            conn, addr = self.sv.accept()

            threading.Thread(target=self.handle_client, args=(conn, addr)).start()


    def handle_client(self, conn, addr):
        BUFSIZ = 8192

        while True:
            try:
                data = conn.recv(BUFSIZ).decode()

                if data:
                    lines = data.split('\r\n')

                    req_line = lines[0]

                    req_method = req_line.split(' ')[0]

                    if req_method == 'GET':
                        response_line = b""
                        response_header = b""
                        blank_line = b"\r\n"
                        response_body = b""


                        requested_file = req_line.split(' ')[1]

                        if requested_file == '/':
                            requested_file = '/index.html'
                        else:
                            pass

                        filepath = self.content_dir + requested_file

                        print(f'Initiating webpage {filepath}')

                        try:
                            with open(filepath, 'rb') as f:
                                response_body = f.read()

                                f.close()

                            response_line = self.create_response_line(status_code=200)
                            response_header = self.create_headers()
                                        
                        
                        except Exception as e:
                            print(f'Something went wrong while trying to serve {filepath}')

                            response_line = self.create_response_line(status_code=404)
                            response_header = self.create_headers()
                            response_body = "<h1>{} {}</h1>".format(
                                404,
                                self.status_codes[404]
                            ).encode('utf8')

                        response = b""

                        response += response_line
                        response += response_header
                        response += blank_line
                        response += response_body

                        conn.send(response)

                        conn.close()

                        break
                
                    else:
                        print(f'Unsupported request method: {req_method}')
                
                else: break
            
            except KeyboardInterrupt:
                self.sv.shutdown()



    def shutdown(self):
        try:
            print("Shutting down...")

            sys.exit(0)
        except: pass
    

    def create_response_line(self, status_code):
        name = self.status_codes[status_code]

        return f"HTTP/1.1 {status_code} {name}\r\n".encode('utf8')
    

    def create_headers(self, extra_headers=None):
        headers = ""

        headers_copy = self.headers.copy()

        if extra_headers:
            headers_copy.update(extra_headers)
        
        for h in self.headers:
            headers += f"{h}: {self.headers[h]}\r\n"
        
        return headers.encode('utf8')


if __name__ == "__main__":
    server = Server()

    server.start()