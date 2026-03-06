# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Produtos(models.Model):
    indice = models.DecimalField(max_digits=15, decimal_places=0, primary_key=True) #indice = models.DecimalField (db_column='INDICE', max_digits=15, decimal_places=0, blank=True, null=True,  primary_key=True)  # Field name made lowercase.
    codigodebarra = models.CharField(db_column='CODIGODEBARRA', max_length=13)  # Field name made lowercase.
    grupo = models.CharField(db_column='GRUPO', max_length=60, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipoproduto = models.CharField(db_column='TIPOPRODUTO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    customedio = models.CharField(db_column='CUSTOMEDIO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ipi = models.CharField(db_column='IPI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.CharField(db_column='FABRICANTE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='OBS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    icms = models.CharField(db_column='ICMS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codigoaliquota = models.CharField(db_column='CODIGOALIQUOTA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    aliquotareduzida = models.CharField(db_column='ALIQUOTAREDUZIDA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fornecedor = models.CharField(db_column='FORNECEDOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    precovendapromo = models.FloatField(db_column='PRECOVENDAPROMO', blank=True, null=True)  # Field name made lowercase.
    comissao = models.FloatField(db_column='COMISSAO', blank=True, null=True)  # Field name made lowercase.
    margem = models.DecimalField(db_column='MARGEM', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    precovenda1 = models.DecimalField(db_column='PRECOVENDA1', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    precovenda2 = models.DecimalField(db_column='PRECOVENDA2', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    precovenda3 = models.DecimalField(db_column='PRECOVENDA3', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tipovenda = models.CharField(db_column='TIPOVENDA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    balanca = models.CharField(db_column='BALANCA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ibpt = models.DecimalField(db_column='IBPT', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    exc = models.CharField(db_column='EXC', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cst = models.CharField(db_column='CST', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ncm = models.CharField(db_column='NCM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    infadicional = models.CharField(db_column='INFADICIONAL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    origemproduto = models.CharField(db_column='ORIGEMPRODUTO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    csticms = models.CharField(db_column='CSTICMS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    codigoibge = models.CharField(db_column='CODIGOIBGE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    codiss = models.CharField(db_column='CODISS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    natoperiss = models.CharField(db_column='NATOPERISS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    indincentivofiscal = models.CharField(db_column='INDINCENTIVOFISCAL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    itemlistaservico = models.CharField(db_column='ITEMLISTASERVICO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    csosn = models.CharField(db_column='CSOSN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    valorbasecalcsimples = models.CharField(db_column='VALORBASECALCSIMPLES', max_length=8, blank=True, null=True)  # Field name made lowercase.
    valoricmsretidosimples = models.CharField(db_column='VALORICMSRETIDOSIMPLES', max_length=8, blank=True, null=True)  # Field name made lowercase.
    modalidadebasecalculo = models.CharField(db_column='MODALIDADEBASECALCULO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    percentreducaobase = models.CharField(db_column='PERCENTREDUCAOBASE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    moddedetdabcdoicmsst = models.CharField(db_column='MODDEDETDABCDOICMSST', max_length=1, blank=True, null=True)  # Field name made lowercase.
    percentualmargemicms = models.CharField(db_column='PERCENTUALMARGEMICMS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    percentualbcicms = models.CharField(db_column='PERCENTUALBCICMS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    valorreducaobcicms = models.CharField(db_column='VALORREDUCAOBCICMS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    valoraliquotaicms = models.CharField(db_column='VALORALIQUOTAICMS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    valoricms = models.CharField(db_column='VALORICMS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    valoricmsdesonerado = models.CharField(db_column='VALORICMSDESONERADO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    motivodesoneracaoicms = models.CharField(db_column='MOTIVODESONERACAOICMS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    valorcreditoicms = models.CharField(db_column='VALORCREDITOICMS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    aliquotacalculocredito = models.CharField(db_column='ALIQUOTACALCULOCREDITO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    valortotaltributos = models.CharField(db_column='VALORTOTALTRIBUTOS', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cstpis = models.CharField(db_column='CSTPIS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    basecalculopis = models.CharField(db_column='BASECALCULOPIS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    aliquotapis = models.CharField(db_column='ALIQUOTAPIS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    valorpis = models.CharField(db_column='VALORPIS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    quantvendidapis = models.CharField(db_column='QUANTVENDIDAPIS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    valoraliquotapis = models.CharField(db_column='VALORALIQUOTAPIS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cstcofins = models.CharField(db_column='CSTCOFINS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    basecalculocofins = models.CharField(db_column='BASECALCULOCOFINS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    aliquotacofins = models.CharField(db_column='ALIQUOTACOFINS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    valorcofins = models.CharField(db_column='VALORCOFINS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    quantvendidacofins = models.CharField(db_column='QUANTVENDIDACOFINS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    valoraliquotacofins = models.CharField(db_column='VALORALIQUOTACOFINS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    indicedepto = models.CharField(db_column='INDICEDEPTO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    unidadedemedida = models.CharField(db_column='UNIDADEDEMEDIDA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    precocusto = models.DecimalField(db_column='PRECOCUSTO', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    precovenda = models.DecimalField(db_column='PRECOVENDA', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lucro = models.DecimalField(db_column='LUCRO', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    estoqueatual = models.DecimalField(db_column='ESTOQUEATUAL', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    estoqueminimo = models.DecimalField(db_column='ESTOQUEMINIMO', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    validade = models.DateField(db_column='VALIDADE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtos'
