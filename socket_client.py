# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 09:53:23 2021

@author: Alagan
"""

import socket
def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 9999  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    control = 'Y'

    while control == 'Y':
        
        message = input("Enter comma seperated float values:")  # take input
        
        client_socket.send(message.encode())  # send message
        
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        control = input("Want to continue (Y/N): ")  # again take input

    client_socket.close()  # close the connection

if __name__=='__main__':
    client_program()
