# -*- coding: utf-8  -*-

#
# Modified from: https://it.wikipedia.org/wiki/Utente:BimBot/Scripts#discussioneanonimi3.py
#

import pymysql
import pywikibot
import re
import socket
import subprocess

from pywikibot import pagegenerators
from pywikibot.exceptions import LockedPageError
from time import *

start = time()
site = pywikibot.Site('it', 'wikipedia')


def run_query(input_file, output_file):
    with open(input_file, "r") as f:
        query = f.read()
    
    db = pymysql.connect(
        read_default_file="~/replica.my.cnf",        
        host="itwiki.analytics.db.svc.eqiad.wmflabs",
        database="itwiki_p"
    )
    
    cursor = db.cursor()
    cursor.execute(query)
    
    results = cursor.fetchall()
    
    db.close()
    
    with open(output_file, "w") as f:
        for result in results:
            f.write(result[0].decode('utf-8') + "\n")


def reverse_hostname(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
    except socket.error:
        return ""
    return hostname


def check_static(ip):
    response = reverse_hostname(ip)
    pywikibot.output('Dig response: ' + response)
    return bool(re.search('[Ss]tatic', response))


def main():
    run_query("talk_ip.sql", "talk_ip.out")

    talkpages = pagegenerators.TextIOPageGenerator('talk_ip.out')
    for talk in talkpages:

        if talk.namespace() != 3 or not talk.exists() or not talk.botMayEdit():
            continue

        pywikibot.output("\n>>>>> " + talk.title() + " <<<<<")

        oldtext = talk.get()

        try:
            if check_static(talk.title(with_ns=False)):
                newtext = u'{{IPcondiviso}}\n' + oldtext
                talk.put(
                    newtext, u'Bot: aggiungo template IPcondiviso ([[Utente:IncolaBot/FAQ|FAQ]])')
            else:
                newtext = u'{{BenvenutoIP}}'
                talk.put(
                    newtext, u'Bot: aggiungo template BenvenutoIP ([[Utente:IncolaBot/FAQ|FAQ]])')
        except LockedPageError:
            continue


if __name__ == "__main__":
    try:
        main()
    finally:
        end = time()
        print("Run time:", end-start)
