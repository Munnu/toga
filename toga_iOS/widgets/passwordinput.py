from .textinput import TextInput


class PasswordInput(TextInput):
    def __init__(self):
        super(PasswordInput, self).__init__()

    def startup(self):
        super(PasswordInput, self).startup()
        self._impl.setSecureTextEntry_(True)