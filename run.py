#!/usr/bin/env python
# -*- coding:utf-8 -*-

from os import path
from flask import Flask, request, Response, abort
from fileoper import img_resize, file_getmime, file_read

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['RESOURCE_ROOT'] = 'img'


@app.route('/<path:uri>')
def index(uri):
    filetypelist = ['jpg', 'jpeg', 'png', 'JPG', 'JPEG', 'PNG']
    filetype = request.path.split('.')[-1]

    # filepath = path.join(app.config.get('RESOURCE_ROOT'),uri)
    filepath = app.config.get('RESOURCE_ROOT') +'/'+uri
    filemime = file_getmime(filepath)
    allargs = request.args

    if not path.exists(filepath):
        abort(404)

    if filetype not in filetypelist:
        content = Response(file_read(filepath), mimetype=filemime)
        return content

    content = Response(img_resize(filepath, allargs, filetype), mimetype=filemime)
    return content

if __name__ == '__main__':
    app.run()