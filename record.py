#!/usr/bin/env python
import os,time

def record_videos(func):
    def info(username='root', hostname=None, port=22):
        current_time = time.strftime('%Y%m%d%H%M%S')
        file_name = '%s-%s-%s' % (current_time, hostname, username)
        cmd = 'bin/script -t 2> videos/%s.time -a videos/%s.his -c "python connection.py %s@%s:%d"' % (file_name, file_name, username, hostname, port)
        os.system(cmd)
    return info
