=========
stevetest
=========

Stevetest is a stevedore based python unittest loader. It enables you to
integrate any `unittest`_ based python test suite into a single entrypoint.

.. _unittest: https://docs.python.org/3/library/unittest.html

Creating a plugin
-----------------

Creating a plugin is fairly straightforward and doesn't require much additional
effort on top of creating a test suite. All you need to do is crate a plugin
class that inherits from the ``stevetest.plugin.Plugin`` abstract class and
define the load_tests method on the class.

Then you just expose the setuptools entry point in the
``stevetest.test_plugins`` namespace. If you are using `pbr`_ this is fairly
straightforward, in the setup.cfg just add something like the following:

.. _pbr: https://docs.openstack.org/pbr/latest/

.. code-block:: ini

  [entry_points]
  stevetest.test_plugins =
      plugin_name = module.path:PluginClass

Running tests with stevedore
----------------------------

To run tests with stevedore just have your test runner run the
``stevetest.test_discovery`` module. (or optionally run discovery on the whole
package) This will trigger the load_tests hook and pull in all the installed
plugins and run the tests.
