#!/usr/bin/env python

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
    except (ValueError,TypeError) as diag:
        retval = str(diag)
    return retval

def main():
    'handles all the data processing'
    log = open('cardlog.txt', 'w')
    try:
        ccfile = open('carddata.txt', 'r')
        txns = ccfile.readlines()
#        ccfile.close()
        
        total = 0.00
        log.write('account log:\n')
        
        for eachTxn in txns:
            result = safe_float(eachTxn)
            if isinstance(result, float):
                total += result
                log.write('data: %s processed \n' % result)
            else:
                log.write('ignored: %s \n' % result)
                
        print('$%.2f (new balance)' % (total))
        log.close()
    except IOError as e:
        log.write('no txns this month\n')
        log.close()
        return  
    finally:
        ccfile.close()
    
if __name__ == '__main__':
    main()



