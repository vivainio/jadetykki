from fabric.api import *

def watch():
	local("jade -w -P -O out/ *.jade")