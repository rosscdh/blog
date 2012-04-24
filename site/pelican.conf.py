#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
PROJECT_DIR = '/home/rossc/Projects/Personal/blog/site'

AUTHOR = u"Ross Crawford-d'Heureuse"
SITENAME = u"Ross Crawford-d'Heureuse - Django flavoured application development"
SITEURL = '/'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG='en'

GITHUB_URL = 'http://github.com/stard0g101/'
REVERSE_CATEGORY_ORDER = True

# Blogroll
# LINKS =  (
#          )

# Social widget
SOCIAL = (
          ('twitter', 'http://twitter.com/stardog101'),
          ('github', 'http://twitter.com/stard0g101'),
         )

DEFAULT_PAGINATION = 5

# global metadata to all the contents
# DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
# STATIC_PATHS = ["pictures", ]

# A list of files to copy from the source to the destination
# FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

THEME = os.path.join(PROJECT_DIR, '../theme')
