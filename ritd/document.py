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


class Document(object):

    def __init__(self, content):
        self.content = content
        self.id_map = {}
        self.tree = fromstring(content)
        for e in self.tree.iter():
            eid = e.attrib.get('id')
            if eid:
                self.id_map[eid] = e

    def fill(self, value, cssId=None):
        self.id_map[id].text = value

    def tostring(self):
        return tostring(self.tree)
