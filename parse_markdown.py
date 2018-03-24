#!/usr/bin/env python

import argparse
import sys

import jinja2
import markdown

import os
import io

TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.0/css/bootstrap-combined.min.css" rel="stylesheet">
    <style>
        body {
            font-family: sans-serif;
        }
        code, pre {
            font-family: monospace;
            }
            h1 code,
            h2 code,
            h3 code,
            h4 code,
            h5 code,
            h6 code {
                font-size: inherit;
        }
        div {
            margin-right: 400px;
            margin-left: 400px;
        }
    </style>
</head>
<body>
<div class="container">
{{content}}
</div>
</body>
</html>
"""

def parse_args(args=None):
    d = 'Make a complete, styled HTML document from a Markdown file.'
    parser = argparse.ArgumentParser(description=d)
    parser.add_argument('mdfile', type=argparse.FileType('r'), nargs='?',
                        default=sys.stdin,
                        help='File to convert. Defaults to stdin.')
    parser.add_argument('-o', '--out', type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='Output file name. Defaults to stdout.')
    return parser.parse_args(args)


def main(args=None):
    args = parse_args(args)
    # md = args.mdfile.read()

    md = ''
    for fname in os.listdir('biases'):
        path = os.path.join('biases', fname)
        print(path)
        with io.open(path, encoding="utf-8") as f:
            md += '\n<h1>  {}</h1>'.format(fname[:-3].replace('-', ' ').title())
            md += f.read()
            md += '\n<hr>'
    print('Done')

    extensions = ['extra', 'smarty']
    html = markdown.markdown(md, extensions=extensions, output_format='html5')
    doc = jinja2.Template(TEMPLATE).render(content=html)
    args.out.write(doc)


if __name__ == '__main__':
    sys.exit(main())