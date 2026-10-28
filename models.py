"""
Модели компонентов ПК с типизацией и валидацией
"""
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class SocketType(Enum):
    """Типы процессорных сокетов"""
    AM4 = "AM4"
    AM5 = "AM5"
    LGA1700 = "LGA1700"
    LGA1851 = "LGA1851"
    FP7 = "FP7"  # Мобильные процессоры (для полноты данных)


class DDRType(Enum):
    """Типы оперативной памяти"""
    DDR4 = "DDR4"
    DDR5 = "DDR5"


class FormFactor(Enum):
    """Форм-факторы материнских плат и корпусов"""
    ATX = "ATX"
    MATX = "Micro-ATX"
    ITX = "Mini-ITX"
    EATX = "E-ATX"


class StorageInterface(Enum):
    """Интерфейсы накопителей"""
    SATA = "SATA"
    NVME = "NVMe M.2"


@dataclass
class CPU:
    """Процессор"""
    id: int
    name: str
    socket: SocketType
    cores: int
    threads: int
    base_freq: float
    boost_freq: float
    tdp: int
    price: float
    integrated_graphics: bool = False
    # НОВЫЕ ПОЛЯ:
    supported_ddr_types: list[DDRType] = field(default_factory=list)
    max_ram_freq: int = 0          # Макс. частота памяти (МГц)
    max_ram_capacity: int = 0      # Макс. объём памяти (ГБ)
    
    def __str__(self) -> str:
        igpu = "встроенная графика" if self.integrated_graphics else "без графики"
        ddr = "/".join([d.value for d in self.supported_ddr_types])
        return (
            f"{self.name} ({self.cores}C/{self.threads}T, "
            f"{self.boost_freq}GHz, TDP: {self.tdp}W, {ddr}-{self.max_ram_freq}, "
            f"max {self.max_ram_capacity}GB, {igpu})"
        )


@dataclass
class Motherboard:
    """Материнская плата"""
    id: int
    name: str
    socket: SocketType
    form_factor: FormFactor
    ddr_type: DDRType
    ram_slots: int
    max_ram: int
    max_ram_freq: int
    m2_slots: int
    sata_ports: int
    price: float
    
    def __str__(self) -> str:
        return (
            f"{self.name} ({self.socket.value}, {self.form_factor.value}, "
            f"{self.ddr_type.value}-{self.max_ram_freq}, {self.ram_slots} слотов)"
        )


@dataclass
class RAM:
    """Оперативная память"""
    id: int
    name: str
    ddr_type: DDRType
    capacity: int
    frequency: int
    modules: int
    price: float
    
    def __str__(self) -> str:
        return (
            f"{self.name} ({self.capacity}GB {self.ddr_type.value}-{self.frequency}, "
            f"{self.modules}x{self.capacity // self.modules}GB)"
        )


@dataclass
class GPU:
    """Видеокарта"""
    id: int
    name: str
    memory: int
    tdp: int
    length: int
    price: float
    
    def __str__(self) -> str:
        return f"{self.name} ({self.memory}GB, TDP: {self.tdp}W, Длина: {self.length}mm)"


@dataclass
class Storage:
    """Накопитель"""
    id: int
    name: str
    interface: StorageInterface
    capacity: int
    read_speed: int
    write_speed: int
    price: float
    
    def __str__(self) -> str:
        return (
            f"{self.name} ({self.capacity}GB, {self.interface.value}, "
            f"R:{self.read_speed}/W:{self.write_speed} MB/s)"
        )


@dataclass
class PSU:
    """Блок питания"""
    id: int
    name: str
    wattage: int
    efficiency: str
    modular: bool
    price: float
    
    def __str__(self) -> str:
        return (
            f"{self.name} ({self.wattage}W, {self.efficiency}, "
            f"{'Модульный' if self.modular else 'Не модульный'})"
        )


@dataclass
class Case:
    """Корпус"""
    id: int
    name: str
    form_factors: list[FormFactor]
    max_gpu_length: int
    max_cooler_height: int
    price: float
    
    def __str__(self) -> str:
        ff = ", ".join([f.value for f in self.form_factors])
        return f"{self.name} ({ff}, GPU до {self.max_gpu_length}mm)"


@dataclass
class Cooling:
    """Система охлаждения"""
    id: int
    name: str
    supported_sockets: list[SocketType]
    height: int
    tdp_support: int
    price: float
    
    def __str__(self) -> str:
        sockets = ", ".join([s.value for s in self.supported_sockets])
        return f"{self.name} (Сокеты: {sockets}, Высота: {self.height}mm, TDP до {self.tdp_support}W)"