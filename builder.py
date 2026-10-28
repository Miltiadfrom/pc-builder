"""
Основной класс конструктора ПК с умной фильтрацией совместимых компонентов
"""
from typing import Optional
from dataclasses import dataclass
from database import Database
from models import CPU, Motherboard, RAM, GPU, Storage, PSU, Case, Cooling
from compatibility import CompatibilityChecker, CompatibilityResult


@dataclass
class PCBuild:
    """Конфигурация ПК"""
    cpu: Optional[CPU] = None
    motherboard: Optional[Motherboard] = None
    ram: Optional[RAM] = None
    gpu: Optional[GPU] = None
    storage: Optional[Storage] = None
    psu: Optional[PSU] = None
    case: Optional[Case] = None
    cooling: Optional[Cooling] = None
    
    def get_total_price(self) -> float:
        """Получить общую стоимость сборки"""
        components = [
            self.cpu, self.motherboard, self.ram, self.gpu,
            self.storage, self.psu, self.case, self.cooling
        ]
        return sum(c.price for c in components if c)
    
    def get_total_tdp(self) -> int:
        """Получить общее энергопотребление"""
        tdp = 100  # Базовое потребление остальных компонентов
        if self.cpu:
            tdp += self.cpu.tdp
        if self.gpu:
            tdp += self.gpu.tdp
        return tdp
    
    def is_complete(self) -> bool:
        """Проверить, все ли обязательные компоненты выбраны"""
        required = [self.cpu, self.motherboard, self.ram, self.psu, self.case]
        return all(component is not None for component in required)
    
    def __str__(self) -> str:
        lines = ["=" * 60, "КОНФИГУРАЦИЯ ПК", "=" * 60]
        
        components = [
            ("Процессор", self.cpu),
            ("Материнская плата", self.motherboard),
            ("Оперативная память", self.ram),
            ("Видеокарта", self.gpu),
            ("Накопитель", self.storage),
            ("Блок питания", self.psu),
            ("Корпус", self.case),
            ("Охлаждение", self.cooling)
        ]
        
        for name, component in components:
            if component:
                lines.append(f"  {name}: {component}")
                lines.append(f"    Цена: {component.price:,.2f} руб.".replace(",", " "))
            else:
                lines.append(f"  {name}: Не выбрано")
        
        lines.append("-" * 60)
        lines.append(f"  Общая стоимость: {self.get_total_price():,.2f} руб.".replace(",", " "))
        lines.append(f"  Энергопотребление: ~{self.get_total_tdp()}W")
        lines.append("=" * 60)
        
        return "\n".join(lines)


class PCBuilder:
    """Конструктор ПК с умной фильтрацией совместимых компонентов"""
    
    def __init__(self, db_path: str = None):
        self.db = Database(db_path)
        self.build = PCBuild()
        self.checker = CompatibilityChecker()
    
    # ===== Сеттеры компонентов =====
    
    def set_cpu(self, cpu_id: int) -> None:
        """Выбрать процессор"""
        cpu = self.db.get_component_by_id('cpu', cpu_id)
        if not cpu:
            raise ValueError(f"Процессор с ID {cpu_id} не найден")
        self.build.cpu = cpu
    
    def set_motherboard(self, mb_id: int) -> None:
        """Выбрать материнскую плату"""
        mb = self.db.get_component_by_id('motherboard', mb_id)
        if not mb:
            raise ValueError(f"Материнская плата с ID {mb_id} не найдена")
        self.build.motherboard = mb
    
    def set_ram(self, ram_id: int) -> None:
        """Выбрать оперативную память"""
        ram = self.db.get_component_by_id('ram', ram_id)
        if not ram:
            raise ValueError(f"Оперативная память с ID {ram_id} не найдена")
        self.build.ram = ram
    
    def set_gpu(self, gpu_id: int) -> None:
        """Выбрать видеокарту"""
        gpu = self.db.get_component_by_id('gpu', gpu_id)
        if not gpu:
            raise ValueError(f"Видеокарта с ID {gpu_id} не найдена")
        self.build.gpu = gpu
    
    def set_storage(self, storage_id: int) -> None:
        """Выбрать накопитель"""
        storage = self.db.get_component_by_id('storage', storage_id)
        if not storage:
            raise ValueError(f"Накопитель с ID {storage_id} не найден")
        self.build.storage = storage
    
    def set_psu(self, psu_id: int) -> None:
        """Выбрать блок питания"""
        psu = self.db.get_component_by_id('psu', psu_id)
        if not psu:
            raise ValueError(f"Блок питания с ID {psu_id} не найден")
        self.build.psu = psu
    
    def set_case(self, case_id: int) -> None:
        """Выбрать корпус"""
        case = self.db.get_component_by_id('case_pc', case_id)
        if not case:
            raise ValueError(f"Корпус с ID {case_id} не найден")
        self.build.case = case
    
    def set_cooling(self, cooling_id: int) -> None:
        """Выбрать охлаждение"""
        cooling = self.db.get_component_by_id('cooling', cooling_id)
        if not cooling:
            raise ValueError(f"Охлаждение с ID {cooling_id} не найдено")
        self.build.cooling = cooling
    
    # ===== Умная фильтрация =====
    
    def get_compatible_components(self, component_type: str) -> list:
        """
        Получить ТОЛЬКО совместимые компоненты с учётом уже выбранной сборки.
        Это ключевой метод — он предотвращает выбор несовместимых деталей.
        """
        all_components = {
            'cpu': self.db.get_all_cpu(),
            'motherboard': self.db.get_all_motherboards(),
            'ram': self.db.get_all_ram(),
            'gpu': self.db.get_all_gpu(),
            'storage': self.db.get_all_storage(),
            'psu': self.db.get_all_psu(),
            'case': self.db.get_all_cases(),
            'cooling': self.db.get_all_cooling()
        }
        
        if component_type not in all_components:
            raise ValueError(f"Неизвестный тип компонента: {component_type}")
        
        compatible = []
        
        for component in all_components[component_type]:
            # Создаём временную сборку с тестируемым компонентом
            temp_build = PCBuild(
                cpu=self.build.cpu if component_type != 'cpu' else component,
                motherboard=self.build.motherboard if component_type != 'motherboard' else component,
                ram=self.build.ram if component_type != 'ram' else component,
                gpu=self.build.gpu if component_type != 'gpu' else component,
                storage=self.build.storage if component_type != 'storage' else component,
                psu=self.build.psu if component_type != 'psu' else component,
                case=self.build.case if component_type != 'case' else component,
                cooling=self.build.cooling if component_type != 'cooling' else component
            )
            
            result = self.checker.check_compatibility(
                temp_build.cpu, temp_build.motherboard, temp_build.ram,
                temp_build.gpu, temp_build.storage, temp_build.psu,
                temp_build.case, temp_build.cooling
            )
            
            # Добавляем только если нет критических ошибок
            if result.is_compatible:
                compatible.append(component)
        
        return compatible
    
    def check_compatibility(self) -> CompatibilityResult:
        """Проверить совместимость текущей сборки"""
        return self.checker.check_compatibility(
            self.build.cpu, self.build.motherboard, self.build.ram,
            self.build.gpu, self.build.storage, self.build.psu,
            self.build.case, self.build.cooling
        )
    
    # ===== Отображение компонентов =====
    
    def display_components(self, component_type: str) -> None:
        """Отобразить все компоненты определенного типа (без фильтрации)"""
        methods = {
            'cpu': self.db.get_all_cpu,
            'motherboard': self.db.get_all_motherboards,
            'ram': self.db.get_all_ram,
            'gpu': self.db.get_all_gpu,
            'storage': self.db.get_all_storage,
            'psu': self.db.get_all_psu,
            'case': self.db.get_all_cases,
            'cooling': self.db.get_all_cooling
        }
        
        if component_type not in methods:
            raise ValueError(f"Неизвестный тип компонента: {component_type}")
        
        components = methods[component_type]()
        
        print(f"\n{'=' * 60}")
        print(f"  Доступные компоненты: {component_type.upper()}")
        print('=' * 60)
        
        for component in components:
            print(f"\n  ID: {component.id}")
            print(f"  {component}")
            print(f"  Цена: {component.price:,.2f} руб.".replace(",", " "))
        
        print('=' * 60)
    
    def reset(self) -> None:
        """Сбросить текущую сборку"""
        self.build = PCBuild()