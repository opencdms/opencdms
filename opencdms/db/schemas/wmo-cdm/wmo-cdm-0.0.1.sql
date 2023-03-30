--
-- PostgreSQL database dump
--

-- Dumped from database version 12.14 (Ubuntu 12.14-1.pgdg22.04+1)
-- Dumped by pg_dump version 12.14 (Ubuntu 12.14-0ubuntu0.20.04.1)

SELECT pg_catalog.set_config('search_path', '', false);

--
-- Name: cdm; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA cdm;




--
-- Name: collection; Type: TABLE; Schema: cdm; Owner: -
--

CREATE TABLE cdm.collection (
    id character varying NOT NULL,
    name character varying,
    links jsonb
);


--
-- Name: COLUMN collection.id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.collection.id IS 'ID / primary key';


--
-- Name: COLUMN collection.name; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.collection.name IS 'Name of collection';


--
-- Name: COLUMN collection.links; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.collection.links IS 'Link(s) to further information on collection';


--
-- Name: feature; Type: TABLE; Schema: cdm; Owner: -
--

CREATE TABLE cdm.feature (
    id character varying NOT NULL,
    type_id integer,
    geometry public.geography(Geometry,4326),
    elevation numeric,
    parent_id character varying,
    name character varying,
    description character varying,
    links jsonb
);


--
-- Name: COLUMN feature.id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.feature.id IS 'ID / primary key';


--
-- Name: COLUMN feature.type_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.feature.type_id IS 'enumerated feature type';


--
-- Name: COLUMN feature.elevation; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.feature.elevation IS 'Elevation of feature above mean sea level';


--
-- Name: COLUMN feature.parent_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.feature.parent_id IS 'Parent feature for this feature if nested';


--
-- Name: COLUMN feature.name; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.feature.name IS 'Name of feature';


--
-- Name: COLUMN feature.description; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.feature.description IS 'Description of feature';


--
-- Name: COLUMN feature.links; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.feature.links IS 'Link(s) to further information on feature';


--
-- Name: feature_type; Type: TABLE; Schema: cdm; Owner: -
--

CREATE TABLE cdm.feature_type (
    id integer NOT NULL,
    name character varying,
    description character varying,
    links jsonb
);


--
-- Name: COLUMN feature_type.id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.feature_type.id IS 'ID / primary key';


--
-- Name: COLUMN feature_type.name; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.feature_type.name IS 'Short name for feature type';


--
-- Name: COLUMN feature_type.description; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.feature_type.description IS 'Description of feature type';


--
-- Name: COLUMN feature_type.links; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.feature_type.links IS 'Link(s) to definition of feature type';


--
-- Name: feature_type_id_seq; Type: SEQUENCE; Schema: cdm; Owner: -
--

CREATE SEQUENCE cdm.feature_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: feature_type_id_seq; Type: SEQUENCE OWNED BY; Schema: cdm; Owner: -
--

ALTER SEQUENCE cdm.feature_type_id_seq OWNED BY cdm.feature_type.id;


--
-- Name: host; Type: TABLE; Schema: cdm; Owner: -
--

CREATE TABLE cdm.host (
    id character varying NOT NULL,
    name character varying,
    description character varying,
    links jsonb,
    location public.geography(Geometry,4326),
    elevation numeric,
    wigos_station_identifier character varying,
    facility_type character varying,
    date_established timestamp with time zone,
    date_closed timestamp with time zone,
    wmo_region character varying,
    territory character varying,
    valid_from timestamp with time zone,
    valid_to timestamp with time zone,
    version integer,
    change_date timestamp with time zone,
    user_id character varying,
    status_id integer,
    comments character varying,
    time_zone_id integer
);


--
-- Name: COLUMN host.id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.id IS 'ID / primary key';


--
-- Name: COLUMN host.name; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.name IS 'Preferred name of host';


--
-- Name: COLUMN host.description; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.description IS 'Description of host';


--
-- Name: COLUMN host.links; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.links IS 'URI to host, e.g. to OSCAR/Surface';


--
-- Name: COLUMN host.location; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.location IS 'Location of station';


--
-- Name: COLUMN host.elevation; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.elevation IS 'Elevation of station above mean sea level';


--
-- Name: COLUMN host.wigos_station_identifier; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.wigos_station_identifier IS 'WIGOS station identifier';


--
-- Name: COLUMN host.facility_type; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.facility_type IS 'Type of observing facility, fixed land, mobile sea, etc';


--
-- Name: COLUMN host.date_established; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.date_established IS 'Date host was first established';


--
-- Name: COLUMN host.date_closed; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.date_closed IS 'Date host was first established';


--
-- Name: COLUMN host.wmo_region; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.wmo_region IS 'WMO region in which the host is located';


--
-- Name: COLUMN host.territory; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.territory IS 'Territory the host is located in';


--
-- Name: COLUMN host.valid_from; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.valid_from IS 'Date from which the details for this record are valid';


--
-- Name: COLUMN host.valid_to; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.valid_to IS 'Date after which the details for this record are no longer valid';


--
-- Name: COLUMN host.version; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.version IS 'Version number of this record';


--
-- Name: COLUMN host.change_date; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.change_date IS 'Date this record was changed';


--
-- Name: COLUMN host.user_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.user_id IS 'Which user last modified this record';


--
-- Name: COLUMN host.status_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.status_id IS 'Whether this is the latest version or an archived version of the record';


--
-- Name: COLUMN host.comments; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.comments IS 'Free text comments on this record, for example description of changes made etc';


--
-- Name: COLUMN host.time_zone_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.host.time_zone_id IS 'Time zone the host is located in';


--
-- Name: observation; Type: TABLE; Schema: cdm; Owner: -
--

CREATE TABLE cdm.observation (
    id character varying NOT NULL,
    location public.geography(Geometry,4326),
    elevation numeric,
    observation_type_id integer,
    phenomenon_start timestamp with time zone,
    phenomenon_end timestamp with time zone,
    result_value numeric,
    result_uom character varying,
    result_description character varying,
    result_quality jsonb,
    result_time timestamp with time zone,
    valid_from timestamp with time zone,
    valid_to timestamp with time zone,
    host_id character varying,
    observer_id character varying,
    observed_property_id integer,
    observing_procedure_id integer,
    report_id character varying,
    collection_id character varying,
    parameter jsonb,
    feature_of_interest_id character varying,
    version integer,
    change_date timestamp with time zone,
    user_id character varying,
    status_id integer,
    comments character varying,
    source_id character varying
);


--
-- Name: COLUMN observation.id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.id IS 'ID / primary key';


--
-- Name: COLUMN observation.location; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.location IS 'Location of observation';


--
-- Name: COLUMN observation.elevation; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.elevation IS 'Elevation of observation above mean sea level';


--
-- Name: COLUMN observation.observation_type_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.observation_type_id IS 'Type of observation';


--
-- Name: COLUMN observation.phenomenon_start; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.phenomenon_start IS 'Start time of the phenomenon being observed or observing period, if missing assumed instantaneous with time given by phenomenon_end';


--
-- Name: COLUMN observation.phenomenon_end; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.phenomenon_end IS 'End time of the phenomenon being observed or observing period';


--
-- Name: COLUMN observation.result_value; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.result_value IS 'The value of the result in float representation';


--
-- Name: COLUMN observation.result_uom; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.result_uom IS 'Units used to represent the value being observed';


--
-- Name: COLUMN observation.result_description; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.result_description IS 'str representation of the result if applicable';


--
-- Name: COLUMN observation.result_quality; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.result_quality IS 'JSON representation of the result quality, key / value pairs';


--
-- Name: COLUMN observation.result_time; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.result_time IS 'Time that the result became available';


--
-- Name: COLUMN observation.valid_from; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.valid_from IS 'Time that the result starts to be valid';


--
-- Name: COLUMN observation.valid_to; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.valid_to IS 'Time after which the result is no longer valid';


--
-- Name: COLUMN observation.host_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.host_id IS 'Host associated with making the observation, equivalent to OGC OMS ''host''';


--
-- Name: COLUMN observation.observer_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.observer_id IS 'Observer associated with making the observation, equivalent to OGC OMS ''observer''';


--
-- Name: COLUMN observation.observed_property_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.observed_property_id IS 'The phenomenon, or thing, being observed';


--
-- Name: COLUMN observation.observing_procedure_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.observing_procedure_id IS 'Procedure used to make the observation';


--
-- Name: COLUMN observation.report_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.report_id IS 'Parent report ID, used to link coincident observations together';


--
-- Name: COLUMN observation.collection_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.collection_id IS 'Primary collection or dataset that this observation belongs to';


--
-- Name: COLUMN observation.parameter; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.parameter IS 'List of key/ value pairs in dict';


--
-- Name: COLUMN observation.feature_of_interest_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.feature_of_interest_id IS 'Feature that this observation is associated with';


--
-- Name: COLUMN observation.version; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.version IS 'Version number of this record';


--
-- Name: COLUMN observation.change_date; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.change_date IS 'Date this record was changed';


--
-- Name: COLUMN observation.user_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.user_id IS 'Which user last modified this record';


--
-- Name: COLUMN observation.status_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.status_id IS 'Whether this is the latest version or an archived version of the record';


--
-- Name: COLUMN observation.comments; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.comments IS 'Free text comments on this record, for example description of changes made etc';


--
-- Name: COLUMN observation.source_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation.source_id IS 'The source of this record';


--
-- Name: observation_type; Type: TABLE; Schema: cdm; Owner: -
--

CREATE TABLE cdm.observation_type (
    id integer NOT NULL,
    name character varying,
    description character varying,
    links jsonb
);


--
-- Name: COLUMN observation_type.id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation_type.id IS 'ID / primary key';


--
-- Name: COLUMN observation_type.name; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation_type.name IS 'Short name for observation type';


--
-- Name: COLUMN observation_type.description; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation_type.description IS 'Description of observation type';


--
-- Name: COLUMN observation_type.links; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observation_type.links IS 'Link(s) to definition of observation type';


--
-- Name: observation_type_id_seq; Type: SEQUENCE; Schema: cdm; Owner: -
--

CREATE SEQUENCE cdm.observation_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: observation_type_id_seq; Type: SEQUENCE OWNED BY; Schema: cdm; Owner: -
--

ALTER SEQUENCE cdm.observation_type_id_seq OWNED BY cdm.observation_type.id;


--
-- Name: observed_property; Type: TABLE; Schema: cdm; Owner: -
--

CREATE TABLE cdm.observed_property (
    id integer NOT NULL,
    short_name character varying,
    standard_name character varying,
    units character varying,
    description character varying,
    links jsonb
);


--
-- Name: COLUMN observed_property.id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observed_property.id IS 'ID / primary key';


--
-- Name: COLUMN observed_property.short_name; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observed_property.short_name IS 'Short name representation of observed property, e.g. ''at''';


--
-- Name: COLUMN observed_property.standard_name; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observed_property.standard_name IS 'CF standard name (if applicable), e.g. ''air_temperature''';


--
-- Name: COLUMN observed_property.units; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observed_property.units IS 'Canonical units, e.g. ''Kelvin''';


--
-- Name: COLUMN observed_property.description; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observed_property.description IS 'Description of observed property';


--
-- Name: COLUMN observed_property.links; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observed_property.links IS 'Link(s) to definition / source of observed property';


--
-- Name: observed_property_id_seq; Type: SEQUENCE; Schema: cdm; Owner: -
--

CREATE SEQUENCE cdm.observed_property_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: observed_property_id_seq; Type: SEQUENCE OWNED BY; Schema: cdm; Owner: -
--

ALTER SEQUENCE cdm.observed_property_id_seq OWNED BY cdm.observed_property.id;


--
-- Name: observer; Type: TABLE; Schema: cdm; Owner: -
--

CREATE TABLE cdm.observer (
    id character varying NOT NULL,
    name character varying,
    description character varying,
    links jsonb,
    location public.geography(Geometry,4326),
    elevation numeric,
    manufacturer character varying,
    model character varying,
    serial_number character varying,
    firmware_version character varying,
    uncertainty character varying,
    observing_method character varying
);


--
-- Name: COLUMN observer.id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observer.id IS 'ID / primary key';


--
-- Name: COLUMN observer.name; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observer.name IS 'Name of sensor';


--
-- Name: COLUMN observer.description; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observer.description IS 'Description of sensor';


--
-- Name: COLUMN observer.links; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observer.links IS 'Link(s) to further information';


--
-- Name: COLUMN observer.location; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observer.location IS 'Location of observer';


--
-- Name: COLUMN observer.elevation; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observer.elevation IS 'Elevation of observer above mean sea level';


--
-- Name: COLUMN observer.manufacturer; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observer.manufacturer IS 'Make, or manufacturer, of sensor';


--
-- Name: COLUMN observer.model; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observer.model IS 'Model of sensor';


--
-- Name: COLUMN observer.serial_number; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observer.serial_number IS 'Serial number of sensor';


--
-- Name: COLUMN observer.firmware_version; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observer.firmware_version IS 'Firmware version of software installed in sensor';


--
-- Name: COLUMN observer.uncertainty; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observer.uncertainty IS 'Standard uncertainty in measurements from sensor';


--
-- Name: COLUMN observer.observing_method; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observer.observing_method IS 'Primary method/principles by which the sensor makes measurements';


--
-- Name: observing_procedure; Type: TABLE; Schema: cdm; Owner: -
--

CREATE TABLE cdm.observing_procedure (
    id integer NOT NULL,
    name character varying,
    description character varying,
    links jsonb
);


--
-- Name: COLUMN observing_procedure.id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observing_procedure.id IS 'ID / primary key';


--
-- Name: COLUMN observing_procedure.name; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observing_procedure.name IS 'Name of observing procedure';


--
-- Name: COLUMN observing_procedure.description; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observing_procedure.description IS 'Description of observing procedure';


--
-- Name: COLUMN observing_procedure.links; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.observing_procedure.links IS 'Link(s) to further information';


--
-- Name: observing_procedure_id_seq; Type: SEQUENCE; Schema: cdm; Owner: -
--

CREATE SEQUENCE cdm.observing_procedure_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: observing_procedure_id_seq; Type: SEQUENCE OWNED BY; Schema: cdm; Owner: -
--

ALTER SEQUENCE cdm.observing_procedure_id_seq OWNED BY cdm.observing_procedure.id;


--
-- Name: record_status; Type: TABLE; Schema: cdm; Owner: -
--

CREATE TABLE cdm.record_status (
    id integer NOT NULL,
    name character varying,
    description character varying
);


--
-- Name: COLUMN record_status.id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.record_status.id IS 'ID / primary key';


--
-- Name: COLUMN record_status.name; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.record_status.name IS 'Short name for status';


--
-- Name: COLUMN record_status.description; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.record_status.description IS 'Description of the status';


--
-- Name: record_status_id_seq; Type: SEQUENCE; Schema: cdm; Owner: -
--

CREATE SEQUENCE cdm.record_status_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: record_status_id_seq; Type: SEQUENCE OWNED BY; Schema: cdm; Owner: -
--

ALTER SEQUENCE cdm.record_status_id_seq OWNED BY cdm.record_status.id;


--
-- Name: source; Type: TABLE; Schema: cdm; Owner: -
--

CREATE TABLE cdm.source (
    id character varying NOT NULL,
    source_type_id character varying,
    name character varying,
    links jsonb,
    processor character varying
);


--
-- Name: COLUMN source.id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.source.id IS 'ID / primary key';


--
-- Name: COLUMN source.source_type_id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.source.source_type_id IS 'The type of source';


--
-- Name: COLUMN source.name; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.source.name IS 'Name of source';


--
-- Name: COLUMN source.links; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.source.links IS 'Link(s) to further information on source';


--
-- Name: COLUMN source.processor; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.source.processor IS 'Name of processor used to ingest the data';


--
-- Name: source_type; Type: TABLE; Schema: cdm; Owner: -
--

CREATE TABLE cdm.source_type (
    id character varying NOT NULL,
    description character varying
);


--
-- Name: COLUMN source_type.id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.source_type.id IS 'ID / primary key';


--
-- Name: COLUMN source_type.description; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.source_type.description IS 'Description of source type, e.g. file etc';


--
-- Name: time_zone; Type: TABLE; Schema: cdm; Owner: -
--

CREATE TABLE cdm.time_zone (
    id integer NOT NULL,
    abbreviation character varying,
    name character varying,
    "offset" character varying
);


--
-- Name: COLUMN time_zone.id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.time_zone.id IS 'ID / primary key';


--
-- Name: COLUMN time_zone.abbreviation; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.time_zone.abbreviation IS 'Abbreviation for time zone';


--
-- Name: COLUMN time_zone.name; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.time_zone.name IS 'Name / description of timezone';


--
-- Name: COLUMN time_zone."offset"; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm.time_zone."offset" IS 'Offset from UTC';


--
-- Name: time_zone_id_seq; Type: SEQUENCE; Schema: cdm; Owner: -
--

CREATE SEQUENCE cdm.time_zone_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: time_zone_id_seq; Type: SEQUENCE OWNED BY; Schema: cdm; Owner: -
--

ALTER SEQUENCE cdm.time_zone_id_seq OWNED BY cdm.time_zone.id;


--
-- Name: user; Type: TABLE; Schema: cdm; Owner: -
--

CREATE TABLE cdm."user" (
    id character varying NOT NULL,
    name character varying
);


--
-- Name: COLUMN "user".id; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm."user".id IS 'ID / primary key';


--
-- Name: COLUMN "user".name; Type: COMMENT; Schema: cdm; Owner: -
--

COMMENT ON COLUMN cdm."user".name IS 'Name of user';


--
-- Name: feature_type id; Type: DEFAULT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.feature_type ALTER COLUMN id SET DEFAULT nextval('cdm.feature_type_id_seq'::regclass);


--
-- Name: observation_type id; Type: DEFAULT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observation_type ALTER COLUMN id SET DEFAULT nextval('cdm.observation_type_id_seq'::regclass);


--
-- Name: observed_property id; Type: DEFAULT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observed_property ALTER COLUMN id SET DEFAULT nextval('cdm.observed_property_id_seq'::regclass);


--
-- Name: observing_procedure id; Type: DEFAULT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observing_procedure ALTER COLUMN id SET DEFAULT nextval('cdm.observing_procedure_id_seq'::regclass);


--
-- Name: record_status id; Type: DEFAULT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.record_status ALTER COLUMN id SET DEFAULT nextval('cdm.record_status_id_seq'::regclass);


--
-- Name: time_zone id; Type: DEFAULT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.time_zone ALTER COLUMN id SET DEFAULT nextval('cdm.time_zone_id_seq'::regclass);


--
-- Data for Name: collection; Type: TABLE DATA; Schema: cdm; Owner: -
--

COPY cdm.collection (id, name, links) FROM stdin;
\.


--
-- Data for Name: feature; Type: TABLE DATA; Schema: cdm; Owner: -
--

COPY cdm.feature (id, type_id, geometry, elevation, parent_id, name, description, links) FROM stdin;
\.


--
-- Data for Name: feature_type; Type: TABLE DATA; Schema: cdm; Owner: -
--

COPY cdm.feature_type (id, name, description, links) FROM stdin;
\.


--
-- Data for Name: host; Type: TABLE DATA; Schema: cdm; Owner: -
--

COPY cdm.host (id, name, description, links, location, elevation, wigos_station_identifier, facility_type, date_established, date_closed, wmo_region, territory, valid_from, valid_to, version, change_date, user_id, status_id, comments, time_zone_id) FROM stdin;
\.


--
-- Data for Name: observation; Type: TABLE DATA; Schema: cdm; Owner: -
--

COPY cdm.observation (id, location, elevation, observation_type_id, phenomenon_start, phenomenon_end, result_value, result_uom, result_description, result_quality, result_time, valid_from, valid_to, host_id, observer_id, observed_property_id, observing_procedure_id, report_id, collection_id, parameter, feature_of_interest_id, version, change_date, user_id, status_id, comments, source_id) FROM stdin;
\.


--
-- Data for Name: observation_type; Type: TABLE DATA; Schema: cdm; Owner: -
--

COPY cdm.observation_type (id, name, description, links) FROM stdin;
\.


--
-- Data for Name: observed_property; Type: TABLE DATA; Schema: cdm; Owner: -
--

COPY cdm.observed_property (id, short_name, standard_name, units, description, links) FROM stdin;
\.


--
-- Data for Name: observer; Type: TABLE DATA; Schema: cdm; Owner: -
--

COPY cdm.observer (id, name, description, links, location, elevation, manufacturer, model, serial_number, firmware_version, uncertainty, observing_method) FROM stdin;
\.


--
-- Data for Name: observing_procedure; Type: TABLE DATA; Schema: cdm; Owner: -
--

COPY cdm.observing_procedure (id, name, description, links) FROM stdin;
\.


--
-- Data for Name: record_status; Type: TABLE DATA; Schema: cdm; Owner: -
--

COPY cdm.record_status (id, name, description) FROM stdin;
\.


--
-- Data for Name: source; Type: TABLE DATA; Schema: cdm; Owner: -
--

COPY cdm.source (id, source_type_id, name, links, processor) FROM stdin;
\.


--
-- Data for Name: source_type; Type: TABLE DATA; Schema: cdm; Owner: -
--

COPY cdm.source_type (id, description) FROM stdin;
\.


--
-- Data for Name: time_zone; Type: TABLE DATA; Schema: cdm; Owner: -
--

COPY cdm.time_zone (id, abbreviation, name, "offset") FROM stdin;
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: cdm; Owner: -
--

COPY cdm."user" (id, name) FROM stdin;
\.


--
-- Name: feature_type_id_seq; Type: SEQUENCE SET; Schema: cdm; Owner: -
--

SELECT pg_catalog.setval('cdm.feature_type_id_seq', 1, false);


--
-- Name: observation_type_id_seq; Type: SEQUENCE SET; Schema: cdm; Owner: -
--

SELECT pg_catalog.setval('cdm.observation_type_id_seq', 1, false);


--
-- Name: observed_property_id_seq; Type: SEQUENCE SET; Schema: cdm; Owner: -
--

SELECT pg_catalog.setval('cdm.observed_property_id_seq', 1, false);


--
-- Name: observing_procedure_id_seq; Type: SEQUENCE SET; Schema: cdm; Owner: -
--

SELECT pg_catalog.setval('cdm.observing_procedure_id_seq', 1, false);


--
-- Name: record_status_id_seq; Type: SEQUENCE SET; Schema: cdm; Owner: -
--

SELECT pg_catalog.setval('cdm.record_status_id_seq', 1, false);


--
-- Name: time_zone_id_seq; Type: SEQUENCE SET; Schema: cdm; Owner: -
--

SELECT pg_catalog.setval('cdm.time_zone_id_seq', 1, false);


--
-- Name: collection collection_pkey; Type: CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.collection
    ADD CONSTRAINT collection_pkey PRIMARY KEY (id);


--
-- Name: feature feature_pkey; Type: CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.feature
    ADD CONSTRAINT feature_pkey PRIMARY KEY (id);


--
-- Name: feature_type feature_type_pkey; Type: CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.feature_type
    ADD CONSTRAINT feature_type_pkey PRIMARY KEY (id);


--
-- Name: host host_pkey; Type: CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.host
    ADD CONSTRAINT host_pkey PRIMARY KEY (id);


--
-- Name: observation observation_pkey; Type: CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observation
    ADD CONSTRAINT observation_pkey PRIMARY KEY (id);


--
-- Name: observation_type observation_type_pkey; Type: CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observation_type
    ADD CONSTRAINT observation_type_pkey PRIMARY KEY (id);


--
-- Name: observed_property observed_property_pkey; Type: CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observed_property
    ADD CONSTRAINT observed_property_pkey PRIMARY KEY (id);


--
-- Name: observer observer_pkey; Type: CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observer
    ADD CONSTRAINT observer_pkey PRIMARY KEY (id);


--
-- Name: observing_procedure observing_procedure_pkey; Type: CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observing_procedure
    ADD CONSTRAINT observing_procedure_pkey PRIMARY KEY (id);


--
-- Name: record_status record_status_pkey; Type: CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.record_status
    ADD CONSTRAINT record_status_pkey PRIMARY KEY (id);


--
-- Name: source source_pkey; Type: CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.source
    ADD CONSTRAINT source_pkey PRIMARY KEY (id);


--
-- Name: source_type source_type_pkey; Type: CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.source_type
    ADD CONSTRAINT source_type_pkey PRIMARY KEY (id);


--
-- Name: time_zone time_zone_pkey; Type: CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.time_zone
    ADD CONSTRAINT time_zone_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: idx_feature_geometry; Type: INDEX; Schema: cdm; Owner: -
--

CREATE INDEX idx_feature_geometry ON cdm.feature USING gist (geometry);


--
-- Name: idx_host_location; Type: INDEX; Schema: cdm; Owner: -
--

CREATE INDEX idx_host_location ON cdm.host USING gist (location);


--
-- Name: idx_observation_location; Type: INDEX; Schema: cdm; Owner: -
--

CREATE INDEX idx_observation_location ON cdm.observation USING gist (location);


--
-- Name: idx_observer_location; Type: INDEX; Schema: cdm; Owner: -
--

CREATE INDEX idx_observer_location ON cdm.observer USING gist (location);


--
-- Name: ix_cdm_observation_collection_id; Type: INDEX; Schema: cdm; Owner: -
--

CREATE INDEX ix_cdm_observation_collection_id ON cdm.observation USING btree (collection_id);


--
-- Name: ix_cdm_observation_location; Type: INDEX; Schema: cdm; Owner: -
--

CREATE INDEX ix_cdm_observation_location ON cdm.observation USING btree (location);


--
-- Name: ix_cdm_observation_observation_type_id; Type: INDEX; Schema: cdm; Owner: -
--

CREATE INDEX ix_cdm_observation_observation_type_id ON cdm.observation USING btree (observation_type_id);


--
-- Name: ix_cdm_observation_observed_property_id; Type: INDEX; Schema: cdm; Owner: -
--

CREATE INDEX ix_cdm_observation_observed_property_id ON cdm.observation USING btree (observed_property_id);


--
-- Name: ix_cdm_observation_phenomenon_end; Type: INDEX; Schema: cdm; Owner: -
--

CREATE INDEX ix_cdm_observation_phenomenon_end ON cdm.observation USING btree (phenomenon_end);


--
-- Name: ix_cdm_observation_source_id; Type: INDEX; Schema: cdm; Owner: -
--

CREATE INDEX ix_cdm_observation_source_id ON cdm.observation USING btree (source_id);


--
-- Name: feature feature_parent_id_fkey; Type: FK CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.feature
    ADD CONSTRAINT feature_parent_id_fkey FOREIGN KEY (parent_id) REFERENCES cdm.feature(id);


--
-- Name: feature feature_type_id_fkey; Type: FK CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.feature
    ADD CONSTRAINT feature_type_id_fkey FOREIGN KEY (type_id) REFERENCES cdm.feature_type(id);


--
-- Name: host host_status_id_fkey; Type: FK CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.host
    ADD CONSTRAINT host_status_id_fkey FOREIGN KEY (status_id) REFERENCES cdm.record_status(id);


--
-- Name: host host_time_zone_id_fkey; Type: FK CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.host
    ADD CONSTRAINT host_time_zone_id_fkey FOREIGN KEY (time_zone_id) REFERENCES cdm.time_zone(id);


--
-- Name: host host_user_id_fkey; Type: FK CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.host
    ADD CONSTRAINT host_user_id_fkey FOREIGN KEY (user_id) REFERENCES cdm."user"(id);


--
-- Name: observation observation_collection_id_fkey; Type: FK CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observation
    ADD CONSTRAINT observation_collection_id_fkey FOREIGN KEY (collection_id) REFERENCES cdm.collection(id);


--
-- Name: observation observation_feature_of_interest_id_fkey; Type: FK CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observation
    ADD CONSTRAINT observation_feature_of_interest_id_fkey FOREIGN KEY (feature_of_interest_id) REFERENCES cdm.feature(id);


--
-- Name: observation observation_host_id_fkey; Type: FK CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observation
    ADD CONSTRAINT observation_host_id_fkey FOREIGN KEY (host_id) REFERENCES cdm.host(id);


--
-- Name: observation observation_observation_type_id_fkey; Type: FK CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observation
    ADD CONSTRAINT observation_observation_type_id_fkey FOREIGN KEY (observation_type_id) REFERENCES cdm.observation_type(id);


--
-- Name: observation observation_observed_property_id_fkey; Type: FK CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observation
    ADD CONSTRAINT observation_observed_property_id_fkey FOREIGN KEY (observed_property_id) REFERENCES cdm.observed_property(id);


--
-- Name: observation observation_observer_id_fkey; Type: FK CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observation
    ADD CONSTRAINT observation_observer_id_fkey FOREIGN KEY (observer_id) REFERENCES cdm.observer(id);


--
-- Name: observation observation_observing_procedure_id_fkey; Type: FK CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observation
    ADD CONSTRAINT observation_observing_procedure_id_fkey FOREIGN KEY (observing_procedure_id) REFERENCES cdm.observing_procedure(id);


--
-- Name: observation observation_source_id_fkey; Type: FK CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observation
    ADD CONSTRAINT observation_source_id_fkey FOREIGN KEY (source_id) REFERENCES cdm.source(id);


--
-- Name: observation observation_status_id_fkey; Type: FK CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observation
    ADD CONSTRAINT observation_status_id_fkey FOREIGN KEY (status_id) REFERENCES cdm.record_status(id);


--
-- Name: observation observation_user_id_fkey; Type: FK CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.observation
    ADD CONSTRAINT observation_user_id_fkey FOREIGN KEY (user_id) REFERENCES cdm."user"(id);


--
-- Name: source source_source_type_id_fkey; Type: FK CONSTRAINT; Schema: cdm; Owner: -
--

ALTER TABLE ONLY cdm.source
    ADD CONSTRAINT source_source_type_id_fkey FOREIGN KEY (source_type_id) REFERENCES cdm.source_type(id);


--
-- PostgreSQL database dump complete
--

