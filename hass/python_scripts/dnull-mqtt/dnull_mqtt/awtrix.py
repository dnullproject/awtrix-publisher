# TODO: import rest of the settings
class Awtrix:
    """
    Docs: https://blueforcer.github.io/awtrix-light/#/api
    """

    def __init__(
        self,
        text=None,
        text_case=0,
        top_text=False,
        text_offset=True,
        center=True,
        color=None,
        gradient=None,
        scroll_speed=100,
    ):
        self.settings = {
            "text": text,
            "textCase": text_case,
            "topText": top_text,
            "textOffset": text_offset,
            "center": center,
            "color": color,
            "gradient": gradient,
            "scrollSpeed": scroll_speed,
        }

    def message(self, message):
        self.settings["text"] = message
        return self.settings
