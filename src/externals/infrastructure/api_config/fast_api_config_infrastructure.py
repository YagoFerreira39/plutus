from fastapi import FastAPI


from src.externals.ports.infrastructures.logs_config.i_logs_config_infrastructure import (
    ILogsConfigInfrastructure,
)

from src.externals.ports.infrastructures.ioc_container.i_ioc_container import (
    IIocContainerConfigInfrastructure,
)

from src.externals.ports.infrastructures.http_config.i_http_server_config_infrastructure import (
    IHttpServerConfigInfrastructure,
)

from src.externals.ports.infrastructures.api_config.i_api_config_infrastructure import (
    IApiConfigInfrastructure,
)


class FastAPIConfigInfrastructure(IApiConfigInfrastructure):
    def __init__(
        self,
        http_server_config_infrastructure: IHttpServerConfigInfrastructure,
        ioc_container_config_infrastructure: IIocContainerConfigInfrastructure,
        logs_config_infrastructure: ILogsConfigInfrastructure,
    ):
        self.__http_server_config_infrastructure = http_server_config_infrastructure
        self.__ioc_container_config_infrastructure = ioc_container_config_infrastructure
        self.__logs_config_infrastructure = logs_config_infrastructure

    def config_api(self) -> FastAPI:
        app = self.__http_server_config_infrastructure.config_http_server()
        self.__ioc_container_config_infrastructure.build_ioc_container()
        self.__logs_config_infrastructure.config_logs()

        return app
