#!/usr/bin/env python
import scrap

lines = scrap.scrap_quotes('astronomy')
for line in lines:
    print(type(lines[0].get_text()))

