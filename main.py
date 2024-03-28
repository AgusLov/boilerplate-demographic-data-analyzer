
# Este es un archivo "entrypoint" que se utilizará en el desarrollo. Comienza
# leyendo README.mdimport demographic_data_analyzer
from unittest import main

# Llama a tu función aquí para probarla
demographic_data_analyzer.calculate_demographic_data()

# Ejecuta las pruebas unitarias automáticamente
main(module='test_module', exit=False)