# -*- coding: utf-8 -*-


class PotFile:
    def __init__(self):
        self.author = []
        self.meta_header = {}
        self.potobj = {}

    def add_author(self, author):
        self.author.append(author)

    def author(self):
        return self.author

    def put_meta_header(self, key, val):
        self.meta_header[key] = val

    def meta_header(self):
        return self.meta_header

    def put_pot_object(self, key, pobj):
        self.potobj[key] = pobj

    def exist_pot_object(self, key):
        return key in self.potobj.keys()

    def pot_object(self, key):
        return self.potobj.get(key)

    def del_pot_object(self, key):
        del self.potobj[key]

    def update_pot_object(self, key, pobj):
        self.potobj.update({key: pobj})

    def pot_objects(self):
        return self.potobj
