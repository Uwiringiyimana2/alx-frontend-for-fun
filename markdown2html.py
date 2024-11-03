#!/usr/bin/python3
"""Markdown file"""
import sys
import os


if __name__ == "__main__":
    '''the number of arguments is less than 2'''
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    if not os.path.isfile(sys.argv[1]):
        sys.stderr.write(f"Missing {sys.argv[1]}")
        sys.exit(1)

    converted_lines = []

    with open(sys.argv[1], 'r') as rf:
        for line in rf:
            line = line.rstrip('\r\n')

            count = 0
            while count < len(line) and line[count] == '#':
                count += 1
            if 1 <= count <= 6 and line[count] == ' ':
                content = line[count + 1:].strip()
                converted_lines.append(f"<h{count}>{content}</h{count}>")
            else:
                converted_lines.append(f"<p>{line}</p>")

    with open(sys.argv[2], 'a') as wf:
        for line in converted_lines:
            wf.write(line + "\n")
