DEBUG = True

QN_ACCESS_KEY = ''
QN_SECRET_KEY = ''

try:
    from config_overwrite import *
except Exception, e:
    print '============', e
    pass
