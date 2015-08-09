# -*- coding: utf-8 -*-
from sys import stderr
from re import findall
from unittest import TestCase


class TestBeautify(TestCase):

    name = ''
    module = ''
    distance = 70

    def get_name(self):
        """ Get the name of the test """
        self.method_name = str(self._testMethodName).split('=')[-1][:-2]
        self.method_name = self.method_name.split('test_')[-1]
        self.method_name = self.method_name.replace('_', ' ')

    def __str__(self):
        self.get_name()
        if self.module is not '':
            out = '\r[%s] %s test ' % (self.module, self.method_name)
        else:
            self.module = findall('[A-Z][a-z]*', self.__class__.__name__)
            self.module = ' '.join(self.module)
            out = '\r[%s] %s test ' % (self.module, self.method_name)
        out = out.ljust(self.distance, '-')
        return out + ' '

    def run(self, result=None):
        stderr.write(self.__str__())
        super(TestBeautify, self).run(result)
        stderr.write(' Done\n')

    def shortDescription(self):
        return "Test from class %s" % self.__class__.__name__
