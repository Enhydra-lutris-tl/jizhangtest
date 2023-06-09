# coding: utf-8
from enum import Enum

from qfluentwidgets import StyleSheetBase, Theme, qconfig


class StyleSheet(StyleSheetBase, Enum):
    """ Style sheet  """

    LINK_CARD = "link_card"
    JIZHANG_VIEW = "jizhangView"
    CHART_VIEW = "ChartView"
    REGULARLY_VIEW = 'RegularlyView'


    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f":/resource/{theme.value.lower()}/{self.value}.qss"
