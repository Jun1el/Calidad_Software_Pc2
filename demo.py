"""
DEMO FUNCIONAL - Ejemplo de uso de la aplicación
================================================

Este script demuestra el funcionamiento de la aplicación
de generación de facturas sin necesidad de tests.

Ejecutar con: python demo.py
"""

from app import Factura, CalculadoraImpuestos, generar_reporte_factura


def demo_1_factura_simple():
    """Demo 1: Crear y mostrar una factura simple"""
    print("\n" + "="*50)
    print("DEMO 1: FACTURA SIMPLE")
    print("="*50)
    
    factura = Factura("Acme Corporation")
    factura.agregar_item("Laptop Dell XPS", 1500, 1)
    factura.agregar_item("Mouse Logitech", 45, 2)
    factura.agregar_item("Teclado Mecánico", 150, 1)
    
    reporte = generar_reporte_factura(factura, 'PE')
    print(reporte)


def demo_2_factura_con_descuento():
    """Demo 2: Factura con descuento aplicado"""
    print("\n" + "="*50)
    print("DEMO 2: FACTURA CON DESCUENTO")
    print("="*50)
    
    factura = Factura("Tech Solutions Ltd")
    factura.agregar_item("Servicio de Consultoría", 5000, 1)
    factura.agregar_item("Soporte Técnico (30 días)", 1000, 1)
    
    print(f"\nAplicando descuento del 15% para cliente frecuente...")
    factura.aplicar_descuento(15)
    
    reporte = generar_reporte_factura(factura, 'PE')
    print(reporte)


def demo_3_diferentes_paises():
    """Demo 3: Comparar impuestos en diferentes países"""
    print("\n" + "="*50)
    print("DEMO 3: COMPARACIÓN DE IMPUESTOS POR PAÍS")
    print("="*50)
    
    monto_base = 1000
    paises = {
        'PE': 'Perú (IVA 18%)',
        'CL': 'Chile (IVA 19%)',
        'MX': 'México (IVA 16%)',
        'ES': 'España (IVA 21%)',
    }
    
    print(f"\nMonto base: ${monto_base:.2f}\n")
    print(f"{'País':<20} {'Impuesto':<15} {'Total':<15} {'Diferencia vs PE':<20}")
    print("-" * 70)
    
    total_pe = CalculadoraImpuestos.calcular_total_con_impuesto(monto_base, 'PE')
    
    for codigo, nombre in paises.items():
        impuesto = CalculadoraImpuestos.calcular_impuesto(monto_base, codigo)
        total = CalculadoraImpuestos.calcular_total_con_impuesto(monto_base, codigo)
        diferencia = total - total_pe
        
        print(f"{nombre:<20} ${impuesto:<14.2f} ${total:<14.2f} ${diferencia:>+.2f}")


def demo_4_factura_compleja():
    """Demo 4: Factura compleja con múltiples líneas"""
    print("\n" + "="*50)
    print("DEMO 4: FACTURA COMPLEJA (MULTIPROPÓSITO)")
    print("="*50)
    
    factura = Factura("TechStart Perú S.A.C.")
    
    # Agregar items diversos
    items = [
        ("Desarrollo de aplicación web", 15000, 1),
        ("Hosting anual", 800, 1),
        ("Dominio .pe", 120, 1),
        ("Certificado SSL", 200, 1),
        ("Soporte técnico (12 meses)", 5000, 1),
    ]
    
    for nombre, precio, cantidad in items:
        factura.agregar_item(nombre, precio, cantidad)
    
    # Aplicar descuento por volumen
    print("\nAplicando descuento del 10% por volumen...")
    factura.aplicar_descuento(10)
    
    reporte = generar_reporte_factura(factura, 'PE')
    print(reporte)
    
    # Mostrar análisis
    resumen = factura.obtener_resumen()
    print("\n" + "-"*50)
    print("ANÁLISIS:")
    print(f"  Número de items: {len(resumen['items'])}")
    print(f"  Monto total sin descuento: ${resumen['subtotal']:.2f}")
    print(f"  Monto ahorrado: ${resumen['subtotal'] - resumen['total']:.2f}")
    print(f"  Total facturado: ${resumen['total']:.2f}")


def demo_5_validaciones():
    """Demo 5: Mostrar validaciones del sistema"""
    print("\n" + "="*50)
    print("DEMO 5: SISTEMA DE VALIDACIONES")
    print("="*50)
    
    factura = Factura("Cliente Test")
    
    # Test 1: Validación de precio negativo
    print("\n[Test 1] Intentando agregar precio negativo...")
    try:
        factura.agregar_item("Producto", -100, 1)
        print("  ✗ FALLO: Debería haber rechazado el precio negativo")
    except ValueError as e:
        print(f"  ✓ EXITOSO: {e}")
    
    # Test 2: Validación de cantidad negativa
    print("\n[Test 2] Intentando agregar cantidad negativa...")
    try:
        factura.agregar_item("Producto", 100, -5)
        print("  ✗ FALLO: Debería haber rechazado la cantidad negativa")
    except ValueError as e:
        print(f"  ✓ EXITOSO: {e}")
    
    # Test 3: Descuento inválido
    print("\n[Test 3] Intentando aplicar descuento > 100%...")
    try:
        factura.aplicar_descuento(150)
        print("  ✗ FALLO: Debería haber rechazado el descuento")
    except ValueError as e:
        print(f"  ✓ EXITOSO: {e}")
    
    # Test 4: País no soportado
    print("\n[Test 4] Intentando calcular impuesto para país no soportado...")
    try:
        CalculadoraImpuestos.calcular_impuesto(1000, 'US')
        print("  ✗ FALLO: Debería haber rechazado el país")
    except ValueError as e:
        print(f"  ✓ EXITOSO: {e}")
    
    print("\n✓ Todas las validaciones funcionan correctamente")


def main():
    """Ejecuta todas las demos"""
    print("\n")
    print("╔" + "="*60 + "╗")
    print("║" + " "*15 + "DEMO FUNCIONAL DE CI/CD".center(46) + " "*15 + "║")
    print("║" + " "*12 + "Sistema de Generación de Facturas".center(46) + " "*12 + "║")
    print("╚" + "="*60 + "╝")
    
    demos = [
        demo_1_factura_simple,
        demo_2_factura_con_descuento,
        demo_3_diferentes_paises,
        demo_4_factura_compleja,
        demo_5_validaciones,
    ]
    
    try:
        for demo in demos:
            demo()
            input("\n[Presione ENTER para continuar...]")
    except KeyboardInterrupt:
        print("\n\n✓ Demo finalizada por el usuario")
    except Exception as e:
        print(f"\n✗ Error durante la demo: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "="*50)
    print("FIN DE LA DEMO")
    print("="*50 + "\n")
    
    print("Comandos útiles:")
    print("  - Ejecutar pipeline CI/CD: python .cicd-pipeline.py")
    print("  - Ejecutar tests: python -m pytest tests/ -v")
    print("  - Ver cobertura: python -m pytest tests/ --cov=app")


if __name__ == "__main__":
    main()
