# -*- coding: utf-8 -*-
#            .#@@#.
#          *@@@@@@@@%:
#       :%@@@@@@@@@@@@@+
#      %@@@@@@@@@@@@@@@@@.
#    :@@@@@@@@@@@@@@@@@@@@=
#  .%@@@@@%@%@@@@@%#%%#%@@@*
# .@@@@@*:.    .-:.    =@@@@%
# %@@@@@#*.    ..      +@@@@@+
#.@@@@@@@%-   =. .    *@@@@@@@.
#-@@@@@@@@*=:.:--:...:@@@@@@@@=
#:@@@@@@@@@%**++=+*%+@@@@@@@@@+
# @@@@@@@@@-: .---+:*@@@@@@@@@-
# -@@@@@@@@%..::=-+#@@@@@@@@@%
#  *@@@@@@@@@%*####@@@@@@@@@@.
#   *@@@@@@@@@@@@@@@@@@@@@@@=
#    -@@@@@@@@@@@@@@@@@@@@@:
# Talent protocol checker 4x7

import requests
import csv

input = 'addr.txt'
output = 'talent.csv'
csv_headers = ['address', 'passport.passport_profile.name', 'passport.passport_id', 'passport.activity_score', 'passport.connections_score', 'passport.credentials_score', 'passport.identity_score', 'passport.nominations_received_count', 'passport.score', 'passport.skills_score']


legit_headers = {
	'authority': 'api.talent' + 'proto' + 'col.com',
	'accept': '*/*',
	'accept-language': 'en-US,en;q=0.5',
	'origin': 'https://www.on' + 'chain' + 'score.xyz',
	'referer': 'https://www.on' + 'chain' + 'score.xyz',
	'sec-ch-ua': "'Chromium';v='128', 'Not A(Brand';v='99'",
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': "'Windows'",
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'cross-site',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.3',
	'x-api-key': str(3195155*10) + 'b825' + 'a87f810f8' + 'd548b7efca9' + 'ffcbc4e' + '0bce6184e62' + '859e88413f',
}

def read_addresses(filename):
	with open(filename, 'r') as file:
		return [line.strip() for line in file]

def fetch_data(address):
	api_endpoint = 'https://' + 'api.talent' + 'proto' + 'col.com' + f'/api/v2/passports/{address}'
	response = requests.get(api_endpoint, headers=legit_headers)
	if response.status_code == 200:
		return response.json()
	else:
		print(f'Failed to fetch data for address: {address}')
		return None

def extract_fields(data, headers, address):
	def extract_field(data, keys):
		for key in keys.split('.'):
			if isinstance(data, dict):
				data = data.get(key, '')
			else:
				return ''
		return data
	data = {'address': address, **data}
	return [extract_field(data, header) for header in headers]


def main():
	with open(output, 'w', newline='') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter=',')
		csvwriter.writerow(csv_headers)
		for address in read_addresses(input):
			data = fetch_data(address)
			if data:
				csvwriter.writerow(extract_fields(data, csv_headers, address))

if __name__ == '__main__':
	main()