# -*- coding: utf8 -*-

class Node:
    def __init__(self, depth, data):
        self.children = []
        self.depth = depth
        self.data = data

    def __repr__(self):
        return 'state : {0}, depth : {1}'.format(self.data.get_state(), self.depth)

    def get_depth(self):
        return self.depth

    def get_data(self):
        return self.data

    def set_parent(self, parent):
        self.parent = parent

    def append_child(self, child):
        self.children.append(child)

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children