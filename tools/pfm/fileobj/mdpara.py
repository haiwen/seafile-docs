# -*- coding: utf-8 -*-


class MdPara:
    def __init__(self):
        self.paraline = []
        self.paratype = ''
        self.paramsg = ''

    # type attribute handling
    def set_type(self, tp, msg):
        self.paratype = tp
        self.paramsg = msg

    def check_type(self, tp):
        return tp == self.paratype

    def add_line_number(self, line):
        self.paraline.append(line)

    def line_number_list(self):
        return self.paraline

    def para_type(self):
        return self.paratype

    def para_msg(self):
        return self.paramsg

    def is_header(self):
        return self.check_type('header')

    def is_headerline(self):
        return self.check_type('headerline')

    def is_common(self):
        return self.check_type('common')

    def is_bquote(self):
        return self.check_type('blockquote')

    def is_unordered(self):
        return self.check_type('unordered')

    def is_ordered(self):
        return self.check_type('ordered')

    def is_codeblock(self):
        return self.check_type('codeblock')

    def is_tagopen(self):
        return self.check_type('tagopen')

    def is_tagclose(self):
        return self.check_type('tagclose')

    def is_tableopen(self):
        return self.check_type('tableopen')

    def is_tableclose(self):
        return self.check_type('tableclose')

    def is_rule(self):
        return self.check_type('hr')

    def is_blank(self):
        return self.check_type('blank')
