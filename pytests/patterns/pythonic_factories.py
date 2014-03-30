#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['DiagramFactory', 'SvgDiagramFactory', 'create_diagram']


class DiagramFactory:

    # components
    class Text:
        pass

    class Rectangle:
        pass

    class Diagram:
        pass

    # interfaces
    @classmethod
    def make_diagram(Class, width, height):
        return Class.Diagram(width, height)

    @classmethod
    def make_text(Class, x, y, text, fontsize):
        return Class.Text(x, y, text, fontsize)

    @classmethod
    def make_rectangle(Class, **kws):
        return Class.Rectangle(**kws)


class SvgDiagramFactory(DiagramFactory):
    SVG_TEXT = "svg markup goes here {x}{y}{fontsize}"
    SVG_SCALE = 20

    class Text:

        def __init__(self, x, y, text, fontsize):
            x *= SvgDiagramFactory.SVG_SCALE
            y *= SvgDiagramFactory.SVG_SCALE
            fontsize *= SvgDiagramFactory.SVG_SCALE
            self.svg = SvgDiagramFactory.SVG_TEXT.format_map(locals())

    class Rectangle:
        pass

    class Diagram:
        pass


def create_diagram(factory):
    # same code of patterns.factories.create_diagram
    pass


def main():

    # no need to create factory instances anymore (see the previous code)
    txt_diagram = create_diagram(DiagramFactory)
    txt_diagram.save('/tmp/diagram.txt')

    svg_diagram = create_diagram(SvgDiagramFactory)
    svg_diagram.save('/tmp/diagram.svg')


if __name__ == '__main__':
    main()
