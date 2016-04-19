# -*- coding: utf-8 -*-


class PoMessage:
    def __init__(self):
        self.fline = []
        self.msgdesc = ''
        self.msgi = ''
        self.msgs = ''

    def add_fileline(self, fl):
        self.fline.append(fl)

    def fileline(self):
        return self.fline

    def set_description(self, descstr):
        self.msgdesc = descstr

    def description(self):
        return self.msgdesc

    def set_msgid(self, mid):
        self.msgi = mid

    def msgid(self):
        return self.msgi

    def set_msgstr(self, mstr):
        self.msgs = mstr

    def msgstr(self):
        return self.msgs
