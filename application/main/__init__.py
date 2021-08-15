from flask import Blueprint


MainBP = Blueprint(
            "MainBP",
            __name__,
            template_folder="templates",
            static_folder="static"
        )


from . import models
from . import routes
