import unittest
import beautify


class TestStringMethods(beautify.TestBeautify, unittest.TestCase):
    module = 'Sample'

    def test_always_fails(self):
        self.assertEqual('foo'.upper(), 'FOO0')

    def test_always_error(self):
        """This test will always give error
        \rDon't worry
        """
        self.assertTrue('FOO'.isupaper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class NoModuleName(beautify.TestBeautify):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


class OverwriteDefault(beautify.TestBeautify):

    def setUp(self):
        self.foo = 'FOO'

    def tearDown(self):
        self.foo = None

    def test_upper(self):
        self.assertEqual('foo'.upper(), self.foo)

if __name__ == '__main__':
    unittest.main()
