#!/usr/bin/python3
# -*- Mode: python -*-
# -*- coding: utf-8 -*-

import glob
import os
import re
from datetime import datetime

from dateutil.tz import tzlocal
from pfm.fileobj.mdfile import MdFile
from pfm.fileobj.pofile import PoFile
from pfm.fileobj.pomsg import PoMessage
from pfm.poparser import PoParser


class CopyrightException(Exception):
    def __str__(self):
        crdesc = '# This file is distributed under the same license ' \
                 'as the PACKAGE package.'
        return 'Copyright is missing. copyright description should say this ' \
               ' \"{}\"'.format(crdesc)


class MissingCreditException(Exception):
    def __str__(self):
        crdt = '# FULL NAME <EMAIL@ADDRESS>, YEAR1, YEAR2.'
        return 'Credit is missing on the header description, ' \
               'should be like this \"{}\"'.format(crdt)


class CreditMismatchException(Exception):
    def __str__(self):
        return 'Credit is not the same with \"Last-Translator\"'


class LocaleMismatchException(Exception):
    def __init__(self, lang, clocale):
        self.errlocale = '{} != {}'.format(lang, clocale)

    def __str__(self):
        return self.errlocale


class LangTeamMissingException(Exception):

    def __str__(self):
        return 'Language team email address is missing.\n' \
               'If there isn\'t, write Language name follows by yours or' \
               ' coordinator\'s email address\n'


class PoCompiler:
    def __init__(self):
        self.sourcedir = '{}/po'.format(os.getcwd())
        self.outputdir = '{}/locale'.format(os.getcwd())
        self.outfile = None

        self.last_trans_name = []
        self.last_trans_email = []
        self.last_trans_year = []

        self.langlist = []
        self.clocale = ''

        self.poparser = PoParser()
        self.crpt = r'^# This file is distributed under the same license as ' \
                    r'the [a-zA-Z0-9\-\.\_]+ package\.\n?$'
        self.creditpt = '^#\s([A-Z][a-z\W]+)([\-\s][A-Z][a-z\W]+)+' \
                        '\s\<[a-zA-Z0-9\.\-_]+\@'\
                        '[a-zA-Z0-9\-_]+(\.[a-zA-Z0-9\-_]+)+\>' \
                        '(,\s([1-2][0-9]{3})(\-([1-2][0-9]{3}))?)+\.\n?$'
        self.langteam = r'^\"Language\-Team: ' \
                        r'([A-Z][a-z]+)\s\<[a-zA-Z0-9\.\-_]+\@' \
                        r'[a-zA-Z0-9\-_]+(\.[a-zA-Z0-9\-_]+)+\>\\n\"\n?$'

        self.cmeta = False
        self.pofile = None
        self.mdfile = None
        self.pomsg = None

        self.f = None

    def verify(self):

        exist_copyright = False
        exist_credit = False

        while 1:
            poline = self.f.readline()[:-1]
            pt = self.poparser.parse(poline)

            # end of verification
            if pt == 'blankline':
                break

            # check header description
            elif pt == 'headerdesc':
                if re.match(self.crpt, poline):
                    exist_copyright = True
                elif re.match(r'{}'.format(self.creditpt), poline):
                    self.last_trans_name.append(poline.split('<')[0].strip())
                    self.last_trans_email.append(
                        poline.split('<')[1].split('>')[0])
                    years = poline[:-1].split('>')[1].split(', ')[1]
                    if '-' in years:
                        years = years.split('-')[1]
                    self.last_trans_year.append(years)

                    thisyear = datetime.now(tzlocal()).strftime('%Y')

                    if self.last_trans_year[-1] == thisyear:
                        exist_credit = True

            # if now is on msgid "", msgstr "" header
            elif pt == 'msgheader':
                if not exist_copyright:
                    raise CopyrightException()
                if not exist_credit:
                    raise MissingCreditException()

            # check po meta header
            elif pt == 'headermeta':
                self.cmeta = True
                keyval = poline[1:-3].split(': ')
                if keyval[0] == 'Language':
                    if keyval[1] != self.clocale:
                        raise LocaleMismatchException(keyval[1], self.clocale)
                elif keyval[0] == 'Last-Translator':
                    name = keyval[1].split('<')[0].strip()
                    email = keyval[1].split('<')[1].split('>')[0].strip()
                    if self.last_trans_name[-1] != name \
                            and self.last_trans_email[-1] != email:
                        raise CreditMismatchException()
                elif keyval[0] == 'Language-Team':
                    if not re.match(r'{}'.format(self.langteam), poline) or \
                       poline == '\"Language-Team: LANGUAGE <LL@li.org>\n\"':
                        raise LangTeamMissingException()

    def get_msg_set(self, poline):
        msgid = poline[:-2].split(' "')[1]
        poline = self.f.readline()
        while self.poparser.parse(poline) != 'msgstr':
            msgid += poline[1:-2]
            poline = self.f.readline()

        msgstr = poline[:-2].split(' "')[1]
        poline = self.f.readline()
        while self.poparser.parse(poline) != 'blankline':
            msgstr += poline[1:-2]
            poline = self.f.readline()

        # print ('{}, {}'.format(msgid, msgstr))

        return msgid, msgstr

    def add_msg_set(self, line, msgid, msgstr):
        self.pomsg = PoMessage()
        self.pomsg.set_msgid(msgid)
        self.pomsg.set_msgstr(msgstr)

        cmdf = line.split(':')[0]
        clnn = int(line.split(':')[1])

        if self.pofile.exist_msg_object(cmdf):
            self.mdfile = self.pofile.msg_object_by_tfile(cmdf)
            self.mdfile.set_md_paragraph(clnn, self.pomsg)
            self.pofile.update_msg_object(cmdf, self.mdfile)
        else:
            if not self.mdfile:
                self.mdfile = MdFile(cmdf)
            else:
                if self.mdfile.md_filename() != cmdf:
                    self.mdfile = MdFile(cmdf)

            self.mdfile.set_md_paragraph(clnn, self.pomsg)
            self.pofile.add_msg_object(cmdf, self.mdfile)

    def analysis(self):
        poline = ''
        fnarr = []
        line = 0

        # skip until it reached to blank line
        while self.poparser.parse(poline) != 'blankline':
            poline = self.f.readline()

        self.pofile = PoFile(self.f.name)

        # structural analysis
        while 1:
            poline = self.f.readline()
            line += 1
            if not poline:
                break

            pt = self.poparser.parse(poline)
            if pt == 'headerdesc' or pt == 'blankline':
                continue

            elif pt == 'stringorgn':
                # print (poline)
                if poline.count(' ') > 1:
                    fa = poline[3:-1].split(' ')
                    for f in fa:
                        fnarr.append(f)
                        # print (fnarr)
                else:
                    fnarr.append(poline[3:-1])

            elif pt == 'fuzzy':
                # consider that this isn't translated
                poline = self.f.readline()
                msgid, msgstr = self.get_msg_set(poline)

                for fn in fnarr:
                    self.add_msg_set(fn, msgid, '')

                del fnarr
                fnarr = []

            elif (pt == 'msgid' or pt == 'msgheader') and self.cmeta:
                msgid, msgstr = self.get_msg_set(poline)

                for fn in fnarr:
                    self.add_msg_set(fn, msgid, msgstr)

                del fnarr
                fnarr = []

    def compile(self):
        # write translation to the target
        # get list of MdFile()
        mdlist = self.pofile.msg_object()
        for mdfn in sorted(mdlist.keys()):
            mdfo = mdlist.get(mdfn)
            tpath = '{}/{}/{}'.format(self.outputdir, self.clocale,
                                      mdfn.split('/')[0])
            if not os.path.exists(tpath) and '/' in mdfn:
                os.makedirs(tpath, 0o755)

            # writeout to md
            self.outfile = open(
                '{}/{}/{}'.format(self.outputdir, self.clocale, mdfn), 'w')
            print('Writing {} ... '.format(self.outfile.name), end='')

            # cln : current line number
            # nln : new line number
            # lim : limit count (refer below code)
            # lndf : line number difference (nln - cln)
            cln, nln, lim, lndf = (0, 0, 0, 0)
            # new line character flag
            lim = 0

            # get list of PoMessage()
            pomarr = mdfo.md_paragraph()
            for poln in sorted(pomarr.keys()):
                if cln == 0:
                    nln = poln
                else:
                    nln = poln
                    lndf = nln - cln

                    while lndf > lim:
                        self.outfile.write('\n')
                        lndf -= 1

                pomobj = pomarr.get(poln)
                if len(pomobj.msgstr()) == 0:
                    lim = pomobj.msgid().count('\\n')
                    self.outfile.write(
                        pomobj.msgid()
                              .replace('\\n', '\n')
                              .replace('\\"', '\"')
                              .replace('\\\\', '\\'))
                else:
                    lim = pomobj.msgstr().count('\\n')
                    self.outfile.write(
                        pomobj.msgstr()
                              .replace('\\n', '\n')
                              .replace('\\"', '\"')
                              .replace('\\\\', '\\'))

                cln = nln

            self.outfile.write('\n\n')
            self.outfile.close()
            print('OK')

    def run(self):
        cll = open('{}/LINGUAS'.format(self.sourcedir), 'r').readline()
        self.langlist = cll[:-1].split(' ')

        for lang in self.langlist:
            polist = glob.glob('{}/*.{}.po'.format(self.sourcedir, lang))
            if len(polist) != 0:
                print('Compiling *.{}.po ...'.format(lang))
            self.clocale = lang
            for po in polist:
                print('Compiling {} ...'.format(po))
                self.f = open(po, 'r')

                self.verify()
                self.analysis()
                self.compile()
                self.f.close()


if __name__ == '__main__':
    c = PoCompiler()
    c.run()
