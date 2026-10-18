#!/usr/bin/env python3
"""Check navigable relative Markdown file links within an ICM workspace.

Wikilinks are intentionally not checked for matching files: [[Term]] groups
occurrences of a shared concept and need not have a definition or page.
No external dependencies.
"""

import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

# Inline Markdown links, not image links. Reference-style links are outside scope.
LINK = re.compile(r'(?<!!)\[[^\]\n]+\]\((<[^>]+>|[^\s)]+)(?:\s+["\'][^\n]*?["\'])?\)')
FENCE = re.compile(r'^\s{0,3}(`{3,}|~{3,})')
INLINE_CODE = re.compile(r'(`+)(.*?)\1')
EXTERNAL = re.compile(r'^[a-zA-Z][a-zA-Z0-9+.-]*:')


def markdown_lines(path):
    fenced = None
    for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        match = FENCE.match(line)
        if match:
            token = match.group(1)
            if fenced is None:
                fenced = token
            elif token[0] == fenced[0] and len(token) >= len(fenced):
                fenced = None
            continue
        if fenced is None:
            yield number, INLINE_CODE.sub('', line)


def check(root):
    root = root.resolve()
    errors, scanned, total_links = [], 0, 0
    for source in sorted(root.rglob('*.md')):
        if any(part in {'.git', 'node_modules', '.venv'} for part in source.relative_to(root).parts):
            continue
        scanned += 1
        for number, line in markdown_lines(source):
            for match in LINK.finditer(line):
                target = match.group(1).strip('<>')
                if not target or target.startswith('#') or EXTERNAL.match(target):
                    continue
                total_links += 1
                path_part = unquote(urlsplit(target).path)
                if not path_part:
                    continue
                if path_part.startswith('/') or re.match(r'^[a-zA-Z]:[\\/]', path_part):
                    errors.append(f'{source.relative_to(root)}:{number}: non-relative file link: {target}')
                    continue
                destination = (source.parent / path_part).resolve()
                if not destination.is_relative_to(root):
                    errors.append(f'{source.relative_to(root)}:{number}: link escapes workspace: {target}')
                elif not destination.exists():
                    errors.append(f'{source.relative_to(root)}:{number}: missing link target: {target}')
    return errors, scanned, total_links


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workspace', nargs='?', default='.', type=Path)
    args = parser.parse_args()
    if not args.workspace.is_dir():
        parser.error('workspace must be an existing directory')
    errors, files, links = check(args.workspace)
    for error in errors:
        print('ERROR:', error)
    print(f'Checked {links} relative file links across {files} Markdown files; {len(errors)} error(s).')
    print('Note: [[wikilinks]] are semantic references; missing definitions or pages are allowed.')
    print('Unmarked cross-file terms and conflicting meanings require a semantic review.')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
