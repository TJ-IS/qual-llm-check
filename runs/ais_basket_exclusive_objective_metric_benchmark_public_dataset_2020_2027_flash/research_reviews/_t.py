# -*- coding: utf-8 -*-
import io, os, sys
print('cwd:', os.getcwd())
print('script dir:', os.path.dirname(os.path.abspath(__file__)))
sys.stdout.flush()
try:
    out = io.open('_accept_out.txt','w',encoding='utf-8')
    out.write('hello\n')
    out.close()
    print('written:', os.path.abspath('_accept_out.txt'))
    print('exists:', os.path.exists('_accept_out.txt'))
except Exception as e:
    print('ERR:', repr(e))