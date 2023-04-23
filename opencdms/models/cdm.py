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
class User(DomainModelBase):
    id: str
    name: str
    description: str
    _comments = {
        "id": "ID / primary key",
        "name": "Name of user/agent",
        "description": "Description of user / agent"
    }
    _comment = "placeholder"


@dataclass
class Status(DomainModelBase):
    id: str
    name: str
    description: str
    _comments = {
        "id": "ID / primary key",
        "name": "Short name for status",
        "description": "Description of the status"
    }
    _comment = "placeholder"


@dataclass
class ResponsibleParty(DomainModelBase):
    id: str
    name: str
    position_name: Optional[str]
    organization: Optional[str]
    logo: Optional[dict]
    contact_information: Optional[dict]
    _comments = {
        "id": "A value uniquely identifying a party (individual or organization).",
        "name": "The name of the organization or the individual.",
        "position_name": "Role or position of the responsible person.",
        "organization": "Organization/affiliation of the individual/responsible person. In case of an organization, the name property should be used and this property is not to be used.",
        "logo": "Graphic identifying a party",
        "contact_information": "Contact information"
    }
    _comment = "Identification of, and means of communication with, person responsible for the resource. oarec party"


@dataclass
class ObservationType(DomainModelBase):
    id: str
    authority: str
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "ID / primary key",
        "authority": "naming authority for code list entry",
        "name": "Short name for observation type",
        "description": "Description of observation type",
        "links": "Link(s) to definition of observation type",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Table to store observation type, e.g. hourly weather report, raw data, etc"


@dataclass
class FacilityType(DomainModelBase):
    id: str
    authority: str
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "ID / primary key",
        "authority": "Naming authority for code list entry",
        "name": "Short name for feature type",
        "description": "Description of feature type",
        "links": "Link(s) to definition of feature type",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "WMDS facility type, type of observing facility"


@dataclass
class FeatureType(DomainModelBase):
    id: str
    authority: str
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "ID / primary key",
        "authority": "Naming authority for code list entry",
        "name": "Short name for feature type",
        "description": "Description of feature type",
        "links": "Link(s) to definition of feature type",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class WmoRegion(DomainModelBase):
    id: str
    name: str
    description: str
    links: dict
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Short name for WMO region",
        "description": "Long name of WMO region",
        "links": "Link(s) to definition of feature type",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class Territory(DomainModelBase):
    id: str
    ISO3c: str
    name: str
    description: str
    wmo_region_id: Optional[str]
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "ID / primary key",
        "ISO3c": "ISO 3 character country code",
        "name": "Short name for feature type",
        "description": "Description of feature type",
        "wmo_region_id": "WMO region that represents the territory",
        "links": "Link(s) to definition of feature type",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class ObservedProperty(DomainModelBase):
    id: str
    authority: str
    short_name: str
    standard_name: Optional[str]
    units: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "ID / primary key",
        "authority": "Naming authority for code list entry",
        "short_name": "Short name representation of observed property, e.g. 'at' for air temperature",
        "standard_name": "CF standard name (if applicable), e.g. 'air_temperature'",
        "units": "Canonical units, e.g. 'Kelvin'",
        "description": "Description of observed property",
        "links": "Link(s) to definition / source of observed property",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class ObservingProcedure(DomainModelBase):
    id: str
    authority: str
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "ID / primary key",
        "authority": "Naming authority for code list entry",
        "name": "Name of observing procedure",
        "description": "Description of observing procedure",
        "links": "Link(s) to further information",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class TimeZone(DomainModelBase):
    id: str
    abbreviation: str
    name: str
    offset: float
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "ID / primary key",
        "abbreviation": "Abbreviation for time zone",
        "name": "Name / description of timezone",
        "offset": "Offset from UTC (hours)",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class SourceType(DomainModelBase):
    id: str
    name: str
    description: str
    scheme: Optional[str]
    links: Optional[str]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Name of source type",
        "description": "Description of source type, e.g. file etc",
        "scheme": "IANA scheme (if applicable)",
        "links": "Links providing further definition of source type",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class MediaType(DomainModelBase):
    id: Optional[str]
    name: Optional[str]
    description: str
    _comments = {
        "id": "",
        "name": "",
        "description": "Type of media uploaded"
    }
    _comment = "placeholder"


@dataclass
class ClimateZone(DomainModelBase):
    id: Optional[str]
    authority: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "",
        "authority": "Naming authority for code list entry",
        "name": "",
        "description": "",
        "links": "Links providing further definition of climate zone",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "wmdr.climate_zone"


@dataclass
class SurfaceCover(DomainModelBase):
    id: Optional[str]
    authority: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "",
        "authority": "Naming authority for code list entry",
        "name": "",
        "description": "",
        "links": "Links providing further definition of climate zone",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class SurfaceRoughness(DomainModelBase):
    id: Optional[str]
    authority: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "",
        "authority": "Naming authority for code list entry",
        "name": "",
        "description": "",
        "links": "Links providing further definition of climate zone",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class Topography(DomainModelBase):
    id: Optional[str]
    authority: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "",
        "authority": "Naming authority for code list entry",
        "name": "",
        "description": "",
        "links": "Links providing further definition of climate zone",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class Season(DomainModelBase):
    id: Optional[str]
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "",
        "name": "",
        "description": "",
        "links": "Links providing further definition of climate zone",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class Programme(DomainModelBase):
    id: Optional[str]
    authority: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "",
        "authority": "Naming authority for code list entry",
        "name": "",
        "description": "",
        "links": "Links providing further definition of climate zone",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class ObservingMethod(DomainModelBase):
    id: Optional[str]
    authority: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "",
        "authority": "Naming authority for code list entry",
        "name": "",
        "description": "Description of observing method",
        "links": "Links providing further definition of observing method",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class Exposure(DomainModelBase):
    id: Optional[str]
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "",
        "name": "",
        "description": "Description of sensor exposure according to WMO-No. 8",
        "links": "Links providing further definition of exposure class",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class ReferenceSurface(DomainModelBase):
    id: Optional[str]
    name: Optional[str]
    description: str
    _comments = {
        "id": "",
        "name": "",
        "description": "Description of reference surface"
    }
    _comment = "placeholder"


@dataclass
class Role(DomainModelBase):
    id: str
    authority: str
    name: str
    description: str
    _comments = {
        "id": "Primary key for this record",
        "authority": "Namelist authority",
        "name": "The name of the role",
        "description": "Description of the role"
    }
    _comment = "The function performed by the responsible party."


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
    _comments = {
        "id": "",
        "media_type_id": "",
        "description": "",
        "created": "",
        "creator": "",
        "rights": "",
        "source": "",
        "data": ""
    }
    _comment = "store for digital media, e.g. photos, reports, videos, etc"


@dataclass
class Host(DomainModelBase):
    id: str
    name: str
    description: Optional[str]
    links: Optional[dict]
    location: Optional[Geography]
    elevation: Optional[float]
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
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Preferred name of host",
        "description": "Description of host",
        "links": "URI to host, e.g. to OSCAR/Surface",
        "location": "Location of station",
        "elevation": "Elevation of station above mean sea level in meters",
        "wigos_station_identifier": "WIGOS station identifier",
        "facility_type_id": "Type of observing facility, fixed land, mobile sea, etc",
        "date_established": "Date host was first established",
        "date_closed": "Date host was first established",
        "wmo_region_id": "WMO region in which the host is located",
        "territory_id": "Territory the host is located in",
        "time_zone_id": "Time zone the host is located in",
        "valid_from": "Date from which the details for this record are valid",
        "valid_to": "Date after which the details for this record are no longer valid",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "wmdr.observing_facility"


@dataclass
class HostEnvironment(DomainModelBase):
    id: str
    host: str
    climate_zone_id: Optional[str]
    surface_cover_id: Optional[str]
    surface_roughness_id: Optional[str]
    topography_id: Optional[str]
    season_id: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "Primary key for this record",
        "host": "Host associated with this record",
        "climate_zone_id": "Climate zone that the associated host is located in",
        "surface_cover_id": "Type of sueface cover",
        "surface_roughness_id": "Typical surface roughness of the site surrounding the host",
        "topography_id": "Topography of the environment surrounding the host",
        "season_id": "Season that is applicable to this record (e.g. all, winter, spring, summer, autumn)",
        "valid_from": "Date the this record is valid from",
        "valid_to": "date that this record is valid to",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Description of the environment at the specified host"


@dataclass
class HostAffiliation(DomainModelBase):
    id: str
    host_id: str
    programme_id: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "Primary key for this record",
        "host_id": "Host described by this record",
        "programme_id": "Observing programme that this host is affiliated with",
        "valid_from": "Date from which the details for this record are valid",
        "valid_to": "Date after which the details for this record are no longer valid",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Which programs this host is affiliated with"


@dataclass
class HostAlias(DomainModelBase):
    id: str
    host_id: str
    alternative: Optional[str]
    alternative_name: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "Primary key for this record",
        "host_id": "Primary ID by which the host is known",
        "alternative": "Alternative ID by which the host is known",
        "alternative_name": "Alternative name by which the host is known",
        "valid_from": "Date the alternative id/name was used from",
        "valid_to": "Date the alternative id/name was used to",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "table to track known aliases for hosts"


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
    comments: str
    _comments = {
        "id": "Unique identifier for this record",
        "responsible_party_id": "The responsible party",
        "role_id": "The role this responsible party plays",
        "host_id": "The host that this record corresponds to",
        "valid_from": "Date this record is valid from",
        "valid_to": "Date this record is valid to",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


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
    comments: str
    _comments = {
        "id": "Primary key for this record",
        "host_id": "",
        "media_id": "",
        "valid_from": "",
        "valid_to": "",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Link table between hosts and media"


@dataclass
class Observer(DomainModelBase):
    id: str
    name: str
    description: str
    links: Optional[dict]
    location: Optional[Geography]
    elevation: Optional[float]
    manufacturer: Optional[str]
    model: Optional[str]
    serial_number: Optional[str]
    firmware_version: Optional[str]
    control_schedule_id: Optional[str]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Name of sensor",
        "description": "Description of sensor",
        "links": "Link(s) to further information",
        "location": "Location of observer",
        "elevation": "Elevation of observer above mean sea level",
        "manufacturer": "Make, or manufacturer, of sensor",
        "model": "Model of sensor",
        "serial_number": "Serial number of sensor",
        "firmware_version": "Firmware version of software installed in sensor",
        "control_schedule_id": "Link to information on calibration schedule and details",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "wmdr.equipment"


@dataclass
class ControlSchedule(DomainModelBase):
    id: Optional[str]
    name: Optional[str]
    description: str
    _comments = {
        "id": "",
        "name": "",
        "description": "Description of control schedule"
    }
    _comment = "placeholder"


@dataclass
class ObserverCharacteristics(DomainModelBase):
    id: str
    observer_id: str
    observed_property_id: Optional[str]
    observing_method_id: Optional[str]
    measurement_units: Optional[int]
    drift_per_unit_time: Optional[float]
    unit_time: Optional[int]
    valid_min: Optional[float]
    valid_max: Optional[float]
    measurement_uncertainty: Optional[float]
    measurement_accuracy: Optional[float]
    measurement_repeatability: Optional[float]
    measurement_resolution: Optional[float]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "Primary key for this record",
        "observer_id": "The observer to which this record applies",
        "observed_property_id": "The observed parameter to which this record applies",
        "observing_method_id": "Primary method/principles by which the sensor makes measurements",
        "measurement_units": "The units used in this record",
        "drift_per_unit_time": "Sensor drift per unit time, units specified by measurement units, unit time by unit time",
        "unit_time": "Unit time for drift per unit time (seconds)",
        "valid_min": "Minimum observable value by sensor, in units specificed by measurement units",
        "valid_max": "Maximum observable value by sensor, in units specificed by measurement units",
        "measurement_uncertainty": "Measurement uncertainty for measurements from this sensor, 2 sigma. Units as per measuremenet units",
        "measurement_accuracy": "Measurement accuracy (trueness) for measurements from this sensor, 2 sigma. Units as per measuremenet units",
        "measurement_repeatability": "Measurement repeatability (precision) for measurements from this sensor, 2 sigma. Units as per measuremenet units",
        "measurement_resolution": "Minimum change detectable for measurements from this sensor. Units as per measurement units",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Table to record sensor specifications"


@dataclass
class ObserverResponsibleParty(DomainModelBase):
    id: Optional[str]
    responsible_party_id: str
    role_id: str
    observer_id: str
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "",
        "responsible_party_id": "",
        "role_id": "",
        "observer_id": "The observer that this record corresponds to",
        "valid_from": "Date this record is valid from",
        "valid_to": "Date this record is valid to",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class ObserverMedia(DomainModelBase):
    id: str
    observer_id: Optional[str]
    media_id: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "Primary key for this record",
        "observer_id": "",
        "media_id": "",
        "valid_from": "",
        "valid_to": "",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Link table between hosts and media"


@dataclass
class Collection(DomainModelBase):
    id: str
    name: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Name of collection",
        "links": "Link(s) to further information on collection",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class Feature(DomainModelBase):
    id: str
    name: Optional[str]
    description: Optional[str]
    links: Optional[dict]
    feature_type_id: str
    geometry: Geography
    elevation: Optional[float]
    parent_id: Optional[str]
    properties: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Name of feature",
        "description": "Description of feature",
        "links": "Link(s) to further information on feature",
        "feature_type_id": "enumerated feature type",
        "geometry": "",
        "elevation": "Meam elevation of feature above mean sea level",
        "parent_id": "Parent feature for this feature if nested",
        "properties": "Array of named values consistent with that defined for the feature type",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "table to contain definition of different geographic features"


@dataclass
class Source(DomainModelBase):
    id: str
    name: str
    description: str
    source_type_id: str
    links: Optional[dict]
    processor: Optional[str]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Name of source",
        "description": "Description of source type, e.g. file etc",
        "source_type_id": "The type of source",
        "links": "Link(s) to further information on source",
        "processor": "Name of processor used to ingest the data",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class Observation(DomainModelBase):
    id: str
    location: Geography
    elevation: Optional[float]
    observation_type_id: Optional[str]
    phenomenon_start: Optional[datetime]
    phenomenon_end: datetime
    result_value: float
    result_uom: Optional[str]
    result_description: Optional[str]
    result_quality: Optional[dict]
    result_time: Optional[datetime]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    host_id: str
    observer_id: Optional[str]
    observed_property_id: str
    observing_procedure_id: Optional[str]
    collection_id: Optional[str]
    parameter: Optional[dict]
    feature_id: Optional[str]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _source_id: str
    _source_identifier: str
    _comments = {
        "id": "ID / primary key",
        "location": "Location of observation",
        "elevation": "Elevation of observation above mean sea level (in meters)",
        "observation_type_id": "Type of observation",
        "phenomenon_start": "Start time of the phenomenon being observed or observing period, if missing assumed instantaneous with time given by phenomenon_end",
        "phenomenon_end": "End time of the phenomenon being observed or observing period",
        "result_value": "The value of the result in float representation",
        "result_uom": "Units used to represent the value being observed",
        "result_description": "str representation of the result if applicable",
        "result_quality": "JSON representation of the result quality, key / value pairs",
        "result_time": "Time that the result became available",
        "valid_from": "Time that the result starts to be valid",
        "valid_to": "Time after which the result is no longer valid",
        "host_id": "Host associated with making the observation, equivalent to OGC OMS 'host'",
        "observer_id": "Observer associated with making the observation, equivalent to OGC OMS 'observer'",
        "observed_property_id": "The phenomenon, or thing, being observed",
        "observing_procedure_id": "Procedure used to make the observation",
        "collection_id": "Primary collection or dataset that this observation belongs to. Note: this is different to the OGC OMS collection concept.",
        "parameter": "List of key/ value pairs in dict",
        "feature_id": "Feature of interest that this observation is associated with",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc",
        "_source_id": "The source of this record",
        "_source_identifier": "The original identifier for the record from the data source"
    }
    _comment = "table to store observations"


@dataclass
class Deployment(DomainModelBase):
    id: str
    host_id: Optional[str]
    observer_id: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    installation_height: Optional[float]
    reference_surface_id: Optional[str]
    exposure_id: Optional[str]
    configuration: Optional[str]
    maintenance_schedule_id: Optional[str]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    comments: str
    _comments = {
        "id": "Unique ID / primary key for deployment",
        "host_id": "",
        "observer_id": "",
        "valid_from": "",
        "valid_to": "",
        "installation_height": "Installation height above reference surface (in meters)",
        "reference_surface_id": "",
        "exposure_id": "",
        "configuration": "Textual description of sensor installation and configuration",
        "maintenance_schedule_id": "",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Table to track deployments of an observer to a host"


@dataclass
class MaintenanceSchedule(DomainModelBase):
    id: Optional[str]
    name: Optional[str]
    description: str
    _comments = {
        "id": "",
        "name": "",
        "description": "Description of maintenance schedule"
    }
    _comment = "placeholder"


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
    comments: str
    _comments = {
        "id": "Primary key for this record",
        "deployment_id": "",
        "media_id": "",
        "valid_from": "",
        "valid_to": "",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Link table between hosts and media"


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
    _comments = {
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
    _comment = "The function performed by the responsible party."
