# -*- coding: utf-8 -*-
from sys import stderr
import unittest


class TestBeautify(object):

    name = ''
    module = ''

    def getName(self):
        """ Get the name of the test """
        self.name = str(self.id).split('=')[-1][:-2]
        self.name = self.name.split('test_')[-1]
        self.name = self.name.replace('_', ' ')

    def __str__(self):
        self.getName()
        out = '\r[%s] %s test ' % (self.module, self.name)
        out = out.ljust(70, '-')
        return out + ' '

    def tearDown(self):
        stderr.write(' Done\n')

    def shortDescription(self):
        return "Test from class %s" % self.__class__.__name__

    def setUp(self):
        stderr.write(self.__str__())
        self.shortDescription()
