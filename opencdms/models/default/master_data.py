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
from abc import ABC as AbstractBase
from dataclasses import dataclass
from datetime import datetime
from typing import NewType, Optional

Geography = NewType("Geography", str)

class DomainModelBase(AbstractBase):
    """
    Base class for OpenCDMS domain models.
    """

    def table_info(self) -> str:
        """Return table comment"""
        return self._comment

    def column_info(self, column: str) -> str:
        """Return column information"""
        return self._comments.get(column)


@dataclass
class Deployment(DomainModelBase):
    id: str
    deployed_equipment_id: Optional[str]
    host_id: Optional[str]
    height_above_local_reference_surface: Optional[float]
    local_reference_surface_id: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    communication_method_id: Optional[str]
    source_of_observation_id: str
    exposure_id: Optional[str]
    measurement_quality_id: Optional[str]
    representativeness_id: Optional[str]
    configuration: Optional[str]
    control_schedule: Optional[str]
    maintenance_schedule: Optional[str]
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "Unique ID / primary key for deployment.",
        "deployed_equipment_id": "The deployed equipment.",
        "host_id": "The host / observing facility where the equipment is deployed.",
        "height_above_local_reference_surface": "Installation height of equipment above reference surface (in meters).",
        "local_reference_surface_id": "The local reference surface.",
        "valid_from": "Date that this record is valid from.",
        "valid_to": "Date that this record is valid to.",
        "communication_method_id": "The primary data communication method.",
        "source_of_observation_id": "The source of the observation (manual, automatic, visual etc.).",
        "exposure_id": "The degree to which an instrument is affected by external influences according to the exposure classification (see WMO No. 8).",
        "measurement_quality_id": "Expected quality of measurements from the sensor in teh current configuration according to the measurement quality classification (see WMO-No. 8).",
        "representativeness_id": "An assessment of the representativeness of the observations.",
        "configuration": "Description of any shielding or configuration/setup of the instrumentation.",
        "control_schedule": "Description of schedule for calibrations or verification of instrument.",
        "maintenance_schedule": "A description (and schedule) of maintenance that is routinely performed on an instrument.",
        "links": "Link(s) to further information on deployment.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Deployed equipment"


@dataclass
class DeploymentApplicationArea(DomainModelBase):
    id: str
    deployment_id: str
    application_area_id: str
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "Primary key for this record.",
        "deployment_id": "The deployment this record belongs to.",
        "application_area_id": "The application area this record belongs to.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Link table between deployments and application area"


@dataclass
class DeploymentLocation(DomainModelBase):
    id: str
    deployment_id: str
    location: Optional[Geography]
    elevation: Optional[float]
    geopositioning_method_id: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "Primary key for this record.",
        "deployment_id": "Host/station associated with this record.",
        "location": "Location of host/station during indicated time period.",
        "elevation": "Elevation of station above mean sea level in meters.",
        "geopositioning_method_id": "Method by which the location was determined",
        "valid_from": "Date from which the details for this record are valid.",
        "valid_to": "Date after which the details for this record are no longer valid.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Location of equipment deployments"


@dataclass
class DeploymentLog(DomainModelBase):
    id: str
    deployment_id: str
    author: str
    datetime: datetime
    description: str
    links: dict
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "deployment_id": "The deployment to which this record applies.",
        "author": "Author of the log entry.",
        "datetime": "Date and time of the event being logged.",
        "description": "Description of of the event being logged.",
        "links": "Links to further documentation of the logged event.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Log of events associated with the deployment of a piece of equipment"


@dataclass
class DeploymentMedia(DomainModelBase):
    id: str
    deployment_id: Optional[str]
    media_id: Optional[int]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "Primary key for this record.",
        "deployment_id": "The deployment this record belongs to.",
        "media_id": "The media this record belongs to.",
        "valid_from": "Date from which the media is valid.",
        "valid_to": "Date from which the media is no longer valid.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Link table between deployments and associated media, e.g. photos"


@dataclass
class DeploymentResponsibleParty(DomainModelBase):
    id: str
    responsible_party_id: str
    role_id: str
    deployment_id: str
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "Unique identifier for this record.",
        "responsible_party_id": "The responsible party.",
        "role_id": "The role this responsible party plays.",
        "deployment_id": "The deployment that this record corresponds to.",
        "valid_from": "Date this record is valid from.",
        "valid_to": "Date this record is valid to.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Nominated points of contact for the host / station metadata"


@dataclass
class Equipment(DomainModelBase):
    id: str
    description: str
    equipment_type_id: str
    online_resource: Optional[dict]
    specification_link: Optional[str]
    firmware_version: Optional[str]
    manufacturer: Optional[str]
    model: Optional[str]
    serial_number: Optional[str]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "description": "Description of sensor.",
        "equipment_type_id": "The type of equipment, e.g. temperature sensor, sensor housing, etc",
        "online_resource": "Link(s) to further information.",
        "specification_link": "Link to manufacturers (or other) specification describing the equipment.",
        "firmware_version": "Firmware version of software installed in sensor.",
        "manufacturer": "Make, or manufacturer, of sensor.",
        "model": "Model of sensor.",
        "serial_number": "Serial number of sensor.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Basic information on equipment"


@dataclass
class EquipmentLog(DomainModelBase):
    id: str
    equipment_id: str
    author: str
    datetime: datetime
    description: str
    links: dict
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "equipment_id": "The equipment / sensor to which this record applies.",
        "author": "Author of the log entry.",
        "datetime": "Date and time of the event being logged.",
        "description": "Description of of the event being logged.",
        "links": "Links to further documentation of the logged event.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Equipment log"


@dataclass
class EquipmentMedia(DomainModelBase):
    id: str
    equipment_id: Optional[str]
    media_id: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "Primary key for this record.",
        "equipment_id": "The equipment this record belongs to.",
        "media_id": "The media this record belongs to.",
        "valid_from": "Date from which the media is valid.",
        "valid_to": "Date from which the media is no longer valid.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Link table between equipment and associated media, e.g. photos"


@dataclass
class EquipmentResponsibleParty(DomainModelBase):
    id: str
    equipment_id: str
    responsible_party_id: str
    role_id: str
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "",
        "equipment_id": "The equipment that this record corresponds to.",
        "responsible_party_id": "The responsible party associated with the record.",
        "role_id": "The role the responsible party plays.",
        "valid_from": "Date this record is valid from.",
        "valid_to": "Date this record is valid to.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "placeholder"


@dataclass
class Feature(DomainModelBase):
    id: str
    name: Optional[str]
    description: Optional[str]
    feature_type_id: str
    geometry: Geography
    elevation: Optional[float]
    parent_id: Optional[str]
    properties: Optional[dict]
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "name": "Name of feature.",
        "description": "Description of feature.",
        "feature_type_id": "Feature type.",
        "geometry": "Location / geospatial geometry of feature.",
        "elevation": "Mean elevation of feature above mean sea level.",
        "parent_id": "Parent feature for this feature if nested.",
        "properties": "Array of named values consistent with that defined for the feature type.",
        "links": "Link(s) to further information on feature.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Basic definition of geographic features"


@dataclass
class Host(DomainModelBase):
    id: str
    name: str
    description: Optional[str]
    links: Optional[dict]
    wigos_station_identifier: Optional[str]
    facility_type_id: Optional[str]
    date_established: Optional[datetime]
    date_closed: Optional[datetime]
    wmo_region_id: Optional[str]
    territory_id: Optional[str]
    time_zone_id: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "name": "Preferred name of host.",
        "description": "Description of host.",
        "links": "URI to host, e.g. to OSCAR/Surface.",
        "wigos_station_identifier": "WIGOS station identifier.",
        "facility_type_id": "Type of observing facility, fixed land, mobile sea, etc.",
        "date_established": "Date host was first established.",
        "date_closed": "Date host was first established.",
        "wmo_region_id": "WMO region in which the host is located.",
        "territory_id": "Territory the host is located in.",
        "time_zone_id": "Time zone the host is located in.",
        "valid_from": "Date from which the details for this record are valid.",
        "valid_to": "Date after which the details for this record are no longer valid.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "wmdr.observing_facility"


@dataclass
class HostAffiliation(DomainModelBase):
    id: str
    host_id: str
    program_id: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    reporting_status: Optional[str]
    program_specific_id: Optional[str]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "Primary key for this record.",
        "host_id": "Host described by this record.",
        "program_id": "Observing program that this host is affiliated with.",
        "valid_from": "Date from which the details for this record are valid.",
        "valid_to": "Date after which the details for this record are no longer valid.",
        "reporting_status": "Declared reporting status of an observing facility with respect to a certain program/network affiliation.",
        "program_specific_id": "WIGOS station identifier.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Host affiliations"


@dataclass
class HostAliases(DomainModelBase):
    id: str
    host_id: str
    alternative_id: Optional[str]
    alternative_name: Optional[str]
    alternative_authority: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "Primary key for this record.",
        "host_id": "Primary ID by which the host is known.",
        "alternative_id": "Alternative ID by which the host is known.",
        "alternative_name": "Alternative name by which the host is known.",
        "alternative_authority": "ID scheme / authority assigning alternative ID.",
        "valid_from": "Date the alternative id/name was used from.",
        "valid_to": "Last date the alternative id/name was used.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Host / station aliases"


@dataclass
class HostEnvironment(DomainModelBase):
    id: str
    host_id: str
    climate_zone_id: Optional[str]
    surface_cover_id: Optional[str]
    surface_roughness_id: Optional[str]
    altitude_or_depth_id: Optional[str]
    local_topography_id: Optional[str]
    relative_elevation_id: Optional[str]
    topographic_context_id: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "Primary key for this record.",
        "host_id": "Host associated with this record.",
        "climate_zone_id": "Climate zone that the associated host is located in.",
        "surface_cover_id": "Type of surface cover.",
        "surface_roughness_id": "Typical surface roughness of the site surrounding the host.",
        "altitude_or_depth_id": "The altitude/depth with respect to mean sea level (enumerated).",
        "local_topography_id": "The local topography.",
        "relative_elevation_id": "The relative elevation.",
        "topographic_context_id": "The topographic context.",
        "valid_from": "Date the this record is valid from",
        "valid_to": "date that this record is valid to",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "_comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Description of the environment at the specified host"


@dataclass
class HostLocation(DomainModelBase):
    id: str
    host_id: str
    location: Optional[Geography]
    elevation: Optional[float]
    geopositioning_method_id: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "Primary key for this record.",
        "host_id": "Host/station associated with this record.",
        "location": "Location of host/station during indicated time period.",
        "elevation": "Elevation of station above mean sea level in meters.",
        "geopositioning_method_id": "Method by which the location was determined",
        "valid_from": "Date from which the details for this record are valid.",
        "valid_to": "Date after which the details for this record are no longer valid.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Host locations"


@dataclass
class HostLog(DomainModelBase):
    id: str
    host_id: str
    author: str
    datetime: datetime
    description: str
    links: dict
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "host_id": "The host to which this record applies.",
        "author": "Author of the log entry.",
        "datetime": "Date and time of the event being logged.",
        "description": "Description of of the event being logged.",
        "links": "Links to further documentation of the logged event.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Host / station log"


@dataclass
class HostMedia(DomainModelBase):
    id: str
    host_id: Optional[str]
    media_id: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "Primary key for this record.",
        "host_id": "The host to which this media belongs.",
        "media_id": "The associated media.",
        "valid_from": "Date from which this record is valid.",
        "valid_to": "Date from which this record is no longer valid.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Link table between hosts and media"


@dataclass
class HostResponsibleParty(DomainModelBase):
    id: str
    responsible_party_id: str
    role_id: str
    host_id: str
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "Unique identifier for this record.",
        "responsible_party_id": "The responsible party.",
        "role_id": "The role this responsible party plays.",
        "host_id": "The host that this record corresponds to.",
        "valid_from": "Date this record is valid from.",
        "valid_to": "Date this record is valid to.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Nominated points of contact for the host / station metadata"


@dataclass
class Media(DomainModelBase):
    id: Optional[str]
    media_type_id: Optional[str]
    description: Optional[str]
    created: Optional[datetime]
    creator: Optional[str]
    rights: Optional[int]
    source: Optional[str]
    data: Optional[dict]
    __comments = {
        "id": "ID / primary key.",
        "media_type_id": "The type of media described by this entry.",
        "description": "Description of the media.",
        "created": "Date the media was created/uploaded.",
        "creator": "Who uploaded the media. ",
        "rights": "Digital rights associated with the media.",
        "source": "Source of the media.",
        "data": "TBD"
    }
    _comment = "(Place holder) Store for digital media, e.g. photos, reports, videos, etc"


@dataclass
class Observation(DomainModelBase):
    id: str
    location: Geography
    elevation: float
    observation_type_id: Optional[str]
    phenomenon_start: Optional[datetime]
    phenomenon_end: datetime
    result_value: float
    result_uom: str
    result_description: Optional[str]
    result_quality: Optional[dict]
    result_time: Optional[datetime]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    host_id: str
    observer_id: Optional[str]
    observed_property_id: str
    observing_procedure_id: Optional[str]
    dataset: Optional[str]
    parameter: Optional[dict]
    featureOfInterest_id: Optional[str]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    _source_id: str
    _source_identifier: str
    __comments = {
        "id": "ID / primary key.",
        "location": "Location of observation.",
        "elevation": "Elevation of observation above mean sea level (in meters).",
        "observation_type_id": "Type of observation.",
        "phenomenon_start": "Start time of the phenomenon being observed or observing period, if missing assumed instantaneous with time given by phenomenon_end.",
        "phenomenon_end": "End time of the phenomenon being observed or observing period.",
        "result_value": "The value of the result in float representation.",
        "result_uom": "Units used to represent the value being observed.",
        "result_description": "str representation of the result if applicable.",
        "result_quality": "JSON representation of the result quality, key / value pairs.",
        "result_time": "Time that the result became available.",
        "valid_from": "Time that the result starts to be valid.",
        "valid_to": "Time after which the result is no longer valid.",
        "host_id": "Host associated with making the observation, equivalent to OGC OMS 'host'.",
        "observer_id": "Observer associated with making the observation, equivalent to OGC OMS 'observer'.",
        "observed_property_id": "The phenomenon, or thing, being observed.",
        "observing_procedure_id": "Procedure used to make the observation.",
        "dataset": "Primary dataset that this observation belongs to.",
        "parameter": "List of key/ value pairs in dict.",
        "featureOfInterest_id": "Feature of interest that this observation is associated with.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc.",
        "_source_id": "The source of this record.",
        "_source_identifier": "The original identifier for the record from the data source (if available)."
    }
    _comment = "table to store observations"


@dataclass
class ReferenceStations(DomainModelBase):
    id: str
    host_id: Optional[str]
    reference_station_id: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key for this record.",
        "host_id": "The host / station this record is for.",
        "reference_station_id": "The host / station acting as a reference station.",
        "valid_from": "Date the reference station started as a reference station for this host.",
        "valid_to": "Date the reference station stopped as a reference station for this host.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Reference stations"


@dataclass
class ResponsibleParty(DomainModelBase):
    id: str
    individual_name: Optional[str]
    position_name: Optional[str]
    organization_name: Optional[str]
    contact_information: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "A value uniquely identifying a party (individual or organization).",
        "individual_name": "The name of the organization or the individual.",
        "position_name": "Role or position of the responsible person.",
        "organization_name": "Organization/affiliation of the individual/responsible person. In case of an organization, the name property should be used and this property is not to be used.",
        "contact_information": "Contact information",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Identification of, and means of communication with, person responsible for the resource."


@dataclass
class SensorCharacteristics(DomainModelBase):
    id: str
    equipment_id: str
    observed_property_id: str
    observing_method_id: str
    observing_method_details: Optional[str]
    measurement_units: Optional[int]
    drift_per_unit_time: Optional[float]
    unit_time: Optional[int]
    valid_min: Optional[float]
    valid_max: Optional[float]
    specified_absolute_uncertainty: Optional[float]
    specified_relative_uncertainty: Optional[float]
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "Primary key for this record.",
        "equipment_id": "The equipment / sensor to which this record applies.",
        "observed_property_id": "The observed parameter to which this record applies.",
        "observing_method_id": "Primary method/principles by which the sensor makes measurements.",
        "observing_method_details": "A description of the method of measurement/observation used.",
        "measurement_units": "The units used in this record.",
        "drift_per_unit_time": "Intrinsic capability of the measurement/observing method - drift per unit time. Typically a percentage per unit time but could be absolute e.g. 1 degree per year.",
        "unit_time": "Unit time for drift per unit time (seconds).",
        "valid_min": "Minimum observable value by sensor, in units specified by measurement units.",
        "valid_max": "Maximum observable value by sensor, in units specified by measurement units.",
        "specified_absolute_uncertainty": "Measurement uncertainty for measurements from this sensor, 2 sigma. Units as per measurement units.",
        "specified_relative_uncertainty": "Measurement uncertainty for measurements from this sensor, 2 sigma. Units in %, e.g. 20 %.",
        "links": "Link(s) to further information.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Table to record sensor specifications"


@dataclass
class SensorOperatingStatus(DomainModelBase):
    id: str
    deployment_id: str
    operating_status_id: str
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    __comments = {
        "id": "Primary key for this record.",
        "deployment_id": "The deployment this record belongs to.",
        "operating_status_id": "The operating status of the deployed equipment.",
        "valid_from": "The date from which this status applies.",
        "valid_to": "The date from which this status is no longer valid.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Operating status"


@dataclass
class Source(DomainModelBase):
    id: str
    name: str
    description: str
    source_type_id: str
    links: Optional[dict]
    processor: Optional[str]
    parameters: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "name": "Name of source.",
        "description": "Description of source type, e.g. file etc.",
        "source_type_id": "The type of source.",
        "links": "Link(s) to further information on source.",
        "processor": "Name of processor used to ingest the data.",
        "parameters": "Parameters required to access the data from this source (NEED TO CHECK THIS, ENCRYPT?).",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "placeholder"


@dataclass
class Record(DomainModelBase):
    id: str
    time: str
    title: str
    location: Geography
    created: str
    updated: str
    resource_type: str
    description: str
    keywords: str
    language: str
    external_ids: dict
    themes: dict
    formats: dict
    providers: dict
    license: str
    rights: str
    links: dict
    __comments = {
        "id": "A unique identifier of the catalogue record.",
        "time": "The temporal extent of the resource. Can be null if there is no associated temporal extent.",
        "title": "A human-readable name given to the resource.",
        "location": "A geometry associated with the resource that is used for discovery. Can be null if there is no associated geometry.",
        "created": "Date of creation of this record.",
        "updated": "The most recent date on which the record was changed.",
        "resource_type": "The nature or genre of the resource. The value should be a code, convenient for filtering records. Where available, a link to the canonical URI of the record type resource will be added to the 'links' property.",
        "description": "A free-text account of the resource.",
        "keywords": "The topic or topics of the resource. Typically represented using free-form keywords, tags, key phrases, or classification codes. Semi-colon delimited",
        "language": "The natural language used for textual values (e.g. titles, descriptions, etc.) of the resource. ISO 639-1/639-2 codes should be used.",
        "external_ids": "An identifier for the resource assigned by an external (to the catalogue) entity.",
        "themes": "A knowledge organization system used to classify the resource.",
        "formats": "A list of available distributions of the resource.",
        "providers": "A list of providers qualified by their role in association to the record.",
        "license": "A legal document under which the resource is made available. The value should be a code, convenient for filtering the records. Where applicable, the use of the identifiers from the SPDX License List is recommended. If multiple licenses apply, it is recommended to use ''various'.  Where available, links to a URI of each applicable license should be added to the 'links' property.",
        "rights": "A statement that concerns all rights not addressed by the license such as a copyright statement.",
        "links": "A list of links for accessing the resource (e.g. download link, access link) in one of the supported distribution formats and/or links to other resources associated with this resource. Also, a list of links for navigating the API (e.g. prev, next, etc.).  Since the specification requires that at least the self link be present then the min items for this list should be one."
    }
    _comment = "Discovery metadata record."



