#python setup.py py2exe
from distutils.core import setup
import py2exe
setup(name='schleich-launcher',
	version='1.0',
	windows=['schleich_launcher.py']
	)
