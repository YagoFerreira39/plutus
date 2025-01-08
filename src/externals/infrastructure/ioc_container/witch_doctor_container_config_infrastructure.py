from src.externals.infrastructure.logs.loglifos_config_infrastructure import (
    LoglifosConfigInfrastructure,
)
from src.externals.ports.infrastructures.logs_config.i_logs_config_infrastructure import (
    ILogsConfigInfrastructure,
)
from src.externals.ports.infrastructures.ioc_container.i_ioc_container import (
    IIocContainerConfigInfrastructure,
)
from witch_doctor import WitchDoctor, InjectionType


class WitchDoctorContainerConfigInfrastructure(IIocContainerConfigInfrastructure):
    @classmethod
    def __create_use_cases_container(cls):
        use_cases_container = WitchDoctor.container("use_cases")

        return use_cases_container

    @classmethod
    def __create_infrastructures_container(cls):
        infrastructures_container = WitchDoctor.container("infrastructures")

        infrastructures_container(
            ILogsConfigInfrastructure,
            LoglifosConfigInfrastructure,
            InjectionType.SINGLETON,
        )

        return infrastructures_container

    @classmethod
    def __create_services_container(cls):
        services_container = WitchDoctor.container("services")

        return services_container

    @classmethod
    def __create_repositories_container(cls):
        repositories_container = WitchDoctor.container("repositories")

        return repositories_container

    @classmethod
    def __create_extensions_container(cls):
        extensions_container = WitchDoctor.container("extensions")

        return extensions_container

    @classmethod
    def __create_containers(cls):
        cls.__create_use_cases_container()
        cls.__create_infrastructures_container()
        cls.__create_services_container()
        cls.__create_repositories_container()
        cls.__create_extensions_container()

    @classmethod
    def __load_containers(cls):
        WitchDoctor.load_container("use_cases")
        WitchDoctor.load_container("infrastructures")
        WitchDoctor.load_container("services")
        WitchDoctor.load_container("repositories")
        WitchDoctor.load_container("extensions")

    @classmethod
    def build_ioc_container(cls):
        cls.__create_containers()
        cls.__load_containers()
