import tkinter as tk
import app_parameters as ap


# Classes
class AppCard(tk.Canvas):
    """  """

    def __init__(self, parent, *args, **kwargs):
        """  """
        super().__init__(parent, *args, **kwargs)


class AppButton(tk.Button):
    """  """

    def __init__(self, parent, *args, **kwargs):
        """  """
        super().__init__(parent, *args, **kwargs)
        self.config(
            background=ap.BACKGROUND_COLOR,
            activebackground=ap.BACKGROUND_COLOR,
            relief="flat",
            highlightthickness=0
        )
