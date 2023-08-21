import time

def check_engine_decorator(function):
    def wrapper_function(car):
        print(f"El auto {car} ha ingresado al taller.")
        print("Diagnosticando el motor...")
        time.sleep(2)  # Simulamos un proceso de diagnóstico de 2 segundos
        print("Diagnóstico completo.")
        print("Reparando el motor...")
        time.sleep(3)  # Simulamos un proceso de reparación de 3 segundos
        print("Reparación completa.")
        print(f"El auto {car} está listo para ser entregado.")
        function(car)
    return wrapper_function

@check_engine_decorator
def replace_spark_plugs(car):
    print(f"Se han reemplazado las bujías del auto {car}.")

@check_engine_decorator
def change_oil(car):
    print(f"Se ha cambiado el aceite del auto {car}.")

replace_spark_plugs("Auto1")
print()
change_oil("Auto2")
