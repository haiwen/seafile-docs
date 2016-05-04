#!/usr/bin/python3
# -*- Mode: python -*-
# -*- coding: utf-8 -*-

import glob
import os


class UpdatePo:
    def __init__(self):
        self.popath = '{}/po'.format(os.getcwd())
        self.cmd_prefix = 'msgmerge -vU '
        self.cmd_pstfix = ' > /dev/null'
        
        self.potlist = []
        self.polist = []

    def create_cmd(self, pofile, potfile):
        argv = '{} {}'.format(pofile, potfile)
        return '{} {} {}'.format(self.cmd_prefix, argv, self.cmd_pstfix)

    def run(self):
        self.potlist = glob.glob('{}/*.pot'.format(self.popath))

        for pot in self.potlist:
            fn = pot.split('/')[-1].split('.')[0]
            self.polist = glob.glob('{}/{}.*.po'.format(self.popath, fn))

            for po in self.polist:
                print('Updating {} ...'.format(po))
                cmd = self.create_cmd(po, pot)
                print('$ {}'.format(cmd))
                os.system(cmd)


if __name__ == '__main__':
    u = UpdatePo()
    u.run()
