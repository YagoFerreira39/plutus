from src.adapters.extensions.process_billing.process_billing_data_extension import (
    ProcessBillingDataExtension,
)
from src.adapters.ports.infrastructure.mongo_db.i_mongo_db_collection import (
    IMongoDbCollection,
)
from src.adapters.repositories.mongo_db.billing_data_repository import (
    BillingDataRepository,
)

from src.externals.infrastructure.mongo_db.mongo_db_collection import MongoDbCollection

from src.externals.infrastructure.mongo_db.mongo_db_infrastructure import (
    MongoDbInfrastructure,
)

from src.adapters.ports.infrastructure.mongo_db.i_mongo_db_infrastructure import (
    IMongoDbInfrastructure,
)

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

from src.externals.services.email_service import EmailService
from src.use_cases.ports.extensions.process_billing.i_process_billing_data_extension import (
    IProcessBillingDataExtension,
)
from src.use_cases.ports.repositories.mongo_db.i_billing_data_repository import (
    IBillingDataRepository,
)
from src.use_cases.ports.services.i_email__service import IEmailService
from src.use_cases.ports.use_cases.i_process_billing_data_use_case import (
    IProcessBillingDataUseCase,
)
from src.use_cases.ports.use_cases.i_send_billing_email_use_case import (
    ISendBillingEmailUseCase,
)
from src.use_cases.process_billing_data_use_case import ProcessBillingDataUseCase
from src.use_cases.send_billing_email_use_case import SendBillingEmailUseCase


class WitchDoctorContainerConfigInfrastructure(IIocContainerConfigInfrastructure):
    @classmethod
    def __create_use_cases_container(cls):
        use_cases_container = WitchDoctor.container("use_cases")

        use_cases_container(
            IProcessBillingDataUseCase,
            ProcessBillingDataUseCase,
            InjectionType.SINGLETON,
        )

        use_cases_container(
            ISendBillingEmailUseCase, SendBillingEmailUseCase, InjectionType.SINGLETON
        )

        return use_cases_container

    @classmethod
    def __create_infrastructures_container(cls):
        infrastructures_container = WitchDoctor.container("infrastructures")

        infrastructures_container(
            IMongoDbCollection, MongoDbCollection, InjectionType.SINGLETON
        )
        infrastructures_container(
            IMongoDbInfrastructure, MongoDbInfrastructure, InjectionType.SINGLETON
        )
        infrastructures_container(
            ILogsConfigInfrastructure,
            LoglifosConfigInfrastructure,
            InjectionType.SINGLETON,
        )

        return infrastructures_container

    @classmethod
    def __create_services_container(cls):
        services_container = WitchDoctor.container("services")

        services_container(IEmailService, EmailService, InjectionType.SINGLETON)

        return services_container

    @classmethod
    def __create_repositories_container(cls):
        repositories_container = WitchDoctor.container("repositories")

        repositories_container(
            IBillingDataRepository, BillingDataRepository, InjectionType.SINGLETON
        )

        return repositories_container

    @classmethod
    def __create_extensions_container(cls):
        extensions_container = WitchDoctor.container("extensions")

        extensions_container(
            IProcessBillingDataExtension,
            ProcessBillingDataExtension,
            InjectionType.SINGLETON,
        )

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
