from django.db import models

#crear modelo atomico (sin llave foranea)

class Rol(models.Model):
    nombre = models.TextField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

#Modelos con llaves foraneas
class User(models.Model):
    username = models.TextField(max_length=100, unique=True)
    password = models.TextField()
    foto = models.TextField()
    correo = models.TextField(unique=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name="users")

    def __str__(self):
        return f"{self.username} ({self.rol.nombre})"
    
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.TextField(max_length=50)
    apellido = models.TextField(max_length=50)
    cedulaIdentidad = models.TextField(unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Cobrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.TextField(max_length=50)
    apellido = models.TextField(max_length=50)
    cedulaIdentidad = models.TextField(unique=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Prestamo(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="prestamos")
    cobrador = models.ForeignKey(Cobrador, on_delete=models.CASCADE, related_name="prestamos")
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2)
    plazo = models.IntegerField(help_text="Plazo en meses")
    fecha_inicio= models.DateTimeField()
    fecha_fin= models.DateTimeField()
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('finalizado', 'Finalizado'), ('mora', 'En mora')], default='activo')

    def __str__(self):
        return f"Prestamo #{self.id} ({self.client})"
    
class Cuota(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, related_name='cuotas')
    numero_cuota = models.IntegerField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('pagada', 'Pagada'),
            ('vencida', 'Vencida')
        ],
        default='pendiente'
    )

    def _str_(self):
        return f"Cuota {self.numero_cuota} - Préstamo {self.prestamo.id}"

class Pago(models.Model):
    cuota = models.ForeignKey(
        Cuota, on_delete=models.CASCADE, related_name='pagos')
    cobrador = models.ForeignKey(
        Cobrador, on_delete=models.SET_NULL, null=True    )
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(
        max_length=50,
        choices=[
            ('efectivo', 'Efectivo'),
            ('transferencia', 'Transferencia'),
            ('qr', 'QR'),
        ]
    )

    def _str_(self):
        return f"Pago {self.id} - Cuota {self.cuota.id}"