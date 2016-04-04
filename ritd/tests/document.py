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

import unittest
import textwrap

from ritd.document import Document


class TestDocument(unittest.TestCase):
    """
    Tests methods from the Document class.
    """

    def test_fill_id(self):
        """
        One can fill an element by id.
        """
        html = textwrap.dedent(
            """\
            <html>
                <body>
                    <div id="div1">test</div>
                    <div id="div2">test</div>
                </body>
            </html>"""
        )

        doc = Document(html)
        doc.fill(cssId='div1', value='REPLACEMENT')

        self.assertEquals(
            doc.tostring(),
            textwrap.dedent("""\
                <html>
                    <body>
                        <div id="div1">REPLACEMENT</div>
                        <div id="div2">test</div>
                    </body>
                </html>"""
            )
        )
