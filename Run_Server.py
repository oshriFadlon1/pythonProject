import My_Server

def Run_Server():
    host_Name = "localHost"

    webServer = My_Server.HTTPServer((host_Name, My_Server.server_Port), My_Server.My_Server)
    print("Server started http://%s:%s" % (host_Name, My_Server.server_Port))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")