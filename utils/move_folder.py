import os
import shutil

def move_dir(src):
	c = 0
	dirs = os.listdir(src)
	for d in dirs:
		t = os.path.join(src, d, 'thrift', 'wrapper')
		if os.path.exists(t) and os.path.isdir(t):
			dest = os.path.join(src, d, 'thrift', 'wrapper2')
			print 'moving ' + t + ' --> ' + dest
			# if os.path.exists(dest) and os.path.isdir(dest):
				# shutil.rmtree(dest)
			os.rename(t, dest)
			c += 1
	print 'moved ' + str(c) + ' packages'



def list_dir(folder):
	dirs = os.listdir(folder)
	for d in dirs:
		if d.endswith('.js') and d.find('.min.') <0:
			print ('<script src="/ipython_report/static/notebook/js/' + d + '"></script>')

if __name__ == '__main__':
	# move_dir('/home/tamvm/Projects/jzcommon-bewrapper/src/main/java/com/vng/zing')
	list_dir('/home/tamvm/Projects/notebook/notebook/static/notebook/js')