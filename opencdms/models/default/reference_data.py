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
class Altitude(DomainModelBase):
    id: str
    inScheme: str
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation for the classification.",
        "description": "Description of the classification area.",
        "links": "Link(s) to further information on the classification.",
        "_version": "Version of this record, e.g. 1.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Altitude / depth classification code list."


@dataclass
class ApplicationArea(DomainModelBase):
    id: str
    inScheme: str
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation for the application area.",
        "description": "Description of the application area.",
        "links": "Link(s) to further information on the application area.",
        "_version": "Version of this record, e.g. 1.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Application area code list."


@dataclass
class ClimateZone(DomainModelBase):
    id: str
    inSchema: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inSchema": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation for the climate zone.",
        "description": "Description of the climate zone",
        "links": "Links providing further definition of climate zone",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "_comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Climate zone code list."


@dataclass
class CommunicationMethod(DomainModelBase):
    id: str
    inScheme: str
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation for the communication method.",
        "description": "Description of the communication method.",
        "links": "Link(s) to further information on the communication method.",
        "_version": "Version of this record, e.g. 1.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Communication method code list."


@dataclass
class EquipmentType(DomainModelBase):
    id: str
    inScheme: str
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation for the equipment type.",
        "description": "Description of the equipment type.",
        "links": "Link(s) to further information on the equipment type.",
        "_version": "Version of this record, e.g. 1.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Equipment type code list."


@dataclass
class Exposure(DomainModelBase):
    id: str
    inSchema: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inSchema": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation for exposure classification.",
        "description": "Description of sensor exposure according to WMO-No. 8.",
        "links": "Links providing further definition of exposure class.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Sensor exposure classification code list."


@dataclass
class FacilityType(DomainModelBase):
    id: str
    inScheme: str
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation for the facility type.",
        "description": "Description of the facility type.",
        "links": "Link(s) to definition of facility type.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Facility type code list."


@dataclass
class FeatureType(DomainModelBase):
    id: str
    inScheme: str
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation for the feature type.",
        "description": "Description of the feature type.",
        "links": "Link(s) to definition of feature type.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Feature type code list."


@dataclass
class GeopositioningMethod(DomainModelBase):
    id: str
    inScheme: str
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation for the geopositioning method.",
        "description": "Description of the geopositioning method.",
        "links": "Link(s) to further information on the geopositioning method.",
        "_version": "Version of this record, e.g. 1.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Geopositioning method code list."


@dataclass
class LocalTopography(DomainModelBase):
    id: str
    inScheme: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation of the local topography classification.",
        "description": "Description of local topography classification.",
        "links": "Links providing further definition of local topography classification.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Local topography classification code list."


@dataclass
class MeasurementQuality(DomainModelBase):
    id: str
    inScheme: str
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation for the measurement quality classification.",
        "description": "Description of the measurement quality classification.",
        "links": "Link(s) to definition of fmeasurement quality classification.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Measurement quality classification code list."


@dataclass
class MediaType(DomainModelBase):
    id: str
    inScheme: str
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation for the media type.",
        "description": "Description of the media type.",
        "links": "Link(s) to definition of media type.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Media type code list."


@dataclass
class ObservationType(DomainModelBase):
    id: str
    inSchema: str
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key",
        "inSchema": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation for the observation type.",
        "description": "Description of the observation type.",
        "links": "Link(s) to definition of the observation type.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Observation type code list."


@dataclass
class ObservedProperty(DomainModelBase):
    id: str
    inScheme: str
    name: str
    description: str
    standard_name: Optional[str]
    units: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation of observed property, e.g. 'at' for air temperature.",
        "description": "Description of observed property.",
        "standard_name": "CF standard name (if applicable), e.g. 'air_temperature'.",
        "units": "Canonical units, e.g. 'Kelvin'.",
        "links": "Link(s) to definition / source of observed property.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Observed property code list."


@dataclass
class ObservingMethod(DomainModelBase):
    id: str
    inScheme: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation of the observing method.",
        "description": "Description of observing method.",
        "links": "Links providing further definition of observing method.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Observing method code list."


@dataclass
class ObservingProcedure(DomainModelBase):
    id: str
    inScheme: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation of the observing procedure.",
        "description": "Description of observing procedure.",
        "links": "Links providing further definition of observing procedure.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Observing procedure code list."


@dataclass
class ObservingProgram(DomainModelBase):
    id: str
    inScheme: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation of the observing program.",
        "description": "Description of observing program.",
        "links": "Links providing further definition of observing program.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Observing program code list."


@dataclass
class OperatingStatus(DomainModelBase):
    id: str
    inScheme: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation of the operating status.",
        "description": "Description of operating status.",
        "links": "Links providing further definition of operating status.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Operating status code list."


@dataclass
class ReferenceSurface(DomainModelBase):
    id: str
    inScheme: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation of the reference surface.",
        "description": "Description of reference surface.",
        "links": "Links providing further definition of reference.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Reference surface code list."


@dataclass
class RelativeElevation(DomainModelBase):
    id: str
    inScheme: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation of the relative elevation classification.",
        "description": "Description of relative elevation classification.",
        "links": "Links providing further definition of relative elevation classification.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Relative elevation classification code list."


@dataclass
class ReportingStatus(DomainModelBase):
    id: str
    inScheme: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation of the reporting status.",
        "description": "Description of reporting status.",
        "links": "Links providing further definition of reporting status.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Reporting status code list."


@dataclass
class Representativeness(DomainModelBase):
    id: str
    inScheme: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation for the representativeness classification.",
        "description": "Description of the representativeness classification.",
        "links": "Links providing further information on the representativeness classification.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Representativeness classification code list."


@dataclass
class Role(DomainModelBase):
    id: str
    inScheme: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation of the role.",
        "description": "Description of the role.",
        "links": "Links providing further information on the role.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "The function performed by the responsible party."


@dataclass
class SourceOfObservation(DomainModelBase):
    id: str
    inScheme: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation of the source of observation.",
        "description": "Description of the source of observation.",
        "links": "Links providing further information on the source of observation.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Source of observation code list."


@dataclass
class SourceType(DomainModelBase):
    id: str
    inScheme: str
    name: str
    description: str
    IANA_scheme: Optional[str]
    links: Optional[str]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Name of source type",
        "description": "Description of source type, e.g. file etc",
        "IANA_scheme": "IANA scheme (if applicable)",
        "links": "Links providing further definition of source type",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "_comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Source type code list"


@dataclass
class Status(DomainModelBase):
    id: str
    inScheme: str
    name: str
    description: str
    _version: int
    _change_date: datetime
    _user_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name for the status",
        "description": "Description of the status",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Controlled vocabulary to record the status of a record"


@dataclass
class SurfaceCover(DomainModelBase):
    id: str
    inScheme: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation of the surface cover classification.",
        "description": "Description of the surface cover classification.",
        "links": "Links providing further information on the surface cover classification.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Surface cover classification code list."


@dataclass
class SurfaceRoughness(DomainModelBase):
    id: str
    inScheme: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation of the surface roughness classification.",
        "description": "Description of the surface roughness classification.",
        "links": "Links providing further information on the surface roughness classification.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Surface roughness classification code list."


@dataclass
class Territory(DomainModelBase):
    id: str
    inScheme: str
    name: str
    description: str
    ISO3c: str
    wmo_region_id: Optional[str]
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation for the territory.",
        "description": "Official name of territory.",
        "ISO3c": "ISO 3 character country code.",
        "wmo_region_id": "WMO region that represents the territory.",
        "links": "Link(s) to further information.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Territory / country code list"


@dataclass
class TimeZone(DomainModelBase):
    id: str
    inScheme: str
    name: str
    description: str
    offset: float
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Name / abbreviation of time zone",
        "description": "Description of the time zone.",
        "offset": "Offset from UTC in hours (decimal)",
        "links": "Link(s) to further information.",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id": "Which user/agent last modified this record",
        "_status_id": "Whether this is the latest version or an archived version of the record",
        "_comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Time zone code list"


@dataclass
class TopographicContext(DomainModelBase):
    id: str
    inScheme: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation of the topography / bathymetry classification.",
        "description": "Description of the topography / bathymetry classification.",
        "links": "Links providing further information on the topography / bathymetry classification.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "Topographic context classification code list."


@dataclass
class WmoRegion(DomainModelBase):
    id: str
    inScheme: str
    name: Optional[str]
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id: str
    _status_id: str
    _comments: str
    __comments = {
        "id": "ID / primary key.",
        "inScheme": "The scheme/vocabulary that this record is from.",
        "name": "Short name / abbreviation of the WMO regional association.",
        "description": "Description of the WMO regional association.",
        "links": "Links providing further information on the WMO regional association.",
        "_version": "Version number of this record.",
        "_change_date": "Date this record was changed.",
        "_user_id": "Which user/agent last modified this record.",
        "_status_id": "Whether this is the latest version or an archived version of the record.",
        "_comments": "Free text comments on this record, for example description of changes made etc."
    }
    _comment = "WMO regional association code list."



