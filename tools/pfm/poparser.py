# -*- coding: utf-8 -*-

import re


class PoParser:
    def __init__(self):
        self.dsc = re.compile(r'^#\s[a-zA-Z0-9\-\._<>@,\s]*$')
        self.phc = re.compile(
            r'^\"([A-Z][A-Za-z0-9]+)(\-[A-Z][A-Za-z0-9]+)+' +
            r':\s[a-zA-Z0-9@<>:;=/\.\-\+\s]+\\n\"')
        self.fnc = re.compile(
            r'^#:(\s[a-zA-Z0-9\-_]+(\.[a-zA-Z0-9\-_]+)*' +
            r'(/[a-zA-Z0-9\-_]+(\.[a-zA-Z0-9\-_]+)*)*:[1-9][0-9]*)+')
        self.fzc = re.compile(r'^#, fuzzy\n?$')
        self.mhc = re.compile(r'^msgid\s\"\"')
        self.mic = re.compile(r'^msgid\s\"[\w\W]*\"')
        self.msc = re.compile(r'^msgstr\s\"[\w\W]*\"')
        self.blc = re.compile(r'^\n?$')

    def parse(self, ostr):
        if self.dsc.match(ostr):
            return 'headerdesc'

        elif self.phc.match(ostr):
            return 'headermeta'

        elif self.fnc.match(ostr):
            return 'stringorgn'

        elif self.fzc.match(ostr):
            return 'fuzzy'

        elif self.mhc.match(ostr):
            return 'msgheader'

        elif self.mic.match(ostr):
            return 'msgid'

        elif self.msc.match(ostr):
            return 'msgstr'

        elif self.blc.match(ostr):
            return 'blankline'
