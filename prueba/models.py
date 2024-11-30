from django.db import models

# Create your models here.

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Carrera(models.Model):
    codigo_unico = models.CharField(primary_key=True, max_length=50)
    cod_carrera = models.CharField(max_length=50, blank=True, null=True)
    nomb_carrera = models.CharField(max_length=200, blank=True, null=True)
    nivel_global = models.CharField(max_length=50, blank=True, null=True)
    nivel_carrera_2 = models.CharField(max_length=100, blank=True, null=True)
    dur_total_carr = models.IntegerField(blank=True, null=True)
    jornada = models.CharField(max_length=50, blank=True, null=True)
    modalidad = models.CharField(max_length=50, blank=True, null=True)
    area_cineunesco = models.CharField(max_length=100, blank=True, null=True)
    area_cine_f_97 = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carrera'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estudia(models.Model):
    e_mrun = models.OneToOneField('Estudiante', models.DO_NOTHING, db_column='e_mrun', primary_key=True)  # The composite primary key (e_mrun, c_codigo_unico) found, that is not supported. The first column is selected.
    c_codigo_unico = models.ForeignKey(Carrera, models.DO_NOTHING, db_column='c_codigo_unico')
    cat_periodo = models.CharField(max_length=10, blank=True, null=True)
    anio_ing_carr_ori = models.IntegerField(blank=True, null=True)
    anio_ing_carr_act = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudia'
        unique_together = (('e_mrun', 'c_codigo_unico'),)


class Estudiante(models.Model):
    mrun = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    gen_alu = models.IntegerField(blank=True, null=True)
    rango_edad = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudiante'


class Pertenece(models.Model):
    c_codigo_unico = models.OneToOneField(Carrera, models.DO_NOTHING, db_column='c_codigo_unico', primary_key=True)  # The composite primary key (c_codigo_unico, u_cod_inst) found, that is not supported. The first column is selected.
    u_cod_inst = models.ForeignKey('Universidad', models.DO_NOTHING, db_column='u_cod_inst')

    class Meta:
        managed = False
        db_table = 'pertenece'
        unique_together = (('c_codigo_unico', 'u_cod_inst'),)


class Sede(models.Model):
    nomb_sede = models.CharField(max_length=200, blank=True, null=True)
    cod_sede = models.CharField(primary_key=True, max_length=50)  # The composite primary key (cod_sede, u_cod_inst) found, that is not supported. The first column is selected.
    u_cod_inst = models.ForeignKey('Universidad', models.DO_NOTHING, db_column='u_cod_inst')
    region_sede = models.CharField(max_length=100, blank=True, null=True)
    comuna_sede = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sede'
        unique_together = (('cod_sede', 'u_cod_inst'),)


class Titulados(models.Model):
    cat_periodo = models.CharField(max_length=10, blank=True, null=True)
    codigo_unico = models.CharField(max_length=50, blank=True, null=True)
    mrun = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    gen_alu = models.IntegerField(blank=True, null=True)
    rango_edad = models.CharField(max_length=50, blank=True, null=True)
    anio_ing_carr_ori = models.IntegerField(blank=True, null=True)
    anio_ing_carr_act = models.IntegerField(blank=True, null=True)
    tipo_inst_1 = models.CharField(max_length=100, blank=True, null=True)
    tipo_inst_3 = models.CharField(max_length=100, blank=True, null=True)
    cod_inst = models.CharField(max_length=50, blank=True, null=True)
    nomb_inst = models.CharField(max_length=200, blank=True, null=True)
    cod_sede = models.CharField(max_length=50, blank=True, null=True)
    nomb_sede = models.CharField(max_length=200, blank=True, null=True)
    cod_carrera = models.CharField(max_length=50, blank=True, null=True)
    nomb_carrera = models.CharField(max_length=200, blank=True, null=True)
    nivel_global = models.CharField(max_length=50, blank=True, null=True)
    nivel_carrera_2 = models.CharField(max_length=100, blank=True, null=True)
    dur_total_carr = models.IntegerField(blank=True, null=True)
    region_sede = models.CharField(max_length=100, blank=True, null=True)
    comuna_sede = models.CharField(max_length=100, blank=True, null=True)
    jornada = models.CharField(max_length=50, blank=True, null=True)
    modalidad = models.CharField(max_length=50, blank=True, null=True)
    area_cineunesco = models.CharField(max_length=100, blank=True, null=True)
    area_cine_f_97 = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titulados'


class Universidad(models.Model):
    nomb_inst = models.CharField(max_length=200, blank=True, null=True)
    cod_inst = models.CharField(primary_key=True, max_length=50)
    tipo_inst_1 = models.CharField(max_length=100, blank=True, null=True)
    tipo_inst_3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'universidad'

class Mes(models.Model):
    nombre = models.CharField(primary_key=True, max_length=255)
    numero = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mes'
