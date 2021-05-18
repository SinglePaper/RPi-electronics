from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import socket

from android.permissions import request_permissions, Permission
request_permissions([Permission.INTERNET])

kv = """
Screen:
    MDLabel:
        text: ""
        id: txt
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}
        halign: 'center'
    MDIconButton:
        id: socket_connect
        icon: "cellphone-off"
        pos_hint: {"center_x": .9, "center_y": .9}
        on_press:
            app.socket_connect()
    MDFillRoundFlatButton:
        pos_hint: {'center_x': 0.5, 'center_y': 0.27}
        width: dp(150)
        height: dp(150)
        md_bg_color: 0, 1, 0, 1
        on_press:
            app.send_direction(0, 1)
        on_release:
            app.send_direction(0, 0)
    MDFillRoundFlatButton:
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        width: dp(150)
        height: dp(150)
        md_bg_color: 1, 0, 0, 1
        on_press:
            app.send_direction(2, 1)
        on_release:
            app.send_direction(0, 0)
    MDFillRoundFlatButton:
        pos_hint: {'center_x': 0.2, 'center_y': 0.1}
        width: dp(150)
        height: dp(150)
        md_bg_color: 0, 1, 1, 1
        on_press:
            app.send_direction(1, 1)
        on_release:
            app.send_direction(0, 0)
    MDFillRoundFlatButton:
        pos_hint: {'center_x': 0.8, 'center_y': 0.1}
        width: dp(150)
        height: dp(150)
        md_bg_color: 0, 1, 1, 1
        on_press:
            app.send_direction(3, 1)
        on_release:
            app.send_direction(0, 0)
"""


class Main(MDApp):
    data = {"direction": 0, "speed": 0, "autodrive": 0}
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def socket_connect(self):
        button = self.root.ids.socket_connect
        button.icon = "cellphone_cog"
        label = self.root.ids.txt
        try:
            self.s.connect(("charlie.local", 5432))
            label.text = "Socket successfully connected!"
            button.icon = "cellphone-sound"
        except:
            label.text = "Socket connection unsuccessful."
            button.icon = "cellphone-off"
        return

    def send_direction(self, direction, speed):
        label = self.root.ids.txt
        message = "d: " + str(direction) + ", s: " + str(speed)
        label.text = message
        self.data["direction"] = direction
        self.data["speed"] = speed
        message = str(self.data["direction"])+str(self.data["speed"])+str(self.data["autodrive"])
        try:
            self.s.send(message.encode("utf-8"))
        except:
            label.text = "Socket not connected."

    def action(self):
        label = self.root.ids.txt
        label.text = "This text is displayed after pressing button"

    def build(self):
        return Builder.load_string(kv)


Main().run()