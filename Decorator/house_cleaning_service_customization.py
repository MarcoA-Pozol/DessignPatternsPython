# Interface
class CleaningService():
    def clean(self) -> str:
        pass

    def get_description(self) -> str:
        pass

    def get_cost(self) -> float:
        pass

# Concrete Component
class HouseCleaningService(CleaningService):
    _service_cost = 20.0
    _description = 'Basic and general house cleaning. '

    def clean(self) -> str:
        return f'\n- Cleaning House $ {self._service_cost}'

    def get_description(self) -> str:
        return self._description

    def get_cost(self) -> float:
        return self._service_cost

# Decorator
class CleaningServiceDecorator(CleaningService):
    _cleaning_service: CleaningService = None

    def __init__(self, cleaning_service: CleaningService) -> None:
        self._cleaning_service = cleaning_service

    @property
    def cleaning_service(self) -> CleaningService:
        return self._cleaning_service
    
    def clean(self) -> str:
        return self._cleaning_service.clean()
    
    def get_description(self):
        return self._cleaning_service.get_description()
    
    def get_cost(self):
        return self._cleaning_service.get_cost()

# Concrete Decorators (Cleaning Services)
class WindowCleaningService(CleaningServiceDecorator):
    _service_cost = 6.0
    _description = 'Windows cleaning. '

    def clean(self) -> str:
        return f'{self._cleaning_service.clean()}\n- Cleaning Windows $ {self._service_cost}'
    
    def get_description(self) -> str:
        return f"{self._cleaning_service.get_description()}{self._description}"

    def get_cost(self) -> float:
        return self._cleaning_service.get_cost() + self._service_cost

class BackyardCleaningService(CleaningServiceDecorator):
    _service_cost = 8.0
    _description = 'Backyard cleaning. '

    def clean(self) -> str:
        return f'{self._cleaning_service.clean()}\n- Cleaning Backyard $ {self._service_cost}'
    
    def get_description(self) -> str:
        return f"{self._cleaning_service.get_description()}{self._description}"

    def get_cost(self) -> float:
        return self._cleaning_service.get_cost() + self._service_cost
    
# Client Code
def client_code(client_request: str, cleaning_service: CleaningService) -> None:
    print(F'Client: {client_request}')
    print(f"Services: {cleaning_service.clean()}")
    print(f"Description: {cleaning_service.get_description()}")
    print(f"Total cost: ${cleaning_service.get_cost()}")
    print('\n')

if __name__ == "__main__":
    simple = HouseCleaningService()
    client_code(client_request='Only a general cleaning please...', cleaning_service=simple)

    house_cleaning = HouseCleaningService()
    windows_cleaning = WindowCleaningService(house_cleaning)
    backyard_cleaning = BackyardCleaningService(windows_cleaning)
    client_code(client_request='Clean house, windows and do something with my backyard please...', cleaning_service=backyard_cleaning)

    clean_house = HouseCleaningService()
    clean_windows = WindowCleaningService(house_cleaning)
    client_code(client_request='I only need my house ordered and swanky, make windows look better please.', cleaning_service=clean_windows)