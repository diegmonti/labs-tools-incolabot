#!/usr/bin/python
# -*- coding: utf-8  -*-
"""
Orphanize redirects in the category Redirect_da_mantenere_orfani

-delete         Run in the category Redirect_da_orfanizzare_e_cancellare
"""
#
# This script based on disambredir.py, solve_disambiguation.py and fixing_redirect.py
#
# (C) Pywikibot team, 2004-2014
# (C) Incola, 2015
#
# Distributed under the terms of the MIT license.
#
import re
import sys
import pywikibot
from pywikibot import pagegenerators
from pywikibot import i18n

def firstcap(string):
    return string[0].upper() + string[1:]


def treat(text, linkedPage, targetPage, redirect, delete):
    """Based on the method of the same name in solve_disambiguation.py."""
    mysite = pywikibot.Site()
    linktrail = mysite.linktrail()

    # make a backup of the original text so we can show the changes later
    linkR = re.compile(r'\[\[(?P<title>[^\]\|#]*)(?P<section>#[^\]\|]*)?(\|(?P<label>[^\]]*))?\]\](?P<linktrail>' + linktrail + ')')
    curpos = 0
    # This loop will run until we have finished the current page
    while True:
        m = linkR.search(text, pos=curpos)
        if not m:
            break
        # Make sure that next time around we will not find this same hit.
        curpos = m.start() + 1
        # ignore interwiki links and links to sections of the same page
        if m.group('title').strip() == '' or \
           mysite.isInterwikiLink(m.group('title')):
            continue
        else:
            actualLinkPage = pywikibot.Page(targetPage.site, m.group('title'))
            # Check whether the link found is to page.
            if actualLinkPage != linkedPage:
                continue

        # The link looks like this:
        # [[page_title|link_text]]trailing_chars
        page_title = m.group('title')
        link_text = m.group('label')

        # We do not see it
        if link_text and not delete:
            continue

        if not link_text:
            link_text = page_title

        if firstcap(link_text) == redirect.title():
            choice = 'rR'
        else:
            choice = 'y'

        if m.group('section') is None:
            section = ''
        else:
            section = m.group('section')
        trailing_chars = m.group('linktrail')
        if trailing_chars:
            link_text += trailing_chars

        if choice in "uU":
            # unlink - we remove the section if there's any
            text = text[:m.start()] + link_text + text[m.end():]
            continue

        replaceit = choice in "rR"

        # remove preleading ":"
        if link_text[0] == ':':
            link_text = link_text[1:]
        if link_text[0].isupper():
            new_page_title = targetPage.title()
        else:
            new_page_title = targetPage.title()[0].lower() + \
            targetPage.title()[1:]

        # remove preleading ":"
        if new_page_title[0] == ':':
            new_page_title = new_page_title[1:]

        if replaceit and trailing_chars:
            newlink = "[[%s%s]]%s" % (new_page_title, section, trailing_chars)
        elif replaceit or (new_page_title == link_text and not section):
            newlink = "[[%s]]" % new_page_title
        # check if we can create a link with trailing characters instead of a
        # pipelink
        elif len(new_page_title) <= len(link_text) and \
             firstcap(link_text[:len(new_page_title)]) == \
             firstcap(new_page_title) and \
             re.sub(re.compile(linktrail), '', link_text[len(new_page_title):]) == '' and not section:
            newlink = "[[%s]]%s" % (link_text[:len(new_page_title)],
                                    link_text[len(new_page_title):])
        else:
            newlink = "[[%s%s|%s]]" % (new_page_title, section, link_text)
        text = text[:m.start()] + newlink + text[m.end():]
        continue
    return text

pageCache = []


def workon(page, redirect, delete):
    mysite = pywikibot.Site()
    try:
        text = page.get()
    except pywikibot.IsRedirectPage:
        pywikibot.output(u'%s is a redirect page. Skipping' % page.title())
        return
    except pywikibot.NoPage:
        pywikibot.output(u'%s does not exist. Skipping' % page.title())
        return

    links = page.linkedPages()
    if links is None:
        pywikibot.output(u'%s does not have links. Skipping' % page.title())
        return

    for page2 in links:
        if page2 == redirect:
            try:
                target = page2.getRedirectTarget()
            except pywikibot.NoPage:
                try:
                    target = page2.getMovedTarget()
                except (pywikibot.NoPage, pywikibot.BadTitle):
                    continue
            except (pywikibot.Error, pywikibot.SectionError):
                continue
            # no fix to other namespaces
            if not target.namespace() in [0]:
                continue
            try:
                text = treat(text, page2, target, redirect, delete)
            except (pywikibot.Error, ValueError):
                continue
    if text != page.get():
        comment = u'Bot: orfanizzo redirect [[%s]]' % redirect.title()
#        pywikibot.showDiff(page.get(), text)
        try:
#            pywikibot.output(comment)
            page.put(text, comment)
        except pywikibot.Error:
            pywikibot.error(u'Unable to save: %s' % page.title())


def main(*args):
    """
    Process command line arguments and invoke bot.

    @param args: command line arguments
    @type args: list of unicode
    """

    # Process global args and prepare generator args parser
    local_args = pywikibot.handle_args(args)
    genFactory = pagegenerators.GeneratorFactory()

    mysite = pywikibot.Site()
    delete = False
    catName = u'Categoria:Redirect_da_mantenere_orfani'

    for arg in local_args:
        if arg == '-delete':
            catName = u'Categoria:Redirect_da_orfanizzare_e_cancellare'
            delete = True

    cat = pywikibot.Category(pywikibot.Site(), catName)
    gen = pagegenerators.CategorizedPageGenerator(cat)
    gen = pagegenerators.NamespaceFilterPageGenerator(gen, [0])	

    for redirect in pagegenerators.PreloadingGenerator(gen):
        pywikibot.output(u"Working on redirect: %s" % redirect.title())
        gen2 = pagegenerators.ReferringPageGenerator(redirect)
        if delete:
            gen2 = pagegenerators.NamespaceFilterPageGenerator(gen2, [0, 4, 6, 10, 12, 14, 100, 102])
        else:
            gen2 = pagegenerators.NamespaceFilterPageGenerator(gen2, [0, 10])
        for page in pagegenerators.PreloadingGenerator(gen2):
            pywikibot.output(u"Working on page: %s" % page.title())
            workon(page, redirect, delete)

if __name__ == "__main__":
    main()
