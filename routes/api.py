from expanse.asynchronous.http.response import Response
from expanse.asynchronous.routing.responder import Responder
from expanse.asynchronous.routing.router import Router


async def welcome(responder: Responder) -> Response:
    from expanse import __version__

    return await responder.json(
        {"message": "Welcome to Expanse!", "version": __version__}
    )


def routes(router: Router) -> None:
    with router.group("api", prefix="/api") as group:
        group.get("/welcome", welcome)
