'''
- BaseException
    |- KeyboardInterrupt
    |- SystemExit
    |- Exception
        |- (all other current built-in exceptions) 所有当前内建异常
'''
def safe_float(obj):
    try:
        retval = float(obj)
    except ValueError:
        retval = 'could not convert non-number to float'
    except TypeError:
        retval = 'object type cannot be converted to float'
    return retval

def safe_float2(obj):
    try:
        retval = float(obj)
    except (ValueError,TypeError):
        retval = 'argument must be a number or a numeric string'
    return retval

def safe_float3(obj):
    try:
        retval = float(obj)
    except (ValueError,TypeError) as diag:
        retval = str(diag)
    return retval

#print(safe_float('12.34'))
#print(safe_float('bad'))
#print(safe_float({'a':'dict'}))
#
#print(safe_float2('12.34'))
#print(safe_float2('bad'))
#print(safe_float2({'a':'dict'}))

print(safe_float3('12.34'))
print(safe_float3('bad'))
print(safe_float3({'a':'dict'}))

try:
    float(['float() does not','like lists',2])
except TypeError as diag:
    pass
#    print(type(diag))
#    print(diag)
#    print(diag.__class__)
#    print(diag.__class__.__doc__)
#    print(diag.__class__.__name__)


