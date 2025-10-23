import random

# 1: Component Interface
class Component():
    def get_description(self) -> str:
        pass

    def get_cost(self) -> float:
        pass

# 2: Concrete Component
class BasicComputer(Component):
    def get_description(self) -> str:
        return '\n- Monitor of 1080p\n- Motherboard with integrated CPU with and GPU Intel i3 3600\n- HDD 1TB\n- Power supply unit of 400W'

    def get_cost(self) -> float:
        return 650.0

# 3: Decorator Interface
class ComponentDecorator(Component):
    def __init__(self, component: Component):
        self._component = component

    def get_description(self) -> str:
        return self._component.get_description()
    
    def get_cost(self) -> float:
        return self._component.get_cost()

# 4: Concrete Decorators
class SsdDecorator(ComponentDecorator):
    ssd_models = [
        ('Samsung 990 EVO Plus 1TB', 99),
        ('Kingston NV3 1TB', 60),
        ('Crucial T705 Gen5 2TB', 143),
        ('WD Black SN850X 2TB', 129)
    ]

    ssd = random.choice(ssd_models)
    
    def get_description(self):
        return self._component.get_description() + f'\n- {self.ssd[0]}'
    
    def get_cost(self):
        return self._component.get_cost() + self.ssd[1]
    
class MouseDecorator(ComponentDecorator):
    mouse_models = [
        ('Logitech MX Master 3S', 99),
        ('Razer DeathAdder V2', 59),
        ('SteelSeries Rival 5', 69),
        ('Corsair Dark Core RGB Pro', 89)
    ]

    mouse = random.choice(mouse_models)
    
    def get_description(self):
        return self._component.get_description() + f'\n- {self.mouse[0]}'
    
    def get_cost(self):
        return self._component.get_cost() + self.mouse[1]

    
class KeyboardDecorator(ComponentDecorator):
    keyboard_models = [
        ('Keychron K6 Wireless', 79),
        ('Logitech MX Mechanical Mini', 99),
        ('Razer BlackWidow V4', 139),
        ('Corsair K100 RGB', 179)
    ]

    keyboard = random.choice(keyboard_models)
    
    def get_description(self):
        return self._component.get_description() + f'\n- {self.keyboard[0]}'
    
    def get_cost(self):
        return self._component.get_cost() + self.keyboard[1]


# 5: Client Code
if __name__ == '__main__':
    basic_computer = BasicComputer()
    add_ssd = SsdDecorator(basic_computer)
    add_keyboard = KeyboardDecorator(add_ssd)
    print(add_keyboard.get_description())
    print(f'\nTotal {'-'*20} $', add_keyboard.get_cost())