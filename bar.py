# -*- coding: utf-8 -*-

#
# (C) Lorenzo Paulatto, 2006
#
# Distributed under the terms of the MIT license.
#
# Modified from: https://it.wikipedia.org/wiki/Utente:.snoopy./bar.py
#

__version__='$Id:'

import os, pywikibot
import re, sys, codecs
from time import *

os.environ['TZ'] = 'Europe/Rome'
inizio=time()

# Global variables
titlelistAux = []

def findtitle(t):
    search_string = "(?m)\{\{[Bb]ar\d\/Segnala(disc|est)\|([^|}\n]*)(}}|\|)([^|}\n]*)"
    try:
        location = re.search(search_string, t)
        kind  = location.group(1)
        link  = location.group(2)
        name  = location.group(4)
    #print "INIZIO:"+kind +" (2: " +title +" (4: " + name + " :FINE"
    except AttributeError:
        #pywikibot.output(u"End of file reached.")
        return
    else:
        if kind == "disc":
            title = "[[Wikipedia:Bar/Discussioni/" +link + "|" + link +"]]"
        #elif kind == "cambusa":
        #title = "[[Wikipedia:Bar/Discussioni/" +link + "|" + link +"]] <small>(cambusata)</small>"
        elif kind == "est":
            if name == "":
                title = "{{Bar3/esterna|" + link + "}}"
            else:
                title = "{{Bar3/esterna|" + link + "|" + name + "}}"
        else:
            title = "C'è un problema..."
        #pywikibot.output(u"* "+title)
        old = re.compile(u"(\[\[|\|)")
        if old.search(link):
            pywikibot.output("Ho trovato un titolo non valido: "+link)
            title = """<span style="color:#999999;">''(titolo non valido)''</span>"""
        titlelistAux.append(title)
    findtitle(t[location.end()+1:])
    return titlelistAux

# ################################################################ #
def main():
    # Time data initialize
    # Tuple format: (YYYY, M, D, h, m, s, day, ?)
    theTime = time()
    siad = 24*60*60 # = Seconds In A Day

    # Loop unrolled for lazier programming
    #days = []
    #days.append(time.gmtime(theTime))        # <-- UTC time!
    #days.append(time.gmtime(theTime-siad))   # yesterday
    #days.append(time.gmtime(theTime-2*siad)) # two days ago
    #days.append(time.gmtime(theTime-3*siad)) # ...
    #days.append(time.gmtime(theTime-4*siad))
    #days.append(time.gmtime(theTime-5*siad))
    #days.append(time.gmtime(theTime-6*siad))

    for i in range(0,6+1):
        day = localtime(theTime-i*siad)
        y = str(day[0])
        m = str(day[1]).zfill(2)
        d = str(day[2]) #.zfill(2)

        titlelist = [] # re-initialize aux list
        del titlelistAux[:]
        text = ""

        pageTitle="Wikipedia:Bar/"+y+"_"+m+"_"+d
        page = pywikibot.Page(site, pageTitle)
        pywikibot.output(u"* "+pageTitle)
        if page.exists():
            text = page.get()                # get the page text
            titlelist = findtitle(text)      # parse the text
        else:
            titlelist = None
            pywikibot.output(u"La pagina "+pageTitle+" non esiste!")
        #genURL="http://it.wikipedia.org/w/index.php?title="+pageTitle+"&action=edit&section=new&preload=template:Bar7/standard"
        #titlelist=["""'''La pagina di discussione di oggi non esiste ancora, per crearla ["""+genURL+""" premi qui]'''"""]
        #continue
        #titlelist = findtitle(text)      # parse the text
        pageTitle = "Template:Bar3/titoli/" + str(i)
        abstract = pywikibot.Page(site, pageTitle)
        if abstract.exists():
            contentsOld = abstract.get()
        else:
            contentsOld = ""
        #
        try:
            titlenum = len(titlelist)
        except TypeError:
            #contents = ""
            #genURL="http://it.wikipedia.org/w/index.php?title="+pageTitle+"&action=edit&section=new&preload=template:Bar7/standard"
            #contents="""<dl><dd>'''La pagina di discussione di oggi non esiste ancora, per crearla ["""+genURL+""" premi qui]'''</dd></dl>"""
            contents="<dl><dd>''Nessuna discussione.''</dd></dl>"
        else:
            contents = "<dl><dd>"
            for j in range(0,titlenum):
                #contents = contents + "[[Wikipedia:Bar/Discussioni/" + titlelist[j] +"|"+titlelist[j]+"]]" + " &middot; "
                contents = contents + titlelist[j] + " &middot; "
            contents = contents[:(len(contents)-10)] + "</dd></dl>"
        #
        if contents != contentsOld:
            abstract.put(contents, comment = commenttext, minorEdit = False)
        else:
            pywikibot.output(u"Aggiornamento non necessario")

    return

site = pywikibot.Site('it', 'wikipedia')
commenttext = "Bot: aggiorno gli estratti delle discussioni al Bar"
if __name__ == "__main__":
    try:
        main()
    finally:
        fine=time()
        print " Tempo di esecuzione della procedura= ", fine-inizio
        print " Ora dell'ultimo aggiornamento: ", ctime(time())
