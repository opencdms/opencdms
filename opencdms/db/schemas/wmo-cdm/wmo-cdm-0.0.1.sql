-- DROP SCHEMA cdm;

CREATE SCHEMA cdm AUTHORIZATION postgres;

-- Drop table

-- DROP TABLE cdm.collections;

CREATE TABLE cdm.collections (
	id varchar NOT NULL,
	"name" varchar NULL,
	link varchar NULL,
	CONSTRAINT collections_pkey PRIMARY KEY (id)
);

-- Drop table

-- DROP TABLE cdm.feature_type;

CREATE TABLE cdm.feature_type (
	id serial4 NOT NULL,
	"name" varchar NULL,
	description varchar NULL,
	link varchar NULL,
	CONSTRAINT feature_type_pkey PRIMARY KEY (id)
);

-- Drop table

-- DROP TABLE cdm.features;

CREATE TABLE cdm.features (
	id varchar NOT NULL,
	"type" int4 NULL,
	geometry public.geography(geometry, 4326) NULL,
	parent varchar NULL,
	CONSTRAINT features_pkey PRIMARY KEY (id),
	CONSTRAINT features_parent_fkey FOREIGN KEY (parent) REFERENCES cdm.features(id),
	CONSTRAINT features_type_fkey FOREIGN KEY ("type") REFERENCES cdm.feature_type(id)
);
CREATE INDEX idx_features_geometry ON cdm.features USING gist (geometry);

-- Drop table

-- DROP TABLE cdm.observation_type;

CREATE TABLE cdm.observation_type (
	id serial4 NOT NULL,
	"name" varchar NULL,
	description varchar NULL,
	link varchar NULL,
	CONSTRAINT observation_type_pkey PRIMARY KEY (id)
);

-- Drop table

-- DROP TABLE cdm.observations;

CREATE TABLE cdm.observations (
	id varchar NOT NULL,
	"location" public.geography(geometry, 4326) NULL,
	observation_type int4 NULL,
	phenomenon_start timestamp NULL,
	phenomenon_end timestamp NULL,
	result_value numeric NULL,
	result_uom varchar NULL,
	result_description varchar NULL,
	result_quality jsonb NULL,
	result_time timestamp NULL,
	valid_from timestamp NULL,
	valid_to timestamp NULL,
	station varchar NULL,
	sensor varchar NULL,
	observed_property int4 NULL,
	observing_procedure int4 NULL,
	report_id varchar NULL,
	collection varchar NULL,
	"parameter" jsonb NULL,
	feature_of_interest varchar NULL,
	"version" int4 NULL,
	change_date timestamp NULL,
	status int4 NULL,
	"comments" varchar NULL,
	CONSTRAINT observations_pkey PRIMARY KEY (id),
	CONSTRAINT observations_collection_fkey FOREIGN KEY (collection) REFERENCES cdm.collections(id),
	CONSTRAINT observations_feature_of_interest_fkey FOREIGN KEY (feature_of_interest) REFERENCES cdm.features(id),
	CONSTRAINT observations_observation_type_fkey FOREIGN KEY (observation_type) REFERENCES cdm.observation_type(id),
	CONSTRAINT observations_observed_property_fkey FOREIGN KEY (observed_property) REFERENCES cdm.observed_property(id),
	CONSTRAINT observations_observing_procedure_fkey FOREIGN KEY (observing_procedure) REFERENCES cdm.observing_procedure(id),
	CONSTRAINT observations_sensor_fkey FOREIGN KEY (sensor) REFERENCES cdm.sensors(id),
	CONSTRAINT observations_station_fkey FOREIGN KEY (station) REFERENCES cdm.stations(id),
	CONSTRAINT observations_status_fkey FOREIGN KEY (status) REFERENCES cdm.record_status(id)
);
CREATE INDEX idx_observations_location ON cdm.observations USING gist (location);

-- Drop table

-- DROP TABLE cdm.observed_property;

CREATE TABLE cdm.observed_property (
	id serial4 NOT NULL,
	short_name varchar NULL,
	standard_name varchar NULL,
	units varchar NULL,
	description varchar NULL,
	link varchar NULL,
	CONSTRAINT observed_property_pkey PRIMARY KEY (id)
);

-- Drop table

-- DROP TABLE cdm.observing_procedure;

CREATE TABLE cdm.observing_procedure (
	id serial4 NOT NULL,
	"name" varchar NULL,
	description varchar NULL,
	link varchar NULL,
	CONSTRAINT observing_procedure_pkey PRIMARY KEY (id)
);

-- Drop table

-- DROP TABLE cdm.record_status;

CREATE TABLE cdm.record_status (
	id serial4 NOT NULL,
	"name" varchar NULL,
	description varchar NULL,
	CONSTRAINT record_status_pkey PRIMARY KEY (id)
);

-- Drop table

-- DROP TABLE cdm.sensors;

CREATE TABLE cdm.sensors (
	id varchar NOT NULL,
	"name" varchar NULL,
	description varchar NULL,
	link varchar NULL,
	CONSTRAINT sensors_pkey PRIMARY KEY (id)
);

-- Drop table

-- DROP TABLE cdm.stations;

CREATE TABLE cdm.stations (
	id varchar NOT NULL,
	"name" varchar NULL,
	description varchar NULL,
	link varchar NULL,
	"location" public.geography(geometry, 4326) NULL,
	elevation numeric NULL,
	wigos_station_identifier varchar NULL,
	facility_type varchar NULL,
	date_established varchar NULL,
	wmo_region varchar NULL,
	territory varchar NULL,
	valid_from timestamp NULL,
	valid_to timestamp NULL,
	"version" int4 NULL,
	change_date timestamp NULL,
	status int4 NULL,
	"comments" varchar NULL,
	CONSTRAINT stations_pkey PRIMARY KEY (id),
	CONSTRAINT stations_status_fkey FOREIGN KEY (status) REFERENCES cdm.record_status(id)
);
CREATE INDEX idx_stations_location ON cdm.stations USING gist (location);
