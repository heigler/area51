#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Factory Pattern demonstration (classical way, not so pythonic)

You can use it when need to create complex objects that are composed of
others objects, each with its specific "family".

WARNING: This is not a functional module, some components are not full
implemented, is just to show the pattern
"""


# components

class Text:

    def __init__(self, x, y, text, fontsize):
        self.x = x
        self.y = y
        self.rows = [list(text)]


SVG_TEXT = """<text x="{x}" y="{y}" text-anchor="left" \
font-family="sans-serif" font-size="{fontsize}">{text}</text>"""
SVG_SCALE = 20


class SvgText:

    def __init__(self, x, y, text, fontsize):
        x *= SVG_SCALE
        y *= SVG_SCALE
        fontsize *= SVG_SCALE // 10
        self.svg = SVG_TEXT.format_map(locals())


class Rectangle:
    pass


class SvgRectangle:
    pass


class Diagram:

    def add(self, component):
        for y, row in enumerate(component.rows):
            for x, char in enumerate(row):
                self.diagram[y + component.y][x + component.x] = char


class SvgDiagram:

    def add(self, component):
        self.diagram.append(component.svg)


# factories

class DiagramFactory:

    """
    interfaces:
        make_diagram
        make_rectangle
        make_text

    All factories must have the same interfaces
    """

    def make_diagram(self, width, height):
        return Diagram(width, height)

    def make_rectangle(self, x, y, width, height, fill='white',
                       stroke='black'):
        return Rectangle(x, y, width, height, fill, stroke)

    def make_text(self, x, y, text, fontsize=12):
        return Text(x, y, text, fontsize)


class SvgDiagramFactory(DiagramFactory):

    def make_diagram(self, width, height):
        return SvgDiagram(width, height)

    def make_rectangle(self, x, y, width, height, fill='white',
                       stroke='black'):
        return SvgRectangle(x, y, width, height, fill, stroke)

    def make_text(self, x, y, text, fontsize=12):
        return SvgText(x, y, text, fontsize)


# generic interface

def create_diagram(factory):
    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 22, 5, 'yellow')
    text = factory.make_text(7, 3, 'Abstract Factory')
    diagram.add(rectangle)
    diagram.add(text)
    return diagram


def main():
    text_filename = '/tmp/text_diagram.txt'
    svg_filename = '/tmp/svg_filename.svg'

    txt_diagram = create_diagram(DiagramFactory())
    txt_diagram.save(text_filename)

    svg_diagram = create_diagram(SvgDiagramFactory())
    svg_diagram.save(svg_filename)
