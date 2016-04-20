# -*- coding: utf8 -*-

import re


class MdParser:
    def __init__(self):
        self.hc = re.compile(r'(^[\s\S]+\n(-[-]+|=[=]+)|' +
                             r'^([#]{1,6})\s[\s\S]+(\s\3)?)')
        self.hlc = re.compile(r'^(-[-]+|=[=]+)\n?$')
        self.bqc = re.compile(r'^(> )+[\s\S]+$')
        self.ulc = re.compile(r"^([\s]*[\*\+\-]\s)[\S\s]+$")
        self.olc = re.compile(r'^[1-9][0-9]*\.\s[\S\s]+$')
        self.hrc = re.compile(r'^([\*\-_]+|([\*\-_]\s){3,})$')
        self.cbc = re.compile(r'^([\s]*```)[\s\S]+$')
        self.toc = re.compile(r'^<[\w]+>\n$')
        self.tcc = re.compile(r'^</[\w]+>\n$')
        self.blc = re.compile(r'^\s*\n$')
        self.wtoc = re.compile(r'^\{\|(\s[a-z]+\=\"[0-9A-Za-z]+\")+\n$')
        self.wtcc = re.compile(r'^\|\}\n$')


    def parse(self, mstr):
        if self.bqc.match(mstr):
            return 'blockquote'

        elif self.ulc.match(mstr):
            return 'unordered'

        elif self.olc.match(mstr):
            return 'ordered'

        elif self.hc.match(mstr):
            return 'header'

        elif self.hlc.match(mstr):
            return 'headerline'

        elif self.hrc.match(mstr):
            return 'hr'

        elif self.blc.match(mstr):
            return 'blank'

        elif self.cbc.match(mstr):
            return 'codeblock'

        elif self.toc.match(mstr):
            return 'tagopen'

        elif self.tcc.match(mstr):
            return 'tagclose'

        elif self.wtoc.match(mstr):
            return 'tableopen'

        elif self.wtcc.match(mstr):
            return 'tableclose'

        else:
            return 'common'
