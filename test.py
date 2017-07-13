#!/usr/bin/env python  
# encoding: utf-8

# import os, sys
# # print(dir(os))
# # import glob
# # print(glob.glob('*.py'))
#
# # print(sys.stderr.write('Warning, log file not found starting a new one\n'))
#
# # from urllib.request import urlopen
# # with urlopen('http://baidu.com') as response:
# #     for line in response:
# #         line = line.decode('utf-8')  # Decoding the binary data to text.
# #         if 'EST' in line or 'EDT' in line:  # look for Eastern Time
# #             print(line)
#
#
# # import struct
# #
# # with open('pyauto-master.zip', 'rb') as f:
# #     data = f.read()
# #
# # start = 0
# # for i in range(3):                      # show the first 3 file headers
# #     start += 14
# #     fields = struct.unpack('<IIIHH', data[start:start+16])
# #     crc32, comp_size, uncomp_size, filenamesize, extra_size = fields
# #
# #     start += 16
# #     filename = data[start:start+filenamesize]
# #     start += filenamesize
# #     extra = data[start:start+extra_size]
# #     print(filename, hex(crc32), comp_size, uncomp_size)
# #
# #     start += extra_size + comp_size     # skip to the next header
#
# # import threading, zipfile
# #
# # class AsyncZip(threading.Thread):
# #     def __init__(self, infile, outfile):
# #         threading.Thread.__init__(self)
# #         self.infile = infile
# #         self.outfile = outfile
# #
# #     def run(self):
# #         f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
# #         f.write(self.infile)
# #         f.close()
# #         print('Finished background zip of:', self.infile)
# #
# # background = AsyncZip('mydata.txt', 'myarchive.zip')
# # background.start()
# # print('The main program continues to run in foreground.')
# #
# # background.join()    # Wait for the background task to finish
# # print('Main program waited until background was done.')
#
# # import logging
# # logging.debug('Debugging information')
# # logging.info('Informational message')
# # logging.warning('Warning:config file %s not found', 'server.conf')
# # logging.error('Error occurred')
# # logging.critical('Critical error -- shutting down')
# from pathlib import Path
#
# p = Path('.')
# # print([x for x in p.iterdir() if x.is_dir()])
# # print(p.iterdir(),p.is_dir())
# # for  i in p.iterdir():
# #     if i.is_dir():
# #         print(i)
#
# print(list(p.glob('**/*.py')))
# from pathlib import Path
# p = Path('/etc')
# q = p / 'init.d' / 'reboot'
# print(q.exists())
# from pathlib import Path
# p = Path('test.py')
# print(oct(33206))






a=64972**999999494949494949494
print(a)

