# -*- coding: utf-8 -*-
from sys import stderr
from re import findall
from unittest import TestCase


class Color(object):

    ngree_color = '\033[01;32m'
    red_color = '\033[01;31m'
    white_color = '\033[01;37m'
    blue_color = '\033[01;94m'
    default_color = '\033[00;39m'

    @classmethod
    def green(cls, text):
        return "%s%s%s" % (cls.green_color, text, cls.default_color)

    @classmethod
    def red(cls, text):
        return "%s%s%s" % (cls.red_color, text, cls.default_color)

    @classmethod
    def white(cls, text):
        return "%s%s%s" % (cls.white_color, text, cls.default_color)

    @classmethod
    def blue(cls, text):
        return "%s%s%s" % (cls.blue_color, text, cls.default_color)


class TestBeautify(TestCase):

    name = ''
    module = ''
    distance = 100

    def get_name(self):
        """ Get the name of the test """
        self.method_name = str(self._testMethodName).split('=')[-1][:-2]
        self.method_name = self.method_name.split('test_')[-1]
        self.method_name = self.method_name.replace('_', ' ')

    def __str__(self):
        self.get_name()
        if self.module is '':
            self.module = findall('[A-Z][a-z]*', self.__class__.__name__)
            self.module = ' '.join(self.module)
            out = '\r[%s] %s test ' % (self.module, self.method_name)

        module = "%s%s%s" % ('[', self.module, ']')
        method_name = "%s%s" % (self.method_name.capitalize(), 'Test')
        out = "\r%s %s " % (Color.blue(module), Color.white(method_name))
        out = out.ljust(self.distance, '_')
        return out + ' '

    def run(self, result=None):
        stderr.write(self.__str__())
        super(TestBeautify, self).run(result)
        stderr.write(' Done\n')

    def shortDescription(self):
        return "Test from class %s" % self.__class__.__name__
