import sys

import expanse

from expanse.asynchronous.routing.responder import Responder


class WelcomeController:
    async def index(self, responder: Responder):
        return await responder.view(
            "welcome",
            {
                "expanse_version": expanse.__version__,
                "python_version": ".".join(str(v) for v in sys.version_info[:3]),
            },
        )
