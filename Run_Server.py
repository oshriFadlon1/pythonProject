import My_server
import requests

def Run_Server():
    host_Name = "localHost"

    webServer = My_server.HTTPServer((host_Name, My_server.server_Port), My_server.My_Server)
    print("Server started http://%s:%s" % (host_Name, My_server.server_Port))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")