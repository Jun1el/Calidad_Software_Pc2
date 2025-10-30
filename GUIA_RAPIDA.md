# 🚀 GUÍA RÁPIDA - CÓMO EJECUTAR EL PROYECTO

## Paso 1: Abrir Terminal
Abre una terminal PowerShell o CMD en la carpeta del proyecto.

## Paso 2: Instalar Dependencias (Primera vez)
```bash
pip install -r requirements.txt
```

## Paso 3: ¡EJECUTAR LA DEMO!

### Opción A: Ver el Pipeline CI/CD Completo ⭐ (RECOMENDADO)
```bash
python .cicd-pipeline.py
```
Esto ejecutará:
- Validación de código
- 19 tests automatizados
- Análisis de cobertura (100%)
- Análisis de seguridad
- Simulación de despliegue
- Generación de reportes

**Tiempo:** ~20 segundos

---

### Opción B: Demo Interactiva de la Aplicación
```bash
python demo.py
```
Verás 5 demostraciones diferentes de facturas (presiona ENTER para pasar)

**Demostraciones incluidas:**
1. Factura simple
2. Factura con descuento
3. Comparación de impuestos por país
4. Factura compleja
5. Sistema de validaciones

**Tiempo:** ~2-3 minutos (interactivo)

---

### Opción C: Ejecutar Tests Directamente
```bash
python -m pytest tests/ -v
```

Con reporte de cobertura:
```bash
python -m pytest tests/ --cov=app --cov-report=term-missing
```

**Resultado esperado:**
```
19 passed in 0.11s
Coverage: 100%
```

---

## 📁 Archivos Principales

| Archivo | Descripción |
|---------|-------------|
| `app.py` | Aplicación de facturas (código a probar) |
| `tests/test_app.py` | 19 tests unitarios |
| `.cicd-pipeline.py` | Pipeline CI/CD automatizado |
| `demo.py` | Demostración interactiva |
| `requirements.txt` | Dependencias necesarias |

---

## ✅ Qué Esperar

### Ejecución Exitosa del Pipeline
```
✓ Validación de Código                     EXITOSO
✓ Instalación de Dependencias              EXITOSO
✓ Ejecución de Tests                       EXITOSO (19/19)
✓ Análisis de Cobertura                    EXITOSO (100%)
✓ Análisis de Seguridad                    EXITOSO
✓ Simulación de Despliegue                 EXITOSO
✓ Generación de Reportes                   EXITOSO

🎉 PIPELINE COMPLETADO EXITOSAMENTE!
```

### Ejecución de Tests
```
tests/test_app.py::TestFactura::test_crear_factura_vacia PASSED          [  5%]
tests/test_app.py::TestFactura::test_agregar_item PASSED                 [ 10%]
...
============================= 19 passed in 0.11s ==============================
```

### Demo Interactiva
```
╔════════════════════════════════════════╗
║           FACTURA                       ║
╚════════════════════════════════════════╝

Cliente: Acme Corporation

ITEMS:
  - Laptop Dell XPS: $1500.00 x 1 = $1500.00
  - Mouse Logitech: $45.00 x 2 = $90.00

Subtotal:           $1590.00
Impuesto (PE):      +$286.20
═════════════════════════════════════════
TOTAL:              $1876.20
```

---

## ⚡ Comandos Rápidos

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar pipeline CI/CD
python .cicd-pipeline.py

# Ejecutar demo
python demo.py

# Ejecutar tests
python -m pytest tests/ -v

# Tests con cobertura
python -m pytest tests/ --cov=app --cov-report=term-missing

# Un solo test
python -m pytest tests/test_app.py::TestFactura::test_crear_factura_vacia -v

# Tests con stop en primer fallo
python -m pytest tests/ -x

# Tests en modo verbose con salida
python -m pytest tests/ -vv -s
```

---

## 🐛 Solución de Problemas

### "No module named 'pytest'"
```bash
pip install pytest pytest-cov
```

### "ModuleNotFoundError: No module named 'app'"
Asegúrate de estar en la carpeta correcta:
```bash
cd "c:\Users\Andres\Documents\Calidad de Software\PC2_LaTorre"
```

### Tests no se ejecutan
```bash
# Verifica que pytest esté instalado
python -m pytest --version

# Si no, instala:
pip install -U pytest pytest-cov
```

---

## 📊 Estructura del Proyecto Explicada

```
PC2_LaTorre/                    # Carpeta principal
│
├── app.py                      # Código principal de la aplicación
│   ├── Factura                 # Clase para gestionar facturas
│   ├── CalculadoraImpuestos    # Clase para calcular impuestos
│   └── generar_reporte_factura()  # Función para reportes
│
├── tests/                      # Carpeta de tests
│   └── test_app.py            # 19 tests unitarios
│       ├── TestFactura         # 10 tests de facturas
│       ├── TestCalculadoraImpuestos  # 7 tests de impuestos
│       └── TestGenerarReporte  # 2 tests de reportes
│
├── .cicd-pipeline.py          # ⭐ Pipeline CI/CD (¡EJECUTAR ESTO!)
│   ├── Step 1: Validación
│   ├── Step 2: Dependencias
│   ├── Step 3: Tests
│   ├── Step 4: Cobertura
│   ├── Step 5: Seguridad
│   ├── Step 6: Despliegue
│   └── Step 7: Reportes
│
├── demo.py                    # Demo interactiva
│   ├── Demo 1: Factura simple
│   ├── Demo 2: Con descuento
│   ├── Demo 3: Comparación impuestos
│   ├── Demo 4: Factura compleja
│   └── Demo 5: Validaciones
│
├── requirements.txt           # Dependencias (pytest, pytest-cov)
├── README.md                  # Documentación completa
└── RESUMEN_EJECUTIVO.md      # Este archivo
```

---

## 🎓 Conceptos Demostrados

### 1. Continuous Integration (CI)
- ✓ Validación automática de código
- ✓ Ejecución de tests en cada cambio
- ✓ Detección temprana de errores

### 2. Continuous Deployment (CD)
- ✓ Despliegue automatizado a múltiples ambientes
- ✓ Requerimientos de aprobación manual para producción

### 3. DevOps
- ✓ Automatización completa del workflow
- ✓ Feedback loops rápidos
- ✓ Monitoreo y reportes

### 4. Testing
- ✓ 19 tests unitarios
- ✓ 100% de cobertura de código
- ✓ Validaciones en cada paso

---

## 💡 Variaciones para Experimentar

### Romper un Test Propositivamente
Edita `app.py` y cambia un número en la clase `CalculadoraImpuestos`:
```python
TASAS_IMPUESTO = {
    'PE': 0.20,  # Cambiar de 0.18 a 0.20
    ...
}
```
Luego ejecuta: `python .cicd-pipeline.py`
Verás que los tests fallan (¡como debe ser!)

### Agregar Más Tests
Edita `tests/test_app.py` y agrega más funciones `test_*`:
```python
def test_nuevo():
    factura = Factura("Test")
    # Tu test aquí
    assert factura.cliente == "Test"
```

### Agregar Nuevas Funcionalidades
Edita `app.py` para agregar nuevas clases o métodos, luego agrega tests para ellos.

---

## 📈 Métricas del Proyecto

| Métrica | Valor |
|---------|-------|
| Líneas de código (app.py) | ~120 |
| Líneas de tests | ~180 |
| Funciones/Métodos | 12 |
| Clases | 3 |
| Tests | 19 |
| Cobertura | 100% |
| Tiempo de ejecución | 20 segundos |

---

## 🎯 Próximos Pasos Sugeridos

1. **Extensión:** Agregar más validaciones o funcionalidades
2. **Integración:** Conectar con GitHub Actions o GitLab CI
3. **Contenerización:** Crear un Dockerfile
4. **Web:** Crear una interfaz web con Flask/FastAPI
5. **Base de datos:** Agregar persistencia con SQLite o PostgreSQL

---

## 📞 Preguntas Comunes

**P: ¿Puedo modificar el código?**
R: ¡Sí! Modifica `app.py` y verifica que los tests sigan pasando con `pytest`.

**P: ¿Puedo agregar más tests?**
R: ¡Absolutamente! Edita `tests/test_app.py` y agrega más funciones `test_*`.

**P: ¿Cómo sé si el pipeline funcionó?**
R: Si ves "PIPELINE COMPLETADO EXITOSAMENTE!" al final, ¡todo está bien!

**P: ¿Qué pasa si un test falla?**
R: El pipeline detiene y te muestra qué falló. Es así de propósito para detectar errores rápido.

---

## ✨ Conclusión

¡Este proyecto demuestra CI/CD de forma funcional y educativa! 

**Pasos principales:**
1. Instala dependencias: `pip install -r requirements.txt`
2. Ejecuta: `python .cicd-pipeline.py` o `python demo.py`
3. ¡Observa la magia de CI/CD en acción!

**¡Diviértete experimentando! 🚀**
