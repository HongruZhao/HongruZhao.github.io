"""Preserve LaTeX for MathJax while Markdown handles the surrounding prose."""
import html
import re
from xml.etree import ElementTree

from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
from markdown.preprocessors import Preprocessor
from markdown.util import AtomicString


class DisplayMath(Preprocessor):
    def run(self, lines):
        def preserve(match):
            if match.group(1):
                return match.group(0)  # Leave inline code examples untouched.
            element = '<div class="math-display">' + html.escape(match.group(0)) + '</div>'
            return '\n\n' + self.md.htmlStash.store(element) + '\n\n'
        return re.sub(r'(`+)[^\n]*?\1|(?<!\\)\$\$[\s\S]+?(?<!\\)\$\$', preserve, '\n'.join(lines)).split('\n')


class InlineMath(InlineProcessor):
    def handleMatch(self, match, data):
        element = ElementTree.Element('span', {'class': 'math-inline'})
        element.text = AtomicString(match.group(0))
        return element, match.start(0), match.end(0)


class MathJaxExtension(Extension):
    def extendMarkdown(self, md):
        # Fenced code is already stashed at priority 25. Inline code runs at 190.
        md.preprocessors.register(DisplayMath(md), 'display_math', 24)
        md.inlinePatterns.register(InlineMath(r'(?<!\\)\$(?!\$)([^\n]+?)(?<!\\)\$(?!\$)', md), 'inline_math', 185)
