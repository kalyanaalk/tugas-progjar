import os
import json
import base64
from glob import glob

class FileInterface:
    def __init__(self):
        if not os.path.exists('files'):
            os.makedirs('files')
        os.chdir('files/')

    def list(self, params=[]):
        try:
            filelist = glob('*.*')
            return dict(status='OK', data=filelist)
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def get(self, params=[]):
        try:
            filename = params[0]
            if not filename:
                return dict(status='ERROR', data='filename is required')
            with open(filename, 'rb') as fp:
                isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK', data_namafile=filename, data_file=isifile)
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def upload(self, params=[]):
        try:
            filename = params[0]
            filecontent = params[1]
            with open(filename, 'wb') as fp:
                fp.write(base64.b64decode(filecontent))
            return dict(status='OK', data='file uploaded successfully')
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def delete(self, params=[]):
        try:
            filename = params[0]
            os.remove(filename)
            return dict(status='OK', data='file deleted successfully')
        except Exception as e:
            return dict(status='ERROR', data=str(e))
