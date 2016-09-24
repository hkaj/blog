#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Haissam Kaj'
SITENAME = u"/dev/urandom"
SITETITLE = u"/dev/urandom"
SITESUBTITLE = u"Haissam's blog"
SITEDESCRIPTION = "Haissam's Thoughts and Writings"
SITEURL = 'https://haissamkaj.com'
FAVICON = SITEURL + '/favicon.ico'
SITELOGO = SITEURL + '/profile.png'

# Analytics
PIWIK_URL = ''
PIWIK_SITE_ID = '' 
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = 'themes/Flex'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/hkaj'),
          ('twitter', 'https://twitter.com/ha_kaj'),
          ('linkedin', 'https://fr.linkedin.com/in/haissamkaj'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
