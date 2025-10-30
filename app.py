"""
Aplicación simple de cálculo de facturas para demostrar CI/CD
"""

class Factura:
    """Clase para gestionar facturas"""
    
    def __init__(self, cliente, items=None):
        """
        Inicializa una factura
        
        Args:
            cliente (str): Nombre del cliente
            items (list): Lista de items con formato {'nombre': str, 'precio': float, 'cantidad': int}
        """
        self.cliente = cliente
        self.items = items or []
        self.descuento = 0
    
    def agregar_item(self, nombre, precio, cantidad=1):
        """Agrega un item a la factura"""
        if precio < 0 or cantidad < 0:
            raise ValueError("Precio y cantidad deben ser positivos")
        
        self.items.append({
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
        })
    
    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento porcentual"""
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("Descuento debe estar entre 0 y 100")
        
        self.descuento = porcentaje
    
    def calcular_subtotal(self):
        """Calcula el subtotal antes de descuento"""
        return sum(item['precio'] * item['cantidad'] for item in self.items)
    
    def calcular_total(self):
        """Calcula el total con descuento aplicado"""
        subtotal = self.calcular_subtotal()
        descuento_amount = subtotal * (self.descuento / 100)
        return subtotal - descuento_amount
    
    def obtener_resumen(self):
        """Retorna un resumen de la factura"""
        return {
            'cliente': self.cliente,
            'items': self.items,
            'subtotal': self.calcular_subtotal(),
            'descuento_porcentaje': self.descuento,
            'total': self.calcular_total()
        }


class CalculadoraImpuestos:
    """Calcula impuestos según país"""
    
    TASAS_IMPUESTO = {
        'PE': 0.18,  # IVA Perú
        'CL': 0.19,  # IVA Chile
        'MX': 0.16,  # IVA México
        'ES': 0.21,  # IVA España
    }
    
    @staticmethod
    def calcular_impuesto(monto, pais='PE'):
        """Calcula el impuesto según el país"""
        if pais not in CalculadoraImpuestos.TASAS_IMPUESTO:
            raise ValueError(f"País {pais} no soportado")
        
        tasa = CalculadoraImpuestos.TASAS_IMPUESTO[pais]
        return monto * tasa
    
    @staticmethod
    def calcular_total_con_impuesto(monto, pais='PE'):
        """Calcula el monto total incluyendo impuesto"""
        impuesto = CalculadoraImpuestos.calcular_impuesto(monto, pais)
        return monto + impuesto


def generar_reporte_factura(factura, pais='PE'):
    """Genera un reporte formateado de la factura"""
    resumen = factura.obtener_resumen()
    total_con_impuesto = CalculadoraImpuestos.calcular_total_con_impuesto(
        resumen['total'], 
        pais
    )
    
    impuesto = total_con_impuesto - resumen['total']
    
    reporte = f"""
╔════════════════════════════════════════╗
║           FACTURA                       ║
╚════════════════════════════════════════╝

Cliente: {resumen['cliente']}

ITEMS:
{chr(10).join(f"  - {item['nombre']}: ${item['precio']:.2f} x {item['cantidad']} = ${item['precio'] * item['cantidad']:.2f}" for item in resumen['items'])}

─────────────────────────────────────────
Subtotal:           ${resumen['subtotal']:.2f}
Descuento ({resumen['descuento_porcentaje']}%):        -${resumen['subtotal'] * (resumen['descuento_porcentaje']/100):.2f}
Subtotal con desc:  ${resumen['total']:.2f}
Impuesto ({pais}):           +${impuesto:.2f}
═════════════════════════════════════════
TOTAL:              ${total_con_impuesto:.2f}
═════════════════════════════════════════
"""
    
    return reporte
