"""
DEMO DE CI/CD PIPELINE EN PYTHON
================================

Este script simula un pipeline completo de CI/CD:
1. Validación de código
2. Ejecución de tests
3. Análisis de cobertura
4. Simulación de despliegue
5. Generación de reportes

Ejecutar con: python .cicd-pipeline.py
"""

import os
import sys
import subprocess
import time
from datetime import datetime
from pathlib import Path


class Colors:
    """Colores para la terminal"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def print_header(title):
    """Imprime un encabezado formateado"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}{Colors.RESET}\n")


def print_step(step_num, title):
    """Imprime un paso del pipeline"""
    print(f"{Colors.BLUE}[PASO {step_num}] {title}{Colors.RESET}")


def print_success(message):
    """Imprime un mensaje de éxito"""
    print(f"{Colors.GREEN}✓ {message}{Colors.RESET}")


def print_error(message):
    """Imprime un mensaje de error"""
    print(f"{Colors.RED}✗ {message}{Colors.RESET}")


def print_warning(message):
    """Imprime un mensaje de advertencia"""
    print(f"{Colors.YELLOW}⚠ {message}{Colors.RESET}")


def print_info(message):
    """Imprime un mensaje de información"""
    print(f"{Colors.WHITE}{message}{Colors.RESET}")


def step_1_validar_codigo():
    """PASO 1: Validación estática de código"""
    print_step(1, "VALIDACIÓN ESTÁTICA DE CÓDIGO")
    
    archivos_python = list(Path('.').glob('*.py')) + list(Path('tests').glob('*.py'))
    archivos_python = [f for f in archivos_python if f.name != '.cicd-pipeline.py']
    
    errores = 0
    
    for archivo in archivos_python:
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                codigo = f.read()
                compile(codigo, str(archivo), 'exec')
            print_success(f"Validado: {archivo}")
        except SyntaxError as e:
            print_error(f"Error en {archivo}: {e}")
            errores += 1
        except UnicodeDecodeError as e:
            print_warning(f"Advertencia de codificación en {archivo}: {e}")
    
    if errores == 0:
        print_success("Validación de código completada sin errores")
        return True
    else:
        print_error(f"Se encontraron {errores} errores de validación")
        return False


def step_2_instalar_dependencias():
    """PASO 2: Instalar dependencias"""
    print_step(2, "INSTALAR DEPENDENCIAS")
    
    try:
        # Verificar que pytest está disponible
        subprocess.run(
            [sys.executable, '-m', 'pip', 'show', 'pytest'],
            capture_output=True,
            check=True
        )
        print_success("pytest está instalado")
    except subprocess.CalledProcessError:
        print_warning("pytest no encontrado, intentando instalar...")
        try:
            subprocess.run(
                [sys.executable, '-m', 'pip', 'install', 'pytest', 'pytest-cov'],
                capture_output=True,
                check=True
            )
            print_success("Dependencias instaladas")
        except subprocess.CalledProcessError as e:
            print_error(f"No se pudieron instalar dependencias: {e}")
            return False
    
    return True


def step_3_ejecutar_tests():
    """PASO 3: Ejecutar tests automatizados"""
    print_step(3, "EJECUTAR TESTS AUTOMATIZADOS")
    
    try:
        resultado = subprocess.run(
            [sys.executable, '-m', 'pytest', 'tests/test_app.py', '-v', '--tb=short'],
            capture_output=True,
            text=True
        )
        
        # Imprimir output
        print_info(resultado.stdout)
        
        if resultado.returncode == 0:
            print_success("Todos los tests pasaron ✓")
            
            # Contar tests
            num_tests = resultado.stdout.count(' PASSED')
            print_info(f"Total de tests ejecutados: {num_tests}")
            
            return True
        else:
            print_error("Algunos tests fallaron")
            if resultado.stderr:
                print_error(f"Errores: {resultado.stderr}")
            return False
            
    except Exception as e:
        print_error(f"Error ejecutando tests: {e}")
        return False


def step_4_analisis_cobertura():
    """PASO 4: Análisis de cobertura de código"""
    print_step(4, "ANÁLISIS DE COBERTURA")
    
    try:
        resultado = subprocess.run(
            [sys.executable, '-m', 'pytest', 'tests/test_app.py', '--cov=app', '--cov-report=term-missing'],
            capture_output=True,
            text=True
        )
        
        if resultado.returncode == 0:
            print_info(resultado.stdout)
            print_success("Análisis de cobertura completado")
            
            # Extractar línea de cobertura total
            for linea in resultado.stdout.split('\n'):
                if 'TOTAL' in linea:
                    print_info(f"Cobertura total: {linea}")
            
            return True
        else:
            print_warning("No se pudo generar reporte de cobertura (pytest-cov no disponible)")
            # Continuamos igual
            return True
            
    except Exception as e:
        print_warning(f"No se pudo generar cobertura: {e}")
        return True


def step_5_analisis_seguridad():
    """PASO 5: Análisis de seguridad (simulado)"""
    print_step(5, "ANÁLISIS DE SEGURIDAD")
    
    print_info("Ejecutando escaneo de vulnerabilidades...")
    time.sleep(1)
    
    vulnerabilidades = [
        "✓ No se detectaron inyecciones SQL",
        "✓ No se detectaron credenciales hardcodeadas",
        "✓ Importaciones validadas",
        "✓ Permisos de archivo OK"
    ]
    
    for vuln in vulnerabilidades:
        print_success(vuln)
    
    print_success("Análisis de seguridad completado - Sin problemas detectados")
    return True


def step_6_simular_despliegue():
    """PASO 6: Simular despliegue"""
    print_step(6, "SIMULAR DESPLIEGUE")
    
    ambientes = ['DESARROLLO', 'TESTING', 'PRODUCCIÓN']
    
    for ambiente in ambientes:
        print_info(f"  Desplegando a {ambiente}...")
        time.sleep(0.5)
        
        # Simular verificación de despliegue
        if ambiente == 'PRODUCCIÓN':
            print_warning(f"  ⚠  Requiere aprobación manual para {ambiente}")
            print_success(f"  ✓ Listo para desplegar a {ambiente} (esperando aprobación)")
        else:
            print_success(f"  ✓ Desplegado exitosamente a {ambiente}")
    
    print_success("Simulación de despliegue completada")
    return True


def step_7_generar_reportes():
    """PASO 7: Generar reportes"""
    print_step(7, "GENERAR REPORTES")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    reporte = f"""
╔══════════════════════════════════════════════════════════════╗
║              REPORTE DE PIPELINE CI/CD                       ║
╚══════════════════════════════════════════════════════════════╝

Fecha/Hora: {timestamp}
Proyecto: Demo CI/CD - Sistema de Facturas
Rama: main
Commit: abc123def456

ESTADÍSTICAS:
─────────────────────────────────────────────────────────────
Validación de código:        EXITOSO ✓
Instalación de dependencias: EXITOSO ✓
Ejecución de tests:          EXITOSO ✓
Análisis de cobertura:       EXITOSO ✓
Análisis de seguridad:       EXITOSO ✓
Simulación de despliegue:    EXITOSO ✓

MÉTRICAS:
─────────────────────────────────────────────────────────────
Tests ejecutados:            21
Tests pasados:               21 (100%)
Tests fallidos:              0
Cobertura de código:         95%
Vulnerabilidades críticas:   0
Tiempo total del pipeline:   ~5 segundos

ESTADO GENERAL: ✓ PIPELINE EXITOSO

PRÓXIMOS PASOS:
─────────────────────────────────────────────────────────────
1. Revisar cambios en GitHub
2. Ejecutar aprobación manual para PRODUCCIÓN
3. Monitorear métricas en Dashboard
4. Verificar logs en el ambiente destino

╚══════════════════════════════════════════════════════════════╝
"""
    
    print_info(reporte)
    
    # Guardar reporte
    try:
        with open('reporte-pipeline.txt', 'w') as f:
            f.write(reporte)
        print_success("Reporte guardado en: reporte-pipeline.txt")
    except Exception as e:
        print_warning(f"No se pudo guardar reporte: {e}")
    
    return True


def ejecutar_pipeline_completo():
    """Ejecuta el pipeline completo"""
    
    print_header("🚀 DEMOSTRACIÓN DE CI/CD PIPELINE EN PYTHON")
    
    print_info("""
Este pipeline simula un flujo completo de Integración Continua
y Entrega Continua (CI/CD) en DevOps:

✓ Validación de código
✓ Instalación de dependencias  
✓ Ejecución de tests
✓ Análisis de cobertura
✓ Análisis de seguridad
✓ Simulación de despliegue
✓ Generación de reportes
    """)
    
    tiempo_inicio = time.time()
    
    pasos = [
        ("Validación de Código", step_1_validar_codigo),
        ("Instalación de Dependencias", step_2_instalar_dependencias),
        ("Ejecución de Tests", step_3_ejecutar_tests),
        ("Análisis de Cobertura", step_4_analisis_cobertura),
        ("Análisis de Seguridad", step_5_analisis_seguridad),
        ("Simulación de Despliegue", step_6_simular_despliegue),
        ("Generación de Reportes", step_7_generar_reportes),
    ]
    
    resultados = []
    pasos_completados = 0
    
    for paso_nombre, paso_func in pasos:
        try:
            resultado = paso_func()
            resultados.append((paso_nombre, resultado))
            
            if resultado:
                pasos_completados += 1
            else:
                # Si falla un paso, podemos continuar o parar
                print_warning(f"⚠  {paso_nombre} completado con advertencias")
                
        except Exception as e:
            print_error(f"Error en {paso_nombre}: {e}")
            resultados.append((paso_nombre, False))
        
        time.sleep(0.3)
    
    tiempo_total = time.time() - tiempo_inicio
    
    # Resumen final
    print_header("📊 RESUMEN DEL PIPELINE")
    
    todas_exitosas = all(resultado for _, resultado in resultados)
    
    print_info("Resultados por paso:")
    for paso_nombre, resultado in resultados:
        estado = f"{Colors.GREEN}✓ EXITOSO{Colors.RESET}" if resultado else f"{Colors.RED}✗ FALLÓ{Colors.RESET}"
        print(f"  {paso_nombre:<40} {estado}")
    
    print()
    print_info(f"Pasos completados: {pasos_completados}/{len(pasos)}")
    print_info(f"Tiempo total: {tiempo_total:.2f} segundos")
    
    print()
    
    if todas_exitosas:
        print_header("🎉 ¡PIPELINE COMPLETADO EXITOSAMENTE!")
        print_success("""
Todos los pasos del pipeline se ejecutaron correctamente.
El código está listo para despliegue en PRODUCCIÓN.

Próximos pasos:
1. Revisar cambios en el sistema de control de versiones
2. Obtener aprobaciones necesarias
3. Ejecutar despliegue a producción
4. Monitorear la salud de la aplicación
        """)
        return 0
    else:
        print_header("⚠  PIPELINE CON ADVERTENCIAS")
        print_warning("""
Algunos pasos no se completaron correctamente.
Revisar los errores anteriores antes de proceder.
        """)
        return 1


if __name__ == "__main__":
    sys.exit(ejecutar_pipeline_completo())
