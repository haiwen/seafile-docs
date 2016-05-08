# -*- coding: utf-8 -*-


class MdFile:
    def __init__(self, fname):
        self.filename = fname
        self.mdpara = {}

    def md_filename(self):
        return self.filename

    def set_md_paragraph(self, key, mdpobj):
        self.mdpara[key] = mdpobj

    def get_md_paragraph(self, key):
        return self.mdpara.get(key)

    def exist_md_paragraph(self, key):
        return key in self.mdpara.keys()

    def update_md_paragraph(self, key, mdpobj):
        self.mdpara.update({key: mdpobj})

    def md_paragraph(self):
        return self.mdpara

    def last_md_paragraph(self):
        return self.mdpara.get(sorted(self.mdpara.keys())[-1])

    def del_last_md_paragraph(self):
        del self.mdpara[sorted(self.mdpara.keys())[-1]]
