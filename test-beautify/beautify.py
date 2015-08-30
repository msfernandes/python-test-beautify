# -*- coding: utf-8 -*-
from sys import stderr
from re import findall
try:
    from unittest2 import TestCase, TestResult
except ImportError:
    from unittest import TestCase, TestResult


class Color(object):

    green_color = '\033[01;32m'
    red_color = '\033[01;31m'
    white_color = '\033[01;37m'
    blue_color = '\033[01;94m'
    black_color = '\033[01;30m'
    default_color = '\033[00;39m'

    @classmethod
    def black(cls, text):
        return "%s%s%s" % (cls.black_color, text, cls.default_color)

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


class _TextTestResult(TestResult):

    def __init__(self, stream):
        super(_TextTestResult, self).__init__(stream)
        self.stream = stream

    def addSuccess(self, test):
        super(_TextTestResult, self).addSuccess(test)
        self.stream.write(Color.green('PASS') + '\n')

    def addFailure(self, test, err):
        super(_TextTestResult, self).addFailure(test, err)
        self.stream.write(Color.red('FAIL') + '\n')

    def addError(self, test, err):
        super(_TextTestResult, self).addError(test, err)
        self.stream.write(Color.black('Error') + '\n')

    def printErrors(self):
        self.printErrorList(Color.black('ERROR'), self.errors)
        self.printErrorList(Color.red('FAIL'), self.failures)


class TestBeautify(TestCase):

    name = ''
    module = ''
    distance = 100

    def get_name(self):
        """ Get the name of the test """
        self.method_name = str(self.id).split('=')[-1][:-2]
        self.method_name = self.method_name.split('test_')[-1]
        self.method_name = self.method_name.replace('_', ' ')

    def __str__(self):
        self.get_name()
        if self.module is '':
            self.module = findall('[A-Z][a-z]*', self.__class__.__name__)
            self.module = ' '.join(self.module)
            out = '\r[%s] %s test ' % (self.module, self.method_name)

        module = "%s%s%s" % ('[', self.module, ']')
        method_name = "%s %s" % (self.method_name.lower(), 'test')
        out = "\r%s %s " % (Color.blue(module), Color.white(method_name))
        out = out.ljust(self.distance, '_')
        return out + ' '

    def shortDescription(self):
        if self._testMethodDoc:
            desc = self._testMethodDoc
        else:
            desc = "Test from method '%s'" % self.method_name.replace(' ', '_')
        return Color.red(desc)

    def run(self, result=None):
        # result = self.defaultTestResult()
        print result
        stderr.write('\n' + self.__str__())
        super(TestBeautify, self).run(result)
        return result

    def defaultTestResult(self):
        return _TextTestResult(stderr)

    def _makeResult(self):
        return _TextTestResult(stderr)
