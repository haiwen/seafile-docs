# -*- coding: utf-8 -*-


class PoFile:
    def __init__(self, name):
        self.filename = name
        self.targetarr = {}

    def add_msg_object(self, tfile, mdarr):
        self.targetarr[tfile] = mdarr

    def msg_object_by_tfile(self, tfile):
        return self.targetarr.get(tfile)

    def exist_msg_object(self, tfile):
        return tfile in self.targetarr.keys()

    def update_msg_object(self, tfile, mdarr):
        self.targetarr.update({tfile: mdarr})

    def filename(self):
        return self.filename

    def msg_object(self):
        return self.targetarr
