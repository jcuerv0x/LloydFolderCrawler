#!/usr/bin/env python3
"""
Description: validataion code for python Daemon
Source: http://web.archive.org/web/20131017130434/http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/
""" 

import os
import shutil
import time
import sys
from daemon import Daemon

"""
class MyDaemon(Daemon):
        def run(self):
                while True:
                        time.sleep(1)
"""

class MyDaemon(Daemon):

    def __init__(self, source, destination, pid='/tmp/daemon-example.pid'):
        self.source = source
        self.destination = destination
        super().__init__(pid)

    def run(self):
        while True:
                content = os.listdir(self.source)
                for files in content:
                    if files.endswith('.mp3') or files.endswith('.flac'):
                        shutil.move(os.path.join(self.source, files), os.path.join(self.destination, files))
                        print(files)
                    elif files not in content:
                        print("waiting for new files")
                time.sleep(10)

if __name__ == "__main__":
        daemon = MyDaemon("/home/andrew53/Downloads", "/home/andrew53/Music/Music", pid='/tmp/amw-example.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print("Unknown command")
                        sys.exit(2)
                sys.exit(0)
        else:
                print("usage: %s start|stop|restart" % sys.argv[0])
                sys.exit(2)
