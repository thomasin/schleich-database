import threading, subprocess
from Tkinter import *

class subprocessthread(threading.Thread):
	def __init__(self, c):
		self.command = c
		threading.Thread.__init__(self)
		self.stdout = None
		self.stderr = None

	def run(self):
		p = subprocess.Popen(self.command, 
				shell=True, 
				stdout=subprocess.PIPE,
				stderr=subprocess.PIPE)
		self.stdout, self.stderr = p.communicate()

root = Tk()
t = subprocessthread(r'python "C:\Program Files\schleich-database\schleich\manage.py" runserver')
t.setDaemon(True)
t.start()
f=subprocessthread(r'"C:\Program Files\Mozilla Firefox\firefox.exe" http://localhost:8000/index.html')
f.setDaemon(True)
f.start()
w = Label(root, 
		text="Running the schleich database\nBrowse to http://localhost:8000/index.html")
w.pack()
root.mainloop()
