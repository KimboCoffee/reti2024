# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 18:03:29 2024

@author: kimbo
"""

import sys, signal
import http.server
import socketserver

def closing_signal_handler(signal, frame):
    print('Closing server: Ctrl + C was pressed')
    
    try:
        if (server):
            server.server_close()
    finally:
        sys.exit(0)
        
signal.signal(signal.SIGINT, closing_signal_handler)

if sys.argv[1:]:
    port = sys.argv[1]
else:
    port = 8080

server = socketserver.ThreadingTCPServer(('', port), http.server.SimpleHTTPRequestHandler)
server.daemon_threads = True
server.allow_reuse_address = True

try:
    while True:
        server.serve_forever() 
except KeyboardInterrupt:
    pass

server.server_close()