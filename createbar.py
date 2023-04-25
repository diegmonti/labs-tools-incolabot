# -*- coding: utf-8 -*-

#
# Modified by Ricordisamoa: https://it.wikipedia.org/wiki/Utente:Ricordisamoa/createbar.py
#

##
# 23.00 UTC -> 0.00 CET
# 22.00 UTC -> 0.00 CEST
##

import os
import time
import pywikibot

os.environ['TZ'] = 'Europe/Rome'
time.tzset()

monthConv = {
    1: 'gennaio',
    2: 'febbraio',
    3: 'marzo',
    4: 'aprile',
    5: 'maggio',
    6: 'giugno',
    7: 'luglio',
    8: 'agosto',
    9: 'settembre',
    10: 'ottobre',
    11: 'novembre',
    12: 'dicembre',
}

site = pywikibot.Site('it', 'wikipedia')

curYear = time.strftime("%Y")
curMonth = time.strftime("%m")
curDay = str(int(time.strftime("%d")))

def create_only(page, text, summary):
    if not page.exists():
        page.text = text
        page.save(summary)
    else:
        pywikibot.output("{} already exists: skip.".format(page))

pageBarTitle = pywikibot.Page(site, "Wikipedia:Bar/{anno} {mese} {giorno}".format(anno=curYear, mese=curMonth, giorno=curDay))
pageBarText = ("<noinclude>{{{{Bar7/light}}}}\n={giorno} {mese}=\n__TOC__\n[[Categoria:Wikipedia Bar - {giorno} {mese} {anno}]]\n"
               "[[Categoria:Archivio bar]]\n</noinclude>"
               ).format(giorno=curDay, mese=monthConv[int(curMonth)], anno=curYear)

create_only(pageBarTitle, pageBarText, u"Bot: creo sottopagina del bar odierno")

dayCatTitle = pywikibot.Category(site, "Wikipedia Bar - {giorno} {mese} {anno}".format(anno=curYear, mese=monthConv[int(curMonth)], giorno=curDay))
dayCatText = "[[Categoria:Wikipedia Bar - {mese} {anno}]]".format(anno=curYear, mese=monthConv[int(curMonth)])

create_only(dayCatTitle, dayCatText, u"Bot: creo categoria del bar odierno")

monthCatTitle = pywikibot.Category(site, "Wikipedia Bar - " + monthConv[int(curMonth)] + ' ' + curYear)
monthCatText = "[[Categoria:Wikipedia Bar - Archivi per mese " + curYear + "| " + curMonth + "]]"

create_only(monthCatTitle, monthCatText, u"Bot: creo categoria mensile del bar")

yearCatTitle = pywikibot.Category(site, "Wikipedia Bar - Archivi per mese " + curYear)
yearCatText = ("In questa categoria sono raggruppate le categorie che raccolgono tutte le sottopagine del bar di uno stesso mese del {anno}. "
               "Ogni categoria mensile contiene le categorie giornaliere, che contengono le pagine giornaliere e tutte le sottopagine di "
               "discussione del giorno.\n\n[[Categoria:Wikipedia Bar - Archivi per mese| {anno}]]"
               ).format(anno=curYear)

create_only(yearCatTitle, yearCatText, u"Bot: creo categoria annuale del bar")

weekCatTitle = pywikibot.Category(site, "Wikipedia Bar - Archivio" + time.strftime(" %G-") + str(int(time.strftime("%V"))))
weekCatText = "[[Categoria:Wikipedia Bar - Archivi per settimana " + time.strftime("%G") + "]]"

create_only(weekCatTitle, weekCatText, u"Bot: creo categoria settimanale del bar")

weekYearCatTitle = pywikibot.Category(site, "Wikipedia Bar - Archivi per settimana" + time.strftime(" %G"))
weekYearCatText = ("In questa categoria sono raggruppate le categorie che raccolgono tutte le sottopagine del bar di una stessa settimana del {anno}. "
                   "Ogni categoria settimanale contiene direttamente ogni sottopagina di discussione della settimana corrispondente.\n\n"
                   "[[Categoria:Wikipedia Bar - Archivi per settimana| {anno}]]"
                   ).format(anno=time.strftime("%G"))

create_only(weekYearCatTitle, weekYearCatText, u"Bot: creo categoria annuale del bar")
