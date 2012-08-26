import unittest2 as unittest
import os
import tempfile
import shutil

from scripttest import TestFileEnvironment


class PyramidTempalteTest(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tempdir)

    def test_everything(self):
        # docs http://pythonpaste.org/scripttest/
        env = TestFileEnvironment(os.path.join(self.tempdir, 'test-output'), ignore_hidden=False)
        root_dir = os.path.join(os.path.dirname(__file__), '../', '../',)
        result = env.run('%s/bin/paster create -t pyramid proj --no-interactive' % root_dir)
        self.assertEqual(
            set(result.files_created.keys()),
            set([
                'proj',
                'proj/bootstrap.py',
                'proj/buildout.cfg',
                'proj/buildout.d',
                'proj/buildout.d/base.cfg',
                'proj/buildout.d/development.cfg',
                'proj/buildout.d/production.cfg',
                'proj/buildout.d/staging.cfg',
                'proj/buildout.d/versions.cfg',
                'proj/docs',
                'proj/docs/api.rst',
                'proj/docs/conf.py',
                'proj/docs/glossary.rst',
                'proj/docs/index.rst',
                'proj/docs/intro.rst',
                'proj/etc',
                'proj/etc/development.ini.in',
                'proj/etc/nginx.conf.in',
                'proj/etc/production.ini.in',
                'proj/.gitignore',
                'proj/HISTORY.rst',
                'proj/LICENSE',
                'proj/MANIFEST.in',
                'proj/.pep8',
                'proj/pre-commit-check.sh',
                'proj/README.rst',
                'proj/setup.cfg',
                'proj/setup.py',
                'proj/src',
                'proj/src/proj',
                'proj/src/proj.egg-info',
                'proj/src/proj.egg-info/dependency_links.txt',
                'proj/src/proj.egg-info/entry_points.txt',
                'proj/src/proj.egg-info/not-zip-safe',
                'proj/src/proj.egg-info/paster_plugins.txt',
                'proj/src/proj.egg-info/PKG-INFO',
                'proj/src/proj.egg-info/requires.txt',
                'proj/src/proj.egg-info/SOURCES.txt',
                'proj/src/proj.egg-info/top_level.txt',
                'proj/src/proj/__init__.py',
                'proj/src/proj/site',
                'proj/src/proj/site/__init__.py',
                'proj/src/proj/site/models.py',
                'proj/src/proj/site/static',
                'proj/src/proj/site/templates',
                'proj/src/proj/site/templates/index.jinja2',
                'proj/src/proj/site/tests',
                'proj/src/proj/site/tests.py',
                'proj/src/proj/site/tests/__init__.py',
                'proj/src/proj/site/tests/test_views.py',
                'proj/src/proj/site/views.py',
                'proj/src/proj/testing.py',
                'proj/src/proj/tests.py',
                'proj/.travis.yml',
                ])
        )

        env.run('python bootstrap.py',
                cwd=os.path.join(env.cwd, 'proj'),
                expect_stderr=True)
        env.run('bin/buildout',
                cwd=os.path.join(env.cwd, 'proj'),
                expect_stderr=True)
        env.run('./pre-commit-check.sh',
                cwd=os.path.join(env.cwd, 'proj'),
                expect_stderr=True)
