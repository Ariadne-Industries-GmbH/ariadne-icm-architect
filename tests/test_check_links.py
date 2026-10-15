"""Focused smoke tests for the workspace link checker."""

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / 'assets' / 'templates' / 'check_links.py'
spec = importlib.util.spec_from_file_location('check_links', SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class LinkCheckerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / 'docs').mkdir()
        (self.root / 'docs' / 'requirements.md').write_text(
            '| Key | Requirement |\n|---|---|\n| [[B1]] | The user can sign in. |\n', encoding='utf-8'
        )

    def tearDown(self):
        self.temp.cleanup()

    def write(self, content):
        (self.root / 'implementation.md').write_text(content, encoding='utf-8')
        return checker.check(self.root)[0]

    def test_real_relative_link(self):
        self.assertEqual([], self.write('Read [Requirements](docs/requirements.md).'))

    def test_virtual_wikilink_requires_no_page(self):
        self.assertEqual([], self.write('Implement [[B1]]; no B1.md file exists.'))

    def test_missing_file_is_error(self):
        self.assertTrue(any('missing link target' in x for x in self.write('Read [Other](docs/other.md).')))

    def test_external_link_is_allowed(self):
        self.assertEqual([], self.write('[External](https://example.org)'))

    def test_link_with_fragment(self):
        self.assertEqual([], self.write('[Requirements](docs/requirements.md#key)'))

    def test_backticked_example_ignored(self):
        self.assertEqual([], self.write('Example: `[Link](does-not-exist.md)`'))

    def test_fenced_example_ignored(self):
        self.assertEqual([], self.write('```markdown\n[Link](does-not-exist.md)\n```'))

    def test_relative_link_cannot_escape_workspace(self):
        self.assertTrue(any('escapes workspace' in x for x in self.write('[Outside](../outside.md)')))

    def test_root_absolute_link_is_error(self):
        self.assertTrue(any('non-relative file link' in x for x in self.write('[Absolute](/docs/requirements.md)')))


if __name__ == '__main__':
    unittest.main()
