#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from shutil import move
import re
import os
dirc = '/home/muna/opensooq/pwa/httpdocs/os_web/web/themes/pwa/js/components'
file = open('/home/muna/opensooq/pwa/httpdocs/os_web/web/themes/pwa/js/translations/NewTranslation.i18n.js', 'r')
pat = re.compile(r'\s+[A-Za-z0-9\_]+\:\s*(.*)+')
def thru(dirf, fname, val, key):
	tmpd = dirf.replace('pwa', 'v2', 1)
	if not os.path.exists(tmpd):
		os.makedirs(tmpd)
	tmpf = tmpd+'/'+fname
	fname = dirf+'/'+fname
	changed = False
	with open(tmpf, 'w+') as outf:
		with open(fname, 'r+') as inf:
			for line in inf:
				if val not in ['', ' ', '\n'] and ('Helpers.t("'+val+'"' in line or "Helpers.t('"+val+"'" in line):
					line = line.replace(val, key)
					changed = True
				outf.write(line)
	if changed:
		move(tmpf, fname)

def crawl(dirc):
	for fname in os.listdir(dirc):
		if fname.endswith(".js"):
			thru(dirc, fname, val, key)
		else:
			dirk = dirc+'/'+fname
			crawl(dirk)

for line in file:
	m = pat.match(line)
	if (m != None):
		line = m.group()
		val = re.sub(r'\s+[A-Za-z0-9\_]+\:\s*[\'\"]', '', line)
		val = re.sub(r'[\'\"]\,*', '', val)
		key = re.sub(r'(\:.*)', '', line)
		key = re.sub(r'\s+', '', key)
		crawl(dirc)