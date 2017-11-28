from RemoteProcessClient import RemoteProcessClient


remote_process_client = RemoteProcessClient('wgforge-srv.wargaming.net', 443)
status, start_data = remote_process_client.login("Mickey")
remote_process_client.logout()
remote_process_client.close()
