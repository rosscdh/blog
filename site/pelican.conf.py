# -*- coding: utf-8 -*-
import os
PROJECT_DIR = os.path.dirname(__file__)

AUTHOR = "Ross Crawford-d'Heureuse"
SITENAME = "Django flavoured"
SITEURL = 'http://stard0g101.github.com'
FEED_DOMAIN = SITEURL

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG='en'
LOCALE='en_GB.UTF-8'

GITHUB_URL = 'http://github.com/stard0g101/'
REVERSE_CATEGORY_ORDER = True


# Blogroll
# LINKS =  (
#          )

# Social widget
SOCIAL = (
          ('twitter', 'http://twitter.com/stardog101'),
          ('github', 'http://github.com/stard0g101'),
         )

DEFAULT_PAGINATION = 5

# global metadata to all the contents
# DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
# STATIC_PATHS = ["pictures", ]

# A list of files to copy from the source to the destination
# FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)
THEME = os.path.join(PROJECT_DIR, '../pelican-themes/subtle')
