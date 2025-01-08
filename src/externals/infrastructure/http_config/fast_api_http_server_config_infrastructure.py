from decouple import config
from fastapi import FastAPI
from src.externals.ports.infrastructures.http_config.i_http_server_config_infrastructure import (
    IHttpServerConfigInfrastructure,
)
from starlette.middleware.cors import CORSMiddleware

from src.externals.routers.plutus_router import PlutusRouter


class FastApiHttpServerConfigInfrastructure(IHttpServerConfigInfrastructure):
    def __init__(self):
        self.__root = config("ROOT_PATH")
        self.__app = FastAPI(
            title="Plutus",
            description="",
            docs_url=self.__root + "/docs",
            openapi_url=self.__root + "/openapi.json",
        )

    def __register_cors_rules(self):
        cors_allowed_origins_str = config("CORS_ALLOWED_ORIGINS")
        cors_allowed_origins = cors_allowed_origins_str.split(",")
        self.__app.add_middleware(
            CORSMiddleware,
            allow_origins=cors_allowed_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def __plutus_router(self):
        plutus_router = PlutusRouter.get_router()

        self.__app.include_router(plutus_router, prefix=self.__root)

    def config_http_server(self) -> FastAPI:
        self.__register_cors_rules()
        self.__plutus_router()
        return self.__app
