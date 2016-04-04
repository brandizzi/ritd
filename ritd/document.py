# !/usr/bin/env python
#
# Copyright 2016 Adam Victor Brandizzi
#
# This file is part of Rain in the Desert.
#
# Rain in the Desert is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# Rain in the Desert is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Rain in the Desert. If not, see <http://www.gnu.org/licenses/>.

from xml.etree.ElementTree import fromstring, tostring
from collections import defaultdict

class Document(object):

    def __init__(self, content):
        self.content = content
        self.id_map = {}
        self.class_map = defaultdict(list)
        self.tree = fromstring(content)
        for e in self.tree.iter():
            eid = e.attrib.get('id')
            if eid:
                self.id_map[eid] = e

            eclass = e.attrib.get('class')
            if eclass:
                self.class_map[eclass].append(e)

    def fill(self, value, cssId=None, cssClass=None):
        if cssId is not None:
            self.id_map[cssId].text = value
        if cssClass is not None:
            for e in self.class_map[cssClass]:
                e.text = value

    def tostring(self):
        return tostring(self.tree)
