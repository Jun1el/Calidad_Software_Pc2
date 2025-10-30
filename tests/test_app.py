"""
Tests para la aplicación de facturas
"""

import pytest
from app import Factura, CalculadoraImpuestos, generar_reporte_factura


class TestFactura:
    """Tests para la clase Factura"""
    
    def test_crear_factura_vacia(self):
        """Test: crear una factura sin items"""
        factura = Factura("Cliente Test")
        assert factura.cliente == "Cliente Test"
        assert factura.items == []
        assert factura.calcular_total() == 0
    
    def test_agregar_item(self):
        """Test: agregar un item a la factura"""
        factura = Factura("Cliente A")
        factura.agregar_item("Laptop", 1000, 1)
        
        assert len(factura.items) == 1
        assert factura.calcular_subtotal() == 1000
    
    def test_agregar_multiples_items(self):
        """Test: agregar múltiples items"""
        factura = Factura("Cliente B")
        factura.agregar_item("Mouse", 25, 2)
        factura.agregar_item("Teclado", 75, 1)
        
        assert len(factura.items) == 2
        assert factura.calcular_subtotal() == 125  # (25*2) + 75
    
    def test_precio_negativo_rechazado(self):
        """Test: rechazar precio negativo"""
        factura = Factura("Cliente C")
        
        with pytest.raises(ValueError):
            factura.agregar_item("Producto", -50, 1)
    
    def test_cantidad_negativa_rechazada(self):
        """Test: rechazar cantidad negativa"""
        factura = Factura("Cliente D")
        
        with pytest.raises(ValueError):
            factura.agregar_item("Producto", 50, -1)
    
    def test_descuento_valido(self):
        """Test: aplicar descuento válido"""
        factura = Factura("Cliente E")
        factura.agregar_item("Producto", 100, 1)
        factura.aplicar_descuento(10)
        
        assert factura.calcular_total() == 90
    
    def test_descuento_50_porciento(self):
        """Test: descuento del 50%"""
        factura = Factura("Cliente F")
        factura.agregar_item("Producto", 200, 1)
        factura.aplicar_descuento(50)
        
        assert factura.calcular_total() == 100
    
    def test_descuento_inválido_negativo(self):
        """Test: rechazar descuento negativo"""
        factura = Factura("Cliente G")
        
        with pytest.raises(ValueError):
            factura.aplicar_descuento(-10)
    
    def test_descuento_inválido_mayor_100(self):
        """Test: rechazar descuento mayor a 100%"""
        factura = Factura("Cliente H")
        
        with pytest.raises(ValueError):
            factura.aplicar_descuento(150)
    
    def test_resumen_completo(self):
        """Test: obtener resumen completo"""
        factura = Factura("Cliente I")
        factura.agregar_item("Producto A", 100, 2)
        factura.aplicar_descuento(20)
        
        resumen = factura.obtener_resumen()
        
        assert resumen['cliente'] == "Cliente I"
        assert resumen['subtotal'] == 200
        assert resumen['descuento_porcentaje'] == 20
        assert resumen['total'] == 160


class TestCalculadoraImpuestos:
    """Tests para la clase CalculadoraImpuestos"""
    
    def test_impuesto_peru(self):
        """Test: calcular impuesto para Perú (18%)"""
        impuesto = CalculadoraImpuestos.calcular_impuesto(100, 'PE')
        assert impuesto == 18
    
    def test_impuesto_chile(self):
        """Test: calcular impuesto para Chile (19%)"""
        impuesto = CalculadoraImpuestos.calcular_impuesto(100, 'CL')
        assert impuesto == 19
    
    def test_impuesto_mexico(self):
        """Test: calcular impuesto para México (16%)"""
        impuesto = CalculadoraImpuestos.calcular_impuesto(100, 'MX')
        assert impuesto == 16
    
    def test_impuesto_españa(self):
        """Test: calcular impuesto para España (21%)"""
        impuesto = CalculadoraImpuestos.calcular_impuesto(100, 'ES')
        assert impuesto == 21
    
    def test_pais_no_soportado(self):
        """Test: rechazar país no soportado"""
        with pytest.raises(ValueError):
            CalculadoraImpuestos.calcular_impuesto(100, 'US')
    
    def test_total_con_impuesto_peru(self):
        """Test: total con impuesto Perú"""
        total = CalculadoraImpuestos.calcular_total_con_impuesto(100, 'PE')
        assert total == 118
    
    def test_total_con_impuesto_chile(self):
        """Test: total con impuesto Chile"""
        total = CalculadoraImpuestos.calcular_total_con_impuesto(100, 'CL')
        assert total == 119


class TestGenerarReporte:
    """Tests para la generación de reportes"""
    
    def test_generar_reporte_simple(self):
        """Test: generar reporte simple"""
        factura = Factura("Acme Corp")
        factura.agregar_item("Servicio", 500, 1)
        
        reporte = generar_reporte_factura(factura, 'PE')
        
        assert "Acme Corp" in reporte
        assert "500.00" in reporte
        assert "FACTURA" in reporte
    
    def test_generar_reporte_con_descuento(self):
        """Test: generar reporte con descuento"""
        factura = Factura("Cliente X")
        factura.agregar_item("Producto", 1000, 1)
        factura.aplicar_descuento(10)
        
        reporte = generar_reporte_factura(factura, 'PE')
        
        assert "10%" in reporte
        assert "900.00" in reporte or "900" in reporte
