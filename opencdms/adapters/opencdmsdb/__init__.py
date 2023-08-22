# =============================================================================
# MIT License
#
# Copyright (c) 2023, OpenCDMS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# =============================================================================
from geoalchemy2 import Geography
from sqlalchemy_json import mutable_json_type
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    MetaData,
    Numeric,
    String,
    Table
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import registry, relationship

from opencdms.models.default import reference_data, master_data


mapper_registry = registry()


user = Table(
    "user",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key", primary_key=True, index=False),
    Column("name", String, comment="Name of user/agent", index=False),
    Column("description", String, comment="Description of user / agent", index=False),
    schema="admin"
)


altitude = Table(
    "altitude",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation for the classification.", index=False),
    Column("description", String, comment="Description of the classification area.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to further information on the classification.", index=False),
    Column("_version", Integer, comment="Version of this record, e.g. 1.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


application_area = Table(
    "application_area",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation for the application area.", index=False),
    Column("description", String, comment="Description of the application area.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to further information on the application area.", index=False),
    Column("_version", Integer, comment="Version of this record, e.g. 1.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


climate_zone = Table(
    "climate_zone",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inSchema", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation for the climate zone.", index=False),
    Column("description", String, comment="Description of the climate zone", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further definition of climate zone", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="reference_data"
)


communication_method = Table(
    "communication_method",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation for the communication method.", index=False),
    Column("description", String, comment="Description of the communication method.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to further information on the communication method.", index=False),
    Column("_version", Integer, comment="Version of this record, e.g. 1.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


equipment_type = Table(
    "equipment_type",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation for the equipment type.", index=False),
    Column("description", String, comment="Description of the equipment type.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to further information on the equipment type.", index=False),
    Column("_version", Integer, comment="Version of this record, e.g. 1.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


exposure = Table(
    "exposure",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inSchema", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation for exposure classification.", index=False),
    Column("description", String, comment="Description of sensor exposure according to WMO-No. 8.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further definition of exposure class.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


facility_type = Table(
    "facility_type",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation for the facility type.", index=False),
    Column("description", String, comment="Description of the facility type.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to definition of facility type.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


feature_type = Table(
    "feature_type",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation for the feature type.", index=False),
    Column("description", String, comment="Description of the feature type.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to definition of feature type.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


geopositioning_method = Table(
    "geopositioning_method",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation for the geopositioning method.", index=False),
    Column("description", String, comment="Description of the geopositioning method.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to further information on the geopositioning method.", index=False),
    Column("_version", Integer, comment="Version of this record, e.g. 1.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


local_topography = Table(
    "local_topography",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation of the local topography classification.", index=False),
    Column("description", String, comment="Description of local topography classification.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further definition of local topography classification.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


measurement_quality = Table(
    "measurement_quality",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation for the measurement quality classification.", index=False),
    Column("description", String, comment="Description of the measurement quality classification.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to definition of fmeasurement quality classification.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


media_type = Table(
    "media_type",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation for the media type.", index=False),
    Column("description", String, comment="Description of the media type.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to definition of media type.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


observation_type = Table(
    "observation_type",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key", primary_key=True, index=False),
    Column("inSchema", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation for the observation type.", index=False),
    Column("description", String, comment="Description of the observation type.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to definition of the observation type.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


observed_property = Table(
    "observed_property",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation of observed property, e.g. 'at' for air temperature.", index=False),
    Column("description", String, comment="Description of observed property.", index=False),
    Column("standard_name", String, comment="CF standard name (if applicable), e.g. 'air_temperature'.", index=False),
    Column("units", String, comment="Canonical units, e.g. 'Kelvin'.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to definition / source of observed property.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


observing_method = Table(
    "observing_method",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation of the observing method.", index=False),
    Column("description", String, comment="Description of observing method.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further definition of observing method.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


observing_procedure = Table(
    "observing_procedure",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation of the observing procedure.", index=False),
    Column("description", String, comment="Description of observing procedure.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further definition of observing procedure.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


observing_program = Table(
    "observing_program",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation of the observing program.", index=False),
    Column("description", String, comment="Description of observing program.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further definition of observing program.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


operating_status = Table(
    "operating_status",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation of the operating status.", index=False),
    Column("description", String, comment="Description of operating status.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further definition of operating status.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


reference_surface = Table(
    "reference_surface",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation of the reference surface.", index=False),
    Column("description", String, comment="Description of reference surface.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further definition of reference.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


relative_elevation = Table(
    "relative_elevation",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation of the relative elevation classification.", index=False),
    Column("description", String, comment="Description of relative elevation classification.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further definition of relative elevation classification.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


reporting_status = Table(
    "reporting_status",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation of the reporting status.", index=False),
    Column("description", String, comment="Description of reporting status.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further definition of reporting status.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


representativeness = Table(
    "representativeness",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation for the representativeness classification.", index=False),
    Column("description", String, comment="Description of the representativeness classification.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further information on the representativeness classification.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


role = Table(
    "role",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation of the role.", index=False),
    Column("description", String, comment="Description of the role.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further information on the role.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


source_of_observation = Table(
    "source_of_observation",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation of the source of observation.", index=False),
    Column("description", String, comment="Description of the source of observation.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further information on the source of observation.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


source_type = Table(
    "source_type",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Name of source type", index=False),
    Column("description", String, comment="Description of source type, e.g. file etc", index=False),
    Column("IANA_scheme", String, comment="IANA scheme (if applicable)", index=False),
    Column("links", String, comment="Links providing further definition of source type", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="reference_data"
)


status = Table(
    "status",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name for the status", index=False),
    Column("description", String, comment="Description of the status", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="reference_data"
)


surface_cover = Table(
    "surface_cover",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation of the surface cover classification.", index=False),
    Column("description", String, comment="Description of the surface cover classification.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further information on the surface cover classification.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


surface_roughness = Table(
    "surface_roughness",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation of the surface roughness classification.", index=False),
    Column("description", String, comment="Description of the surface roughness classification.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further information on the surface roughness classification.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


territory = Table(
    "territory",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation for the territory.", index=False),
    Column("description", String, comment="Official name of territory.", index=False),
    Column("ISO3c", String, comment="ISO 3 character country code.", index=False),
    Column("wmo_region_id", ForeignKey("reference_data.wmo_region.id"), comment="WMO region that represents the territory.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to further information.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


time_zone = Table(
    "time_zone",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Name / abbreviation of time zone", index=False),
    Column("description", String, comment="Description of the time zone.", index=False),
    Column("offset", Numeric, comment="Offset from UTC in hours (decimal)", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to further information.", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="reference_data"
)


topographic_context = Table(
    "topographic_context",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation of the topography / bathymetry classification.", index=False),
    Column("description", String, comment="Description of the topography / bathymetry classification.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further information on the topography / bathymetry classification.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


wmo_region = Table(
    "wmo_region",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("inScheme", String, comment="The scheme/vocabulary that this record is from.", index=False),
    Column("name", String, comment="Short name / abbreviation of the WMO regional association.", index=False),
    Column("description", String, comment="Description of the WMO regional association.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links providing further information on the WMO regional association.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="reference_data"
)


deployment = Table(
    "deployment",
    mapper_registry.metadata,
    Column("id", String, comment="Unique ID / primary key for deployment.", primary_key=True, index=False),
    Column("deployed_equipment_id", ForeignKey("master_data.equipment.id"), comment="The deployed equipment.", index=False),
    Column("host_id", ForeignKey("master_data.host.id"), comment="The host / observing facility where the equipment is deployed.", index=False),
    Column("height_above_local_reference_surface", Numeric, comment="Installation height of equipment above reference surface (in meters).", index=False),
    Column("local_reference_surface_id", ForeignKey("reference_data.reference_surface.id"), comment="The local reference surface.", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date that this record is valid from.", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Date that this record is valid to.", index=False),
    Column("communication_method_id", ForeignKey("reference_data.communication_method.id"), comment="The primary data communication method.", index=False),
    Column("source_of_observation_id", ForeignKey("reference_data.source_of_observation.id"), comment="The source of the observation (manual, automatic, visual etc.).", index=False),
    Column("exposure_id", ForeignKey("reference_data.exposure.id"), comment="The degree to which an instrument is affected by external influences according to the exposure classification (see WMO No. 8).", index=False),
    Column("measurement_quality_id", ForeignKey("reference_data.measurement_quality.id"), comment="Expected quality of measurements from the sensor in teh current configuration according to the measurement quality classification (see WMO-No. 8).", index=False),
    Column("representativeness_id", ForeignKey("reference_data.representativeness.id"), comment="An assessment of the representativeness of the observations.", index=False),
    Column("configuration", String, comment="Description of any shielding or configuration/setup of the instrumentation.", index=False),
    Column("control_schedule", String, comment="Description of schedule for calibrations or verification of instrument.", index=False),
    Column("maintenance_schedule", String, comment="A description (and schedule) of maintenance that is routinely performed on an instrument.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to further information on deployment.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


deployment_application_area = Table(
    "deployment_application_area",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record.", primary_key=True, index=False),
    Column("deployment_id", ForeignKey("master_data.deployment.id"), comment="The deployment this record belongs to.", index=False),
    Column("application_area_id", ForeignKey("reference_data.application_area.id"), comment="The application area this record belongs to.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


deployment_location = Table(
    "deployment_location",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record.", primary_key=True, index=False),
    Column("deployment_id", ForeignKey("master_data.deployment.id"), comment="Host/station associated with this record.", index=False),
    Column("location", Geography, comment="Location of host/station during indicated time period.", index=False),
    Column("elevation", Numeric, comment="Elevation of station above mean sea level in meters.", index=False),
    Column("geopositioning_method_id", ForeignKey("reference_data.geopositioning_method.id"), comment="Method by which the location was determined", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date from which the details for this record are valid.", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Date after which the details for this record are no longer valid.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


deployment_log = Table(
    "deployment_log",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("deployment_id", ForeignKey("master_data.deployment.id"), comment="The deployment to which this record applies.", index=False),
    Column("author", String, comment="Author of the log entry.", index=False),
    Column("datetime", DateTime(timezone=True), comment="Date and time of the event being logged.", index=False),
    Column("description", String, comment="Description of of the event being logged.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links to further documentation of the logged event.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


deployment_media = Table(
    "deployment_media",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record.", primary_key=True, index=False),
    Column("deployment_id", ForeignKey("master_data.deployment.id"), comment="The deployment this record belongs to.", index=False),
    Column("media_id", ForeignKey("master_data.media.id"), comment="The media this record belongs to.", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date from which the media is valid.", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Date from which the media is no longer valid.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


deployment_responsible_party = Table(
    "deployment_responsible_party",
    mapper_registry.metadata,
    Column("id", String, comment="Unique identifier for this record.", primary_key=True, index=False),
    Column("responsible_party_id", ForeignKey("master_data.responsible_party.id"), comment="The responsible party.", index=False),
    Column("role_id", ForeignKey("reference_data.role.id"), comment="The role this responsible party plays.", index=False),
    Column("deployment_id", ForeignKey("master_data.deployment.id"), comment="The deployment that this record corresponds to.", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date this record is valid from.", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Date this record is valid to.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


equipment = Table(
    "equipment",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("description", String, comment="Description of sensor.", index=False),
    Column("equipment_type_id", ForeignKey("reference_data.equipment_type.id"), comment="The type of equipment, e.g. temperature sensor, sensor housing, etc", index=False),
    Column("online_resource", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to further information.", index=False),
    Column("specification_link", String, comment="Link to manufacturers (or other) specification describing the equipment.", index=False),
    Column("firmware_version", String, comment="Firmware version of software installed in sensor.", index=False),
    Column("manufacturer", String, comment="Make, or manufacturer, of sensor.", index=False),
    Column("model", String, comment="Model of sensor.", index=False),
    Column("serial_number", String, comment="Serial number of sensor.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


equipment_log = Table(
    "equipment_log",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("equipment_id", ForeignKey("master_data.equipment.id"), comment="The equipment / sensor to which this record applies.", index=False),
    Column("author", String, comment="Author of the log entry.", index=False),
    Column("datetime", DateTime(timezone=True), comment="Date and time of the event being logged.", index=False),
    Column("description", String, comment="Description of of the event being logged.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links to further documentation of the logged event.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


equipment_media = Table(
    "equipment_media",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record.", primary_key=True, index=False),
    Column("equipment_id", ForeignKey("master_data.equipment.id"), comment="The equipment this record belongs to.", index=False),
    Column("media_id", ForeignKey("master_data.media.id"), comment="The media this record belongs to.", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date from which the media is valid.", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Date from which the media is no longer valid.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


equipment_responsible_party = Table(
    "equipment_responsible_party",
    mapper_registry.metadata,
    Column("id", String, comment="", primary_key=True, index=False),
    Column("equipment_id", ForeignKey("master_data.equipment.id"), comment="The equipment that this record corresponds to.", index=False),
    Column("responsible_party_id", ForeignKey("master_data.responsible_party.id"), comment="The responsible party associated with the record.", index=False),
    Column("role_id", ForeignKey("reference_data.role.id"), comment="The role the responsible party plays.", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date this record is valid from.", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Date this record is valid to.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


feature = Table(
    "feature",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("name", String, comment="Name of feature.", index=False),
    Column("description", String, comment="Description of feature.", index=False),
    Column("feature_type_id", ForeignKey("reference_data.feature_type.id"), comment="Feature type.", index=False),
    Column("geometry", Geography, comment="Location / geospatial geometry of feature.", index=False),
    Column("elevation", Numeric, comment="Mean elevation of feature above mean sea level.", index=False),
    Column("parent_id", ForeignKey("master_data.feature.id"), comment="Parent feature for this feature if nested.", index=False),
    Column("properties", mutable_json_type(dbtype=JSONB, nested=True), comment="Array of named values consistent with that defined for the feature type.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to further information on feature.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


host = Table(
    "host",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("name", String, comment="Preferred name of host.", index=False),
    Column("description", String, comment="Description of host.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="URI to host, e.g. to OSCAR/Surface.", index=False),
    Column("wigos_station_identifier", String, comment="WIGOS station identifier.", index=False),
    Column("facility_type_id", ForeignKey("reference_data.facility_type.id"), comment="Type of observing facility, fixed land, mobile sea, etc.", index=False),
    Column("date_established", DateTime(timezone=True), comment="Date host was first established.", index=False),
    Column("date_closed", DateTime(timezone=True), comment="Date host was first established.", index=False),
    Column("wmo_region_id", ForeignKey("reference_data.wmo_region.id"), comment="WMO region in which the host is located.", index=False),
    Column("territory_id", ForeignKey("reference_data.territory.id"), comment="Territory the host is located in.", index=False),
    Column("time_zone_id", ForeignKey("reference_data.time_zone.id"), comment="Time zone the host is located in.", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date from which the details for this record are valid.", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Date after which the details for this record are no longer valid.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


host_affiliation = Table(
    "host_affiliation",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record.", primary_key=True, index=False),
    Column("host_id", ForeignKey("master_data.host.id"), comment="Host described by this record.", index=False),
    Column("program_id", ForeignKey("reference_data.observing_program.id"), comment="Observing program that this host is affiliated with.", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date from which the details for this record are valid.", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Date after which the details for this record are no longer valid.", index=False),
    Column("reporting_status", String, comment="Declared reporting status of an observing facility with respect to a certain program/network affiliation.", index=False),
    Column("program_specific_id", String, comment="WIGOS station identifier.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


host_aliases = Table(
    "host_aliases",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record.", primary_key=True, index=False),
    Column("host_id", ForeignKey("master_data.host.id"), comment="Primary ID by which the host is known.", index=False),
    Column("alternative_id", String, comment="Alternative ID by which the host is known.", index=False),
    Column("alternative_name", String, comment="Alternative name by which the host is known.", index=False),
    Column("alternative_authority", String, comment="ID scheme / authority assigning alternative ID.", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date the alternative id/name was used from.", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Last date the alternative id/name was used.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


host_environment = Table(
    "host_environment",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record.", primary_key=True, index=False),
    Column("host_id", ForeignKey("master_data.host.id"), comment="Host associated with this record.", index=False),
    Column("climate_zone_id", ForeignKey("reference_data.climate_zone.id"), comment="Climate zone that the associated host is located in.", index=False),
    Column("surface_cover_id", ForeignKey("reference_data.surface_cover.id"), comment="Type of surface cover.", index=False),
    Column("surface_roughness_id", ForeignKey("reference_data.surface_roughness.id"), comment="Typical surface roughness of the site surrounding the host.", index=False),
    Column("altitude_or_depth_id", ForeignKey("reference_data.altitude.id"), comment="The altitude/depth with respect to mean sea level (enumerated).", index=False),
    Column("local_topography_id", ForeignKey("reference_data.local_topography.id"), comment="The local topography.", index=False),
    Column("relative_elevation_id", ForeignKey("reference_data.relative_elevation.id"), comment="The relative elevation.", index=False),
    Column("topographic_context_id", ForeignKey("reference_data.topographic_context.id"), comment="The topographic context.", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date the this record is valid from", index=False),
    Column("valid_to", DateTime(timezone=True), comment="date that this record is valid to", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="master_data"
)


host_location = Table(
    "host_location",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record.", primary_key=True, index=False),
    Column("host_id", ForeignKey("master_data.host.id"), comment="Host/station associated with this record.", index=False),
    Column("location", Geography, comment="Location of host/station during indicated time period.", index=False),
    Column("elevation", Numeric, comment="Elevation of station above mean sea level in meters.", index=False),
    Column("geopositioning_method_id", ForeignKey("reference_data.geopositioning_method.id"), comment="Method by which the location was determined", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date from which the details for this record are valid.", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Date after which the details for this record are no longer valid.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


host_log = Table(
    "host_log",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("host_id", ForeignKey("master_data.host.id"), comment="The host to which this record applies.", index=False),
    Column("author", String, comment="Author of the log entry.", index=False),
    Column("datetime", DateTime(timezone=True), comment="Date and time of the event being logged.", index=False),
    Column("description", String, comment="Description of of the event being logged.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Links to further documentation of the logged event.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


host_media = Table(
    "host_media",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record.", primary_key=True, index=False),
    Column("host_id", ForeignKey("master_data.host.id"), comment="The host to which this media belongs.", index=False),
    Column("media_id", ForeignKey("master_data.media.id"), comment="The associated media.", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date from which this record is valid.", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Date from which this record is no longer valid.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


host_responsible_party = Table(
    "host_responsible_party",
    mapper_registry.metadata,
    Column("id", String, comment="Unique identifier for this record.", primary_key=True, index=False),
    Column("responsible_party_id", ForeignKey("master_data.responsible_party.id"), comment="The responsible party.", index=False),
    Column("role_id", ForeignKey("reference_data.role.id"), comment="The role this responsible party plays.", index=False),
    Column("host_id", ForeignKey("master_data.host.id"), comment="The host that this record corresponds to.", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date this record is valid from.", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Date this record is valid to.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


media = Table(
    "media",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("media_type_id", ForeignKey("reference_data.media_type.id"), comment="The type of media described by this entry.", index=False),
    Column("description", String, comment="Description of the media.", index=False),
    Column("created", DateTime(timezone=True), comment="Date the media was created/uploaded.", index=False),
    Column("creator", String, comment="Who uploaded the media. ", index=False),
    Column("rights", Integer, comment="Digital rights associated with the media.", index=False),
    Column("source", String, comment="Source of the media.", index=False),
    Column("data", mutable_json_type(dbtype=JSONB, nested=True), comment="TBD", index=False),
    schema="master_data"
)


observation = Table(
    "observation",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("location", Geography, comment="Location of observation.", index=True),
    Column("elevation", Numeric, comment="Elevation of observation above mean sea level (in meters).", index=False),
    Column("observation_type_id", ForeignKey("reference_data.observation_type.id"), comment="Type of observation.", index=True),
    Column("phenomenon_start", DateTime(timezone=True), comment="Start time of the phenomenon being observed or observing period, if missing assumed instantaneous with time given by phenomenon_end.", index=False),
    Column("phenomenon_end", DateTime(timezone=True), comment="End time of the phenomenon being observed or observing period.", index=True),
    Column("result_value", Numeric, comment="The value of the result in float representation.", index=False),
    Column("result_uom", String, comment="Units used to represent the value being observed.", index=False),
    Column("result_description", String, comment="str representation of the result if applicable.", index=False),
    Column("result_quality", mutable_json_type(dbtype=JSONB, nested=True), comment="JSON representation of the result quality, key / value pairs.", index=False),
    Column("result_time", DateTime(timezone=True), comment="Time that the result became available.", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Time that the result starts to be valid.", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Time after which the result is no longer valid.", index=False),
    Column("host_id", ForeignKey("master_data.host.id"), comment="Host associated with making the observation, equivalent to OGC OMS 'host'.", index=False),
    Column("observer_id", ForeignKey("master_data.equipment.id"), comment="Observer associated with making the observation, equivalent to OGC OMS 'observer'.", index=False),
    Column("observed_property_id", ForeignKey("reference_data.observed_property.id"), comment="The phenomenon, or thing, being observed.", index=True),
    Column("observing_procedure_id", ForeignKey("reference_data.observing_procedure.id"), comment="Procedure used to make the observation.", index=False),
    Column("dataset", String, comment="Primary dataset that this observation belongs to.", index=True),
    Column("parameter", mutable_json_type(dbtype=JSONB, nested=True), comment="List of key/ value pairs in dict.", index=False),
    Column("featureOfInterest_id", ForeignKey("master_data.feature.id"), comment="Feature of interest that this observation is associated with.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    Column("_source_id", ForeignKey("master_data.source.id"), comment="The source of this record.", index=True),
    Column("_source_identifier", String, comment="The original identifier for the record from the data source (if available).", index=True),
    schema="master_data"
)


reference_stations = Table(
    "reference_stations",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key for this record.", primary_key=True, index=False),
    Column("host_id", ForeignKey("master_data.host.id"), comment="The host / station this record is for.", index=False),
    Column("reference_station_id", ForeignKey("master_data.host.id"), comment="The host / station acting as a reference station.", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date the reference station started as a reference station for this host.", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Date the reference station stopped as a reference station for this host.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


responsible_party = Table(
    "responsible_party",
    mapper_registry.metadata,
    Column("id", String, comment="A value uniquely identifying a party (individual or organization).", primary_key=True, index=False),
    Column("individual_name", String, comment="The name of the organization or the individual.", index=False),
    Column("position_name", String, comment="Role or position of the responsible person.", index=False),
    Column("organization_name", String, comment="Organization/affiliation of the individual/responsible person. In case of an organization, the name property should be used and this property is not to be used.", index=False),
    Column("contact_information", mutable_json_type(dbtype=JSONB, nested=True), comment="Contact information", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


sensor_characteristics = Table(
    "sensor_characteristics",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record.", primary_key=True, index=False),
    Column("equipment_id", ForeignKey("master_data.equipment.id"), comment="The equipment / sensor to which this record applies.", index=False),
    Column("observed_property_id", ForeignKey("reference_data.observed_property.id"), comment="The observed parameter to which this record applies.", index=False),
    Column("observing_method_id", ForeignKey("reference_data.observing_method.id"), comment="Primary method/principles by which the sensor makes measurements.", index=False),
    Column("observing_method_details", String, comment="A description of the method of measurement/observation used.", index=False),
    Column("measurement_units", Integer, comment="The units used in this record.", index=False),
    Column("drift_per_unit_time", Numeric, comment="Intrinsic capability of the measurement/observing method - drift per unit time. Typically a percentage per unit time but could be absolute e.g. 1 degree per year.", index=False),
    Column("unit_time", Integer, comment="Unit time for drift per unit time (seconds).", index=False),
    Column("valid_min", Numeric, comment="Minimum observable value by sensor, in units specified by measurement units.", index=False),
    Column("valid_max", Numeric, comment="Maximum observable value by sensor, in units specified by measurement units.", index=False),
    Column("specified_absolute_uncertainty", Numeric, comment="Measurement uncertainty for measurements from this sensor, 2 sigma. Units as per measurement units.", index=False),
    Column("specified_relative_uncertainty", Numeric, comment="Measurement uncertainty for measurements from this sensor, 2 sigma. Units in %, e.g. 20 %.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to further information.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


sensor_operating_status = Table(
    "sensor_operating_status",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record.", primary_key=True, index=False),
    Column("deployment_id", ForeignKey("master_data.deployment.id"), comment="The deployment this record belongs to.", index=False),
    Column("operating_status_id", ForeignKey("reference_data.operating_status.id"), comment="The operating status of the deployed equipment.", index=False),
    Column("valid_from", DateTime(timezone=True), comment="The date from which this status applies.", index=False),
    Column("valid_to", DateTime(timezone=True), comment="The date from which this status is no longer valid.", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


source = Table(
    "source",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key.", primary_key=True, index=False),
    Column("name", String, comment="Name of source.", index=False),
    Column("description", String, comment="Description of source type, e.g. file etc.", index=False),
    Column("source_type_id", ForeignKey("reference_data.source_type.id"), comment="The type of source.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="Link(s) to further information on source.", index=False),
    Column("processor", String, comment="Name of processor used to ingest the data.", index=False),
    Column("parameters", mutable_json_type(dbtype=JSONB, nested=True), comment="Parameters required to access the data from this source (NEED TO CHECK THIS, ENCRYPT?).", index=False),
    Column("_version", Integer, comment="Version number of this record.", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed.", index=False),
    Column("_user_id", ForeignKey("admin.user.id"), comment="Which user/agent last modified this record.", index=False),
    Column("_status_id", ForeignKey("reference_data.status.id"), comment="Whether this is the latest version or an archived version of the record.", index=False),
    Column("_comments", String, comment="Free text comments on this record, for example description of changes made etc.", index=False),
    schema="master_data"
)


record = Table(
    "record",
    mapper_registry.metadata,
    Column("id", String, comment="A unique identifier of the catalogue record.", primary_key=True, index=False),
    Column("time", String, comment="The temporal extent of the resource. Can be null if there is no associated temporal extent.", index=False),
    Column("title", String, comment="A human-readable name given to the resource.", index=False),
    Column("location", Geography, comment="A geometry associated with the resource that is used for discovery. Can be null if there is no associated geometry.", index=False),
    Column("created", String, comment="Date of creation of this record.", index=False),
    Column("updated", String, comment="The most recent date on which the record was changed.", index=False),
    Column("resource_type", String, comment="The nature or genre of the resource. The value should be a code, convenient for filtering records. Where available, a link to the canonical URI of the record type resource will be added to the 'links' property.", index=False),
    Column("description", String, comment="A free-text account of the resource.", index=False),
    Column("keywords", String, comment="The topic or topics of the resource. Typically represented using free-form keywords, tags, key phrases, or classification codes. Semi-colon delimited", index=False),
    Column("language", String, comment="The natural language used for textual values (e.g. titles, descriptions, etc.) of the resource. ISO 639-1/639-2 codes should be used.", index=False),
    Column("external_ids", mutable_json_type(dbtype=JSONB, nested=True), comment="An identifier for the resource assigned by an external (to the catalogue) entity.", index=False),
    Column("themes", mutable_json_type(dbtype=JSONB, nested=True), comment="A knowledge organization system used to classify the resource.", index=False),
    Column("formats", mutable_json_type(dbtype=JSONB, nested=True), comment="A list of available distributions of the resource.", index=False),
    Column("providers", mutable_json_type(dbtype=JSONB, nested=True), comment="A list of providers qualified by their role in association to the record.", index=False),
    Column("license", String, comment="A legal document under which the resource is made available. The value should be a code, convenient for filtering the records. Where applicable, the use of the identifiers from the SPDX License List is recommended. If multiple licenses apply, it is recommended to use ''various'.  Where available, links to a URI of each applicable license should be added to the 'links' property.", index=False),
    Column("rights", String, comment="A statement that concerns all rights not addressed by the license such as a copyright statement.", index=False),
    Column("links", mutable_json_type(dbtype=JSONB, nested=True), comment="A list of links for accessing the resource (e.g. download link, access link) in one of the supported distribution formats and/or links to other resources associated with this resource. Also, a list of links for navigating the API (e.g. prev, next, etc.).  Since the specification requires that at least the self link be present then the min items for this list should be one.", index=False),
    schema="master_data"
)


def start_mappers():
    mapper_registry.map_imperatively(admin.User, user)
    mapper_registry.map_imperatively(reference_data.Altitude, altitude)
    mapper_registry.map_imperatively(reference_data.ApplicationArea, application_area)
    mapper_registry.map_imperatively(reference_data.ClimateZone, climate_zone)
    mapper_registry.map_imperatively(reference_data.CommunicationMethod, communication_method)
    mapper_registry.map_imperatively(reference_data.EquipmentType, equipment_type)
    mapper_registry.map_imperatively(reference_data.Exposure, exposure)
    mapper_registry.map_imperatively(reference_data.FacilityType, facility_type)
    mapper_registry.map_imperatively(reference_data.FeatureType, feature_type)
    mapper_registry.map_imperatively(reference_data.GeopositioningMethod, geopositioning_method)
    mapper_registry.map_imperatively(reference_data.LocalTopography, local_topography)
    mapper_registry.map_imperatively(reference_data.MeasurementQuality, measurement_quality)
    mapper_registry.map_imperatively(reference_data.MediaType, media_type)
    mapper_registry.map_imperatively(reference_data.ObservationType, observation_type)
    mapper_registry.map_imperatively(reference_data.ObservedProperty, observed_property)
    mapper_registry.map_imperatively(reference_data.ObservingMethod, observing_method)
    mapper_registry.map_imperatively(reference_data.ObservingProcedure, observing_procedure)
    mapper_registry.map_imperatively(reference_data.ObservingProgram, observing_program)
    mapper_registry.map_imperatively(reference_data.OperatingStatus, operating_status)
    mapper_registry.map_imperatively(reference_data.ReferenceSurface, reference_surface)
    mapper_registry.map_imperatively(reference_data.RelativeElevation, relative_elevation)
    mapper_registry.map_imperatively(reference_data.ReportingStatus, reporting_status)
    mapper_registry.map_imperatively(reference_data.Representativeness, representativeness)
    mapper_registry.map_imperatively(reference_data.Role, role)
    mapper_registry.map_imperatively(reference_data.SourceOfObservation, source_of_observation)
    mapper_registry.map_imperatively(reference_data.SourceType, source_type)
    mapper_registry.map_imperatively(reference_data.Status, status)
    mapper_registry.map_imperatively(reference_data.SurfaceCover, surface_cover)
    mapper_registry.map_imperatively(reference_data.SurfaceRoughness, surface_roughness)
    mapper_registry.map_imperatively(reference_data.Territory, territory)
    mapper_registry.map_imperatively(reference_data.TimeZone, time_zone)
    mapper_registry.map_imperatively(reference_data.TopographicContext, topographic_context)
    mapper_registry.map_imperatively(reference_data.WmoRegion, wmo_region)
    mapper_registry.map_imperatively(master_data.Deployment, deployment)
    mapper_registry.map_imperatively(master_data.DeploymentApplicationArea, deployment_application_area)
    mapper_registry.map_imperatively(master_data.DeploymentLocation, deployment_location)
    mapper_registry.map_imperatively(master_data.DeploymentLog, deployment_log)
    mapper_registry.map_imperatively(master_data.DeploymentMedia, deployment_media)
    mapper_registry.map_imperatively(master_data.DeploymentResponsibleParty, deployment_responsible_party)
    mapper_registry.map_imperatively(master_data.Equipment, equipment)
    mapper_registry.map_imperatively(master_data.EquipmentLog, equipment_log)
    mapper_registry.map_imperatively(master_data.EquipmentMedia, equipment_media)
    mapper_registry.map_imperatively(master_data.EquipmentResponsibleParty, equipment_responsible_party)
    mapper_registry.map_imperatively(master_data.Feature, feature)
    mapper_registry.map_imperatively(master_data.Host, host)
    mapper_registry.map_imperatively(master_data.HostAffiliation, host_affiliation)
    mapper_registry.map_imperatively(master_data.HostAliases, host_aliases)
    mapper_registry.map_imperatively(master_data.HostEnvironment, host_environment)
    mapper_registry.map_imperatively(master_data.HostLocation, host_location)
    mapper_registry.map_imperatively(master_data.HostLog, host_log)
    mapper_registry.map_imperatively(master_data.HostMedia, host_media)
    mapper_registry.map_imperatively(master_data.HostResponsibleParty, host_responsible_party)
    mapper_registry.map_imperatively(master_data.Media, media)
    mapper_registry.map_imperatively(master_data.Observation, observation)
    mapper_registry.map_imperatively(master_data.ReferenceStations, reference_stations)
    mapper_registry.map_imperatively(master_data.ResponsibleParty, responsible_party)
    mapper_registry.map_imperatively(master_data.SensorCharacteristics, sensor_characteristics)
    mapper_registry.map_imperatively(master_data.SensorOperatingStatus, sensor_operating_status)
    mapper_registry.map_imperatively(master_data.Source, source)
    mapper_registry.map_imperatively(master_data.Record, record)

