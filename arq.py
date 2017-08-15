# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class AccountAccount(models.Model):
    user = models.ForeignKey('PeopleProfile', models.DO_NOTHING, unique=True)
    timezone = models.CharField(max_length=100)
    language = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'account_account'


class AccountAccountdeletion(models.Model):
    user = models.ForeignKey('PeopleProfile', models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=75)
    date_requested = models.DateTimeField()
    date_expunged = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_accountdeletion'


class AccountEmailaddress(models.Model):
    user = models.ForeignKey('PeopleProfile', models.DO_NOTHING)
    email = models.CharField(unique=True, max_length=75)
    verified = models.BooleanField()
    primary = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AccountSignupcode(models.Model):
    code = models.CharField(unique=True, max_length=64)
    max_uses = models.IntegerField()
    expiry = models.DateTimeField(blank=True, null=True)
    inviter = models.ForeignKey('PeopleProfile', models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=75)
    notes = models.TextField()
    sent = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    use_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'account_signupcode'


class AccountSignupcodeextended(models.Model):
    signupcode = models.ForeignKey(AccountSignupcode, models.DO_NOTHING, primary_key=True)
    username = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'account_signupcodeextended'


class AccountSignupcoderesult(models.Model):
    signup_code = models.ForeignKey(AccountSignupcode, models.DO_NOTHING)
    user = models.ForeignKey('PeopleProfile', models.DO_NOTHING)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'account_signupcoderesult'


class ActivityresourceActivity(models.Model):
    iriobject = models.CharField(db_column='iriObject', max_length=200, blank=True, null=True)  # Field name made lowercase.
    iriobjecttarget = models.CharField(db_column='iriObjectTarget', max_length=200, blank=True, null=True)  # Field name made lowercase.
    iriaction = models.CharField(db_column='iriAction', max_length=200)  # Field name made lowercase.
    iriactor = models.CharField(db_column='iriActor', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'activityResource_activity'


class ActstreamAction(models.Model):
    actor_content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    actor_object_id = models.CharField(max_length=255)
    verb = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    target_content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    target_object_id = models.CharField(max_length=255, blank=True, null=True)
    action_object_content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    action_object_object_id = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField()
    public = models.BooleanField()
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actstream_action'


class ActstreamFollow(models.Model):
    user = models.ForeignKey('PeopleProfile', models.DO_NOTHING)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    object_id = models.CharField(max_length=255)
    actor_only = models.BooleanField()
    started = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'actstream_follow'
        unique_together = (('user', 'content_type', 'object_id'),)


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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adm_posto_fiscal_p'


class AgonRatingsOverallrating(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    rating = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agon_ratings_overallrating'
        unique_together = (('object_id', 'content_type', 'category'),)


class AgonRatingsRating(models.Model):
    overall_rating = models.ForeignKey(AgonRatingsOverallrating, models.DO_NOTHING, blank=True, null=True)
    object_id = models.IntegerField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    user = models.ForeignKey('PeopleProfile', models.DO_NOTHING)
    rating = models.IntegerField()
    timestamp = models.DateTimeField()
    category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agon_ratings_rating'
        unique_together = (('object_id', 'content_type', 'user', 'category'),)


class AnnouncementsAnnouncement(models.Model):
    title = models.CharField(max_length=50)
    level = models.IntegerField()
    content = models.TextField()
    creator = models.ForeignKey('PeopleProfile', models.DO_NOTHING)
    creation_date = models.DateTimeField()
    site_wide = models.BooleanField()
    members_only = models.BooleanField()
    dismissal_type = models.IntegerField()
    publish_start = models.DateTimeField()
    publish_end = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'announcements_announcement'


class AnnouncementsDismissal(models.Model):
    user = models.ForeignKey('PeopleProfile', models.DO_NOTHING)
    announcement = models.ForeignKey(AnnouncementsAnnouncement, models.DO_NOTHING)
    dismissed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'announcements_dismissal'


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
    user_uuid = models.UUIDField()

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


class AvatarAvatar(models.Model):
    user = models.ForeignKey('PeopleProfile', models.DO_NOTHING)
    primary = models.BooleanField()
    avatar = models.CharField(max_length=1024)
    date_uploaded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'avatar_avatar'


class BaseAction(models.Model):
    receiver_serialized = models.CharField(max_length=10000)
    message_name = models.CharField(max_length=200)
    parameter_serialized = models.CharField(max_length=10000)
    executed = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'base_action'


class BaseContactrole(models.Model):
    resource = models.ForeignKey('BaseResourcebase', models.DO_NOTHING)
    contact = models.ForeignKey('PeopleProfile', models.DO_NOTHING)
    role = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'base_contactrole'
        unique_together = (('contact', 'resource', 'role'),)


class BaseInvitation(models.Model):
    requested_date = models.DateTimeField()
    expired_date = models.DateTimeField(blank=True, null=True)
    invite_reason = models.CharField(max_length=100, blank=True, null=True)
    accepted = models.NullBooleanField()
    invited = models.ForeignKey('PeopleProfile', models.DO_NOTHING, blank=True, null=True)
    inviter = models.ForeignKey('PeopleProfile', models.DO_NOTHING, unique=True)
    opened = models.NullBooleanField()
    action = models.ForeignKey(BaseAction, models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_invitation'


class BaseLicense(models.Model):
    identifier = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    abbreviation = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=2000, blank=True, null=True)
    license_text = models.TextField(blank=True, null=True)
    license_text_en = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_license'


class BaseLink(models.Model):
    resource = models.ForeignKey('BaseResourcebase', models.DO_NOTHING)
    extension = models.CharField(max_length=255)
    link_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mime = models.CharField(max_length=255)
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'base_link'


class BaseMembership(models.Model):
    date_joined = models.DateField()
    is_blocked = models.BooleanField()
    is_banned = models.BooleanField()
    can_edit = models.BooleanField()
    can_invite = models.BooleanField()
    invite_reason = models.CharField(max_length=300, blank=True, null=True)
    member = models.ForeignKey('PeopleProfile', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'base_membership'


class BaseRegion(models.Model):
    code = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'base_region'


class BaseResourcebase(models.Model):
    polymorphic_ctype = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    uuid = models.CharField(max_length=36)
    owner = models.ForeignKey('PeopleProfile', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    date_type = models.CharField(max_length=255)
    edition = models.CharField(max_length=255, blank=True, null=True)
    abstract = models.TextField()
    purpose = models.TextField(blank=True, null=True)
    maintenance_frequency = models.CharField(max_length=255, blank=True, null=True)
    restriction_code_type = models.ForeignKey('BaseRestrictioncodetype', models.DO_NOTHING, blank=True, null=True)
    constraints_other = models.TextField(blank=True, null=True)
    license = models.ForeignKey(BaseLicense, models.DO_NOTHING, blank=True, null=True)
    language = models.CharField(max_length=3)
    category = models.ForeignKey('BaseTopiccategory', models.DO_NOTHING, blank=True, null=True)
    spatial_representation_type = models.ForeignKey('BaseSpatialrepresentationtype', models.DO_NOTHING, blank=True, null=True)
    temporal_extent_start = models.DateTimeField(blank=True, null=True)
    temporal_extent_end = models.DateTimeField(blank=True, null=True)
    supplemental_information = models.TextField()
    distribution_url = models.TextField(blank=True, null=True)
    distribution_description = models.TextField(blank=True, null=True)
    data_quality_statement = models.TextField(blank=True, null=True)
    bbox_x0 = models.DecimalField(max_digits=19, decimal_places=10, blank=True, null=True)
    bbox_x1 = models.DecimalField(max_digits=19, decimal_places=10, blank=True, null=True)
    bbox_y0 = models.DecimalField(max_digits=19, decimal_places=10, blank=True, null=True)
    bbox_y1 = models.DecimalField(max_digits=19, decimal_places=10, blank=True, null=True)
    srid = models.CharField(max_length=255)
    csw_typename = models.CharField(max_length=32)
    csw_schema = models.CharField(max_length=64)
    csw_mdsource = models.CharField(max_length=256)
    csw_insert_date = models.DateTimeField(blank=True, null=True)
    csw_type = models.CharField(max_length=32)
    csw_anytext = models.TextField(blank=True, null=True)
    csw_wkt_geometry = models.TextField()
    metadata_uploaded = models.BooleanField()
    metadata_xml = models.TextField(blank=True, null=True)
    popular_count = models.IntegerField()
    share_count = models.IntegerField()
    featured = models.BooleanField()
    is_published = models.BooleanField()
    thumbnail_url = models.TextField(blank=True, null=True)
    detail_url = models.CharField(max_length=255, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_resourcebase'


class BaseResourcebaseRegions(models.Model):
    resourcebase = models.ForeignKey(BaseResourcebase, models.DO_NOTHING)
    region = models.ForeignKey(BaseRegion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'base_resourcebase_regions'
        unique_together = (('resourcebase', 'region'),)


class BaseRestrictioncodetype(models.Model):
    identifier = models.CharField(max_length=255)
    description = models.TextField()
    description_en = models.TextField(blank=True, null=True)
    gn_description = models.TextField()
    gn_description_en = models.TextField(blank=True, null=True)
    is_choice = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'base_restrictioncodetype'


class BaseSpatialrepresentationtype(models.Model):
    identifier = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    description_en = models.CharField(max_length=255, blank=True, null=True)
    gn_description = models.CharField(max_length=255)
    gn_description_en = models.CharField(max_length=255, blank=True, null=True)
    is_choice = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'base_spatialrepresentationtype'


class BaseTopiccategory(models.Model):
    identifier = models.CharField(max_length=255)
    description = models.TextField()
    description_en = models.TextField(blank=True, null=True)
    gn_description = models.TextField(blank=True, null=True)
    gn_description_en = models.TextField(blank=True, null=True)
    is_choice = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'base_topiccategory'


class BlocoR9(models.Model):
    gid = models.AutoField(primary_key=True)
    nomenclatu = models.CharField(max_length=50, blank=True, null=True)
    situacao_b = models.CharField(max_length=1, blank=True, null=True)
    indice_blo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    nome_bacia = models.CharField(max_length=50, blank=True, null=True)
    nome_setor = models.CharField(max_length=50, blank=True, null=True)
    id4 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    area_bloco = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bloco_r9'


class BookmarkerBookmark(models.Model):
    name = models.CharField(max_length=255)
    url_visual = models.CharField(max_length=1000)
    url_api = models.CharField(max_length=1000)
    zoom = models.IntegerField()
    resourcetype = models.CharField(db_column='resourceType', max_length=255)  # Field name made lowercase.
    coordinates = models.CharField(max_length=1000)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bookmarker_bookmark'


class CadastroCivil(models.Model):
    id_servidor_portal = models.CharField(max_length=255, blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(max_length=255, blank=True, null=True)
    matricula = models.CharField(max_length=255, blank=True, null=True)
    descricao_cargo = models.CharField(max_length=255, blank=True, null=True)
    classe_cargo = models.CharField(max_length=255, blank=True, null=True)
    referencia_cargo = models.CharField(max_length=255, blank=True, null=True)
    padrao_cargo = models.CharField(max_length=255, blank=True, null=True)
    nivel_cargo = models.CharField(max_length=255, blank=True, null=True)
    sigla_funcao = models.CharField(max_length=255, blank=True, null=True)
    nivel_funcao = models.CharField(max_length=255, blank=True, null=True)
    funcao = models.CharField(max_length=255, blank=True, null=True)
    codigo_atividade = models.CharField(max_length=255, blank=True, null=True)
    atividade = models.CharField(max_length=255, blank=True, null=True)
    opcao_parcial = models.CharField(max_length=255, blank=True, null=True)
    cod_uorg_lotacao = models.CharField(max_length=255, blank=True, null=True)
    uorg_lotacao = models.CharField(max_length=255, blank=True, null=True)
    cod_org_lotacao = models.CharField(max_length=255, blank=True, null=True)
    org_lotacao = models.CharField(max_length=255, blank=True, null=True)
    cod_orgsup_lotacao = models.CharField(max_length=255, blank=True, null=True)
    orgsup_lotacao = models.CharField(max_length=255, blank=True, null=True)
    cod_uorg_exercicio = models.CharField(max_length=255, blank=True, null=True)
    uorg_exercicio = models.CharField(max_length=255, blank=True, null=True)
    cod_org_exercicio = models.CharField(max_length=255, blank=True, null=True)
    org_exercicio = models.CharField(max_length=255, blank=True, null=True)
    cod_orgsup_exercicio = models.CharField(max_length=255, blank=True, null=True)
    orgsup_exercicio = models.CharField(max_length=255, blank=True, null=True)
    tipo_vinculo = models.CharField(max_length=255, blank=True, null=True)
    situacao_vinculo = models.CharField(max_length=255, blank=True, null=True)
    data_inicio_afastamento = models.CharField(max_length=255, blank=True, null=True)
    data_termino_afastamento = models.CharField(max_length=255, blank=True, null=True)
    regime_juridico = models.CharField(max_length=255, blank=True, null=True)
    jornada_de_trabalho = models.CharField(max_length=255, blank=True, null=True)
    data_ingresso_cargofuncao = models.CharField(max_length=255, blank=True, null=True)
    data_nomeacao_cargofuncao = models.CharField(max_length=255, blank=True, null=True)
    data_ingresso_orgao = models.CharField(max_length=255, blank=True, null=True)
    documento_ingresso_servicopublico = models.CharField(max_length=255, blank=True, null=True)
    data_diploma_ingresso_servicopublico = models.CharField(max_length=255, blank=True, null=True)
    diploma_ingresso_cargofuncao = models.CharField(max_length=255, blank=True, null=True)
    diploma_ingresso_orgao = models.CharField(max_length=255, blank=True, null=True)
    diploma_ingresso_servicopublico = models.CharField(max_length=255, blank=True, null=True)
    uf_exercicio = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cadastro_civil'


class CeleryTaskmeta(models.Model):
    task_id = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=50)
    result = models.TextField(blank=True, null=True)
    date_done = models.DateTimeField()
    traceback = models.TextField(blank=True, null=True)
    hidden = models.BooleanField()
    meta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celery_taskmeta'


class CeleryTasksetmeta(models.Model):
    taskset_id = models.CharField(unique=True, max_length=255)
    result = models.TextField()
    date_done = models.DateTimeField()
    hidden = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'celery_tasksetmeta'


class CommunityApiCommunity(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    need_invitation = models.BooleanField()
    date_creation = models.DateTimeField(blank=True, null=True)
    id_manager = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_manager')

    class Meta:
        managed = False
        db_table = 'community_api_community'


class CommunityApiInvitation(models.Model):
    email = models.CharField(max_length=255)
    community = models.ForeignKey(CommunityApiCommunity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'community_api_invitation'


class CommunityApiMembershipcommunity(models.Model):
    date_joined = models.DateField()
    is_blocked = models.BooleanField()
    is_banned = models.BooleanField()
    invite_reason = models.CharField(max_length=100, blank=True, null=True)
    community = models.ForeignKey(CommunityApiCommunity, models.DO_NOTHING)
    member = models.ForeignKey(AuthUser, models.DO_NOTHING)
    role = models.ForeignKey('CommunityApiRolemembership', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'community_api_membershipcommunity'


class CommunityApiRolemembership(models.Model):
    name = models.CharField(max_length=255)
    actions = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'community_api_rolemembership'


class CommunityCommunity(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    need_invitation = models.BooleanField()
    date_creation = models.DateTimeField(blank=True, null=True)
    id_manager = models.ForeignKey('PeopleProfile', models.DO_NOTHING, db_column='id_manager')

    class Meta:
        managed = False
        db_table = 'community_community'


class CommunityComposercommunity(models.Model):
    headline = models.TextField(blank=True, null=True)
    community = models.ForeignKey(CommunityCommunity, models.DO_NOTHING)
    main_layer = models.ForeignKey('LayersLayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'community_composercommunity'


class CommunityComposerlayer(models.Model):
    checked = models.BooleanField()
    composer_community = models.ForeignKey(CommunityComposercommunity, models.DO_NOTHING)
    layer = models.ForeignKey('LayersLayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'community_composerlayer'


class CommunityFilesApiFile(models.Model):
    name = models.CharField(max_length=1000)
    creation_date = models.DateTimeField()
    file = models.CharField(max_length=100)
    community = models.ForeignKey(CommunityApiCommunity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'community_files_api_file'


class CommunityFilesApiFilelayer(models.Model):
    name = models.CharField(max_length=1000)
    creation_date = models.DateTimeField()
    file = models.CharField(max_length=100)
    layer = models.ForeignKey('CommunityLayerApiCommunityinformation', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'community_files_api_filelayer'


class CommunityLayerApiCommunityinformation(models.Model):
    properties = models.TextField()  # This field type is a guess.
    geom = models.GeometryField(blank=True, null=True)
    community = models.ForeignKey(CommunityApiCommunity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'community_layer_api_communityinformation'


class CommunityLayerApiCommunityinformationfieldschema(models.Model):
    name_field = models.CharField(max_length=100)
    type_field = models.CharField(max_length=20)
    name_module_field = models.CharField(max_length=100)
    options = models.TextField()  # This field type is a guess.
    community = models.ForeignKey(CommunityApiCommunity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'community_layer_api_communityinformationfieldschema'


class CommunityMembershipcommunity(models.Model):
    membership_ptr = models.ForeignKey(BaseMembership, models.DO_NOTHING, primary_key=True)
    community = models.ForeignKey(CommunityCommunity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'community_membershipcommunity'


class ContextApiClass(models.Model):
    name = models.CharField(unique=True, max_length=1000)
    spatial = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'context_api_class'


class ContextApiContext(models.Model):
    attribute = models.CharField(max_length=255)
    means = models.CharField(max_length=1000)
    type = models.CharField(max_length=1000, blank=True, null=True)
    classname = models.ForeignKey(ContextApiClass, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'context_api_context'


class CorsheadersCorsmodel(models.Model):
    cors = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'corsheaders_corsmodel'


class DashboardDashboard(models.Model):
    information = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey('PeopleProfile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dashboard_dashboard'


class DialogosComment(models.Model):
    author = models.ForeignKey('PeopleProfile', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    object_id = models.IntegerField()
    comment = models.TextField()
    submit_date = models.DateTimeField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    public = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'dialogos_comment'


class DiscussionListDiscussionthread(models.Model):
    title = models.CharField(max_length=1000)
    issue = models.CharField(max_length=10000)
    post_date = models.DateTimeField()
    community = models.ForeignKey(CommunityApiCommunity, models.DO_NOTHING)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'discussion_list_discussionthread'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('PeopleProfile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'), ('app_label', 'model'),)


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


class DjangoSite(models.Model):
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class DjceleryCrontabschedule(models.Model):
    minute = models.CharField(max_length=64)
    hour = models.CharField(max_length=64)
    day_of_week = models.CharField(max_length=64)
    day_of_month = models.CharField(max_length=64)
    month_of_year = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'djcelery_crontabschedule'


class DjceleryIntervalschedule(models.Model):
    every = models.IntegerField()
    period = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'djcelery_intervalschedule'


class DjceleryPeriodictask(models.Model):
    name = models.CharField(unique=True, max_length=200)
    task = models.CharField(max_length=200)
    interval = models.ForeignKey(DjceleryIntervalschedule, models.DO_NOTHING, blank=True, null=True)
    crontab = models.ForeignKey(DjceleryCrontabschedule, models.DO_NOTHING, blank=True, null=True)
    args = models.TextField()
    kwargs = models.TextField()
    queue = models.CharField(max_length=200, blank=True, null=True)
    exchange = models.CharField(max_length=200, blank=True, null=True)
    routing_key = models.CharField(max_length=200, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    last_run_at = models.DateTimeField(blank=True, null=True)
    total_run_count = models.IntegerField()
    date_changed = models.DateTimeField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'djcelery_periodictask'


class DjceleryPeriodictasks(models.Model):
    ident = models.SmallIntegerField(primary_key=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'djcelery_periodictasks'


class DjceleryTaskstate(models.Model):
    state = models.CharField(max_length=64)
    task_id = models.CharField(unique=True, max_length=36)
    name = models.CharField(max_length=200, blank=True, null=True)
    tstamp = models.DateTimeField()
    args = models.TextField(blank=True, null=True)
    kwargs = models.TextField(blank=True, null=True)
    eta = models.DateTimeField(blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    runtime = models.FloatField(blank=True, null=True)
    retries = models.IntegerField()
    worker = models.ForeignKey('DjceleryWorkerstate', models.DO_NOTHING, blank=True, null=True)
    hidden = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'djcelery_taskstate'


class DjceleryWorkerstate(models.Model):
    hostname = models.CharField(unique=True, max_length=255)
    last_heartbeat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djcelery_workerstate'


class DocumentsDocument(models.Model):
    resourcebase_ptr = models.ForeignKey(BaseResourcebase, models.DO_NOTHING, primary_key=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    abstract_en = models.TextField(blank=True, null=True)
    purpose_en = models.TextField(blank=True, null=True)
    constraints_other_en = models.TextField(blank=True, null=True)
    supplemental_information_en = models.TextField(blank=True, null=True)
    distribution_description_en = models.TextField(blank=True, null=True)
    data_quality_statement_en = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    object_id = models.IntegerField(blank=True, null=True)
    doc_file = models.CharField(max_length=100, blank=True, null=True)
    extension = models.CharField(max_length=128, blank=True, null=True)
    doc_type = models.CharField(max_length=128, blank=True, null=True)
    doc_url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_document'


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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enc_torre_energia_p'


class GeoprojectMembershipproject(models.Model):
    membership_ptr = models.ForeignKey(BaseMembership, models.DO_NOTHING, primary_key=True)
    project = models.ForeignKey('GeoprojectProject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'geoproject_membershipproject'


class GeoprojectProject(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    onwer = models.ForeignKey('PeopleProfile', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'geoproject_project'


class GeoprojectTypeofproject(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geoproject_typeofproject'


class GroupsGroupinvitation(models.Model):
    group = models.ForeignKey('GroupsGroupprofile', models.DO_NOTHING)
    token = models.CharField(max_length=40)
    email = models.CharField(max_length=75)
    user = models.ForeignKey('PeopleProfile', models.DO_NOTHING, blank=True, null=True)
    from_user = models.ForeignKey('PeopleProfile', models.DO_NOTHING)
    role = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'groups_groupinvitation'
        unique_together = (('group', 'email'),)


class GroupsGroupmember(models.Model):
    group = models.ForeignKey('GroupsGroupprofile', models.DO_NOTHING)
    user = models.ForeignKey('PeopleProfile', models.DO_NOTHING)
    role = models.CharField(max_length=10)
    joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'groups_groupmember'


class GroupsGroupprofile(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, unique=True)
    title = models.CharField(max_length=50)
    slug = models.CharField(unique=True, max_length=50)
    logo = models.CharField(max_length=100)
    description = models.TextField()
    email = models.CharField(max_length=75, blank=True, null=True)
    access = models.CharField(max_length=15)
    last_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'groups_groupprofile'


class GuardianGroupobjectpermission(models.Model):
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    object_pk = models.CharField(max_length=255)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'guardian_groupobjectpermission'
        unique_together = (('group', 'permission', 'object_pk'),)


class GuardianUserobjectpermission(models.Model):
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    object_pk = models.CharField(max_length=255)
    user = models.ForeignKey('PeopleProfile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'guardian_userobjectpermission'
        unique_together = (('user', 'permission', 'object_pk'),)


class HidBancoAreiaA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    tipobanco = models.CharField(max_length=14, blank=True, null=True)
    situacaoemagua = models.CharField(max_length=17, blank=True, null=True)
    materialpredominante = models.CharField(max_length=27, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_barragem_l'


class HidCorredeiraL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_corredeira_l'


class HidCorredeiraP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_corredeira_p'


class HidFozMaritimaL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_trecho_massa_dagua_a'


class HydraSupportedoperation(models.Model):
    identifier = models.CharField(max_length=1000, blank=True, null=True)
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    method = models.CharField(max_length=100)
    possible_status = models.CharField(max_length=100, blank=True, null=True)
    expects = models.ForeignKey('ContextClass', models.DO_NOTHING, blank=True, null=True)
    hydra_class = models.ForeignKey('ContextClass', models.DO_NOTHING)
    returns = models.ForeignKey('ContextClass', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hydra_supportedoperation'


class HydraSupportedproperty(models.Model):
    property = models.CharField(max_length=100)
    required = models.BooleanField()
    readable = models.BooleanField()
    writeable = models.BooleanField()
    hydra_class = models.ForeignKey('ContextClass', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hydra_supportedproperty'


class InstitutionContainer(models.Model):
    name = models.CharField(unique=True, max_length=255)
    institution = models.ForeignKey('InstitutionInstitutionprofile', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'institution_container'


class InstitutionInstitutionprofile(models.Model):
    name = models.CharField(max_length=1000)
    initials = models.CharField(unique=True, max_length=255, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'institution_institutionprofile'


class InstitutionLink(models.Model):
    url = models.CharField(max_length=1000)
    institution = models.ForeignKey(InstitutionInstitutionprofile, models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institution_link'


class KnowledgemanagementFrequencia(models.Model):
    frequencia = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'knowledgeManagement_frequencia'


class KnowledgemanagementKnowledge(models.Model):
    camada = models.ForeignKey('LayersLayer', models.DO_NOTHING, blank=True, null=True)
    mapa = models.ForeignKey('MapsMap', models.DO_NOTHING, blank=True, null=True)
    usuario = models.ForeignKey('PeopleProfile', models.DO_NOTHING, blank=True, null=True)
    frequencia = models.ForeignKey(KnowledgemanagementFrequencia, models.DO_NOTHING)
    pub_date = models.DateTimeField()
    whatfor = models.CharField(db_column='whatFor', max_length=200)  # Field name made lowercase.
    desirable_scale = models.CharField(max_length=200)
    status = models.CharField(max_length=1)
    missing_information = models.TextField(blank=True, null=True)
    resolution = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'knowledgeManagement_knowledge'


class LayersAttribute(models.Model):
    layer = models.ForeignKey('LayersLayer', models.DO_NOTHING)
    attribute = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    attribute_label = models.CharField(max_length=255, blank=True, null=True)
    attribute_type = models.CharField(max_length=50)
    visible = models.BooleanField()
    display_order = models.IntegerField()
    count = models.IntegerField()
    min = models.CharField(max_length=255, blank=True, null=True)
    max = models.CharField(max_length=255, blank=True, null=True)
    average = models.CharField(max_length=255, blank=True, null=True)
    median = models.CharField(max_length=255, blank=True, null=True)
    stddev = models.CharField(max_length=255, blank=True, null=True)
    sum = models.CharField(max_length=255, blank=True, null=True)
    unique_values = models.TextField(blank=True, null=True)
    last_stats_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'layers_attribute'


class LayersLayer(models.Model):
    resourcebase_ptr = models.ForeignKey(BaseResourcebase, models.DO_NOTHING, primary_key=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    abstract_en = models.TextField(blank=True, null=True)
    purpose_en = models.TextField(blank=True, null=True)
    constraints_other_en = models.TextField(blank=True, null=True)
    supplemental_information_en = models.TextField(blank=True, null=True)
    distribution_description_en = models.TextField(blank=True, null=True)
    data_quality_statement_en = models.TextField(blank=True, null=True)
    workspace = models.CharField(max_length=128)
    store = models.CharField(max_length=128)
    storetype = models.CharField(db_column='storeType', max_length=128)  # Field name made lowercase.
    name = models.CharField(max_length=128)
    typename = models.CharField(max_length=128, blank=True, null=True)
    default_style = models.ForeignKey('LayersStyle', models.DO_NOTHING, blank=True, null=True)
    charset = models.CharField(max_length=255)
    upload_session = models.ForeignKey('LayersUploadsession', models.DO_NOTHING, blank=True, null=True)
    service = models.ForeignKey('ServicesService', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layers_layer'


class LayersLayerStyles(models.Model):
    layer = models.ForeignKey(LayersLayer, models.DO_NOTHING)
    style = models.ForeignKey('LayersStyle', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'layers_layer_styles'
        unique_together = (('layer', 'style'),)


class LayersLayerfile(models.Model):
    upload_session = models.ForeignKey('LayersUploadsession', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    base = models.BooleanField()
    file = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'layers_layerfile'


class LayersStyle(models.Model):
    name = models.CharField(unique=True, max_length=255)
    sld_title = models.CharField(max_length=255, blank=True, null=True)
    sld_body = models.TextField(blank=True, null=True)
    sld_version = models.CharField(max_length=12, blank=True, null=True)
    sld_url = models.CharField(max_length=1000, blank=True, null=True)
    workspace = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layers_style'


class LayersUploadsession(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey('PeopleProfile', models.DO_NOTHING)
    processed = models.BooleanField()
    error = models.TextField(blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    context = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layers_uploadsession'


class LimAreaDesenvolvimentoControleA(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    classificacao = models.CharField(max_length=100, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_unidade_uso_sustentavel_a'


class LinkedbookmarkappLinkedbookmarkitemresource(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    iri = models.CharField(max_length=200)
    linkedbookmark = models.ForeignKey('LinkedbookmarkappLinkedbookmarkresource', models.DO_NOTHING, db_column='linkedBookmark_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'linkedBookmarkApp_linkedbookmarkitemresource'


class LinkedbookmarkappLinkedbookmarkresource(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'linkedBookmarkApp_linkedbookmarkresource'


class LocAglomeradoRuralDeExtensaoUrbanaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_capital_p'


class LocCidadeP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_cidade_p'


class LocVilaP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_vila_p'


class MapsMap(models.Model):
    resourcebase_ptr = models.ForeignKey(BaseResourcebase, models.DO_NOTHING, primary_key=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    abstract_en = models.TextField(blank=True, null=True)
    purpose_en = models.TextField(blank=True, null=True)
    constraints_other_en = models.TextField(blank=True, null=True)
    supplemental_information_en = models.TextField(blank=True, null=True)
    distribution_description_en = models.TextField(blank=True, null=True)
    data_quality_statement_en = models.TextField(blank=True, null=True)
    zoom = models.IntegerField()
    projection = models.CharField(max_length=32)
    center_x = models.FloatField()
    center_y = models.FloatField()
    last_modified = models.DateTimeField()
    urlsuffix = models.CharField(max_length=255)
    featuredurl = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'maps_map'


class MapsMaplayer(models.Model):
    map = models.ForeignKey(MapsMap, models.DO_NOTHING)
    stack_order = models.IntegerField()
    format = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    opacity = models.FloatField()
    styles = models.CharField(max_length=200, blank=True, null=True)
    transparent = models.BooleanField()
    fixed = models.BooleanField()
    group = models.CharField(max_length=200, blank=True, null=True)
    visibility = models.BooleanField()
    ows_url = models.CharField(max_length=200, blank=True, null=True)
    layer_params = models.TextField()
    source_params = models.TextField()
    local = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'maps_maplayer'


class MapsMapsnapshot(models.Model):
    map = models.ForeignKey(MapsMap, models.DO_NOTHING)
    config = models.TextField()
    created_dttm = models.DateTimeField()
    user = models.ForeignKey('PeopleProfile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maps_mapsnapshot'


class PeopleProfile(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    organization = models.CharField(max_length=255, blank=True, null=True)
    profile = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    voice = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    delivery = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'people_profile'


class PeopleProfileGroups(models.Model):
    profile = models.ForeignKey(PeopleProfile, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'people_profile_groups'
        unique_together = (('profile', 'group'),)


class PeopleProfileUserPermissions(models.Model):
    profile = models.ForeignKey(PeopleProfile, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'people_profile_user_permissions'
        unique_together = (('profile', 'permission'),)


class PibMunicipio(models.Model):
    ano_referencia = models.CharField(max_length=20, blank=True, null=True)
    codigo_uf = models.CharField(max_length=10, blank=True, null=True)
    nome_uf = models.CharField(max_length=25, blank=True, null=True)
    codigo_municipio = models.CharField(max_length=20, blank=True, null=True)
    nome_municipio = models.CharField(max_length=40, blank=True, null=True)
    regiao_metropolitana = models.CharField(max_length=110, blank=True, null=True)
    codigo_meso_regiao = models.CharField(max_length=20, blank=True, null=True)
    nome_meso_regiao = models.CharField(max_length=40, blank=True, null=True)
    codigo_micro_regiao = models.CharField(max_length=20, blank=True, null=True)
    nome_micro_regiao = models.CharField(max_length=40, blank=True, null=True)
    populacao = models.BigIntegerField(blank=True, null=True)
    pib = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pib_municipio'


class RelCurvaBatimetricaL(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    profundidade = models.IntegerField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_elemento_fisiografico_natural_p'


class RelPicoP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_pico_p'


class RelPontoCotadoAltimetricoP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    geometriaaproximada = models.CharField(max_length=3, blank=True, null=True)
    cota = models.FloatField(blank=True, null=True)
    cotacomprovada = models.CharField(max_length=3, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_ponto_cotado_altimetrico_p'


class RelPontoCotadoBatimetricoP(models.Model):
    id_objeto = models.IntegerField(primary_key=True)
    profundidade = models.FloatField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_ponto_cotado_batimetrico_p'


class SdiManagementInstancesdico(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sdi_management_instancesdico'


class ServicesService(models.Model):
    resourcebase_ptr = models.ForeignKey(BaseResourcebase, models.DO_NOTHING, primary_key=True)
    type = models.CharField(max_length=4)
    method = models.CharField(max_length=1)
    base_url = models.CharField(unique=True, max_length=200)
    version = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    online_resource = models.CharField(max_length=200, blank=True, null=True)
    fees = models.CharField(max_length=1000, blank=True, null=True)
    access_constraints = models.CharField(max_length=255, blank=True, null=True)
    connection_params = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    api_key = models.CharField(max_length=255, blank=True, null=True)
    workspace_ref = models.CharField(max_length=200, blank=True, null=True)
    store_ref = models.CharField(max_length=200, blank=True, null=True)
    resources_ref = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField()
    last_updated = models.DateTimeField()
    first_noanswer = models.DateTimeField(blank=True, null=True)
    noanswer_retries = models.IntegerField(blank=True, null=True)
    external_id = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_service'


class ServicesServicelayer(models.Model):
    service = models.ForeignKey(ServicesService, models.DO_NOTHING)
    layer = models.ForeignKey(LayersLayer, models.DO_NOTHING, blank=True, null=True)
    typename = models.CharField(max_length=255)
    title = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)
    styles = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_servicelayer'


class ServicesServiceprofilerole(models.Model):
    profiles = models.ForeignKey(PeopleProfile, models.DO_NOTHING)
    service = models.ForeignKey(ServicesService, models.DO_NOTHING)
    role = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'services_serviceprofilerole'


class ServicesWebserviceharvestlayersjob(models.Model):
    service = models.ForeignKey(ServicesService, models.DO_NOTHING, unique=True)
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'services_webserviceharvestlayersjob'


class ServicesWebserviceregistrationjob(models.Model):
    base_url = models.CharField(unique=True, max_length=200)
    type = models.CharField(max_length=4)
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'services_webserviceregistrationjob'


class Sprint(models.Model):
    id_sprint = models.AutoField(primary_key=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sprint'


class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'taggit_tag'


class TaggitTaggeditem(models.Model):
    tag = models.ForeignKey(TaggitTag, models.DO_NOTHING)
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taggit_taggeditem'


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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task'


class TastypieApiaccess(models.Model):
    identifier = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    request_method = models.CharField(max_length=10)
    accessed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tastypie_apiaccess'


class TastypieApikey(models.Model):
    user = models.ForeignKey(PeopleProfile, models.DO_NOTHING, unique=True)
    key = models.CharField(max_length=128)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tastypie_apikey'


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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_tunel_l'


class TweeterstreamTweeterstream(models.Model):
    name = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    center_longitude = models.FloatField()
    center_latitude = models.FloatField()
    zoom = models.IntegerField()
    creation_date = models.DateTimeField()
    init_date = models.DateTimeField()
    end_date = models.DateTimeField()
    usergeonode = models.ForeignKey(PeopleProfile, models.DO_NOTHING, db_column='userGeonode_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tweeterStream_tweeterstream'


class TwitterStreamApiAccounttwitter(models.Model):
    consumer_key = models.CharField(max_length=100, blank=True, null=True)
    consumer_secret = models.CharField(max_length=100, blank=True, null=True)
    consumer_token = models.CharField(max_length=100, blank=True, null=True)
    consumer_token_secret = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'twitter_stream_api_accounttwitter'


class TwitterStreamApiGeotwitter(models.Model):
    created_on = models.DateTimeField()
    monitor_twitter_id = models.IntegerField()
    sender_avatar = models.CharField(max_length=250, blank=True, null=True)
    sender_id = models.CharField(max_length=50, blank=True, null=True)
    sender_name = models.CharField(max_length=100, blank=True, null=True)
    sender_screen_name = models.CharField(max_length=50, blank=True, null=True)
    twitter_id = models.CharField(max_length=50, blank=True, null=True)
    twitter_text = models.TextField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'twitter_stream_api_geotwitter'


class TwitterStreamApiMonitortwitter(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=300, blank=True, null=True)
    initial_date = models.DateTimeField()
    final_date = models.DateTimeField()
    interval = models.CharField(max_length=8)
    created_on = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    since_id = models.BigIntegerField()
    last_searched_date = models.DateTimeField(blank=True, null=True)
    search_term = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'twitter_stream_api_monitortwitter'


class UploadUpload(models.Model):
    import_id = models.BigIntegerField(blank=True, null=True)
    user = models.ForeignKey(PeopleProfile, models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=16)
    date = models.DateTimeField()
    layer = models.ForeignKey(LayersLayer, models.DO_NOTHING, blank=True, null=True)
    upload_dir = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    complete = models.BooleanField()
    session = models.TextField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upload_upload'


class UploadUploadfile(models.Model):
    upload = models.ForeignKey(UploadUpload, models.DO_NOTHING, blank=True, null=True)
    file = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'upload_uploadfile'


class UserMessagesMessage(models.Model):
    thread = models.ForeignKey('UserMessagesThread', models.DO_NOTHING)
    sender = models.ForeignKey(PeopleProfile, models.DO_NOTHING)
    sent_at = models.DateTimeField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'user_messages_message'


class UserMessagesThread(models.Model):
    subject = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'user_messages_thread'


class UserMessagesUserthread(models.Model):
    thread = models.ForeignKey(UserMessagesThread, models.DO_NOTHING)
    user = models.ForeignKey(PeopleProfile, models.DO_NOTHING)
    unread = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'user_messages_userthread'


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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

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
    iri_metadata = models.CharField(max_length=1000, blank=True, null=True)
    iri_style = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veg_veg_restinga_a'
