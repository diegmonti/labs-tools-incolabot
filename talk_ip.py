# -*- coding: utf-8  -*-

#
# Modified from: https://it.wikipedia.org/wiki/Utente:BimBot/Scripts#discussioneanonimi3.py
#

import pywikibot
import re
import subprocess

from pywikibot import pagegenerators
from time import *

start = time()
site = pywikibot.Site('it', 'wikipedia')


def main():
    subprocess.check_call('mysql --defaults-file=~/replica.my.cnf -h ' +
                          'itwiki.analytics.db.svc.eqiad.wmflabs -BN < talk_ip.sql > talk_ip.out', shell=True)

    talkpages = pagegenerators.TextfilePageGenerator('talk_ip.out')
    for talk in talkpages:
        static = False
        if talk.namespace() != 3 or not talk.exists() or not talk.canBeEdited():
            continue
        pywikibot.output("\n>>>>> " + talk.title() + " <<<<<")

        oldtext = talk.get()

        if checkStatic(talk.title(withNamespace=False)):
            newtext = u'{{IPcondiviso}}\n' + oldtext
            talk.put(
                newtext, u'Bot: aggiungo template IPcondiviso ([[Utente:IncolaBot/FAQ|FAQ]])')
        else:
            newtext = u'{{BenvenutoIP}}'
            talk.put(
                newtext, u'Bot: aggiungo template BenvenutoIP ([[Utente:IncolaBot/FAQ|FAQ]])')


def checkStatic(ip):
    response = subprocess.check_output(('dig', '-x', ip, '+short'))
    pywikibot.output('Dig response: ' + response)
    return bool(re.search('[Ss]tatic', response))


if __name__ == "__main__":
    try:
        main()
    finally:
        end = time()
        print "Run time: ", end-start
