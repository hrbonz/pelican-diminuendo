# -*- coding: utf-8 -*-
from __future__ import with_statement, unicode_literals, print_function
import logging
from os import walk
import os.path
import six

from pelican import signals

from diminuendo import htmlmin

# make sure open supports unicode py2x/py3x
if not six.PY3:
    from codecs import open


__author__ = "Stefan \"hr\" Berder"
__contact__ = "hr@bonz.org"
__license__ = "BSD 3-Clause"
__version__ = "0.1.1"

logger = logging.getLogger(__name__)


def minify_html(pelican):
    """Minify all HTML files passed in a pelican instance.

    :param pelican: a pelican object
    :type pelican: object
    """
    for (dirpath, dirnames, filenames) in walk(
        pelican.settings['OUTPUT_PATH']):
        for filename in filenames:
            if filename.endswith('.html'):
                filepath = os.path.join(dirpath, filename)
                fdin = open(filepath, encoding='utf-8')
                code = fdin.read()
                with open(filepath, 'w', encoding='utf-8') as fdout:
                    try:
                        fdout.write(htmlmin.minify(code))
                    except IOError:
                        logger.error(
                            "problem minifying ({})".format(IOError))
                    finally:
                        fdout.close()
                fdin.close()
                logger.info(
                    "minified {} ({})".format(filename, dirpath))
                        

def register():
    """Register minifying as post processing"""
    signals.finalized.connect(minify_html)
