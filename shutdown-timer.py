import os


minute = input("Enter when you want to shutdown (in minute) (-a to abort): ")

if(minute == "-a"):
	os.system("shutdown -a")
else:
	sec = int(minute) * 60
	os.system(f"shutdown -s -t {sec}")