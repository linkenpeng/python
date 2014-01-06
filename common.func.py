#/usr/bin/env python
# coding:utf-8 http://www.admin10000.com/document/3573.html
import itertools as it, glob, os,logging, inspect,uuid,hmac,hashlib,json,zlib
import atexit
import time
import math

def function(arg1="", arg2=""):
	print("arg1:{0}".format(arg1))
	print("arg2:{0}".format(arg2))

#带任意数量参数的函数
def foo(*args):
	numargs = len(args)
	print("Number of arguments:{0}".format(numargs))
	'''for i, x in enumerate(args):
		print("Argument {0} is : {1}".format(i,x)
	'''

#使用Glob()查找文件
def multiple_file_types(*patterns):
    return it.chain.from_iterable(glob.glob(pattern) for pattern in patterns)

#调试
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(filename)s:%(lineno)-4d: %(message)s',
    datefmt='%m-%d %H:%M',
    )
logging.debug('A debug message')
logging.info('Some information')
logging.warning('A shot across the bow')
  
def testDebug():
    frame,filename,line_number,function_name,lines,index=\
        inspect.getouterframes(inspect.currentframe())[1]
    print(frame,filename,line_number,function_name,lines,index)
  
def uniqueId():
	key='1'
	data='a'
	print hmac.new(key, data, hashlib.sha256).hexdigest()
	  
	m = hashlib.sha1()
	m.update("The quick brown fox jumps over the lazy dog")
	return m.hexdigest()

def jsonTest():
	variable = ['hello', 42, [1,'two'],'apple']
	print "Original {0} - {1}".format(variable,type(variable))
	  
	# encoding
	encode = json.dumps(variable)
	print "Encoded {0} - {1}".format(encode,type(encode))
	  
	#deccoding
	decoded = json.loads(encode)
	print "Decoded {0} - {1}".format(decoded,type(decoded))
	
def zlibTest():
	string =  """   Lorem ipsum dolor sit amet, consectetur
                adipiscing elit. Nunc ut elit id mi ultricies
                adipiscing. Nulla facilisi. Praesent pulvinar,
                sapien vel feugiat vestibulum, nulla dui pretium orci,
                non ultricies elit lacus quis ante. Lorem ipsum dolor
                sit amet, consectetur adipiscing elit. Aliquam
                pretium ullamcorper urna quis iaculis. Etiam ac massa
                sed turpis tempor luctus. Curabitur sed nibh eu elit
                mollis congue. Praesent ipsum diam, consectetur vitae
                ornare a, aliquam a nunc. In id magna pellentesque
                tellus posuere adipiscing. Sed non mi metus, at lacinia
                augue. Sed magna nisi, ornare in mollis in, mollis
                sed nunc. Etiam at justo in leo congue mollis.
                Nullam in neque eget metus hendrerit scelerisque
                eu non enim. Ut malesuada lacus eu nulla bibendum
                id euismod urna sodales. """
  
	print "Original Size: {0}".format(len(string))
	  
	compressed = zlib.compress(string)
	print "Compressed Size: {0}".format(len(compressed))
	  
	decompressed = zlib.decompress(compressed)
	print "Decompressed Size: {0}".format(len(decompressed))

def microtime(get_as_float = False) :
    if get_as_float:
        return time.time()
    else:
        return '%f %d' % math.modf(time.time())

def shutdown():
    global start_time
    print "Execution took: {0} seconds".format(start_time)

if __name__ == '__main__': 
	function("hello", "world")
	function()
	foo()
	foo("hello")
	foo("hello","world","Again")
	for filename in multiple_file_types("*.txt", "*.py"): # add as many filetype arguements
		pass
		#print os.path.realpath(filename)
	
	testDebug()
	
	#生成唯一id
	#result = uuid.uuid1()
	result = uniqueId()
	print result
	
	jsonTest()
	
	zlibTest()
	
	#注册Shutdown函数
	start_time = microtime(False)
	atexit.register(start_time)
	atexit.register(shutdown)
	
	
	
	
	
	