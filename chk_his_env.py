import os
import glob
import credentials as cred
from os.path import expanduser, expandvars

import requests
import string


GM_U = cred.GM_U
GM_PW = cred.GM_PW
L_RECIPIENTS = cred.L_RECIPIENTS


L_YIELD_VCB = ['gov.gov.gov.il'
               # , 'finance.yahoo'
               # , 'finance.yaho'
               # , 'icar.co.il'
               # , 'investing.com'
               #
               # , 'cet.ac.il'
               # , 'edu.gov.il'
               # , 'zoom.us'
               # , 'accounts.google.co'
               # , 'mail.google.co'
               # , 'myaccount.google.co'

               ]


#
# TODO: optional - get/chg db location from 'requests' ??

# Windows XP
# C:\Documents and Settings\<username>\Local Settings\Application Data\Google\Chrome\User Data\Default
# C:\Documents and Settings\<username>\Local Settings\Application Data\Google\Chrome\User Data\Default\Cache
# Windows Vista, 7, 8, 10
# C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default
# C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default\Cache
# ['/home/mona/.mozilla/firefox/8r1zqyhx.default/places.sqlite',
#  '/home/mona/.mozilla/firefox/3lfi5dxs.default-release/places.sqlite',
#  '/home/mona/.config/google-chrome/Default/History']
if os.name == 'posix':
    L_HISTORY_DB = glob.glob(expanduser('~/.mozilla/firefox/*/places.sqlite'))          # "*"
                                       # ~/.mozilla/firefox/8r1zqyhx.default/places.sqlite
                                       # ~/.mozilla/firefox/3lfi5dxs.default-release/places.sqlite  <---
    L_HISTORY_DB += glob.glob(expanduser('~/.config/google-chrome/Default/History'))    # glob.glob to make it list elem.~
    L_HISTORY_DB += glob.glob(expanduser('~/.config/opera/History'))                    # glob.glob to make it list elem.~
    # find -L $HOME -maxdepth 3 -name *chromiu* -printf '[%y] %H/%P \n'
    # ~/.cache/ ???
    # find -L /home/mona/snap -maxdepth 5 -name *History* -printf '[%y] %H/%P \n'
    L_HISTORY_DB += glob.glob(expanduser('~/snap/chromium/common/chromium/Default/History'))
    L_HISTORY_DB += glob.glob(expanduser('~/.config/chromium/History'))
else:
    # TODO: Internet Explorer DB file ???
    # TODO: path of different windows version ???
    L_HISTORY_DB = glob.glob(expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\Default\History'))
    L_HISTORY_DB += glob.glob(expanduser(r'%LOCALAPPDATA%\Mozilla\Firefox\*\places.sqlite'))
#  ___________________%LOCALAPPDATA%\Google\Chrome\User Data
#  C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default
# from os import path
# sendto_dir = path.expandvars(r'%APPDATA%\Microsoft\Windows\SendTo')
# opera history windows: https://i.imgur.com/DrZWnvB.jpg


#
# without 'where':
# SELECT datetime(last_visit_time/1000000-11644473600, "unixepoch") as last_visited,
SQL_QUERY_SELECT_CHROME = \
    '''
         SELECT datetime(last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime')
                ,url
           FROM urls; 
    '''

SQL_QUERY_SELECT_FIREFOX = \
    '''
       SELECT --*
        datetime(a.visit_date/1000000, 'unixepoch', 'localtime') AS visit_date, 
        b.url 
      FROM moz_historyvisits a,     --AS a --JOIN 
           moz_places b             --AS b 
        ON a.place_id   = b.id 
    '''
# TODO: Internet Explorer query ???


EMAIL_TEXT = """\
From: %s
To: %s
Subject: %s

%s
"""


def get_yield_vcb():
    log_ref = '***get yield vcb***'
    l_yield_vcb = []

    try:
        # r = requests.get('http://localhost:5000/get_info/1', data = {'key':'value'})
        # https://requests.readthedocs.io/en/master/user/quickstart/
        # r = requests.get('http://localhost:5000/get_yield')
        r = requests.get(cred.YIELD_HOST)                 # returns jsonify(l_yield_vcb) <--- ['gov.il', ... ]
        # print(r.status_code)
        # print(r.text)
        # print(type(r.json()))                           # ==> r.json will receive the type from server was jsonify-ed
        # a=r.text
        # d_translation = a.maketrans('', '', ']["')      # maketrans ---> {93: None, 91: None, 34: None}
        # line = a.translate(d_translation)               # '["gov.il","abc","eddu"]' ---> 'gov.il,abc,eddu'

        if r.status_code is 200 and type(r.json()) is list:
            l_yield_vcb += r.json()

    except Exception as e:
        print('%s %s' % (log_ref, e))

    return l_yield_vcb


