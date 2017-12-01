# This file is part of stevetest
#
# stevetest is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# stevetest is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with stevetest. If not, see <http://www.gnu.org/licenses/>

import unittest2 as unittest

from stevetest import plugin


def load_tests(loader, test, pattern):
    plugins = plugin.PluginManager()
    suite = unittest.TestSuite()
    plugin_load_tests = plugins.get_plugin_load_tests_tuple()

    # Load any installed plugin tests
    for suite in plugin_load_tests:
        test_dir, top_path = plugin_load_tests[suite]
        if not pattern:
            suite.addTests(loader.discover(test_dir, top_level_dir=top_path))
        else:
            suite.addTests(loader.discover(test_dir, pattern=pattern,
                                           top_level_dir=top_path))
    return suite
