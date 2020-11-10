# Embedded file name: /usr/lib/enigma2/python/Components/Renderer/SkalliNextEvents.py
from Components.VariableText import VariableText
from Components.Renderer.Renderer import Renderer
from enigma import eLabel, eEPGCache
from time import localtime

class SkalliNextEvents(VariableText, Renderer):

    def __init__(self):
        Renderer.__init__(self)
        VariableText.__init__(self)
        self.epgcache = eEPGCache.getInstance()

    GUI_WIDGET = eLabel

    def connect(self, source):
        Renderer.connect(self, source)
        self.changed((self.CHANGED_DEFAULT,))

    def changed(self, what):
        if what[0] == self.CHANGED_CLEAR:
            self.text = ''
        else:
            list = self.epgcache.lookupEvent(['BDT', (self.source.text,
              0,
              -1,
              360)])
            text = ''
            if len(list):
                i = 1
                for event in list:
                    if len(event) == 3 and i > 1:
                        begin = localtime(event[0])
                        end = localtime(event[0] + event[1])
                        event_str = '%02d:%02d - %02d:%02d  %s\n' % (begin[3],
                         begin[4],
                         end[3],
                         end[4],
                         event[2])
                        text = text + event_str
                    i = i + 1
                    if i >= 6:
                        break

            self.text = text