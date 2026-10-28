"""
Пошаговый мастер сборки ПК с автоматической фильтрацией совместимых компонентов
"""
from builder import PCBuilder


# Порядок выбора: от базовых зависимостей к зависимым
# Это важно — сначала CPU (определяет сокет), потом MB (определяет DDR, форм-фактор),
# потом RAM/Cooling/Storage/Case (зависят от MB и CPU), потом GPU, и в конце PSU
BUILD_STEPS = [
    ('cpu', 'Процессор', 'set_cpu', False),
    ('motherboard', 'Материнская плата', 'set_motherboard', False),
    ('ram', 'Оперативная память', 'set_ram', False),
    ('cooling', 'Охлаждение (кулер)', 'set_cooling', True),   # опционально
    ('storage', 'Накопитель (SSD/HDD)', 'set_storage', True), # опционально
    ('gpu', 'Видеокарта', 'set_gpu', True),                   # опционально
    ('case', 'Корпус', 'set_case', False),
    ('psu', 'Блок питания', 'set_psu', False),
]


def format_component_list(components: list, start_index: int = 1) -> None:
    """Красиво вывести список компонентов"""
    for idx, component in enumerate(components, start=start_index):
        print(f"\n  [{idx}] {component}")
        print(f"      Цена: {component.price:,.2f} руб.".replace(",", " "))


def select_component_step(builder: PCBuilder, component_type: str, 
                          display_name: str, setter_name: str, 
                          optional: bool) -> bool:
    """
    Один шаг выбора компонента.
    Возвращает True если компонент выбран, False если пропущен.
    """
    print(f"\n{'=' * 60}")
    print(f"  ШАГ: Выбор — {display_name}")
    print('=' * 60)
    
    # Получаем ТОЛЬКО совместимые компоненты
    compatible = builder.get_compatible_components(component_type)
    
    if not compatible:
        print("\n  ⚠️  Нет совместимых компонентов данного типа.")
        if optional:
            print("  Шаг пропущен (компонент опциональный).")
            return False
        else:
            print("  Необходимо выбрать другой предыдущий компонент.")
            return False
    
    print(f"\n  Найдено совместимых вариантов: {len(compatible)}")
    format_component_list(compatible)
    
    print("\n  [0] Пропустить этот компонент")
    
    setter = getattr(builder, setter_name)
    
    while True:
        try:
            choice = input(f"\n  Выберите {display_name.lower()} (0-{len(compatible)}): ").strip()
            
            if not choice:
                continue
            
            choice_num = int(choice)
            
            if choice_num == 0:
                if optional:
                    print(f"  ⏭️  {display_name} пропущен.")
                    return False
                else:
                    print(f"  ❌ {display_name} — обязательный компонент. Выберите вариант.")
                    continue
            
            if 1 <= choice_num <= len(compatible):
                selected = compatible[choice_num - 1]
                setter(selected.id)
                print(f"  ✓ Выбрано: {selected.name}")
                return True
            else:
                print(f"  ❌ Введите число от 0 до {len(compatible)}")
        
        except ValueError:
            print("  ❌ Введите корректное число")


def build_wizard(builder: PCBuilder) -> None:
    """Пошаговый мастер сборки ПК"""
    print("\n" + "=" * 60)
    print("  🖥️  МАСТЕР СБОРКИ ПК")
    print("  Компоненты будут подбираться автоматически")
    print("  с учётом совместимости с уже выбранными.")
    print("=" * 60)
    
    # Проходим по всем шагам
    for component_type, display_name, setter_name, optional in BUILD_STEPS:
        select_component_step(
            builder, component_type, display_name, setter_name, optional
        )
    
    # Финальный отчёт
    show_final_report(builder)


def show_final_report(builder: PCBuilder) -> None:
    """Показать итоговый отчёт о сборке"""
    print("\n" + "=" * 60)
    print("  📋 ИТОГОВАЯ КОНФИГУРАЦИЯ")
    print("=" * 60)
    print(builder.build)
    
    # Финальная проверка совместимости (на случай, если что-то пошло не так)
    result = builder.check_compatibility()
    
    print("\n" + "-" * 60)
    print("  ПРОВЕРКА СОВМЕСТИМОСТИ")
    print("-" * 60)
    
    if result.is_compatible and not result.warnings:
        print("  ✅ Все компоненты полностью совместимы!")
        print("  🎉 Сборка готова к заказу.")
    elif result.is_compatible:
        print("  ✅ Критических проблем совместимости нет.")
        print("\n  Предупреждения:")
        for warning in result.warnings:
            print(f"    ⚠️  {warning}")
    else:
        print("  ❌ Обнаружены проблемы совместимости:")
        for error in result.errors:
            print(f"    ❌ {error}")
    
    print("=" * 60)


def main_menu():
    """Главное меню"""
    print("\n" + "=" * 60)
    print("  🖥️  КОНСТРУКТОР ПК")
    print("=" * 60)
    print("  1. 🛠️  Начать сборку ПК (пошаговый мастер)")
    print("  2. 📋 Показать текущую сборку")
    print("  3. 🔄 Проверить совместимость")
    print("  4. 🗑️  Сбросить сборку")
    print("  5. 📦 Посмотреть все компоненты (без фильтрации)")
    print("  0. 🚪 Выход")
    print("=" * 60)


def show_all_components(builder: PCBuilder):
    """Показать все компоненты без фильтрации (для ознакомления)"""
    print("\nВыберите категорию для просмотра:")
    categories = [
        ('cpu', 'Процессоры'),
        ('motherboard', 'Материнские платы'),
        ('ram', 'Оперативная память'),
        ('gpu', 'Видеокарты'),
        ('storage', 'Накопители'),
        ('psu', 'Блоки питания'),
        ('case', 'Корпуса'),
        ('cooling', 'Охлаждение')
    ]
    
    for idx, (_, name) in enumerate(categories, 1):
        print(f"  {idx}. {name}")
    
    choice = input("\nВаш выбор (0 — назад): ").strip()
    
    if choice == '0' or not choice.isdigit():
        return
    
    choice_num = int(choice)
    if 1 <= choice_num <= len(categories):
        component_type = categories[choice_num - 1][0]
        builder.display_components(component_type)
    else:
        print("❌ Неверный выбор")


def main():
    """Главная функция"""
    builder = PCBuilder()
    
    while True:
        main_menu()
        choice = input("\n  Ваш выбор: ").strip()
        
        if choice == '0':
            print("\n  👋 До свидания! Удачных сборок!")
            break
        elif choice == '1':
            build_wizard(builder)
        elif choice == '2':
            print("\n" + str(builder.build))
        elif choice == '3':
            result = builder.check_compatibility()
            print("\n" + str(result))
        elif choice == '4':
            builder.reset()
            print("  ✓ Сборка сброшена")
        elif choice == '5':
            show_all_components(builder)
        else:
            print("  ❌ Неверный выбор")


if __name__ == "__main__":
    main()