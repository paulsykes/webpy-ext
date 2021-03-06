#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Store for saving a session in memcache
'''

import web.session

class MemcacheStore(web.session.Store):
    '''
    Store for saving a session in memcache
    '''

    def __init__(self, mc, prefix='session.', 
            timeout=web.config.session_parameters['timeout']):
        self.mc = mc
        self.prefix = prefix
        self.timeout = timeout

    def __contains__(self, key):
        key = self.prefix + key
        return self.mc.append(key, '')

    def __getitem__(self, key):
        key = self.prefix + key
        value = self.mc.get(key)
        value = self.decode(value)
        return value

    def __setitem__(self, key, value):
        key = self.prefix + key
        value = self.encode(value)
        self.mc.set(key, value, self.timeout)

    def __delitem__(self, key):
        key = self.prefix + key
        self.mc.delete(key)
    
    def cleanup(self, timeout):
        pass
