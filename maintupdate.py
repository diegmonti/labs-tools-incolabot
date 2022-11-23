# -*- coding: utf-8 -*-

import pywikibot
import csv

site = pywikibot.Site('it', 'wikipedia')

with open('/data/project/maintgraph/bot.csv', 'r') as f:
    reader = csv.reader(f)
    line = next(reader)

page = pywikibot.Page(site, u"Template:Situazione_lavoro_sporco/Controllare_copyright")
page.put(line[5], u"Bot: aggiorno statistiche manutenzioni")

page = pywikibot.Page(site, u"Template:Situazione_lavoro_sporco/Verificare_enciclopedicità")
page.put(line[8], u"Bot: aggiorno statistiche manutenzioni")

page = pywikibot.Page(site, u"Template:Situazione_lavoro_sporco/Aiutare")
page.put(line[2], u"Bot: aggiorno statistiche manutenzioni")

page = pywikibot.Page(site, u"Template:Situazione_lavoro_sporco/Pagine_orfane")
page.put(line[12], u"Bot: aggiorno statistiche manutenzioni")

page = pywikibot.Page(site, u"Template:Situazione_lavoro_sporco/Voci_non_neutrali")
page.put(line[22], u"Bot: aggiorno statistiche manutenzioni")

page = pywikibot.Page(site, u"Template:Situazione_lavoro_sporco/Senza_fonti")
page.put(line[14], u"Bot: aggiorno statistiche manutenzioni")

page = pywikibot.Page(site, u"Template:Situazione_lavoro_sporco/Controllare")
page.put(line[4], u"Bot: aggiorno statistiche manutenzioni")

page = pywikibot.Page(site, u"Template:Situazione_lavoro_sporco/Wikificare")
page.put(line[24], u"Bot: aggiorno statistiche manutenzioni")

page = pywikibot.Page(site, u"Template:Situazione_lavoro_sporco/Unire")
page.put(line[21], u"Bot: aggiorno statistiche manutenzioni")

page = pywikibot.Page(site, u"Template:Situazione_lavoro_sporco/Tradurre")
page.put(line[20], u"Bot: aggiorno statistiche manutenzioni")

page = pywikibot.Page(site, u"Template:Situazione_lavoro_sporco/Stub")
page.put(line[18], u"Bot: aggiorno statistiche manutenzioni")

page = pywikibot.Page(site, u"Template:Situazione_lavoro_sporco/Aggiungere_template")
page.put(line[1], u"Bot: aggiorno statistiche manutenzioni")

page = pywikibot.Page(site, u"Template:Situazione_lavoro_sporco/Categorizzare")
page.put(line[3], u"Bot: aggiorno statistiche manutenzioni")

page = pywikibot.Page(site, u"Template:Situazione_lavoro_sporco/Correggere")
page.put(line[6], u"Bot: aggiorno statistiche manutenzioni")

page = pywikibot.Page(site, u"Template:Situazione_lavoro_sporco/Localismo")
page.put(line[10], u"Bot: aggiorno statistiche manutenzioni")

page = pywikibot.Page(site, u"Template:Situazione_lavoro_sporco/Organizzare")
page.put(line[11], u"Bot: aggiorno statistiche manutenzioni")
