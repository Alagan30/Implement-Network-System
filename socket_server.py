# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 09:54:44 2021

@author: Alagan
"""
import socket 

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 9999  # initiate port

    server_socket = socket.socket()  # get instance

    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(1)
    
    conn, address = server_socket.accept()  # accept new connection
    
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        
        if not data:
            # if data is not received break
            break
        
        print("from connected user: " + str(data))
        data = data.split(',')
        
        
        ans = []
        base_dictionary = {329.0525:'A', 305.0413:'C', 345.0474:'G', 306.0253:'U'}
        n = len(data)
        i, j = 0, 1
        while i<n-1:
            diff = abs(float(data[i]) - float(data[j]))
            for k in base_dictionary:
                if abs(diff - k) <= 1e-6:
                    ans.append((data[i], data[j], base_dictionary[k]))
            i += 1
            j += 1
        
        ans = str(ans)
        conn.send(ans.encode())  # send data to the client
    conn.close()  # close the connection

    
if __name__ == '__main__':
    server_program()
