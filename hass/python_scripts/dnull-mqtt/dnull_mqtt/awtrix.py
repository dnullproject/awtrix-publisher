# TODO: color methods

from colors import HexColors


class Awtrix:
    """
    Docs: https://blueforcer.github.io/awtrix-light/#/api
    """

    def __init__(
        self,
        # string	The text to display. Keep in mind the font does not have a fixed size and I uses less space than W. This facts affects when text will start scrolling
        text=None,
        # integer	Changes the Uppercase setting. 0=global setting, 1=forces uppercase; 2=shows as it sent.       text_case=0,
        text_case=2,
        # boolean	Draw the text on top.
        top_text=False,
        # integer	Sets an offset for the x position of a starting text.
        text_offset=0,
        # boolean	Centers a short, non-scrollable text.
        center=True,
        # string or array of integers	The text, bar or line color.
        color=None,
        # Array of string or integers	Colorizes the text in a gradient of two given colors
        gradient=None,
        # integer	Blinks the text in an given interval, not compatible with gradient or rainbow
        blink_text=None,
        # Integer	Fades the text on and off in an given interval, not compatible with gradient or rainbow
        fade_text=None,
        # string or array of integers	Sets a background color.
        background=None,
        # boolean	Fades each letter in the text differently through the entire RGB spectrum.
        rainbow=False,
        # string	The icon ID or filename (without extension) to display on the app. You can also send a 8x8 jpg as Base64 String
        icon=None,
        # integer	0 = Icon doesn't move. 1 = Icon moves with text and will not appear again. 2 = Icon moves with text but appears again when the text starts to scroll again.
        push_icon=0,
        # integer	Sets how many times the text should be scrolled through the matrix before the app ends.
        repeat=0,
        # integer	Sets how long the app or notification should be displayed.
        duration=5,
        # boolean	Set it to true, to hold your notification on top until you press the middle button or dismiss it via HomeAssistant. This key only belongs to notification.
        hold=False,
        # string	The filename of your RTTTL ringtone file placed in the MELODIES folder (without extension).
        sound=None,
        # string	Allows to send the RTTTL sound string with the json.
        rtttl=None,
        # boolean	Loops the sound or rtttl as long as the notification is running.
        loop_sound=False,
        # array of integers	Draws a bargraph. Without icon maximum 16 values, with icon 11 values.
        bar=None,
        # array of integers	Draws a linechart. Without icon maximum 16 values, with icon 11 values.
        line=None,
        # boolean	Enables or disables autoscaling for bar and linechart.
        autoscale=True,
        # integer	Shows a progress bar. Value can be 0-100.
        progress=-1,
        # string or array of integers	The color of the progress bar.
        progress_c=-1,
        # string or array of integers	The color of the progress bar background.
        progress_bc=-1,
        # integer	Defines the position of your custom page in the loop, starting at 0 for the first position. This will only apply with your first push. This function is experimental.
        pos=None,
        # array of objects	Array of drawing instructions. Each object represents a drawing command. See the drawing instructions below.
        # draw	=
        # integer	Removes the custom app when there is no update after the given time in seconds.
        lifetime=0,
        # integer	0 = deletes the app, 1 = marks it as staled with a red rectangle around the app
        lifetime_mode=0,
        # boolean	Defines if the notification will be stacked. false will immediately replace the current notification.
        stack=True,
        # boolean	If the Matrix is off, the notification will wake it up for the time of the notification.
        wakeup=False,
        # boolean	Disables the text scrolling.
        no_scroll=False,
        # integer	Modifies the scroll speed. Enter a percentage value of the original scroll speed.
        scroll_speed=100,
    ):
        self.settings = {
            "autoscale": autoscale,
            "background": background,
            "bar": bar,
            "blinkText": blink_text,
            "center": center,
            "color": color,
            "duration": duration,
            "fadeText": fade_text,
            "gradient": gradient,
            "hold": hold,
            "icon": icon,
            "lifetime": lifetime,
            "lifetimeMode": lifetime_mode,
            "line": line,
            "loopSound": loop_sound,
            "noScroll": no_scroll,
            "pos": pos,
            "progress": progress,
            "progressBC": progress_bc,
            "progressC": progress_c,
            "pushIcon": push_icon,
            "rainbow": rainbow,
            "repeat": repeat,
            "rtttl": rtttl,
            "scrollSpeed": scroll_speed,
            "sound": sound,
            "stack": stack,
            "text": text,
            "textCase": text_case,
            "textOffset": text_offset,
            "topText": top_text,
            "wakeup": wakeup,
        }
        self.icons = {
            "default": "28035",
            "missing": "47687",
            "binance": "43722",
            "green_checkmark": "47199",
            "error": "56224",
            "notion": "57587",
            # 1/
            "11": "57635",
            "12": "57636",
            "13": "57637",
            "14": "57638",
            "15": "57639",
            # 2/
            "22": "57640",
            "23": "57641",
            "24": "57642",
            "25": "57643",
            # 3/
            "33": "57644",
            "34": "57645",
            "35": "57646",
            # 4/
            "44": "57647",
            "45": "57648",
            # 5/
            "55": "57649",
        }
        self.color = HexColors()

    # def message(self, message):
    #     self.settings["text"] = message
    #     return self.settings

    def icon(self, icon_name):
        self.settings["icon"] = self.icons.get(icon_name, self.icons["missing"])

    def warning(self, message):
        self.settings["color"] = self.color.to_hex["Amber"]
        self.settings["text"] = message
        return self.settings

    def critical(self, message):
        self.settings["color"] = self.color.to_hex["Red"]
        self.settings["text"] = message
        return self.settings

    def message(self, raw_message):
        result = list()
        if "--" not in raw_message:
            self.settings["text"] = raw_message
        else:
            messages = raw_message.split("--")
            for message in messages:
                color = None
                if len(message) == 0:
                    continue
                if "::" in message:
                    color, text = message.split("::")
                    color = self.color.to_hex.get(color, "FFFFFF")
                else:
                    text = message
                result.append({"t": text, "c": color})

            self.settings["text"] = result
        return self.settings
