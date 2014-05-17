# -*- coding: utf-8  -*-

#
# Modified from: https://it.wikipedia.org/wiki/Utente:BimBot/Scripts#discussioneanonimi3.py
#

import pywikibot, re

args = pywikibot.handleArgs()
site = pywikibot.Site('it', 'wikipedia')

def main():
    talkpages = pywikibot.Page(site, u'Wikipedia:Elenchi generati offline/Discussioni utenti anonimi').linkedPages();
    for talk in talkpages:
        static=False
        if talk.namespace() != 3 or not talk.exists() or not talk.canBeEdited():
            continue
        pywikibot.output(">>>>> " + talk.title() + " <<<<<")

        oldtext = talk.get()

        if checkStatic(talk.titleWithoutNamespace()):
            newtext = oldtext + u'\n[[Categoria:IP statici]]'
            pywikibot.showDiff(oldtext, newtext)
	    pywikibot.setAction(u'Bot: categorizzo in [[:Categoria:IP statici]]')
            talk.put(newtext)
        else:
            newtext = u'{{BenvenutoIP}}'
            match = re.search("\{\{IPcondiviso.*?\}\}", oldtext)
            if match != None:
                newtext = match.group() + '\n' + newtext
            pywikibot.showDiff(oldtext, newtext)
	    pywikibot.setAction(u'Bot: svuotata pagina ed inserito benvenuto')
            talk.put(newtext)

def checkStatic(ip):
    response = commands.getoutput("dig -x " + ip + " +short")
    pywikibot.output('Dig response: ' + response)
    return bool(re.search('[Ss]tatic', response))

if __name__ == "__main__":
    try:
        main()
