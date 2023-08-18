from django.db import models


class Cargo(models.Model):
    carg_ID = models.AutoField('Id',primary_key=True)
    Carg_descrip = models.CharField('Descripcion',max_length = 50, blank=True,null=True)
    Carg_salario = models.FloatField('Salario',max_length=10, blank=False, null=False)

    class Meta:
        verbose_name='Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return '{}'.format(self.Carg_descrip)


class Empleados(models.Model):
    Emp_ID = models.AutoField('Id',primary_key=True)
    Emp_nombre = models.CharField('Nombre',max_length=50, blank=False, null=False)
    Emp_apellido = models.CharField('Apellido',max_length=50, blank=False, null=False)
    Emp_direccion = models.CharField('Direccion',max_length=200, blank=False, null=False)
    Emp_cedula = models.CharField('Cedula', max_length=10, blank=False, null=False, unique=True)
    Emp_telefono = models.CharField('Telefono',max_length=10, blank=True, null=True)
    Emp_cargo_id = models.ForeignKey(Cargo, on_delete=models.CASCADE)


    class Meta:
        verbose_name='Empleado'
        verbose_name_plural = 'Cobrador'

    def __str__(self):
        return '{}''{}''{}'.format(self.Emp_nombre ," ",self.Emp_apellido)

class proveedores(models.Model):
    Prov_ID=models.AutoField('Id',primary_key=True)
    Prov_nit=models.CharField('Nit',max_length=16, blank=False, null=False, unique=True)
    Prov_nombre=models.CharField('Nombre',max_length=200, blank=False, null=False)
    Prov_replegal=models.CharField('Representante legal',max_length=200, blank=False, null=False)
    Prov_ciudad=models.CharField('Ciudad',max_length=50, blank=False, null=False)
    Prov_direccion=models.CharField('Direccion',max_length=200, blank=False, null=False)
    Prov_telefono=models.CharField('Telefono',max_length=10, blank=False, null=False)


    class Meta:
        verbose_name='Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return '{}'.format(self.Prov_nombre)

class categoria_pro(models.Model):
    Cate_id=models.AutoField('Id',primary_key=True)
    Cate_nombre=models.CharField('Nombre',max_length=50, blank=False, null=False )
    Cate_descripcion=models.TextField('Descripcion',blank=True, null=True)


    class Meta:
        verbose_name='Categoria productos'
        verbose_name_plural = 'Categorias productos'

    def __str__(self):
        return '{}'.format(self.Cate_nombre)


class productos(models.Model):
    Prod_id = models.AutoField('Id',primary_key=True)
    Prod_categoria = models.ForeignKey(categoria_pro,on_delete=models.CASCADE)
    Prod_nombre = models.CharField('Nombre',max_length=50, blank=False, null=False )
    Prod_embalaje = models.CharField('Embalaje',max_length=50, blank=False, null=False )
    Prod_cantidad = models.IntegerField('Cantidad',max_length=4, blank=False, null=False )
    Prod_precioin = models.FloatField('Precio inicial',max_length=6, blank=False, null=False )
    Prod_preciomayor = models.FloatField('Precio al por mayor',max_length=6, blank=False, null=False )
    Prod_preciopublico = models.FloatField('Precio a el publico',max_length=6, blank=False, null=False )
    Prod_provedor = models.ForeignKey(proveedores,on_delete=models.CASCADE)


    class Meta:
        verbose_name='Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return '{}'.format(self.Prod_nombre)


class Factura(models.Model):
    Fac_id=models.AutoField('Id',primary_key=True)
    Fac_codigo=models.CharField('Codigo',max_length=45, blank=False, null=False )
    Fac_fecha=models.DateField('Fecha',blank=False, null=False)
    Fac_cantpro=models.IntegerField('Cantidad de productos',max_length=3, blank=False, null=False )
    Fac_prod=models.ForeignKey(productos,on_delete=models.CASCADE)


    class Meta:
        verbose_name='Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return '{}'.format(self.Fac_codigo)


class Pago_empleado(models.Model):
    Pagemple_id=models.AutoField('Id',primary_key=True)
    Pagemple_empl_id=models.ForeignKey(Empleados,on_delete=models.CASCADE)
    Pagemple_carg_id=models.ForeignKey(Cargo,on_delete=models.CASCADE)
    Pagemple_sueldo=models.FloatField('Sueldo',max_length=50, blank=False, null=False )
    Pagempl_h_extras=models.IntegerField('Horas extras',max_length=10, blank=True, null=True)
    Pagempl_credito=models.FloatField('Credito',max_length=50, blank=True, null=True)
    Pagemple_bono=models.FloatField('Bono',max_length=10, blank=True, null=True)


    class Meta:
        verbose_name='Pago empleado'
        verbose_name_plural = 'Pagos empleados'

    def __str__(self):
        return '{}'.format(self.Pagemple_empl_id)


class clientes(models.Model):
    Cli_id=models.AutoField('Id',primary_key=True)
    Cli_nombre=models.CharField('Nombre',max_length=50, blank=False, null=False )
    Cli_apellido=models.CharField('Apellido',max_length=10, blank=False, null=False )
    Cli_cedula=models.CharField('Cedula',max_length=10, blank=False, null=False, unique=True)
    Cli_ciudad = models.CharField('Ciudad',max_length=50, blank=False, null=False )
    Cli_direccion = models.CharField('Direccion',max_length=50, blank=False, null=False )
    Cli_telefono = models.CharField('Teléfono',max_length=10, blank=True, null=True )


    class Meta:
        verbose_name='Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return '{}'.format(self.Cli_nombre)


class Detalle_fac(models.Model):
    Det_id=models.AutoField('Id',primary_key=True)
    Det_id_cli=models.ForeignKey(clientes,on_delete=models.CASCADE)
    Det_fac_id=models.ForeignKey(Factura,on_delete=models.CASCADE)
    Det_impuesto=models.CharField('Impuesto',max_length=45)


    class Meta:
        verbose_name='Detalle factura'
        verbose_name_plural = 'Detalles Facturas'

    def __str__(self):
        return '{}'.format(self.Det_id)



class Usuarios(models.Model):
    Usu_id=models.AutoField('Id',primary_key=True)
    Usu_emp_id=models.ForeignKey(Empleados,on_delete=models.CASCADE)
    Usu_nombre=models.CharField('Nombre',max_length=10,blank=False, null=False,unique=True)
    Usu_password=models.CharField('Contraseña',max_length=10,blank=False, null=False)
    Usu_cargo_id = models.ForeignKey(Cargo,on_delete=models.CASCADE)


    class Meta:
        verbose_name='Usuarios'
        verbose_name_plural = 'Ususario'

    def __str__(self):
        return '{}'.format(self.Usu_nombre)
