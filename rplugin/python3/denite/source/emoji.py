# -*- coding: utf-8 -*-
# FILE: emoji.py
# AUTHOR: pocari <caffelattenonsugar at gmail.com>
# License: MIT license

from .base import Base

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'emoji'
        self.kind = 'word'

    def gather_candidates(self, context):
        candidates = []
        for emoji_name, code in self.vim.eval('emoji#data#dict()').items():
            if isinstance(code, list):
                emoji = "".join(map(chr, code))
            else:
                emoji = chr(code)
            candidates += [{
                'word': "{0} {1}".format(emoji, emoji_name),
                'action__text': emoji
            }]
        return candidates
