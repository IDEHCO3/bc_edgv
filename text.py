# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class AdmEdifPubMilitarA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipoedifmil = models.CharField(max_length=26, blank=True, null=True)
    tipousoedif = models.CharField(max_length=21, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adm_edif_pub_militar_a'


class AdmEdifPubMilitarP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipoedifmil = models.CharField(max_length=26, blank=True, null=True)
    tipousoedif = models.CharField(max_length=21, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adm_edif_pub_militar_p'


class AdmPostoFiscalP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    tipopostofisc = models.CharField(max_length=22, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adm_posto_fiscal_p'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class EcoEdifAgropecExtVegetalPescaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    tipoedifagropec = models.CharField(max_length=50, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eco_edif_agropec_ext_vegetal_pesca_p'


class EcoEdifIndustrialP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    chamine = models.CharField(max_length=3, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    tipodivisaocnae = models.CharField(max_length=180, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eco_edif_industrial_p'


class EcoExtMineralA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tiposecaocnae = models.CharField(max_length=50, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    tipoextmin = models.CharField(max_length=20, blank=True, null=True)
    tipoprodutoresiduo = models.CharField(max_length=40, blank=True, null=True)
    tipopocomina = models.CharField(max_length=15, blank=True, null=True)
    procextracao = models.CharField(max_length=12, blank=True, null=True)
    formaextracao = models.CharField(max_length=12, blank=True, null=True)
    atividade = models.CharField(max_length=12, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eco_ext_mineral_a'


class EcoExtMineralP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tiposecaocnae = models.CharField(max_length=50, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    tipoextmin = models.CharField(max_length=20, blank=True, null=True)
    tipoprodutoresiduo = models.CharField(max_length=40, blank=True, null=True)
    tipopocomina = models.CharField(max_length=15, blank=True, null=True)
    procextracao = models.CharField(max_length=12, blank=True, null=True)
    formaextracao = models.CharField(max_length=12, blank=True, null=True)
    atividade = models.CharField(max_length=12, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eco_ext_mineral_p'


class EduEdifReligiosaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    religiao = models.CharField(max_length=100, blank=True, null=True)
    tipoedifrelig = models.CharField(max_length=12, blank=True, null=True)
    ensino = models.CharField(max_length=12, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edu_edif_religiosa_p'


class EncEstGeradEnergiaEletricaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    codigoestacao = models.CharField(max_length=30, blank=True, null=True)
    potenciaoutorgada = models.IntegerField(blank=True, null=True)
    potenciafiscalizada = models.IntegerField(blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    tipoestgerad = models.CharField(max_length=15, blank=True, null=True)
    destenergelet = models.CharField(max_length=56, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enc_est_gerad_energia_eletrica_p'


class EncHidreletricaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    potenciaoutorgada = models.IntegerField(blank=True, null=True)
    potenciafiscalizada = models.IntegerField(blank=True, null=True)
    codigohidreletrica = models.CharField(max_length=30, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enc_hidreletrica_p'


class EncTermeletricaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    potenciaoutorgada = models.IntegerField(blank=True, null=True)
    potenciafiscalizada = models.IntegerField(blank=True, null=True)
    combrenovavel = models.CharField(max_length=3, blank=True, null=True)
    tipomaqtermica = models.CharField(max_length=33, blank=True, null=True)
    geracao = models.CharField(max_length=20, blank=True, null=True)
    tipocombustivel = models.CharField(max_length=17, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enc_termeletrica_p'


class EncTorreEnergiaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    alturaestimada = models.FloatField(blank=True, null=True)
    arranjofases = models.CharField(max_length=50, blank=True, null=True)
    ovgd = models.CharField(max_length=12, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    tipotorre = models.CharField(max_length=12, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enc_torre_energia_p'


class HidBancoAreiaA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipobanco = models.CharField(max_length=14, blank=True, null=True)
    situacaoemagua = models.CharField(max_length=17, blank=True, null=True)
    materialpredominante = models.CharField(max_length=27, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_banco_areia_a'


class HidBarragemL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    usoprincipal = models.CharField(max_length=15, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_barragem_l'


class HidCorredeiraL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_corredeira_l'


class HidCorredeiraP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_corredeira_p'


class HidFozMaritimaL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_foz_maritima_l'


class HidIlhaA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipoilha = models.CharField(max_length=8, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_ilha_a'


class HidMassaDaguaA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipomassadagua = models.CharField(max_length=18, blank=True, null=True)
    salinidade = models.CharField(max_length=16, blank=True, null=True)
    regime = models.CharField(max_length=31, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_massa_dagua_a'


class HidQuedaDaguaL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    altura = models.FloatField(blank=True, null=True)
    tipoqueda = models.CharField(max_length=15, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_queda_dagua_l'


class HidQuedaDaguaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    altura = models.FloatField(blank=True, null=True)
    tipoqueda = models.CharField(max_length=15, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_queda_dagua_p'


class HidRecifeA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tiporecife = models.CharField(max_length=16, blank=True, null=True)
    situamare = models.CharField(max_length=35, blank=True, null=True)
    situacaocosta = models.CharField(max_length=12, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_recife_a'


class HidRecifeP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tiporecife = models.CharField(max_length=16, blank=True, null=True)
    situamare = models.CharField(max_length=35, blank=True, null=True)
    situacaocosta = models.CharField(max_length=12, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_recife_p'


class HidRochaEmAguaA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    alturalamina = models.FloatField(blank=True, null=True)
    situacaoemagua = models.CharField(max_length=17, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_rocha_em_agua_a'


class HidRochaEmAguaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    alturalamina = models.FloatField(blank=True, null=True)
    situacaoemagua = models.CharField(max_length=17, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_rocha_em_agua_p'


class HidSumidouroVertedouroP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    causa = models.CharField(max_length=25, blank=True, null=True)
    tiposumvert = models.CharField(max_length=12, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_sumidouro_vertedouro_p'


class HidTerrenoSujeitoInundacaoA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    periodicidadeinunda = models.CharField(max_length=20, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_terreno_sujeito_inundacao_a'


class HidTrechoDrenagemL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    dentrodepoligono = models.CharField(max_length=3, blank=True, null=True)
    compartilhado = models.CharField(max_length=3, blank=True, null=True)
    eixoprincipal = models.CharField(max_length=3, blank=True, null=True)
    caladomax = models.FloatField(blank=True, null=True)
    larguramedia = models.FloatField(blank=True, null=True)
    velocidademedcorrente = models.FloatField(blank=True, null=True)
    profundidademedia = models.FloatField(blank=True, null=True)
    coincidecomdentrode = models.CharField(max_length=35, blank=True, null=True)
    navegabilidade = models.CharField(max_length=16, blank=True, null=True)
    regime = models.CharField(max_length=31, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_trecho_drenagem_l'


class HidTrechoMassaDaguaA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipotrechomassa = models.CharField(max_length=13, blank=True, null=True)
    salinidade = models.CharField(max_length=16, blank=True, null=True)
    regime = models.CharField(max_length=31, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_trecho_massa_dagua_a'


class LimAreaDesenvolvimentoControleA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    classificacao = models.CharField(max_length=100, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_area_desenvolvimento_controle_a'


class LimMarcoDeLimiteP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipomarcolim = models.CharField(max_length=13, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    altitudeortometrica = models.FloatField(blank=True, null=True)
    orgresp = models.CharField(max_length=10, blank=True, null=True)
    sistemageodesico = models.CharField(max_length=16, blank=True, null=True)
    outrarefplan = models.CharField(max_length=20, blank=True, null=True)
    outrarefalt = models.CharField(max_length=20, blank=True, null=True)
    referencialaltim = models.CharField(max_length=16, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_marco_de_limite_p'


class LimMunicipioA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geocodigo = models.CharField(max_length=15, blank=True, null=True)
    anodereferencia = models.IntegerField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_municipio_a'


class LimOutrasUnidProtegidasA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    anocriacao = models.IntegerField(blank=True, null=True)
    sigla = models.CharField(max_length=6, blank=True, null=True)
    areaoficial = models.CharField(max_length=15, blank=True, null=True)
    administracao = models.TextField(blank=True, null=True)
    tipooutunidprot = models.CharField(max_length=30, blank=True, null=True)
    historicomodificacao = models.CharField(max_length=255, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_outras_unid_protegidas_a'


class LimOutrosLimitesOficiaisL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    coincidecomdentrode = models.CharField(max_length=50, blank=True, null=True)
    extensao = models.FloatField(blank=True, null=True)
    obssituacao = models.CharField(max_length=100, blank=True, null=True)
    tipooutlimofic = models.CharField(max_length=50, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_outros_limites_oficiais_l'


class LimPaisA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    sigla = models.CharField(max_length=3, blank=True, null=True)
    codiso3166 = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_pais_a'


class LimTerraIndigenaA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    perimetrooficial = models.FloatField(blank=True, null=True)
    areaoficialha = models.FloatField(blank=True, null=True)
    grupoetnico = models.CharField(max_length=100, blank=True, null=True)
    datasituacaojuridica = models.CharField(max_length=20, blank=True, null=True)
    situacaojuridica = models.CharField(max_length=23, blank=True, null=True)
    nometi = models.CharField(max_length=100, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    codigofunai = models.IntegerField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_terra_indigena_a'


class LimTerraIndigenaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    perimetrooficial = models.FloatField(blank=True, null=True)
    areaoficialha = models.FloatField(blank=True, null=True)
    grupoetnico = models.CharField(max_length=100, blank=True, null=True)
    datasituacaojuridica = models.CharField(max_length=20, blank=True, null=True)
    situacaojuridica = models.CharField(max_length=23, blank=True, null=True)
    nometi = models.CharField(max_length=100, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    codigofunai = models.IntegerField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_terra_indigena_p'


class LimUnidadeConservacaoNaoSnucA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    anocriacao = models.IntegerField(blank=True, null=True)
    sigla = models.CharField(max_length=6, blank=True, null=True)
    areaoficial = models.CharField(max_length=15, blank=True, null=True)
    administracao = models.TextField(blank=True, null=True)
    classificacao = models.CharField(max_length=100, blank=True, null=True)
    atolegal = models.CharField(max_length=100, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_unidade_conservacao_nao_snuc_a'


class LimUnidadeFederacaoA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    sigla = models.CharField(max_length=3, blank=True, null=True)
    geocodigo = models.CharField(max_length=15, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_unidade_federacao_a'


class LimUnidadeProtecaoIntegralA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    anocriacao = models.IntegerField(blank=True, null=True)
    sigla = models.CharField(max_length=6, blank=True, null=True)
    areaoficial = models.CharField(max_length=15, blank=True, null=True)
    administracao = models.TextField(blank=True, null=True)
    atolegal = models.CharField(max_length=100, blank=True, null=True)
    tipounidprotinteg = models.CharField(max_length=100, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_unidade_protecao_integral_a'


class LimUnidadeUsoSustentavelA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    anocriacao = models.IntegerField(blank=True, null=True)
    sigla = models.CharField(max_length=6, blank=True, null=True)
    areaoficial = models.CharField(max_length=15, blank=True, null=True)
    administracao = models.TextField(blank=True, null=True)
    atolegal = models.CharField(max_length=100, blank=True, null=True)
    tipounidusosust = models.CharField(max_length=100, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_unidade_uso_sustentavel_a'


class LocAglomeradoRuralDeExtensaoUrbanaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_aglomerado_rural_de_extensao_urbana_p'


class LocAglomeradoRuralIsoladoP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipoaglomrurisol = models.CharField(max_length=35, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_aglomerado_rural_isolado_p'


class LocAldeiaIndigenaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    codigofunai = models.CharField(max_length=15, blank=True, null=True)
    terraindigena = models.CharField(max_length=100, blank=True, null=True)
    etnia = models.CharField(max_length=100, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_aldeia_indigena_p'


class LocAreaEdificadaA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geocodigo = models.CharField(max_length=15, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_area_edificada_a'


class LocCapitalP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipocapital = models.CharField(max_length=20, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_capital_p'


class LocCidadeP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_cidade_p'


class LocVilaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_vila_p'


class ModeloTeste(models.Model):
    data = models.DateField(blank=True, null=True)
    sigla = models.CharField(max_length=2, blank=True, null=True)
    contador = models.IntegerField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    id_modelo_teste = models.IntegerField(primary_key=True)
    tempo = models.TimeField(blank=True, null=True)
    data_hora = models.DateTimeField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modelo_teste'


class RelCurvaBatimetricaL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    profundidade = models.IntegerField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_curva_batimetrica_l'


class RelCurvaNivelL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    cota = models.IntegerField(blank=True, null=True)
    depressao = models.CharField(max_length=3, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    indice = models.CharField(max_length=16, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_curva_nivel_l'


class RelDunaA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    fixa = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_duna_a'


class RelElementoFisiograficoNaturalL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipoelemnat = models.CharField(max_length=12, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_elemento_fisiografico_natural_l'


class RelElementoFisiograficoNaturalP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipoelemnat = models.CharField(max_length=12, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_elemento_fisiografico_natural_p'


class RelPicoP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_pico_p'


class RelPontoCotadoAltimetricoP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    cota = models.FloatField(blank=True, null=True)
    cotacomprovada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_ponto_cotado_altimetrico_p'


class RelPontoCotadoBatimetricoP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    profundidade = models.FloatField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_ponto_cotado_batimetrico_p'


class Sprint(models.Model):
    id_sprint = models.AutoField(primary_key=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sprint'


class Task(models.Model):
    id_task = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    started = models.DateField(blank=True, null=True)
    due = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)
    id_sprint = models.ForeignKey(Sprint, models.DO_NOTHING, db_column='id_sprint', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task'


class TraEclusaL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    desnivel = models.FloatField(blank=True, null=True)
    largura = models.FloatField(blank=True, null=True)
    extensao = models.FloatField(blank=True, null=True)
    calado = models.FloatField(blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_eclusa_l'


class TraEdifConstPortuariaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipoedifport = models.CharField(max_length=23, blank=True, null=True)
    administracao = models.TextField(blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_edif_const_portuaria_p'


class TraEdifConstrAeroportuariaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    administracao = models.TextField(blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    tipoedifaero = models.CharField(max_length=23, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_edif_constr_aeroportuaria_p'


class TraEdifMetroFerroviariaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    multimodal = models.CharField(max_length=12, blank=True, null=True)
    funcaoedifmetroferrov = models.CharField(max_length=44, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    administracao = models.TextField(blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_edif_metro_ferroviaria_p'


class TraFundeadouroP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    administracao = models.TextField(blank=True, null=True)
    destinacaofundeadouro = models.CharField(max_length=43, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_fundeadouro_p'


class TraPistaPontoPousoP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    largura = models.FloatField(blank=True, null=True)
    extensao = models.FloatField(blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    homologacao = models.CharField(max_length=12, blank=True, null=True)
    tipopista = models.CharField(max_length=14, blank=True, null=True)
    usopista = models.CharField(max_length=15, blank=True, null=True)
    revestimento = models.TextField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_pista_ponto_pouso_p'


class TraPonteL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    tipoponte = models.CharField(max_length=12, blank=True, null=True)
    modaluso = models.CharField(max_length=15, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    vaolivrehoriz = models.FloatField(blank=True, null=True)
    vaovertical = models.FloatField(blank=True, null=True)
    cargasuportmaxima = models.FloatField(blank=True, null=True)
    nrpistas = models.IntegerField(blank=True, null=True)
    nrfaixas = models.IntegerField(blank=True, null=True)
    extensao = models.FloatField(blank=True, null=True)
    largura = models.FloatField(blank=True, null=True)
    posicaopista = models.CharField(max_length=13, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_ponte_l'


class TraSinalizacaoP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    tiposinal = models.CharField(max_length=21, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_sinalizacao_p'


class TraTravessiaL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    tipotravessia = models.CharField(max_length=18, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_travessia_l'


class TraTravessiaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    tipotravessia = models.CharField(max_length=18, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_travessia_p'


class TraTrechoDutoL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    nrdutos = models.IntegerField(blank=True, null=True)
    tipotrechoduto = models.CharField(max_length=22, blank=True, null=True)
    mattransp = models.CharField(max_length=12, blank=True, null=True)
    setor = models.CharField(max_length=21, blank=True, null=True)
    posicaorelativa = models.CharField(max_length=15, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    situacaoespacial = models.CharField(max_length=11, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_trecho_duto_l'


class TraTrechoFerroviarioL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    codtrechoferrov = models.CharField(max_length=25, blank=True, null=True)
    posicaorelativa = models.CharField(max_length=15, blank=True, null=True)
    tipotrechoferrov = models.CharField(max_length=12, blank=True, null=True)
    bitola = models.CharField(max_length=27, blank=True, null=True)
    eletrificada = models.CharField(max_length=12, blank=True, null=True)
    nrlinhas = models.CharField(max_length=12, blank=True, null=True)
    emarruamento = models.CharField(max_length=12, blank=True, null=True)
    jurisdicao = models.TextField(blank=True, null=True)
    administracao = models.TextField(blank=True, null=True)
    concessionaria = models.CharField(max_length=100, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    cargasuportmaxima = models.FloatField(blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_trecho_ferroviario_l'


class TraTrechoHidroviarioL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    extensaotrecho = models.FloatField(blank=True, null=True)
    caladomaxseca = models.FloatField(blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    regime = models.CharField(max_length=31, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_trecho_hidroviario_l'


class TraTrechoRodoviarioL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    codtrechorodov = models.CharField(max_length=25, blank=True, null=True)
    tipotrechorod = models.TextField(blank=True, null=True)
    jurisdicao = models.TextField(blank=True, null=True)
    administracao = models.TextField(blank=True, null=True)
    concessionaria = models.CharField(max_length=100, blank=True, null=True)
    revestimento = models.TextField(blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    nrpistas = models.IntegerField(blank=True, null=True)
    nrfaixas = models.IntegerField(blank=True, null=True)
    trafego = models.TextField(blank=True, null=True)
    canteirodivisorio = models.CharField(max_length=4, blank=True, null=True)
    capaccarga = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_trecho_rodoviario_l'


class TraTunelL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    modaluso = models.CharField(max_length=15, blank=True, null=True)
    nrpistas = models.IntegerField(blank=True, null=True)
    nrfaixas = models.IntegerField(blank=True, null=True)
    extensao = models.FloatField(blank=True, null=True)
    altura = models.FloatField(blank=True, null=True)
    largura = models.FloatField(blank=True, null=True)
    posicaopista = models.CharField(max_length=13, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    tipotunel = models.CharField(max_length=28, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_tunel_l'


class VegBrejoPantanoA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    alturamediaindividuos = models.FloatField(blank=True, null=True)
    classificacaoporte = models.CharField(max_length=12, blank=True, null=True)
    tipobrejopantano = models.CharField(max_length=27, blank=True, null=True)
    denso = models.CharField(max_length=12, blank=True, null=True)
    antropizada = models.CharField(max_length=23, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veg_brejo_pantano_a'


class VegMangueA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    alturamediaindividuos = models.FloatField(blank=True, null=True)
    classificacaoporte = models.CharField(max_length=12, blank=True, null=True)
    denso = models.CharField(max_length=12, blank=True, null=True)
    antropizada = models.CharField(max_length=23, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veg_mangue_a'


class VegVegRestingaA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    alturamediaindividuos = models.FloatField(blank=True, null=True)
    classificacaoporte = models.CharField(max_length=12, blank=True, null=True)
    denso = models.CharField(max_length=12, blank=True, null=True)
    antropizada = models.CharField(max_length=23, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1024, blank=True, null=True)
    iri_style = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veg_veg_restinga_a'
