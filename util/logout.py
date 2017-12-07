from RemoteProcessClient import RemoteProcessClient


remote_process_client = RemoteProcessClient('wgforge-srv.wargaming.net', 443)
player = remote_process_client.write_message('LOGIN', {"name": "Mickey"})
remote_process_client.logout()
remote_process_client.close()
