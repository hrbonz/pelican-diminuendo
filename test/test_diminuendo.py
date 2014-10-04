# -*- coding: utf-8 -*-

import os
import shutil
import six
import unittest

from pelican import read_settings

if not six.PY3:
    from codecs import open


class TestDiminuendo(unittest.TestCase):

    def setUp(self):
        """create a pelican instance"""
        here = os.path.abspath(os.path.dirname(__file__))
        self.settings = read_settings(
            os.path.join(here, 'pelican.conf'),
            override={'PATH': os.path.join(here, 'content')})

        cls = self.settings['PELICAN_CLASS']
        if isinstance(cls, six.string_types):
            module, cls_name = cls.rsplit('.', 1)
            module = __import__(module)
            cls = getattr(module, cls_name)
        self.pelican = cls(self.settings)

    def tearDown(self):
        here = os.path.abspath(os.path.dirname(__file__))
        shutil.rmtree(os.path.join(here, self.settings['OUTPUT_PATH']),
                      ignore_errors=True)
        shutil.rmtree(os.path.join(here, self.settings['CACHE_PATH']),
                      ignore_errors=True)

    def test_basic(self):
        """Reproduce a pelican run and check the output.
        .. warning:: This is a very weak test as it relies on a lot of pelican
                     defaults.
        """
        self.pelican.run()
        here = os.path.abspath(os.path.dirname(__file__))
        resultfd = open(os.path.join(here, self.settings['OUTPUT_PATH'],
                                 'test_page.html'))
        self.assertEqual(resultfd.read(88), """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><title>A smart title</title>""")
        resultfd.close()
        resultfd = open(os.path.join(here, self.settings['OUTPUT_PATH'],
                                 'pages/about.html'))
        self.assertEqual(resultfd.read(83), """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><title>About me</title>""")
        resultfd.close()
