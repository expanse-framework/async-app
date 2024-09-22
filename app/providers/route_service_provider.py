from expanse.asynchronous.core.application import Application
from expanse.asynchronous.core.support.providers.route_service_provider import (
    RouteServiceProvider as ServiceProvider,
)
from expanse.asynchronous.routing.router import Router


class RouteServiceProvider(ServiceProvider):
    async def boot(self, router: Router, application: Application) -> None:
        await self.load_routes_from_file(
            router, application.base_path.joinpath("routes/api.py")
        )
        await self.load_routes_from_file(
            router, application.base_path.joinpath("routes/web.py")
        )
