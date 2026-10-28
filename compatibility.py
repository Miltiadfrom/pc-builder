"""
Проверка совместимости компонентов ПК
"""
from dataclasses import dataclass
from models import CPU, Motherboard, RAM, GPU, Storage, PSU, Case, Cooling


@dataclass
class CompatibilityResult:
    """Результат проверки совместимости"""
    is_compatible: bool
    errors: list[str]
    warnings: list[str]
    
    def __str__(self) -> str:
        result = []
        if self.is_compatible:
            result.append("✅ Все компоненты совместимы")
        else:
            result.append("❌ Обнаружены проблемы совместимости:")
            for error in self.errors:
                result.append(f"  ❌ {error}")
        
        if self.warnings:
            result.append("\nПредупреждения:")
            for warning in self.warnings:
                result.append(f"  ⚠️  {warning}")
        
        return "\n".join(result)


class CompatibilityChecker:
    """Проверка совместимости компонентов"""
    
    @staticmethod
    def check_compatibility(
        cpu: CPU | None, motherboard: Motherboard | None,
        ram: RAM | None, gpu: GPU | None, storage: Storage | None,
        psu: PSU | None, case: Case | None, cooling: Cooling | None
    ) -> CompatibilityResult:
        errors = []
        warnings = []
        
        # === CPU ↔ Материнская плата ===
        if cpu and motherboard:
            if cpu.socket != motherboard.socket:
                errors.append(
                    f"Процессор {cpu.socket.value} не совместим с платой {motherboard.socket.value}"
                )
        
        # === CPU ↔ RAM (тип памяти) ===
        if cpu and ram:
            if ram.ddr_type not in cpu.supported_ddr_types:
                supported = ", ".join([d.value for d in cpu.supported_ddr_types])
                errors.append(
                    f"Процессор {cpu.name} не поддерживает {ram.ddr_type.value} "
                    f"(поддерживает: {supported})"
                )
            
            # Частота памяти
            if ram.frequency > cpu.max_ram_freq:
                warnings.append(
                    f"Частота памяти {ram.frequency}МГц выше максимально поддерживаемой "
                    f"процессором ({cpu.max_ram_freq}МГц). Память может работать на пониженной частоте."
                )
            
            # Объём памяти
            if ram.capacity > cpu.max_ram_capacity:
                errors.append(
                    f"Объём памяти {ram.capacity}GB превышает максимум процессора "
                    f"({cpu.max_ram_capacity}GB)"
                )
        
        # === Материнская плата ↔ RAM ===
        if motherboard and ram:
            if ram.ddr_type != motherboard.ddr_type:
                errors.append(
                    f"Память {ram.ddr_type.value} не совместима с платой "
                    f"{motherboard.ddr_type.value}"
                )
            
            if ram.capacity > motherboard.max_ram:
                errors.append(
                    f"Объём памяти {ram.capacity}GB превышает максимум платы "
                    f"({motherboard.max_ram}GB)"
                )
            
            if ram.frequency > motherboard.max_ram_freq:
                warnings.append(
                    f"Частота памяти {ram.frequency}МГц выше максимума платы "
                    f"({motherboard.max_ram_freq}МГц)"
                )
        
        # === Материнская плата ↔ Корпус ===
        if motherboard and case:
            if motherboard.form_factor not in case.form_factors:
                errors.append(
                    f"Плата {motherboard.form_factor.value} не помещается в корпус"
                )
        
        # === Материнская плата ↔ Накопитель ===
        if motherboard and storage:
            if storage.interface.value == "NVMe M.2" and motherboard.m2_slots == 0:
                errors.append("На плате нет слотов M.2 для NVMe накопителя")
        
        # === Кулер ↔ CPU ===
        if cooling and cpu:
            if cpu.socket not in cooling.supported_sockets:
                errors.append(f"Кулер не поддерживает сокет {cpu.socket.value}")
            
            if cpu.tdp > cooling.tdp_support:
                warnings.append(
                    f"TDP процессора ({cpu.tdp}W) превышает возможности кулера "
                    f"({cooling.tdp_support}W)"
                )
        
        # === Кулер ↔ Корпус ===
        if cooling and case:
            if cooling.height > case.max_cooler_height:
                errors.append(
                    f"Кулер ({cooling.height}mm) не помещается в корпус "
                    f"(макс. {case.max_cooler_height}mm)"
                )
        
        # === GPU ↔ Корпус ===
        if gpu and case:
            if gpu.length > case.max_gpu_length:
                errors.append(
                    f"Видеокарта ({gpu.length}mm) не помещается в корпус "
                    f"(макс. {case.max_gpu_length}mm)"
                )
        
        # === Блок питания ===
        if psu:
            total_tdp = 100  # базовое потребление
            if cpu:
                total_tdp += cpu.tdp
            if gpu:
                total_tdp += gpu.tdp
            
            required_wattage = int(total_tdp / 0.8)
            if total_tdp > psu.wattage * 0.8:
                errors.append(
                    f"Недостаточная мощность БП. Нужно минимум {required_wattage}W, "
                    f"имеется {psu.wattage}W"
                )
        
        # === Видеокарта и встроенная графика ===
        if cpu and not gpu and not cpu.integrated_graphics:
            warnings.append("У процессора нет встроенной графики — видеокарта обязательна")
        
        return CompatibilityResult(
            is_compatible=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )