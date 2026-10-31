"""
Веб-приложение конструктора ПК на Flask
"""
from flask import Flask, render_template, jsonify, request
import sys
import os

# Добавляем родительскую директорию в путь для импорта
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import Database
from models import CPU, Motherboard, RAM, GPU, Storage, PSU, Case, Cooling
from builder import PCBuilder

app = Flask(__name__)
db = Database(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'pc_builder.db'))

# Категории товаров
CATEGORIES = {
    'cpu': {
        'name': 'Процессоры',
        'description': 'Мощные процессоры для любых задач',
        'getter': db.get_all_cpu,
        'icon': '🖥️'
    },
    'motherboard': {
        'name': 'Материнские платы',
        'description': 'Надежная основа вашей системы',
        'getter': db.get_all_motherboards,
        'icon': '🔌'
    },
    'ram': {
        'name': 'Оперативная память',
        'description': 'Быстрая память для многозадачности',
        'getter': db.get_all_ram,
        'icon': '💾'
    },
    'gpu': {
        'name': 'Видеокарты',
        'description': 'Графическая мощь для игр и работы',
        'getter': db.get_all_gpu,
        'icon': '🎮'
    },
    'storage': {
        'name': 'Накопители',
        'description': 'Быстрые SSD и вместительные HDD',
        'getter': db.get_all_storage,
        'icon': '💿'
    },
    'psu': {
        'name': 'Блоки питания',
        'description': 'Надежное питание всех компонентов',
        'getter': db.get_all_psu,
        'icon': '⚡'
    },
    'case': {
        'name': 'Корпуса',
        'description': 'Стильные и функциональные корпуса',
        'getter': db.get_all_cases,
        'icon': '📦'
    },
    'cooling': {
        'name': 'Охлаждение',
        'description': 'Эффективное охлаждение процессора',
        'getter': db.get_all_cooling,
        'icon': '❄️'
    }
}


def format_price(price: float) -> str:
    """Форматировать цену"""
    return f"{price:,.0f}".replace(",", " ")


def get_component_details(component):
    """Получить детальную информацию о компоненте в виде словаря"""
    details = {}
    
    if isinstance(component, CPU):
        details = {
            'id': component.id,
            'name': component.name,
            'price': format_price(component.price),
            'price_raw': component.price,
            'type': 'cpu',
            'specs': [
                f"Сокет: {component.socket.value}",
                f"Ядер: {component.cores}",
                f"Потоков: {component.threads}",
                f"Частота: {component.base_freq}-{component.boost_freq} GHz",
                f"TDP: {component.tdp}W",
                f"Память: {', '.join([d.value for d in component.supported_ddr_types])} до {component.max_ram_freq}MHz",
                f"Макс. память: {component.max_ram_capacity}GB",
                f"Графика: {'Есть' if component.integrated_graphics else 'Нет'}"
            ]
        }
    
    elif isinstance(component, Motherboard):
        details = {
            'id': component.id,
            'name': component.name,
            'price': format_price(component.price),
            'price_raw': component.price,
            'type': 'motherboard',
            'specs': [
                f"Сокет: {component.socket.value}",
                f"Форм-фактор: {component.form_factor.value}",
                f"Память: {component.ddr_type.value}",
                f"Слотов RAM: {component.ram_slots}",
                f"Макс. RAM: {component.max_ram}GB",
                f"Макс. частота RAM: {component.max_ram_freq}MHz",
                f"Слотов M.2: {component.m2_slots}",
                f"Портов SATA: {component.sata_ports}"
            ]
        }
    
    elif isinstance(component, RAM):
        details = {
            'id': component.id,
            'name': component.name,
            'price': format_price(component.price),
            'price_raw': component.price,
            'type': 'ram',
            'specs': [
                f"Тип: {component.ddr_type.value}",
                f"Объём: {component.capacity}GB",
                f"Частота: {component.frequency}MHz",
                f"Модулей: {component.modules}×{component.capacity // component.modules}GB"
            ]
        }
    
    elif isinstance(component, GPU):
        details = {
            'id': component.id,
            'name': component.name,
            'price': format_price(component.price),
            'price_raw': component.price,
            'type': 'gpu',
            'specs': [
                f"Память: {component.memory}GB",
                f"TDP: {component.tdp}W",
                f"Длина: {component.length}mm"
            ]
        }
    
    elif isinstance(component, Storage):
        details = {
            'id': component.id,
            'name': component.name,
            'price': format_price(component.price),
            'price_raw': component.price,
            'type': 'storage',
            'specs': [
                f"Интерфейс: {component.interface.value}",
                f"Объём: {component.capacity}GB",
                f"Чтение: {component.read_speed} MB/s",
                f"Запись: {component.write_speed} MB/s"
            ]
        }
    
    elif isinstance(component, PSU):
        details = {
            'id': component.id,
            'name': component.name,
            'price': format_price(component.price),
            'price_raw': component.price,
            'type': 'psu',
            'specs': [
                f"Мощность: {component.wattage}W",
                f"Сертификат: {component.efficiency}",
                f"Модульный: {'Да' if component.modular else 'Нет'}"
            ]
        }
    
    elif isinstance(component, Case):
        details = {
            'id': component.id,
            'name': component.name,
            'price': format_price(component.price),
            'price_raw': component.price,
            'type': 'case',
            'specs': [
                f"Форм-факторы: {', '.join([f.value for f in component.form_factors])}",
                f"Макс. длина GPU: {component.max_gpu_length}mm",
                f"Макс. высота кулера: {component.max_cooler_height}mm"
            ]
        }
    
    elif isinstance(component, Cooling):
        details = {
            'id': component.id,
            'name': component.name,
            'price': format_price(component.price),
            'price_raw': component.price,
            'type': 'cooling',
            'specs': [
                f"Сокеты: {', '.join([s.value for s in component.supported_sockets])}",
                f"Высота: {component.height}mm",
                f"TDP поддержка: до {component.tdp_support}W"
            ]
        }
    
    return details


def get_recommended_cpus():
    """Получить 3 рекомендуемых процессора: дешёвый, средний, дорогой"""
    all_cpus = db.get_all_cpu()
    
    # Сортируем по цене
    sorted_cpus = sorted(all_cpus, key=lambda x: x.price)
    
    # Берём 3 процессора из разных ценовых категорий
    budget = sorted_cpus[0]  # Самый дешёвый
    mid_range = sorted_cpus[len(sorted_cpus) // 2]  # Средний
    premium = sorted_cpus[-1]  # Самый дорогой
    
    return [budget, mid_range, premium]


@app.route('/')
def index():
    """Главная страница с пошаговым конструктором"""
    return render_template('index.html')


@app.route('/category/<category_key>')
def category(category_key):
    """Страница категории"""
    if category_key not in CATEGORIES:
        return "Категория не найдена", 404
    
    category = CATEGORIES[category_key]
    components = category['getter']()
    
    components_data = [get_component_details(c) for c in components]
    
    return render_template(
        'category.html',
        category_name=category['name'],
        category_description=category['description'],
        category_icon=category['icon'],
        components=components_data,
        category_key=category_key
    )


@app.route('/api/builder/step/<int:step>', methods=['GET'])
def get_builder_step(step):
    """API для получения компонентов на каждом шаге конструктора"""
    # Получаем выбранные компоненты из query параметров
    selected = {
        'cpu': request.args.get('cpu'),
        'motherboard': request.args.get('motherboard'),
        'ram': request.args.get('ram'),
        'gpu': request.args.get('gpu'),
        'storage': request.args.get('storage'),
        'cooling': request.args.get('cooling'),
        'case': request.args.get('case'),
        'psu': request.args.get('psu')
    }
    
    # Создаём временный builder с выбранными компонентами
    builder = PCBuilder()
    
    try:
        if selected['cpu']:
            builder.set_cpu(int(selected['cpu']))
        if selected['motherboard']:
            builder.set_motherboard(int(selected['motherboard']))
        if selected['ram']:
            builder.set_ram(int(selected['ram']))
        if selected['gpu']:
            builder.set_gpu(int(selected['gpu']))
        if selected['storage']:
            builder.set_storage(int(selected['storage']))
        if selected['cooling']:
            builder.set_cooling(int(selected['cooling']))
        if selected['case']:
            builder.set_case(int(selected['case']))
        if selected['psu']:
            builder.set_psu(int(selected['psu']))
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    # Определяем какой компонент нужен на этом шаге
    step_config = {
        1: ('cpu', 'Процессор', db.get_all_cpu),
        2: ('motherboard', 'Материнская плата', builder.get_compatible_components),
        3: ('ram', 'Оперативная память', builder.get_compatible_components),
        4: ('gpu', 'Видеокарта', builder.get_compatible_components),
        5: ('storage', 'Накопитель', builder.get_compatible_components),
        6: ('cooling', 'Охлаждение', builder.get_compatible_components),
        7: ('case', 'Корпус', builder.get_compatible_components),
        8: ('psu', 'Блок питания', builder.get_compatible_components),
    }
    
    if step not in step_config:
        return jsonify({'error': 'Неверный шаг'}), 400
    
    component_type, title, getter = step_config[step]
    
    # Получаем компоненты
    if step == 1:
        components = getter()
    else:
        components = getter(component_type)
    
    # Формируем ответ
    components_data = [get_component_details(c) for c in components]
    
    return jsonify({
        'step': step,
        'title': title,
        'component_type': component_type,
        'components': components_data,
        'optional': component_type in ['gpu', 'storage', 'cooling', 'case']
    })


@app.route('/api/builder/summary', methods=['POST'])
def get_builder_summary():
    """API для получения итоговой сборки"""
    data = request.json
    
    builder = PCBuilder()
    
    try:
        if data.get('cpu'):
            builder.set_cpu(int(data['cpu']))
        if data.get('motherboard'):
            builder.set_motherboard(int(data['motherboard']))
        if data.get('ram'):
            builder.set_ram(int(data['ram']))
        if data.get('gpu'):
            builder.set_gpu(int(data['gpu']))
        if data.get('storage'):
            builder.set_storage(int(data['storage']))
        if data.get('cooling'):
            builder.set_cooling(int(data['cooling']))
        if data.get('case'):
            builder.set_case(int(data['case']))
        if data.get('psu'):
            builder.set_psu(int(data['psu']))
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    # Проверка совместимости
    compatibility = builder.check_compatibility()
    
    # Формируем список выбранных компонентов
    selected_components = []
    
    if builder.build.cpu:
        selected_components.append(get_component_details(builder.build.cpu))
    if builder.build.motherboard:
        selected_components.append(get_component_details(builder.build.motherboard))
    if builder.build.ram:
        selected_components.append(get_component_details(builder.build.ram))
    if builder.build.gpu:
        selected_components.append(get_component_details(builder.build.gpu))
    if builder.build.storage:
        selected_components.append(get_component_details(builder.build.storage))
    if builder.build.cooling:
        selected_components.append(get_component_details(builder.build.cooling))
    if builder.build.case:
        selected_components.append(get_component_details(builder.build.case))
    if builder.build.psu:
        selected_components.append(get_component_details(builder.build.psu))
    
    return jsonify({
        'total_price': format_price(builder.build.get_total_price()),
        'total_tdp': builder.build.get_total_tdp(),
        'components': selected_components,
        'is_compatible': compatibility.is_compatible,
        'errors': compatibility.errors,
        'warnings': compatibility.warnings,
        'contact': {
            'phone': '+7 (999) 123-45-67',
            'email': 'support@pcbuilder.ru'
        }
    })

@app.route('/categories')
def categories_list():
    """Страница со списком всех категорий"""
    categories_data = []
    for key, category in CATEGORIES.items():
        components = category['getter']()
        categories_data.append({
            'key': key,
            'name': category['name'],
            'description': category['description'],
            'icon': category['icon'],
            'count': len(components)
        })
        
    return render_template('categories.html', categories=categories_data)

@app.route('/about')
def about():
    """Страница о проекте"""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
