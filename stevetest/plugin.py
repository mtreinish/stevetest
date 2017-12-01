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

import abc

import six
import stevedore


def singleton(cls):
    """Simple wrapper for classes that should only have a single instance."""
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@six.addmetaclass(abc.ABCMeta)
class Plugin(object):
    """Provide a hook to enable stevetest to load a unittest"""

    @abc.abstractmethod
    def load_tests(self):
        """Return the information necessary to load the tests in the plugin.

        :return: a tuple with the first value being the test_dir and the second
                 being the top_level
        :rtype: tuple
        """
        return


@singleton
class PluginManager(object):
    def __init__(self):
        self.ext_plugins = stevedore.ExtensionManager(
            'stevetest.test_plugins', invoke_on_load=True,
            propagate_map_exceptions=True,
            on_load_failure_callback=self.failure_hook)

    @staticmethod
    def failure_hook(_, ep, err):
        print('Could not load %r: %s', ep.name, err)
        raise err
