from ninja import NinjaAPI

api = NinjaAPI(title="Eninja")

api.add_router("accounts/", "core.auths.api.router", tags=["auth"])
