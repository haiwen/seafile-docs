#!/usr/bin/python3
# -*- Mode: python -*-
# -*- coding: utf-8 -*-

import glob
import os
import re
import time

from pfm.fileobj.mdfile import MdFile
from pfm.fileobj.mdpara import MdPara
from pfm.fileobj.pot import PoTemplate
from pfm.mdparser import MdParser


class PFMMain:
    def __init__(self):
        self.conf = 'POTFILES.in'

        self.filelist = []

        self.cwd = '{}/'.format(os.getcwd())
        self.potpath = '{}po'.format(self.cwd)
        self.potobj = None

        self.mdparser = MdParser()

    def scan_md(self):
        # if corresponding directory doesn't exist
        if not os.path.exists(self.potpath):
            os.makedirs(self.potpath)

        # open POTFILES.in
        outfile = open('{}/{}'.format(self.potpath, self.conf), 'w')

        print('Scanning markdown files ...')
        time.sleep(1)

        # list all md files on the document root
        files = glob.glob(os.getcwd() + '/*.md')
        files.sort()

        for file in files:
            print('{} is found'.format(file.replace(self.cwd, '')))
            outfile.write(file.replace(self.cwd, '') + '\n')

        dirs = os.listdir(os.getcwd())
        dirs.sort()

        for dirn in dirs:
            if os.path.isdir(dirn):
                mdfiles = glob.glob('{}{}/*.md'.format(self.cwd, dirn))
                mdfiles.sort()

                for mdfile in mdfiles:
                    print('{} is found'.format(mdfile.replace(self.cwd, '')))
                    outfile.write(mdfile.replace(self.cwd, '') + '\n')

        print('File list is saved to po/POTFILES.in\n')
        outfile.close()

    def parse_md(self, filename):
        mdfile = open('{}/{}'.format(os.getcwd(), filename), 'r')
        mdobj = MdFile(filename)

        print('Extracting messages from {} ... '.format(filename))
        mdp_list = []
        line = 0

        # parsing routine per one markdown file
        while 1:
            mdstr = mdfile.readline()
            if not mdstr:
                break
            line += 1

            # print('%d: %s' % (line, mdstr), end="", flush=True)
            mdptype = self.mdparser.parse(mdstr)
            if mdptype == 'blank':
                continue

            mdp = MdPara()
            mdp.set_type(mdptype, mdstr)
            cline = line

            # if paragraph is common and is expectable to be a header
            # by looking forward the next line
            if mdp.is_headerline():
                bmdp = mdp_list[-1]

                # if 2 line header found
                if bmdp.is_common():
                    cline = mdp_list[-1].line_number_list()[-1]
                    del mdp_list[-1]
                    mdp.set_type('header', bmdp.para_msg() + mdp.para_msg())

            # if paragraph is code block
            if mdp.is_codeblock():
                while 1:
                    mdstr = mdfile.readline()
                    line += 1
                    if not mdstr:
                        break
                    # print('%d: %s' % (line, mdstr), end="", flush=True)
                    mdp.set_type(mdp.para_type(), mdp.para_msg() + mdstr)

                    if self.mdparser.parse(mdstr) == 'codeblock':
                        break

            # if paragraph is inline HTML
            elif mdp.is_tagopen():
                tagcls = '</{}>'.format(
                    re.search('<(\S+)>', mdp.para_msg()).group(1))
                while 1:
                    mdstr = mdfile.readline()
                    line += 1
                    if not mdstr:
                        break
                    # print('%d: %s' % (line, mdstr), end="", flush=True)
                    mdp.set_type(mdp.para_type(), mdp.para_msg() + mdstr)

                    if self.mdparser.parse(
                            mdstr) == 'tagclose' and tagcls == mdstr[:-1]:
                        break

            elif mdp.is_tableopen():
                while 1:
                    mdstr = mdfile.readline()
                    line += 1
                    if not mdstr:
                        break

                    mdp.set_type(mdp.para_type(), mdp.para_msg() + mdstr)

                    if self.mdparser.parse(mdstr) == 'tableclose':
                        break

            mdp.add_line_number(cline)
            mdp_list.append(mdp)

        # file should be closed after all of lines are parsed
        mdfile.close()

        for mdp in mdp_list:
            # blank line (ignore)
            if mdp.para_msg() == '\n':
                continue

            if mdobj.exist_md_paragraph(mdp.para_msg()):
                tmdp = mdobj.get_md_paragraph(mdp.para_msg())
                tmdp.add_line_number(mdp.line_number_list()[-1])
                mdobj.update_md_paragraph(tmdp.para_msg(), tmdp)
            else:
                mdobj.set_md_paragraph(mdp.para_msg(), mdp)

        # clear temporary list
        del mdp_list

        return mdobj

    def init_pot(self, dstr):
        # init pot
        self.potobj = PoTemplate()
        self.potobj.set_filename(dstr)
        self.potobj.set_project_title(os.getcwd().split('/')[-1])
        self.potobj.set_report_bug(
            'https://github.com/haiwen/seafile-docs/issues')

    def run(self):
        # check all of exist md files
        self.scan_md()

        # open POTFILES.in
        dfl = open('{}/{}'.format(self.potpath, self.conf), 'r')
        dname = ''

        while 1:
            # fetch one line having directory/file.md
            filename = dfl.readline()
            if not filename:
                break

            # create pot file per directory
            filename = filename[:-1]
            dstr = '/' in filename and filename.split('/')[0] or 'doc-root'

            # if directory has changed
            if dname != dstr:
                # if this step is not initial
                if dname != '':
                    self.potobj.export()

                self.init_pot(dstr)
                dname = dstr

            self.potobj.add_file(self.parse_md(filename))

        # create last pot
        self.potobj.export()

        dfl.close()


if __name__ == '__main__':
    s = PFMMain()
    s.run()
