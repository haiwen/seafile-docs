# -*- coding: utf-8 -*-

import os
from datetime import datetime
from dateutil.tz import tzlocal

from pfm.fileobj.mdfile import MdFile
from pfm.fileobj.mdpara import MdPara
from pfm.poparser import PoParser


class PoTemplate:
    def __init__(self):
        self.filename = ''
        self.project = ''
        self.report_bug = ''

        # pot file
        self.fi = None
        self.fo = None

        # md file array
        self.mdf = []
        self.mdfd = {}
        self.mdp = None

        self.poc = PoParser()
        self.creditpt = r'^#' \
                        r'\s([A-Z][a-z\W]+)([\-\s][A-Z][a-z\W]+)+' \
                        r'\s\<[a-zA-Z0-9\.\-_]+\@' \
                        r'[a-zA-Z0-9\-_]+(\.[a-zA-Z0-9\-_]+)+\>' \
                        r'(,\s([1-2][0-9]{3})(\-([1-2][0-9]{3}))?)+\.$'
        self.fileline = ''
        self.msgdesc = ''
        self.msgidstr = ''

    def set_filename(self, name):
        self.filename = name

    def set_project_title(self, title):
        self.project = title

    def set_report_bug(self, email):
        self.report_bug = email

    def prepare_header_description(self):
        self.fo.write('# SOME DESCRIPTIVE TITLE.\n')
        self.fo.write('# Copyright (C) YEAR THE PACKAGE\'S COPYRIGHT HOLDER\n')
        self.fo.write('# This file is distributed under the same license ')
        self.fo.write('as the PACKAGE package.\n')
        self.fo.write('# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.\n')
        self.fo.write('# \n')

    def prepare_header_pot(self):
        self.fo.write('msgid ""\n')
        self.fo.write('msgstr ""\n')

        piv = '"Project-Id-Version: '
        piv += self.project
        piv += '\\n"\n'
        self.fo.write(piv)

        rbg = '"Report-Msgid-Bugs-To: '
        rbg += self.report_bug
        rbg += '\\n"\n'
        self.fo.write(rbg)

        cdt = '"POT-Creation-Date: '
        cdt += datetime.now(tzlocal()).strftime('%Y-%m-%d %H:%M:%S%z')
        cdt += '\\n"\n'
        self.fo.write(cdt)

        self.fo.write('"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"\n')
        self.fo.write('"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n"\n')
        self.fo.write('"Language-Team: LANGUAGE <LL@li.org>\\n"\n')
        self.fo.write('"MIME-Version: 1.0\\n"\n')
        self.fo.write('"Content-Type: text/plain; charset=UTF-8\\n"\n')
        self.fo.write('"Content-Transfer-Encoding: 8bit\\n"\n')

    def prepare_header(self):
        self.prepare_header_description()
        self.prepare_header_pot()

    def add_file(self, fileobj):
        self.mdf.append(fileobj)

    def remove_redundancy(self):
        tmdp_list = {}

        # MdFile
        for fobj in self.mdf:
            mdfn = fobj.md_filename()
            self.mdp = fobj.md_paragraph()

            # MdPara
            for msg in self.mdp.keys():
                pobj = self.mdp[msg]
                lnlist = pobj.line_number_list()

                if msg in tmdp_list.keys():
                    tmdp = tmdp_list[msg]
                    for ln in lnlist:
                        tmdp.add_line_number('{}:{}'.format(mdfn, ln))
                    tmdp_list.update({msg: tmdp})
                else:
                    tmdp = MdPara()
                    tmdp.set_type(pobj.para_type(), pobj.para_msg())
                    for ln in lnlist:
                        tmdp.add_line_number('{}:{}'.format(mdfn, ln))
                    tmdp_list[msg] = tmdp

        del self.mdf
        self.mdfd = {}

        for msg in tmdp_list.keys():
            tmdp = tmdp_list[msg]
            fnln = tmdp.line_number_list()[0].split(':')
            fn = fnln[0]
            ln = int(fnln[1])
            if fn in self.mdfd.keys():
                fobj = self.mdfd.get(fn)
                fobj.set_md_paragraph(ln, tmdp)
                self.mdfd.update({fn: fobj})
            else:
                fobj = MdFile(fn)
                fobj.set_md_paragraph(ln, tmdp)
                self.mdfd[fn] = fobj

        del tmdp_list

    def export(self):
        fpath = '{}/{}/{}.pot'.format(os.getcwd(), 'po', self.filename)
        print('Creating {} ... '.format(
            fpath.replace(os.getcwd() + '/', '')), end='')
        self.fo = open(fpath, 'w')

        self.prepare_header()
        self.remove_redundancy()

        fkeys = sorted(self.mdfd.keys())
        for fn in fkeys:
            self.mdp = self.mdfd[fn]
            tmdp_list = self.mdp.md_paragraph()
            skeys = sorted(tmdp_list.keys())
            for line in skeys:
                pobj = tmdp_list[line]
                # ignore blank line
                if pobj.is_blank():
                    continue

                # start of message object
                self.fo.write('\n')

                # message metadata
                for ln in pobj.line_number_list():
                    self.fo.write('#: {}\n'.format(ln))

                # message type description
                if pobj.is_header():
                    self.fo.write('# header\n')

                elif pobj.is_bquote():
                    self.fo.write('# blockquote, which can be cascaded\n')

                elif pobj.is_unordered():
                    self.fo.write('# unordered list\n')

                elif pobj.is_ordered():
                    self.fo.write('# ordered list\n')

                elif pobj.is_codeblock():
                    self.fo.write('# code block\n')

                elif pobj.is_tagopen():
                    self.fo.write('# inline html\n')

                elif pobj.is_tableopen():
                    self.fo.write('# table\n')

                elif pobj.is_rule():
                    self.fo.write(
                        '# horizontal rule. just copy and paste from the msgid')

                # message id
                self.fo.write('msgid "')
                msg = pobj.para_msg()[:-1] \
                    .replace('\\', '\\\\') \
                    .replace('\"', '\\"')
                self.fo.write('\\n"\n"'.join(msg.split('\n')) + '"\n')

                # message string placeholder
                self.fo.write('msgstr ""\n')

            del tmdp_list

        self.fo.write('\n')
        self.fo.close()

        print('[ OK ]\n')
