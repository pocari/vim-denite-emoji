# -*- coding: utf-8 -*-
# FILE: emoji.py
# AUTHOR: pocari <caffelattenonsugar at gmail.com>
# License: MIT license

from .base import Base

class Base(base):
    def __init__(self, vim):
        self.vim = vim

class Source(Base):
    EMOJI_LIST = {
        0x1f44b: "WAVING HAND SIGN",
        0x1f44c: "OK HAND SIGN"
    }

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'emoji'
        self.kind = 'word'

    def gather_candidates(self, context):
        candidates = []
        for code, emoji_name in Source.EMOJI_LIST.items():
            emoji = chr(code)
            candidates += [{
                'word': emoji,
                'action__text': "{0} ({1})".format(emoji, emoji_name)
            }]
        return candidates
