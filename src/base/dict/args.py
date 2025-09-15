# coding=gb2312
#/usr/bin/env python

#元组
def tupleVarArgs(arg1, arg2='defaultB',*theRest):
    'display regular args and non-keyword variale args'
    print('formal arg 1:', arg1)
    print('formal arg 2:', arg2)
    for eachXtrArg in theRest:
        print('another arg:', eachXtrArg)
    
    print('tupleVarArgs() ','--'*20)
        
tupleVarArgs('abc')
tupleVarArgs(23, 4.56)
tupleVarArgs('abc', 123, 'xyz',456.789)

print('||'*20)

#字典
def dictVarArgs(arg1, arg2='defaultB',**theRest):
    'display regular args and non-keyword variale args'
    print('formal arg 1:', arg1)
    print('formal arg 2:', arg2)
    for eachXtrArg in theRest.keys():
        print('Xtra arg %s: %s' % (eachXtrArg,theRest[eachXtrArg]))
        
    print('dictVarArgs() ','--'*20)
        
dictVarArgs(1220, 740.0, c='grail')
dictVarArgs(arg2='tables',c=123, d='poe',arg1='mystery')
dictVarArgs('one', d=10, e='zoo',men=('freud','gaudi'))

print('||'*20)

def newfoo(arg1, arg2, *nkw, **kw):
    print('arg1:', arg1)
    print('arg2:', arg2)
    
    for narg in nkw:
        print('nkw:', narg)
        
    for kwarg in kw.keys():
        print('kw.keys:%s kw.val:%s' % (kwarg, kw[kwarg]))
        
    print('newfoo():','--'*20)
        
newfoo('abc',23,'cc','dd',d='d',e='e')

print('||'*20)

aTuple = (6,7,8)
bDict = {'z': 9}
newfoo(1,2,3,x=4,y=5,*aTuple,**bDict)
        
        
        
        
            
    
    
    
    
    







