"""
Заполнение базы данных реальными компонентами.
Запуск: python populate_db.py
ВНИМАНИЕ: удаляет существующие данные и заполняет заново!
"""
import sqlite3
from database import Database


def reset_tables(cursor):
    """Удалить все таблицы для пересоздания"""
    tables = ['cpu', 'motherboard', 'ram', 'gpu', 'storage', 'psu', 'case_pc', 'cooling']
    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table}")


def populate_cpu(cursor):
    """Заполнить таблицу процессоров"""
    
    # ================================================================
    # INTEL 12 ПОКОЛЕНИЕ (Alder Lake) — LGA1700, DDR4-3200/DDR5-4800, max 128GB
    # ================================================================
    intel_12gen = [
        # (name, cores, threads, base, boost, tdp, price, igpu)
        ("Intel Core i3-12100",      4,  8,  3.3, 4.3,  60,  8990,  1),
        ("Intel Core i3-12100F",     4,  8,  3.3, 4.3,  58,  7490,  0),
        ("Intel Core i5-12400",      6, 12,  2.5, 4.4,  65, 13990,  1),
        ("Intel Core i5-12400F",     6, 12,  2.5, 4.4,  65, 11990,  0),
        ("Intel Core i5-12500",      6, 12,  3.0, 4.6,  65, 16990,  1),
        ("Intel Core i5-12600",      6, 12,  3.3, 4.8,  65, 18990,  1),
        ("Intel Core i5-12600K",    10, 16,  3.7, 4.9, 125, 21990,  1),
        ("Intel Core i5-12600KF",   10, 16,  3.7, 4.9, 125, 19990,  0),
        ("Intel Core i7-12700",     12, 20,  2.1, 4.9,  65, 27990,  1),
        ("Intel Core i7-12700F",    12, 20,  2.1, 4.9,  65, 25990,  0),
        ("Intel Core i7-12700K",    12, 20,  3.6, 5.0, 125, 32990,  1),
        ("Intel Core i7-12700KF",   12, 20,  3.6, 5.0, 125, 29990,  0),
        ("Intel Core i9-12900",     16, 24,  2.4, 5.1,  65, 39990,  1),
        ("Intel Core i9-12900F",    16, 24,  2.4, 5.1,  65, 37990,  0),
        ("Intel Core i9-12900K",    16, 24,  3.2, 5.2, 125, 46990,  1),
        ("Intel Core i9-12900KF",   16, 24,  3.2, 5.2, 125, 43990,  0),
        ("Intel Core i9-12900KS",   16, 24,  3.4, 5.5, 150, 54990,  1),
    ]
    
    for name, cores, threads, base, boost, tdp, price, igpu in intel_12gen:
        cursor.execute(
            "INSERT INTO cpu (name, socket, cores, threads, base_freq, boost_freq, "
            "tdp, price, integrated_graphics, supported_ddr_types, max_ram_freq, max_ram_capacity) "
            "VALUES (?, 'LGA1700', ?, ?, ?, ?, ?, ?, ?, 'DDR4,DDR5', 4800, 128)",
            (name, cores, threads, base, boost, tdp, price, igpu)
        )
    
    # ================================================================
    # INTEL 13 ПОКОЛЕНИЕ (Raptor Lake) — LGA1700, DDR4-3200/DDR5-5600, max 128GB
    # ================================================================
    intel_13gen = [
        ("Intel Core i3-13100",      4,  8,  3.4, 4.5,  60,  10990, 1),
        ("Intel Core i3-13100F",     4,  8,  3.4, 4.5,  58,   9490, 0),
        ("Intel Core i5-13400",     10, 16,  2.5, 4.6,  65,  17990, 1),
        ("Intel Core i5-13400F",    10, 16,  2.5, 4.6,  65,  15990, 0),
        ("Intel Core i5-13500",     14, 20,  2.5, 4.8,  65,  21990, 1),
        ("Intel Core i5-13600",     14, 20,  2.7, 5.0,  65,  24990, 1),
        ("Intel Core i5-13600K",    14, 20,  3.5, 5.1, 125,  28990, 1),
        ("Intel Core i5-13600KF",   14, 20,  3.5, 5.1, 125,  26990, 0),
        ("Intel Core i7-13700",     16, 24,  2.1, 5.2,  65,  33990, 1),
        ("Intel Core i7-13700F",    16, 24,  2.1, 5.2,  65,  31990, 0),
        ("Intel Core i7-13700K",    16, 24,  3.4, 5.4, 125,  40990, 1),
        ("Intel Core i7-13700KF",   16, 24,  3.4, 5.4, 125,  38990, 0),
        ("Intel Core i9-13900",     24, 32,  2.0, 5.2,  65,  44990, 1),
        ("Intel Core i9-13900F",    24, 32,  2.0, 5.2,  65,  42990, 0),
        ("Intel Core i9-13900K",    24, 32,  3.0, 5.8, 125,  54990, 1),
        ("Intel Core i9-13900KF",   24, 32,  3.0, 5.8, 125,  52990, 0),
        ("Intel Core i9-13900KS",   24, 32,  3.2, 6.0, 150,  62990, 1),
    ]
    
    for name, cores, threads, base, boost, tdp, price, igpu in intel_13gen:
        cursor.execute(
            "INSERT INTO cpu (name, socket, cores, threads, base_freq, boost_freq, "
            "tdp, price, integrated_graphics, supported_ddr_types, max_ram_freq, max_ram_capacity) "
            "VALUES (?, 'LGA1700', ?, ?, ?, ?, ?, ?, ?, 'DDR4,DDR5', 5600, 128)",
            (name, cores, threads, base, boost, tdp, price, igpu)
        )
    
    # ================================================================
    # INTEL 14 ПОКОЛЕНИЕ (Raptor Lake Refresh) — LGA1700, DDR4-3200/DDR5-5600, max 192GB
    # ================================================================
    intel_14gen = [
        ("Intel Core i5-14400",     10, 16,  2.5, 4.7,  65,  18990, 1),
        ("Intel Core i5-14400F",    10, 16,  2.5, 4.7,  65,  16990, 0),
        ("Intel Core i5-14500",     14, 20,  2.6, 5.0,  65,  23990, 1),
        ("Intel Core i5-14600",     14, 20,  2.7, 5.2,  65,  26990, 1),
        ("Intel Core i5-14600K",    14, 20,  3.5, 5.3, 125,  30990, 1),
        ("Intel Core i5-14600KF",   14, 20,  3.5, 5.3, 125,  28990, 0),
        ("Intel Core i7-14700",     20, 28,  2.1, 5.4,  65,  37990, 1),
        ("Intel Core i7-14700F",    20, 28,  2.1, 5.4,  65,  35990, 0),
        ("Intel Core i7-14700K",    20, 28,  3.4, 5.6, 125,  44990, 1),
        ("Intel Core i7-14700KF",   20, 28,  3.4, 5.6, 125,  42990, 0),
        ("Intel Core i9-14900",     24, 32,  2.0, 5.4,  65,  48990, 1),
        ("Intel Core i9-14900F",    24, 32,  2.0, 5.4,  65,  46990, 0),
        ("Intel Core i9-14900K",    24, 32,  3.2, 6.0, 125,  58990, 1),
        ("Intel Core i9-14900KF",   24, 32,  3.2, 6.0, 125,  56990, 0),
        ("Intel Core i9-14900KS",   24, 32,  3.2, 6.2, 150,  66990, 1),
    ]
    
    for name, cores, threads, base, boost, tdp, price, igpu in intel_14gen:
        cursor.execute(
            "INSERT INTO cpu (name, socket, cores, threads, base_freq, boost_freq, "
            "tdp, price, integrated_graphics, supported_ddr_types, max_ram_freq, max_ram_capacity) "
            "VALUES (?, 'LGA1700', ?, ?, ?, ?, ?, ?, ?, 'DDR4,DDR5', 5600, 192)",
            (name, cores, threads, base, boost, tdp, price, igpu)
        )
    
    # ================================================================
    # AMD RYZEN 5000 (Zen 3) — AM4, DDR4-3200, max 128GB
    # ================================================================
    amd_5000 = [
        ("AMD Ryzen 5 5500",      6, 12, 3.6, 4.2,  65,  8990,  0),
        ("AMD Ryzen 5 5600",      6, 12, 3.5, 4.4,  65, 11990,  0),
        ("AMD Ryzen 5 5600X",     6, 12, 3.7, 4.6,  65, 14990,  0),
        ("AMD Ryzen 5 5600G",     6, 12, 3.9, 4.4,  65, 12990,  1),
        ("AMD Ryzen 7 5700G",     8, 16, 3.8, 4.6,  65, 17990,  1),
        ("AMD Ryzen 7 5700X",     8, 16, 3.4, 4.6,  65, 16990,  0),
        ("AMD Ryzen 7 5800X",     8, 16, 3.8, 4.7, 105, 21990,  0),
        ("AMD Ryzen 7 5800X3D",   8, 16, 3.4, 4.5, 105, 27990,  0),
        ("AMD Ryzen 9 5900X",    12, 24, 3.7, 4.8, 105, 32990,  0),
        ("AMD Ryzen 9 5950X",    16, 32, 3.4, 4.9, 105, 44990,  0),
    ]
    
    for name, cores, threads, base, boost, tdp, price, igpu in amd_5000:
        cursor.execute(
            "INSERT INTO cpu (name, socket, cores, threads, base_freq, boost_freq, "
            "tdp, price, integrated_graphics, supported_ddr_types, max_ram_freq, max_ram_capacity) "
            "VALUES (?, 'AM4', ?, ?, ?, ?, ?, ?, ?, 'DDR4', 3200, 128)",
            (name, cores, threads, base, boost, tdp, price, igpu)
        )
    
    # ================================================================
    # AMD RYZEN 6000 (Zen 3+, Rembrandt) — FP7 (мобильные), DDR5-4800, max 64GB
    # Примечание: это мобильные процессоры, включены для полноты данных
    # ================================================================
    amd_6000 = [
        ("AMD Ryzen 5 6600H (mobile)",   6, 12, 3.3, 4.5,  45, 14990, 1),
        ("AMD Ryzen 7 6800H (mobile)",   8, 16, 3.2, 4.7,  45, 19990, 1),
        ("AMD Ryzen 7 6800HS (mobile)",  8, 16, 3.2, 4.7,  35, 18990, 1),
        ("AMD Ryzen 9 6900HX (mobile)",  8, 16, 3.3, 4.9,  45, 24990, 1),
        ("AMD Ryzen 9 6900HS (mobile)",  8, 16, 3.3, 4.9,  35, 23990, 1),
        ("AMD Ryzen 9 6980HX (mobile)",  8, 16, 3.3, 5.0,  45, 29990, 1),
    ]
    
    for name, cores, threads, base, boost, tdp, price, igpu in amd_6000:
        cursor.execute(
            "INSERT INTO cpu (name, socket, cores, threads, base_freq, boost_freq, "
            "tdp, price, integrated_graphics, supported_ddr_types, max_ram_freq, max_ram_capacity) "
            "VALUES (?, 'FP7', ?, ?, ?, ?, ?, ?, ?, 'DDR5', 4800, 64)",
            (name, cores, threads, base, boost, tdp, price, igpu)
        )
    
    # ================================================================
    # AMD RYZEN 7000 (Zen 4) — AM5, DDR5-5200, max 128GB
    # ================================================================
    amd_7000 = [
        ("AMD Ryzen 5 7600",      6, 12, 3.8, 5.1,  65, 19990, 1),
        ("AMD Ryzen 5 7600X",     6, 12, 4.7, 5.3, 105, 24990, 1),
        ("AMD Ryzen 7 7700",      8, 16, 3.8, 5.3,  65, 28990, 1),
        ("AMD Ryzen 7 7700X",     8, 16, 4.5, 5.4, 105, 34990, 1),
        ("AMD Ryzen 9 7900",     12, 24, 3.7, 5.4,  65, 38990, 1),
        ("AMD Ryzen 9 7900X",    12, 24, 4.7, 5.6, 170, 46990, 1),
        ("AMD Ryzen 9 7950X",    16, 32, 4.5, 5.7, 170, 58990, 1),
        ("AMD Ryzen 9 7950X3D",  16, 32, 4.2, 5.7, 120, 64990, 1),
    ]
    
    for name, cores, threads, base, boost, tdp, price, igpu in amd_7000:
        cursor.execute(
            "INSERT INTO cpu (name, socket, cores, threads, base_freq, boost_freq, "
            "tdp, price, integrated_graphics, supported_ddr_types, max_ram_freq, max_ram_capacity) "
            "VALUES (?, 'AM5', ?, ?, ?, ?, ?, ?, ?, 'DDR5', 5200, 128)",
            (name, cores, threads, base, boost, tdp, price, igpu)
        )
    
    # ================================================================
    # AMD RYZEN 8000 (Zen 4 APU) — AM5, DDR5-5200, max 256GB
    # ================================================================
    amd_8000 = [
        ("AMD Ryzen 5 8500G",     6, 12, 3.5, 5.0,  65, 17990, 1),
        ("AMD Ryzen 5 8600G",     6, 12, 4.3, 5.0,  65, 22990, 1),
        ("AMD Ryzen 7 8700G",     8, 16, 4.2, 5.1,  65, 29990, 1),
        ("AMD Ryzen 7 8700F",     8, 16, 4.1, 5.0,  65, 24990, 0),
    ]
    
    for name, cores, threads, base, boost, tdp, price, igpu in amd_8000:
        cursor.execute(
            "INSERT INTO cpu (name, socket, cores, threads, base_freq, boost_freq, "
            "tdp, price, integrated_graphics, supported_ddr_types, max_ram_freq, max_ram_capacity) "
            "VALUES (?, 'AM5', ?, ?, ?, ?, ?, ?, ?, 'DDR5', 5200, 256)",
            (name, cores, threads, base, boost, tdp, price, igpu)
        )
    
    # ================================================================
    # AMD RYZEN 9000 (Zen 5) — AM5, DDR5-5600, max 256GB
    # ================================================================
    amd_9000 = [
        ("AMD Ryzen 5 9600X",     6, 12, 3.9, 5.4,  65, 24990, 1),
        ("AMD Ryzen 7 9700X",     8, 16, 3.8, 5.5,  65, 34990, 1),
        ("AMD Ryzen 9 9900X",    12, 24, 4.4, 5.6, 120, 44990, 1),
        ("AMD Ryzen 9 9950X",    16, 32, 4.3, 5.7, 170, 59990, 1),
    ]
    
    for name, cores, threads, base, boost, tdp, price, igpu in amd_9000:
        cursor.execute(
            "INSERT INTO cpu (name, socket, cores, threads, base_freq, boost_freq, "
            "tdp, price, integrated_graphics, supported_ddr_types, max_ram_freq, max_ram_capacity) "
            "VALUES (?, 'AM5', ?, ?, ?, ?, ?, ?, ?, 'DDR5', 5600, 256)",
            (name, cores, threads, base, boost, tdp, price, igpu)
        )
    
    total = (len(intel_12gen) + len(intel_13gen) + len(intel_14gen) +
             len(amd_5000) + len(amd_6000) + len(amd_7000) +
             len(amd_8000) + len(amd_9000))
    
    print(f"  ✓ Процессоры: {total} шт.")
    print(f"    - Intel 12 gen: {len(intel_12gen)}")
    print(f"    - Intel 13 gen: {len(intel_13gen)}")
    print(f"    - Intel 14 gen: {len(intel_14gen)}")
    print(f"    - AMD Ryzen 5000: {len(amd_5000)}")
    print(f"    - AMD Ryzen 6000: {len(amd_6000)} (мобильные)")
    print(f"    - AMD Ryzen 7000: {len(amd_7000)}")
    print(f"    - AMD Ryzen 8000: {len(amd_8000)}")
    print(f"    - AMD Ryzen 9000: {len(amd_9000)}")


def populate_motherboards(cursor):
    """Заполнить материнские платы"""
    boards = [
        # AM4 — DDR4
        ("ASUS TUF Gaming B550-PLUS",      "AM4", "ATX",      "DDR4", 4, 128, 4800, 2, 6, 14990),
        ("MSI MAG B550 TOMAHAWK",          "AM4", "ATX",      "DDR4", 4, 128, 4800, 2, 6, 16990),
        ("Gigabyte B550 AORUS ELITE V2",   "AM4", "ATX",      "DDR4", 4, 128, 4733, 2, 6, 13990),
        ("ASUS ROG STRIX B550-F Gaming",   "AM4", "ATX",      "DDR4", 4, 128, 4800, 2, 6, 17990),
        ("MSI B550M PRO-VDH WIFI",         "AM4", "Micro-ATX","DDR4", 4, 128, 4400, 2, 4, 10990),
        ("Gigabyte X570 AORUS ELITE",      "AM4", "ATX",      "DDR4", 4, 128, 4400, 2, 6, 18990),
        
        # LGA1700 — DDR4
        ("MSI PRO B660M-A DDR4",           "LGA1700", "Micro-ATX", "DDR4", 4, 128, 4800, 2, 4, 11990),
        ("ASUS TUF Gaming B660-PLUS D4",   "LGA1700", "ATX",       "DDR4", 4, 128, 4800, 2, 4, 14990),
        ("Gigabyte B760M DS3H DDR4",       "LGA1700", "Micro-ATX", "DDR4", 4, 128, 5333, 2, 4, 12990),
        ("ASUS PRIME B760-PLUS D4",        "LGA1700", "ATX",       "DDR4", 4, 128, 5333, 2, 4, 15990),
        
        # LGA1700 — DDR5
        ("ASUS TUF Gaming Z690-PLUS D5",   "LGA1700", "ATX",       "DDR5", 4, 128, 6000, 3, 6, 24990),
        ("MSI MPG Z690 EDGE WIFI DDR5",    "LGA1700", "ATX",       "DDR5", 4, 128, 6400, 3, 6, 29990),
        ("ASUS ROG STRIX Z790-A D5",       "LGA1700", "ATX",       "DDR5", 4, 192, 7800, 4, 6, 34990),
        ("MSI MAG Z790 TOMAHAWK WIFI",     "LGA1700", "ATX",       "DDR5", 4, 192, 7200, 4, 6, 32990),
        ("Gigabyte Z790 AORUS ELITE AX",   "LGA1700", "ATX",       "DDR5", 4, 192, 7600, 4, 6, 36990),
        ("ASUS TUF Gaming B760-PLUS D5",   "LGA1700", "ATX",       "DDR5", 4, 192, 7800, 2, 4, 18990),
        ("MSI PRO Z790-A WIFI DDR5",       "LGA1700", "ATX",       "DDR5", 4, 192, 7200, 4, 6, 27990),
        
        # AM5 — DDR5
        ("ASUS TUF Gaming B650-PLUS",      "AM5", "ATX",       "DDR5", 4, 128, 6400, 2, 4, 22990),
        ("MSI MAG B650 TOMAHAWK WIFI",     "AM5", "ATX",       "DDR5", 4, 128, 6400, 2, 4, 24990),
        ("Gigabyte B650 AORUS ELITE AX",   "AM5", "ATX",       "DDR5", 4, 128, 6600, 2, 4, 23990),
        ("ASUS ROG STRIX B650E-F Gaming",  "AM5", "ATX",       "DDR5", 4, 128, 6400, 3, 4, 28990),
        ("MSI MAG X670E TOMAHAWK WIFI",    "AM5", "ATX",       "DDR5", 4, 128, 6600, 3, 6, 34990),
        ("ASUS ROG STRIX X670E-E Gaming",  "AM5", "ATX",       "DDR5", 4, 128, 6400, 4, 6, 44990),
        ("Gigabyte X670E AORUS MASTER",    "AM5", "E-ATX",     "DDR5", 4, 128, 6600, 4, 6, 54990),
        ("ASUS ROG STRIX X870E-E Gaming",  "AM5", "ATX",       "DDR5", 4, 256, 8000, 4, 4, 54990),
        ("MSI MEG X870E ACE",              "AM5", "ATX",       "DDR5", 4, 256, 8400, 4, 6, 64990),
    ]
    
    cursor.executemany(
        "INSERT INTO motherboard (name, socket, form_factor, ddr_type, ram_slots, "
        "max_ram, max_ram_freq, m2_slots, sata_ports, price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        boards
    )
    print(f"  ✓ Материнские платы: {len(boards)} шт.")


def populate_ram(cursor):
    """Заполнить оперативную память"""
    ram_modules = [
        # DDR4
        ("Kingston Fury Beast 16GB DDR4-3200",   "DDR4", 16, 3200, 2, 4990),
        ("Kingston Fury Beast 32GB DDR4-3200",   "DDR4", 32, 3200, 2, 8990),
        ("G.Skill Ripjaws V 16GB DDR4-3600",     "DDR4", 16, 3600, 2, 5490),
        ("G.Skill Ripjaws V 32GB DDR4-3600",     "DDR4", 32, 3600, 2, 9990),
        ("Corsair Vengeance LPX 16GB DDR4-3200", "DDR4", 16, 3200, 2, 5290),
        ("Corsair Vengeance LPX 32GB DDR4-3600", "DDR4", 32, 3600, 2, 10490),
        ("Kingston Fury Beast 64GB DDR4-3200",   "DDR4", 64, 3200, 2, 16990),
        
        # DDR5
        ("Kingston Fury Beast 16GB DDR5-5200",   "DDR5", 16, 5200, 2, 6990),
        ("Kingston Fury Beast 32GB DDR5-5200",   "DDR5", 32, 5200, 2, 12990),
        ("Kingston Fury Beast 32GB DDR5-5600",   "DDR5", 32, 5600, 2, 13990),
        ("Kingston Fury Beast 64GB DDR5-5600",   "DDR5", 64, 5600, 2, 24990),
        ("G.Skill Trident Z5 32GB DDR5-6000",    "DDR5", 32, 6000, 2, 16990),
        ("G.Skill Trident Z5 32GB DDR5-6400",    "DDR5", 32, 6400, 2, 18990),
        ("Corsair Vengeance 32GB DDR5-5200",     "DDR5", 32, 5200, 2, 13490),
        ("Corsair Vengeance 32GB DDR5-6000",     "DDR5", 32, 6000, 2, 17490),
        ("Corsair Dominator Titanium 64GB DDR5-6000", "DDR5", 64, 6000, 2, 32990),
        ("G.Skill Trident Z5 Neo 32GB DDR5-6000","DDR5", 32, 6000, 2, 17990),
        ("G.Skill Trident Z5 Neo 64GB DDR5-6000","DDR5", 64, 6000, 2, 31990),
        ("Kingston Fury Beast 96GB DDR5-5600",   "DDR5", 96, 5600, 2, 34990),
        ("Corsair Vengeance 96GB DDR5-6000",     "DDR5", 96, 6000, 2, 42990),
        ("G.Skill Trident Z5 128GB DDR5-6000",   "DDR5", 128, 6000, 4, 59990),
        ("Kingston Fury Beast 128GB DDR5-5600",  "DDR5", 128, 5600, 4, 54990),
    ]
    
    cursor.executemany(
        "INSERT INTO ram (name, ddr_type, capacity, frequency, modules, price) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        ram_modules
    )
    print(f"  ✓ Оперативная память: {len(ram_modules)} шт.")


def populate_gpu(cursor):
    """Заполнить видеокарты"""
    gpus = [
        ("NVIDIA GeForce RTX 3060",       12, 170, 267, 34990),
        ("NVIDIA GeForce RTX 3060 Ti",     8, 200, 267, 39990),
        ("NVIDIA GeForce RTX 3070",        8, 220, 285, 44990),
        ("NVIDIA GeForce RTX 3080",       10, 320, 305, 59990),
        ("NVIDIA GeForce RTX 4060",        8, 115, 240, 34990),
        ("NVIDIA GeForce RTX 4060 Ti",     8, 160, 240, 42990),
        ("NVIDIA GeForce RTX 4070",       12, 200, 244, 54990),
        ("NVIDIA GeForce RTX 4070 SUPER", 12, 220, 266, 62990),
        ("NVIDIA GeForce RTX 4070 Ti SUPER", 16, 285, 305, 79990),
        ("NVIDIA GeForce RTX 4080 SUPER", 16, 320, 336, 109990),
        ("NVIDIA GeForce RTX 4090",       24, 450, 336, 179990),
        ("AMD Radeon RX 6600 XT",          8, 160, 267, 29990),
        ("AMD Radeon RX 6700 XT",         12, 230, 267, 39990),
        ("AMD Radeon RX 6800 XT",         16, 300, 267, 54990),
        ("AMD Radeon RX 7600",             8, 165, 267, 29990),
        ("AMD Radeon RX 7700 XT",         12, 245, 267, 44990),
        ("AMD Radeon RX 7800 XT",         16, 263, 267, 52990),
        ("AMD Radeon RX 7900 GRE",        16, 260, 267, 59990),
        ("AMD Radeon RX 7900 XT",         20, 315, 287, 79990),
        ("AMD Radeon RX 7900 XTX",        24, 355, 287, 94990),
    ]
    
    cursor.executemany(
        "INSERT INTO gpu (name, memory, tdp, length, price) VALUES (?, ?, ?, ?, ?)",
        gpus
    )
    print(f"  ✓ Видеокарты: {len(gpus)} шт.")


def populate_storage(cursor):
    """Заполнить накопители"""
    storage = [
        ("Samsung 970 EVO Plus 500GB",    "NVMe M.2",  500, 3500, 3300,  5990),
        ("Samsung 970 EVO Plus 1TB",      "NVMe M.2", 1000, 3500, 3300,  9990),
        ("Samsung 980 PRO 1TB",           "NVMe M.2", 1000, 7000, 5000, 12990),
        ("Samsung 980 PRO 2TB",           "NVMe M.2", 2000, 7000, 5100, 21990),
        ("Samsung 990 PRO 1TB",           "NVMe M.2", 1000, 7450, 6900, 14990),
        ("Samsung 990 PRO 2TB",           "NVMe M.2", 2000, 7450, 6900, 24990),
        ("Samsung 990 PRO 4TB",           "NVMe M.2", 4000, 7450, 6900, 44990),
        ("WD Black SN850X 1TB",           "NVMe M.2", 1000, 7300, 6300, 11990),
        ("WD Black SN850X 2TB",           "NVMe M.2", 2000, 7300, 6600, 19990),
        ("Kingston A2000 500GB",          "NVMe M.2",  500, 2200, 2000,  4490),
        ("Kingston A2000 1TB",            "NVMe M.2", 1000, 2200, 2000,  7490),
        ("Kingston NV2 1TB",              "NVMe M.2", 1000, 3500, 2100,  6490),
        ("Kingston NV2 2TB",              "NVMe M.2", 2000, 3500, 2800, 11990),
        ("Kingston Fury Renegade 1TB",    "NVMe M.2", 1000, 7300, 6000, 12990),
        ("Kingston Fury Renegade 2TB",    "NVMe M.2", 2000, 7300, 7000, 22990),
        ("Samsung 870 EVO 1TB",           "SATA",     1000,  560,  530,  8990),
        ("Samsung 870 EVO 2TB",           "SATA",     2000,  560,  530, 16990),
        ("Kingston A400 480GB",           "SATA",      480,  500,  450,  3490),
        ("Kingston A400 960GB",           "SATA",      960,  500,  450,  5990),
    ]
    
    cursor.executemany(
        "INSERT INTO storage (name, interface, capacity, read_speed, write_speed, price) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        storage
    )
    print(f"  ✓ Накопители: {len(storage)} шт.")


def populate_psu(cursor):
    """Заполнить блоки питания"""
    psus = [
        ("be quiet! Pure Power 12 M 550W",      550,  "80+ Gold",     0,  6990),
        ("be quiet! Pure Power 12 M 650W",      650,  "80+ Gold",     1,  8490),
        ("Corsair RM650 (2024)",                650,  "80+ Gold",     1,  8990),
        ("Corsair RM750e (2023)",               750,  "80+ Gold",     1,  9990),
        ("be quiet! Pure Power 12 M 750W",      750,  "80+ Gold",     1,  9990),
        ("Corsair RM850x (2024)",               850,  "80+ Gold",     1, 12990),
        ("be quiet! Straight Power 12 850W",    850,  "80+ Platinum", 1, 14990),
        ("Seasonic Focus GX-850",               850,  "80+ Gold",     1, 13990),
        ("Corsair RM1000x (2024)",             1000,  "80+ Gold",     1, 16990),
        ("be quiet! Straight Power 12 1000W",  1000,  "80+ Platinum", 1, 18990),
        ("Seasonic Focus GX-1000",             1000,  "80+ Gold",     1, 15990),
        ("be quiet! Dark Power 13 1200W",      1200,  "80+ Titanium", 1, 27990),
        ("Corsair AX1600i",                    1600,  "80+ Titanium", 1, 44990),
    ]
    
    cursor.executemany(
        "INSERT INTO psu (name, wattage, efficiency, modular, price) VALUES (?, ?, ?, ?, ?)",
        psus
    )
    print(f"  ✓ Блоки питания: {len(psus)} шт.")


def populate_cases(cursor):
    """Заполнить корпуса"""
    cases = [
        ("Deepcool MATREXX 40",              "Micro-ATX,Mini-ITX",         320, 165,  3990),
        ("Zalman i3 Neo",                    "ATX,Micro-ATX,Mini-ITX",     330, 160,  4990),
        ("Deepcool CC560 V2",                "ATX,Micro-ATX,Mini-ITX",     340, 165,  5990),
        ("Cougar MX330-G",                   "ATX,Micro-ATX,Mini-ITX",     350, 160,  5490),
        ("NZXT H5 Flow",                     "ATX,Micro-ATX,Mini-ITX",     365, 165,  8990),
        ("Fractal Design Pop Air",           "ATX,Micro-ATX,Mini-ITX",     405, 170,  7990),
        ("Fractal Design Meshify 2 Compact", "ATX,Micro-ATX,Mini-ITX",     360, 169, 11990),
        ("Lian Li LANCOOL 216",              "ATX,Micro-ATX,Mini-ITX",     392, 180, 10990),
        ("Lian Li LANCOOL III",              "ATX,Micro-ATX,Mini-ITX,E-ATX", 400, 187, 13990),
        ("be quiet! Pure Base 500DX",        "ATX,Micro-ATX,Mini-ITX",     369, 190, 11990),
        ("be quiet! Silent Base 802",        "ATX,Micro-ATX,Mini-ITX,E-ATX", 432, 185, 14990),
        ("Fractal Design Torrent",           "ATX,Micro-ATX,Mini-ITX,E-ATX", 461, 188, 17990),
        ("Lian Li O11 Dynamic EVO",          "ATX,Micro-ATX,Mini-ITX,E-ATX", 422, 167, 15990),
        ("Corsair 5000D Airflow",            "ATX,Micro-ATX,Mini-ITX",     400, 170, 13990),
        ("NZXT H7 Flow",                     "ATX,Micro-ATX,Mini-ITX",     400, 185, 12990),
        ("Phanteks Eclipse G360A",           "ATX,Micro-ATX,Mini-ITX",     400, 163,  8990),
    ]
    
    cursor.executemany(
        "INSERT INTO case_pc (name, form_factors, max_gpu_length, max_cooler_height, price) "
        "VALUES (?, ?, ?, ?, ?)",
        cases
    )
    print(f"  ✓ Корпуса: {len(cases)} шт.")


def populate_cooling(cursor):
    """Заполнить системы охлаждения"""
    coolers = [
        # Башенные кулеры
        ("ID-COOLING SE-214-XT",           "AM4,AM5,LGA1700", 154, 180,  1990),
        ("Deepcool AK400",                 "AM4,AM5,LGA1700", 155, 220,  2990),
        ("Deepcool AK620",                 "AM4,AM5,LGA1700", 160, 260,  5990),
        ("be quiet! Pure Rock 2",          "AM4,AM5,LGA1700", 155, 150,  3490),
        ("be quiet! Dark Rock 4",          "AM4,AM5,LGA1700", 160, 200,  6490),
        ("Noctua NH-U12S redux",           "AM4,AM5,LGA1700", 158, 180,  5490),
        ("Noctua NH-D15",                  "AM4,AM5,LGA1700", 165, 250,  9990),
        ("Noctua NH-D15 chromax.black",    "AM4,AM5,LGA1700", 165, 250, 10990),
        ("Arctic Freezer 34 eSports",      "AM4,AM5,LGA1700", 157, 200,  4490),
        ("Arctic Freezer 34 eSports DUO",  "AM4,AM5,LGA1700", 157, 210,  5490),
        ("Thermalright Peerless Assassin 120 SE", "AM4,AM5,LGA1700", 155, 245, 4490),
        ("Thermalright Phantom Spirit 120 SE",    "AM4,AM5,LGA1700", 154, 245, 4990),
        ("Deepcool Assassin IV",           "AM4,AM5,LGA1700", 164, 280,  8990),
        ("be quiet! Dark Rock Pro 5",      "AM4,AM5,LGA1700", 168, 270,  9990),
        
        # СВО (жидкостное охлаждение)
        ("Arctic Liquid Freezer II 240",   "AM4,AM5,LGA1700",  63, 250,  7990),
        ("Arctic Liquid Freezer II 360",   "AM4,AM5,LGA1700",  63, 350,  9990),
        ("Deepcool LT520",                 "AM4,AM5,LGA1700",  62, 250,  8990),
        ("Deepcool LT720",                 "AM4,AM5,LGA1700",  62, 350, 11990),
        ("be quiet! Pure Loop 2 FX 240",   "AM4,AM5,LGA1700",  57, 250,  9990),
        ("be quiet! Pure Loop 2 FX 360",   "AM4,AM5,LGA1700",  57, 350, 12990),
        ("NZXT Kraken 240",                "AM4,AM5,LGA1700",  62, 250, 12990),
        ("NZXT Kraken 360",                "AM4,AM5,LGA1700",  62, 350, 16990),
        ("Corsair iCUE H150i Elite LCD",   "AM4,AM5,LGA1700",  57, 350, 24990),
    ]
    
    cursor.executemany(
        "INSERT INTO cooling (name, supported_sockets, height, tdp_support, price) "
        "VALUES (?, ?, ?, ?, ?)",
        coolers
    )
    print(f"  ✓ Охлаждение: {len(coolers)} шт.")


def populate_database():
    """Полное заполнение базы данных"""
    db = Database()
    
    with db.get_connection() as conn:
        cursor = conn.cursor()
        
        print("\n🗑️  Удаление старых данных...")
        reset_tables(cursor)
        
        print("📦 Создание таблиц...")
        # Пересоздаём таблицы через init_database
        conn.commit()
    
    # Пересоздаём структуру
    db.init_database()
    
    with db.get_connection() as conn:
        cursor = conn.cursor()
        
        print("\n📥 Заполнение компонентами...")
        populate_cpu(cursor)
        populate_motherboards(cursor)
        populate_ram(cursor)
        populate_gpu(cursor)
        populate_storage(cursor)
        populate_psu(cursor)
        populate_cases(cursor)
        populate_cooling(cursor)
    
    print("\n✅ База данных успешно заполнена!")
    print("=" * 50)
    
    # Вывод статистики
    with db.get_connection() as conn:
        cursor = conn.cursor()
        tables = {
            'cpu': 'Процессоры',
            'motherboard': 'Материнские платы',
            'ram': 'Оперативная память',
            'gpu': 'Видеокарты',
            'storage': 'Накопители',
            'psu': 'Блоки питания',
            'case_pc': 'Корпуса',
            'cooling': 'Охлаждение'
        }
        print("\n📊 Итоговая статистика:")
        total = 0
        for table, label in tables.items():
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]
            total += count
            print(f"  {label}: {count}")
        print(f"\n  ВСЕГО компонентов: {total}")
    print("=" * 50)


if __name__ == "__main__":
    populate_database()