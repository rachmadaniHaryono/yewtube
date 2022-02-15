#!/usr/bin/python3

""" setup.py for yewtube.

https://github.com/iamtalhaasghar/yewtube

python setup.py sdist bdist_wheel
"""

import sys, os
from datetime import datetime

if sys.version_info < (3, 6):
    sys.exit("yewtube requires minimum python 3.6")

from setuptools import setup

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()
    
# with open("requirements.txt", "r", encoding="utf-8") as fh:
#     requirements = fh.readlines()
    
    
options = dict(
    name="yewtube",
    version=datetime.utcnow().strftime('%y.%m.%d'),
    description="A Terminal based YouTube player and downloader. No Youtube API key required. Forked from mps-youtube",
    keywords=["video", "music", "audio", "youtube", "stream", "download"],
    author="talha_programmer",
    author_email="talhaasghar.contact@simplelogin.fr",
    url="https://github.com/iamtalhaasghar/yewtube",
    download_url="https://github.com/iamtalhaasghar/yewtube/releases",
    packages=['mps_youtube', 'mps_youtube.commands', 'mps_youtube.listview', 'mps_youtube.players'],
    entry_points={'console_scripts': ['yt = mps_youtube:main.main']},
    python_requires='>=3.6',
    install_requires=[
        'pyreadline ; platform_system=="Linux"',
        'pyreadline3 ; platform_system=="Windows"',
        'pyperclip',
        'youtube-search-python',
        'yt-dlp',
    ],
    classifiers=[
        "Topic :: Utilities",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Multimedia :: Sound/Audio :: Players",
        "Topic :: Multimedia :: Video",
        "Environment :: Console",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS 9",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows XP",
        "Operating System :: Microsoft :: Windows :: Windows Vista",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    options={
        "py2exe": {
            "excludes": ("readline, win32api, win32con, dbus, gi,"
                         " urllib.unquote_plus, urllib.urlencode,"
                         " PyQt4, gtk"),
            "bundle_files": 1
        }
    },
    package_data={"": ["LICENSE", "README.md", "CHANGELOG"]},
    #long_description_content_type='text/markdown',
    long_description="Will be added soon. Meanwhile check this out https://github.com/iamtalhaasghar/yewtube"
)

if sys.platform.startswith('linux'):
    # Install desktop file. Required for mpris on Ubuntu
    options['data_files'] = [('share/applications/', ['yewtube.desktop'])]

if os.name == "nt":
    try:
        import py2exe
        # Only setting these when py2exe imports successfully prevents warnings
        # in easy_install
        options['console'] = ['yt']
        options['zipfile'] = None
    except ImportError:
        pass

setup(**options)
