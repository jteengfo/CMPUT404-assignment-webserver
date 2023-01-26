#  coding: utf-8 
import socketserver
from pathlib import Path
import os 

# Copyright 2013 Abram Hindle, Eddie Antonio Santos
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/


class MyWebServer(socketserver.BaseRequestHandler):
    ''' A class of a request handler '''
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print ("Got a request of: %s\n" % self.data)

        #############################################
        # decode the data from bytes to string 
        decoded_data = decode_data(self.data)
        print("\n The decoded data is: " + decoded_data)
        # split the string to different smaller string using whitespace
        decoded_data_split = decoded_data.split(" ")
        print("\nThe string after GET is: " + decoded_data_split[1])
        # print("The decoded data split is: " + decoded_data_split[1])
        # find root path
        # root_path = os.path.dirname(os.path.abspath(__file__))
        root_path = os.path.abspath(__file__)
        print("\nThe root path is: " + root_path)
        complete_path = root_path + '/www' + decoded_data_split[1]
        print("\nThe complete path is: " + complete_path)
        self.request.sendall(bytearray("ok", "utf-8"))
        # print("comeplete path is: " + complete_path)
        # complete_path = Path(complete_path)

        # # check if method is GET
        # if decoded_data_split[0] == 'GET':
        #     # if complete_path.exists():
        #     if os.path.exists(complete_path):
        #         # check if it is trying to move out of www/
        #         check_string = '..'
        #         string = decoded_data_split[1]
        #         split_string = string.split('/')
        #         if check_string in split_string[0] or check_string in split_string[1]:
        #             data = "Sorry! The webpage you're requesting does not exist."
        #             self.request.sendall(bytearray("HTTP/1.1 404 Not FOUND\n\n" + data,'utf-8'))
        #         # check if file 
        #         elif os.path.isfile(complete_path):
        #             # getting the file type
        #             file_split = decoded_data_split[1].split('.')
        #             file_type = file_split[1]
        #             # print(file_type)
        #             content_type = "text/" + file_type
        #             # p = Path(complete_path)
        #             # if exists, open file, store read data
        #             # p = Path(complete_path)
        #             with open(complete_path) as f:
        #                 data = f.read()
        #                 # print(data)
        #             self.request.sendall(bytearray("HTTP/1.1 200 OK\r\n" + "Content-Type: " + content_type + "\n\n" + data,'utf-8'))
        #         # else its a dir
        #         else:
        #             # initialize checks variables
        #             # doing a left strip to see diff between /deep/ or deep/
        #             string_lstrip = decoded_data_split[1].lstrip('/')
        #             count = string_lstrip.count('/')

        #             # if just a forward slash, add index.html
        #             if decoded_data_split[1] == '/':
        #                 print("It is just a forward slash\n")
        #                 default_path = str(complete_path) + 'index.html'
        #                 # default_path = Path(default_path)
        #                 f = open(default_path)
        #                 print("The default path now is: " + default_path)
        #                 # with default_path.open() as f:
        #                 #     data = f.read()
        #                 data = f.read()
        #                 self.request.sendall(bytearray("HTTP/1.1 200 OK\r\n" + "Content-Type: text/html\n\n" + data,'utf-8'))
        #             # check if its a directory with a slash
        #             elif count >= 1:
        #                 print("It is a dir with a slash.\n")
        #                 print("The complete path is: " + complete_path)
        #                 default_path = str(complete_path) + 'index.html'
        #                 # default_path = Path(default_path)
        #                 print("The default path now is: " + default_path)
        #                 relative_path = decoded_data_split[1]
        #                 print("The relative path now is: " + relative_path)
        #                 f = open(default_path)
        #                 # with default_path.open() as f:
        #                 #     data = f.read()
        #                 data = f.read()
        #                 # self.request.sendall(bytearray("HTTP/1.1 200 OK\r\n" + "Content-Type: text/html\n\n" + data,'utf-8'))
        #                 self.request.sendall(bytearray("HTTP/1.1 301 Moved Permanently\r\n" + "Location: " + relative_path + '\n\n' +  data,'utf-8'))
        #             # else it a dir without a slash
        #             else:
        #                 print("It is a dir without a slash.\n")
        #                 relative_path = decoded_data_split[1] + '/'
        #                 print("The relative path is: " + relative_path)
        #                 data = "HTTP/1.1 301 Moved Permanently"
        #                 self.request.sendall(bytearray("HTTP/1.1 301 Moved Permanently\r\n" + "Location: " + relative_path + "\n\n" + data,'utf-8'))
        #     # file DNE, could be a directory without '/' or DNE 
        #     else:
        #         data = "Sorry! The webpage you're requesting does not exist."
        #         self.request.sendall(bytearray("HTTP/1.1 404 Not FOUND\n\n" + data,'utf-8'))
        # # else it is not a GET method and we don't support it
        # else:
        #     data = "405 Method Not Allowed"
        #     self.request.sendall(bytearray("HTTP/1.1 405 Not FOUND\n\n" + data, "utf-8"))

def decode_data(byte_data):
    decoded_data = byte_data.decode("utf-8")
    return decoded_data



if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 8080
    ''' server_address, RequestHandlerClass'''
    server = socketserver.TCPServer((HOST, PORT), MyWebServer)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

