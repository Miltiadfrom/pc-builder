"""
Управление базой данных компонентов
"""
import sqlite3
import os
from contextlib import contextmanager
from models import (CPU, Motherboard, RAM, GPU, Storage, PSU, Case, Cooling,
                    SocketType, DDRType, FormFactor, StorageInterface)


class Database:
    """Класс для работы с БД компонентов"""
    
    def __init__(self, db_path: str = None):
        # Если путь не передан — используем абсолютный путь: файл pc_builder.db
        # в той же директории, где находится этот файл (database.py)
        if db_path is None:
            db_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                'pc_builder.db'
            )
        
        self.db_path = db_path
        
        # Отладка: выводим используемый путь при запуске Flask
        print(f"📂 Database path: {self.db_path}")
        print(f"📂 Database exists: {os.path.exists(self.db_path)}")
        
        self.init_database()
    
    @contextmanager
    def get_connection(self):
        """Контекстный менеджер для подключения к БД"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()
    
    def init_database(self):
        """Инициализация структуры БД"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cpu (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    socket TEXT NOT NULL,
                    cores INTEGER NOT NULL,
                    threads INTEGER NOT NULL,
                    base_freq REAL NOT NULL,
                    boost_freq REAL NOT NULL,
                    tdp INTEGER NOT NULL,
                    price REAL NOT NULL,
                    integrated_graphics INTEGER DEFAULT 0,
                    supported_ddr_types TEXT NOT NULL,
                    max_ram_freq INTEGER NOT NULL,
                    max_ram_capacity INTEGER NOT NULL
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS motherboard (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    socket TEXT NOT NULL,
                    form_factor TEXT NOT NULL,
                    ddr_type TEXT NOT NULL,
                    ram_slots INTEGER NOT NULL,
                    max_ram INTEGER NOT NULL,
                    max_ram_freq INTEGER NOT NULL,
                    m2_slots INTEGER NOT NULL,
                    sata_ports INTEGER NOT NULL,
                    price REAL NOT NULL
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ram (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    ddr_type TEXT NOT NULL,
                    capacity INTEGER NOT NULL,
                    frequency INTEGER NOT NULL,
                    modules INTEGER NOT NULL,
                    price REAL NOT NULL
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS gpu (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    memory INTEGER NOT NULL,
                    tdp INTEGER NOT NULL,
                    length INTEGER NOT NULL,
                    price REAL NOT NULL
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS storage (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    interface TEXT NOT NULL,
                    capacity INTEGER NOT NULL,
                    read_speed INTEGER NOT NULL,
                    write_speed INTEGER NOT NULL,
                    price REAL NOT NULL
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS psu (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    wattage INTEGER NOT NULL,
                    efficiency TEXT NOT NULL,
                    modular INTEGER NOT NULL,
                    price REAL NOT NULL
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS case_pc (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    form_factors TEXT NOT NULL,
                    max_gpu_length INTEGER NOT NULL,
                    max_cooler_height INTEGER NOT NULL,
                    price REAL NOT NULL
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cooling (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    supported_sockets TEXT NOT NULL,
                    height INTEGER NOT NULL,
                    tdp_support INTEGER NOT NULL,
                    price REAL NOT NULL
                )
            """)
    
    def get_all_cpu(self) -> list[CPU]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cpu ORDER BY name")
            return [
                CPU(
                    id=row['id'], name=row['name'],
                    socket=SocketType(row['socket']),
                    cores=row['cores'], threads=row['threads'],
                    base_freq=row['base_freq'], boost_freq=row['boost_freq'],
                    tdp=row['tdp'], price=row['price'],
                    integrated_graphics=bool(row['integrated_graphics']),
                    supported_ddr_types=[DDRType(t) for t in row['supported_ddr_types'].split(',')],
                    max_ram_freq=row['max_ram_freq'],
                    max_ram_capacity=row['max_ram_capacity']
                )
                for row in cursor.fetchall()
            ]
    
    def get_all_motherboards(self) -> list[Motherboard]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM motherboard ORDER BY name")
            return [
                Motherboard(
                    id=row['id'], name=row['name'],
                    socket=SocketType(row['socket']),
                    form_factor=FormFactor(row['form_factor']),
                    ddr_type=DDRType(row['ddr_type']),
                    ram_slots=row['ram_slots'], max_ram=row['max_ram'],
                    max_ram_freq=row['max_ram_freq'],
                    m2_slots=row['m2_slots'], sata_ports=row['sata_ports'],
                    price=row['price']
                )
                for row in cursor.fetchall()
            ]
    
    def get_all_ram(self) -> list[RAM]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ram ORDER BY ddr_type, frequency")
            return [
                RAM(
                    id=row['id'], name=row['name'],
                    ddr_type=DDRType(row['ddr_type']),
                    capacity=row['capacity'], frequency=row['frequency'],
                    modules=row['modules'], price=row['price']
                )
                for row in cursor.fetchall()
            ]
    
    def get_all_gpu(self) -> list[GPU]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM gpu ORDER BY name")
            return [
                GPU(id=row['id'], name=row['name'], memory=row['memory'],
                    tdp=row['tdp'], length=row['length'], price=row['price'])
                for row in cursor.fetchall()
            ]
    
    def get_all_storage(self) -> list[Storage]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM storage ORDER BY name")
            return [
                Storage(id=row['id'], name=row['name'],
                        interface=StorageInterface(row['interface']),
                        capacity=row['capacity'], read_speed=row['read_speed'],
                        write_speed=row['write_speed'], price=row['price'])
                for row in cursor.fetchall()
            ]
    
    def get_all_psu(self) -> list[PSU]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM psu ORDER BY wattage")
            return [
                PSU(id=row['id'], name=row['name'], wattage=row['wattage'],
                    efficiency=row['efficiency'], modular=bool(row['modular']),
                    price=row['price'])
                for row in cursor.fetchall()
            ]
    
    def get_all_cases(self) -> list[Case]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM case_pc ORDER BY name")
            return [
                Case(id=row['id'], name=row['name'],
                     form_factors=[FormFactor(f) for f in row['form_factors'].split(',')],
                     max_gpu_length=row['max_gpu_length'],
                     max_cooler_height=row['max_cooler_height'],
                     price=row['price'])
                for row in cursor.fetchall()
            ]
    
    def get_all_cooling(self) -> list[Cooling]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cooling ORDER BY name")
            return [
                Cooling(id=row['id'], name=row['name'],
                        supported_sockets=[SocketType(s) for s in row['supported_sockets'].split(',')],
                        height=row['height'], tdp_support=row['tdp_support'],
                        price=row['price'])
                for row in cursor.fetchall()
            ]
    
    def get_component_by_id(self, table: str, component_id: int):
        methods = {
            'cpu': self.get_all_cpu,
            'motherboard': self.get_all_motherboards,
            'ram': self.get_all_ram,
            'gpu': self.get_all_gpu,
            'storage': self.get_all_storage,
            'psu': self.get_all_psu,
            'case_pc': self.get_all_cases,
            'cooling': self.get_all_cooling
        }
        if table not in methods:
            raise ValueError(f"Неизвестная таблица: {table}")
        for component in methods[table]():
            if component.id == component_id:
                return component
        return None