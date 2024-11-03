#!/usr/bin/python3
"""Markdown file"""
import sys
import os


if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    sys.exit(1)
if not os.path.isfile(sys.argv[1]):
    sys.stderr.write(f"Missing {sys.argv[1]}")
    sys.exit(1)

sys.exit(0)
