import tkinter as tk
import app_parameters as ap


# Classes
# class AppCardCanvas(tk.Canvas):
#     """  """

#     def __init__(self, *args, **kwargs):
#         """  """
#         super().__init__(*args, **kwargs)


class AppButton(tk.Button):
    """  """

    def __init__(self, *args, **kwargs):
        """  """
        super().__init__(*args, **kwargs)
        self.config(
            bg=ap.BACKGROUND_COLOR,
            highlightthickness=0
        )
