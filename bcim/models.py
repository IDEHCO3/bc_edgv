
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.contrib.gis.db import models


class EdifPubMilitar(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipoedifmil = models.CharField(max_length=26, blank=True, null=True)
    tipousoedif = models.CharField(max_length=21, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'adm_edif_pub_militar_a'


class AdmEdifPubMilitarP(models.Model): #precisa juntar as tabelas
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipoedifmil = models.CharField(max_length=26, blank=True, null=True)
    tipousoedif = models.CharField(max_length=21, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'adm_edif_pub_militar_p'


class PostoFiscal(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    tipopostofisc = models.CharField(max_length=22, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'adm_posto_fiscal_p'



class EdifAgropecExtVegetalPesca(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    tipoedifagropec = models.CharField(max_length=50, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'eco_edif_agropec_ext_vegetal_pesca_p'


class EdifIndustrial(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    chamine = models.CharField(max_length=3, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    tipodivisaocnae = models.CharField(max_length=180, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'eco_edif_industrial_p'


class ExtMineral(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'eco_ext_mineral_a'


class EcoExtMineralP(models.Model):  #precisa juntar as tabelas
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'eco_ext_mineral_p'


class EdifReligiosa(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'edu_edif_religiosa_p'


class Employee(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class EstGeradEnergiaEletrica(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'enc_est_gerad_energia_eletrica_p'


class Hidreletrica(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    potenciaoutorgada = models.IntegerField(blank=True, null=True)
    potenciafiscalizada = models.IntegerField(blank=True, null=True)
    codigohidreletrica = models.CharField(max_length=30, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'enc_hidreletrica_p'


class Termeletrica(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'enc_termeletrica_p'


class TorreEnergia(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'enc_torre_energia_p'


class BancoAreia(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipobanco = models.CharField(max_length=14, blank=True, null=True)
    situacaoemagua = models.CharField(max_length=17, blank=True, null=True)
    materialpredominante = models.CharField(max_length=27, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_banco_areia_a'


class Barragem(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    usoprincipal = models.CharField(max_length=15, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_barragem_l'


class Corredeira(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_corredeira_l'


class HidCorredeiraP(models.Model): #precisa juntar as tabelas
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_corredeira_p'


class FozMaritima(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_foz_maritima_l'


class Ilha(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipoilha = models.CharField(max_length=8, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_ilha_a'


class MassaDagua(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipomassadagua = models.CharField(max_length=18, blank=True, null=True)
    salinidade = models.CharField(max_length=16, blank=True, null=True)
    regime = models.CharField(max_length=31, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_massa_dagua_a'


class QuedaDagua(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    altura = models.FloatField(blank=True, null=True)
    tipoqueda = models.CharField(max_length=15, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_queda_dagua_l'


class HidQuedaDaguaP(models.Model): #precisa juntar tabelas
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    altura = models.FloatField(blank=True, null=True)
    tipoqueda = models.CharField(max_length=15, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_queda_dagua_p'


class Recife(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tiporecife = models.CharField(max_length=16, blank=True, null=True)
    situamare = models.CharField(max_length=35, blank=True, null=True)
    situacaocosta = models.CharField(max_length=12, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_recife_a'


class HidRecifeP(models.Model): #precisa juntar tabelas
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tiporecife = models.CharField(max_length=16, blank=True, null=True)
    situamare = models.CharField(max_length=35, blank=True, null=True)
    situacaocosta = models.CharField(max_length=12, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_recife_p'


class RochaEmAgua(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    alturalamina = models.FloatField(blank=True, null=True)
    situacaoemagua = models.CharField(max_length=17, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_rocha_em_agua_a'


class HidRochaEmAguaP(models.Model): #precisa juntar tabelas
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    alturalamina = models.FloatField(blank=True, null=True)
    situacaoemagua = models.CharField(max_length=17, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_rocha_em_agua_p'


class SumidouroVertedouro(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    causa = models.CharField(max_length=25, blank=True, null=True)
    tiposumvert = models.CharField(max_length=12, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_sumidouro_vertedouro_p'


class TerrenoSujeitoInundacao(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    periodicidadeinunda = models.CharField(max_length=20, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_terreno_sujeito_inundacao_a'


class TrechoDrenagem(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_trecho_drenagem_l'


class TrechoMassaDagua(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipotrechomassa = models.CharField(max_length=13, blank=True, null=True)
    salinidade = models.CharField(max_length=16, blank=True, null=True)
    regime = models.CharField(max_length=31, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'hid_trecho_massa_dagua_a'


class AreaDesenvolvimentoControle(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    classificacao = models.CharField(max_length=100, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'lim_area_desenvolvimento_controle_a'


class MarcoDeLimite(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'lim_marco_de_limite_p'


class Municipio(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geocodigo = models.CharField(max_length=15, blank=True, null=True)
    anodereferencia = models.IntegerField(blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'lim_municipio_a'


class OutrasUnidProtegidas(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    anocriacao = models.IntegerField(null=True)
    sigla = models.CharField(max_length=6, blank=True, null=True)
    areaoficial = models.CharField(max_length=15, blank=True, null=True)
    administracao = models.TextField(blank=True, null=True)
    tipooutunidprot = models.CharField(max_length=30, blank=True, null=True)
    historicomodificacao = models.CharField(max_length=255, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'lim_outras_unid_protegidas_a'


class OutrosLimitesOficiais(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    coincidecomdentrode = models.CharField(max_length=50, blank=True, null=True)
    extensao = models.FloatField(blank=True, null=True)
    obssituacao = models.CharField(max_length=100, blank=True, null=True)
    tipooutlimofic = models.CharField(max_length=50, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'lim_outros_limites_oficiais_l'


class Pais(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    sigla = models.CharField(max_length=3, blank=True, null=True)
    codiso3166 = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'lim_pais_a'


class TerraIndigena(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    codigofunai = models.IntegerField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'lim_terra_indigena_a'


class LimTerraIndigenaP(models.Model): #precisa juntar as tabelas
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    codigofunai = models.IntegerField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'lim_terra_indigena_p'


class UnidadeConservacaoNaoSnuc(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'lim_unidade_conservacao_nao_snuc_a'


class UnidadeFederacao(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    sigla = models.CharField(max_length=3, blank=True, null=True)
    geocodigo = models.CharField(max_length=15, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'lim_unidade_federacao_a'


class UnidadeProtecaoIntegral(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'lim_unidade_protecao_integral_a'


class UnidadeUsoSustentavel(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'lim_unidade_uso_sustentavel_a'


class AglomeradoRuralDeExtensaoUrbana(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'loc_aglomerado_rural_de_extensao_urbana_p'


class AglomeradoRuralIsolado(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipoaglomrurisol = models.CharField(max_length=35, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'loc_aglomerado_rural_isolado_p'


class AldeiaIndigena(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    codigofunai = models.CharField(max_length=15, blank=True, null=True)
    terraindigena = models.CharField(max_length=100, blank=True, null=True)
    etnia = models.CharField(max_length=100, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'loc_aldeia_indigena_p'


class AreaEdificada(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geocodigo = models.CharField(max_length=15, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'loc_area_edificada_a'


class Capital(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipocapital = models.CharField(max_length=20, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'loc_capital_p'


class Cidade(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'loc_cidade_p'


class Vila(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'loc_vila_p'


class Orderpart(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    part_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderpart'


class Part(models.Model):
    part_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'part'


class CurvaBatimetrica(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    profundidade = models.IntegerField(blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'rel_curva_batimetrica_l'


class CurvaNivel(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    cota = models.IntegerField(blank=True, null=True)
    depressao = models.CharField(max_length=3, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    indice = models.CharField(max_length=16, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'rel_curva_nivel_l'


class Duna(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    fixa = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'rel_duna_a'


class ElementoFisiograficoNatural(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipoelemnat = models.CharField(max_length=12, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'rel_elemento_fisiografico_natural_l'


class RelElementoFisiograficoNaturalP(models.Model): #precisa juntar as tabelas
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipoelemnat = models.CharField(max_length=12, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'rel_elemento_fisiografico_natural_p'


class Pico(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'rel_pico_p'


class PontoCotadoAltimetrico(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    cota = models.FloatField(blank=True, null=True)
    cotacomprovada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'rel_ponto_cotado_altimetrico_p'


class PontoCotadoBatimetrico(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    profundidade = models.FloatField(blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'rel_ponto_cotado_batimetrico_p'


class Salesorder(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    ship_date = models.DateField(blank=True, null=True)
    payment = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salesorder'


class Salesorder1(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    customer_oid = models.TextField(blank=True, null=True)  # This field type is a guess.
    employee_oid = models.TextField(blank=True, null=True)  # This field type is a guess.
    part_oid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'salesorder1'


class TLogradouro(models.Model):
    cod_setor = models.BigIntegerField(blank=True, null=True)
    cod_situacao_setor = models.CharField(max_length=2, blank=True, null=True)
    cod_tipo_setor = models.CharField(max_length=2, blank=True, null=True)
    cod_especie = models.CharField(max_length=2, blank=True, null=True)
    nom_tipo_seglogr = models.CharField(max_length=20, blank=True, null=True)
    nom_titulo_seglogr = models.CharField(max_length=30, blank=True, null=True)
    nom_seglogr = models.CharField(max_length=60, blank=True, null=True)
    num_endereco = models.IntegerField(blank=True, null=True)
    dsc_modificador = models.CharField(max_length=7, blank=True, null=True)
    nom_comp_elem1 = models.CharField(max_length=20, blank=True, null=True)
    val_comp_elem1 = models.CharField(max_length=10, blank=True, null=True)
    nom_comp_elem2 = models.CharField(max_length=20, blank=True, null=True)
    val_comp_elem2 = models.CharField(max_length=10, blank=True, null=True)
    nom_comp_elem3 = models.CharField(max_length=20, blank=True, null=True)
    val_comp_elem3 = models.CharField(max_length=10, blank=True, null=True)
    nom_comp_elem4 = models.CharField(max_length=20, blank=True, null=True)
    val_comp_elem4 = models.CharField(max_length=10, blank=True, null=True)
    nom_comp_elem5 = models.CharField(max_length=20, blank=True, null=True)
    val_comp_elem5 = models.CharField(max_length=10, blank=True, null=True)
    nom_comp_elem6 = models.CharField(max_length=20, blank=True, null=True)
    val_comp_elem6 = models.CharField(max_length=10, blank=True, null=True)
    dsc_ponto_referencia = models.CharField(max_length=60, blank=True, null=True)
    dsc_localidade = models.CharField(max_length=60, blank=True, null=True)
    cep_face = models.CharField(max_length=8, blank=True, null=True)
    val_latitude_padrao = models.CharField(max_length=15, blank=True, null=True)
    val_longitude_padrao = models.CharField(max_length=15, blank=True, null=True)
    dsc_estabelecimento = models.CharField(max_length=40, blank=True, null=True)
    cod_indicador_estab_endereco = models.CharField(max_length=1, blank=True, null=True)
    cod_indicador_const_endereco = models.CharField(max_length=1, blank=True, null=True)
    cod_indicador_finalidade_const = models.CharField(max_length=1, blank=True, null=True)
    cod_indicador_const_endereco2 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_logradouro'


class Eclusa(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'tra_eclusa_l'


class EdifConstPortuaria(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipoedifport = models.CharField(max_length=23, blank=True, null=True)
    administracao = models.TextField(blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'tra_edif_const_portuaria_p'


class EdifConstrAeroportuaria(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    administracao = models.TextField(blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    tipoedifaero = models.CharField(max_length=23, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'tra_edif_constr_aeroportuaria_p'


class EdifMetroFerroviaria(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'tra_edif_metro_ferroviaria_p'


class Fundeadouro(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    administracao = models.TextField(blank=True, null=True)
    destinacaofundeadouro = models.CharField(max_length=43, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'tra_fundeadouro_p'


class PistaPontoPouso(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'tra_pista_ponto_pouso_p'


class Ponte(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'tra_ponte_l'


class Sinalizacao(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    tiposinal = models.CharField(max_length=21, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'tra_sinalizacao_p'


class Travessia(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    tipotravessia = models.CharField(max_length=18, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'tra_travessia_l'


class TraTravessiaP(models.Model): #precisa juntar as tabelas
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    tipotravessia = models.CharField(max_length=18, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'tra_travessia_p'


class TrechoDuto(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'tra_trecho_duto_l'


class TrechoFerroviario(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'tra_trecho_ferroviario_l'


class TrechoHidroviario(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    extensaotrecho = models.FloatField(blank=True, null=True)
    caladomaxseca = models.FloatField(blank=True, null=True)
    operacional = models.CharField(max_length=12, blank=True, null=True)
    situacaofisica = models.TextField(blank=True, null=True)
    regime = models.CharField(max_length=31, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'tra_trecho_hidroviario_l'


class TrechoRodoviario(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'tra_trecho_rodoviario_l'


class Tunel(models.Model):
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
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'tra_tunel_l'


class VDescricao(models.Model):
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_descricao'


class BrejoPantano(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    alturamediaindividuos = models.FloatField(blank=True, null=True)
    classificacaoporte = models.CharField(max_length=12, blank=True, null=True)
    tipobrejopantano = models.CharField(max_length=27, blank=True, null=True)
    denso = models.CharField(max_length=12, blank=True, null=True)
    antropizada = models.CharField(max_length=23, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'veg_brejo_pantano_a'


class Mangue(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    alturamediaindividuos = models.FloatField(blank=True, null=True)
    classificacaoporte = models.CharField(max_length=12, blank=True, null=True)
    denso = models.CharField(max_length=12, blank=True, null=True)
    antropizada = models.CharField(max_length=23, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'veg_mangue_a'


class VegRestinga(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    alturamediaindividuos = models.FloatField(blank=True, null=True)
    classificacaoporte = models.CharField(max_length=12, blank=True, null=True)
    denso = models.CharField(max_length=12, blank=True, null=True)
    antropizada = models.CharField(max_length=23, blank=True, null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'veg_veg_restinga_a'


class Vegetable(models.Model):
    animal_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vegetable'


class PontosExibicaoWgs84(models.Model):
    id_gps = models.IntegerField(primary_key=True)
    long_decimal = models.FloatField(blank=True, null=True)
    lat_decimal = models.FloatField(blank=True, null=True)
    sistema_geodesico = models.TextField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'pontos_exibicao_wgs84'

