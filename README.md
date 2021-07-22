# Implement-Network-System

The repository consists of 2 files,
  1. socket_server.py - Used for executing the server in the local system with on port 9999.
  2. socket_client.py - Used for executing the client in the local system 


**Executing Procedure:**
1. Open terminal and run the socket_server.py
2. Open another terminal and run the socket_client.py. You will be able to see the connection established message on the server terminal.

3. In the client terminal enter comma seperated float values as an request to the server.
      
      eg: 340.0, 10.9475, 315.9888
      
4. The server recieves the float values and process them for basecalling and returns the answer back to the client terminal.
    
      sol: [('340', ' 10.9475', 'A'), (' 10.9475', ' 315.9888', 'C')]
