# -*- coding: utf-8  -*-

#
# Modified from: https://it.wikipedia.org/wiki/Utente:BimBot/Scripts#discussioneanonimi3.py
#

import pywikibot, re, subprocess
from pywikibot import pagegenerators
from time import *

start=time()

path = '/data/project/lists/output/itwiki/EGO/Discussioni/Discussioni_utenti_anonimi'

ls = subprocess.Popen(('ls', path), stdout=subprocess.PIPE)
fileName = subprocess.check_output(('tail', '-1'), stdin=ls.stdout)
ls.wait()
fullPath = (path + '/' + fileName).rstrip()

args = pywikibot.handleArgs()
site = pywikibot.Site('it', 'wikipedia')

def main():
    talkpages = pagegenerators.TextfilePageGenerator(fullPath)
    for talk in talkpages:
        static=False
        if talk.namespace() != 3 or not talk.exists() or not talk.canBeEdited():
            continue
        pywikibot.output(">>>>> " + talk.title() + " <<<<<")

        oldtext = talk.get()

        if checkStatic(talk.title(withNamespace=False)):
            newtext = oldtext + u'\n[[Categoria:IP statici]]'
            pywikibot.showDiff(oldtext, newtext)
	    pywikibot.setAction(u'Bot: categorizzo in [[:Categoria:IP statici]] ([[Utente:IncolaBot/FAQ|FAQ]])')
            talk.put(newtext)
        else:
            newtext = u'{{BenvenutoIP}}'
            match = re.search("\{\{IPcondiviso.*?\}\}", oldtext)
            if match != None:
                newtext = match.group() + '\n' + newtext
            pywikibot.showDiff(oldtext, newtext)
	    pywikibot.setAction(u'Bot: svuotata pagina ed inserito benvenuto ([[Utente:IncolaBot/FAQ|FAQ]])')
            talk.put(newtext)

def checkStatic(ip):
    response = subprocess.check_output(('dig', '-x', ip, '+short'))
    pywikibot.output('Dig response: ' + response)
    return bool(re.search('[Ss]tatic', response))

if __name__ == "__main__":
    try:
        main()
    finally:
       end=time()
       print "Run time: ", end-start
