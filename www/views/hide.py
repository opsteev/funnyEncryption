# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, request, make_response
from flask.views import MethodView
from lib import generatePic
from lib.generatePic import generateAtbashPicture

class HideView(MethodView):
    __view__ = 'hide'
    @classmethod
    def getView(cls):
        return cls.__view__
    def get(self):
        return render_template('hide.html')
    def post(self):
        if request.form.has_key('cleartext'):
            img_hex = generateAtbashPicture(request.form['cleartext'])
            response = make_response(img_hex)
            response.headers.set('Content-Type', 'image/png')
            return response
        return redirect(url_for(self.__view__))
