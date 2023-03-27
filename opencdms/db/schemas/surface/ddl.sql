CREATE SCHEMA IF NOT EXISTS public;

CREATE EXTENSION IF NOT EXISTS postgis;

CREATE EXTENSION IF NOT EXISTS "timescaledb" CASCADE;


-- public.auth_group definition

-- Drop table

-- DROP TABLE public.auth_group;

CREATE TABLE IF NOT EXISTS public.auth_group (
	id serial NOT NULL,
	"name" varchar(150) NOT NULL,
	CONSTRAINT auth_group_name_key UNIQUE (name),
	CONSTRAINT auth_group_pkey PRIMARY KEY (id)
);
CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


-- public.auth_user definition

-- Drop table

-- DROP TABLE public.auth_user;

CREATE TABLE IF NOT EXISTS public.auth_user (
	id serial NOT NULL,
	"password" varchar(128) NOT NULL,
	last_login timestamptz NULL,
	is_superuser bool NOT NULL,
	username varchar(150) NOT NULL,
	first_name varchar(150) NOT NULL,
	last_name varchar(150) NOT NULL,
	email varchar(254) NOT NULL,
	is_staff bool NOT NULL,
	is_active bool NOT NULL,
	date_joined timestamptz NOT NULL,
	CONSTRAINT auth_user_pkey PRIMARY KEY (id),
	CONSTRAINT auth_user_username_key UNIQUE (username)
);
CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


-- public.daily_summary definition

-- Drop table

-- DROP TABLE public.daily_summary;

CREATE TABLE IF NOT EXISTS public.daily_summary (
	"day" date NULL,
	station_id int4 NULL,
	variable_id int4 NULL,
	min_value float4 NULL,
	max_value float4 NULL,
	avg_value float4 NULL,
	sum_value float4 NULL,
	num_records int4 NULL,
	created_at timestamptz NULL,
	updated_at timestamptz NULL,
	CONSTRAINT daily_summary_uniq UNIQUE (day, station_id, variable_id)
);


-- public.django_celery_beat_clockedschedule definition

-- Drop table

-- DROP TABLE public.django_celery_beat_clockedschedule;

CREATE TABLE IF NOT EXISTS public.django_celery_beat_clockedschedule (
	id serial NOT NULL,
	clocked_time timestamptz NOT NULL,
	CONSTRAINT django_celery_beat_clockedschedule_pkey PRIMARY KEY (id)
);


-- public.django_celery_beat_crontabschedule definition

-- Drop table

-- DROP TABLE public.django_celery_beat_crontabschedule;

CREATE TABLE IF NOT EXISTS public.django_celery_beat_crontabschedule (
	id serial NOT NULL,
	"minute" varchar(240) NOT NULL,
	"hour" varchar(96) NOT NULL,
	day_of_week varchar(64) NOT NULL,
	day_of_month varchar(124) NOT NULL,
	month_of_year varchar(64) NOT NULL,
	timezone varchar(63) NOT NULL,
	CONSTRAINT django_celery_beat_crontabschedule_pkey PRIMARY KEY (id)
);


-- public.django_celery_beat_intervalschedule definition

-- Drop table

-- DROP TABLE public.django_celery_beat_intervalschedule;

CREATE TABLE IF NOT EXISTS public.django_celery_beat_intervalschedule (
	id serial NOT NULL,
	"every" int4 NOT NULL,
	"period" varchar(24) NOT NULL,
	CONSTRAINT django_celery_beat_intervalschedule_pkey PRIMARY KEY (id)
);


-- public.django_celery_beat_periodictasks definition

-- Drop table

-- DROP TABLE public.django_celery_beat_periodictasks;

CREATE TABLE IF NOT EXISTS public.django_celery_beat_periodictasks (
	ident int2 NOT NULL,
	last_update timestamptz NOT NULL,
	CONSTRAINT django_celery_beat_periodictasks_pkey PRIMARY KEY (ident)
);


-- public.django_celery_beat_solarschedule definition

-- Drop table

-- DROP TABLE public.django_celery_beat_solarschedule;

CREATE TABLE IF NOT EXISTS public.django_celery_beat_solarschedule (
	id serial NOT NULL,
	"event" varchar(24) NOT NULL,
	latitude numeric(9, 6) NOT NULL,
	longitude numeric(9, 6) NOT NULL,
	CONSTRAINT django_celery_beat_solar_event_latitude_longitude_ba64999a_uniq UNIQUE (event, latitude, longitude),
	CONSTRAINT django_celery_beat_solarschedule_pkey PRIMARY KEY (id)
);


-- public.django_content_type definition

-- Drop table

-- DROP TABLE public.django_content_type;

CREATE TABLE IF NOT EXISTS public.django_content_type (
	id serial NOT NULL,
	app_label varchar(100) NOT NULL,
	model varchar(100) NOT NULL,
	CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model),
	CONSTRAINT django_content_type_pkey PRIMARY KEY (id)
);


-- public.django_migrations definition

-- Drop table

-- DROP TABLE public.django_migrations;

CREATE TABLE IF NOT EXISTS public.django_migrations (
	id bigserial NOT NULL,
	app varchar(255) NOT NULL,
	"name" varchar(255) NOT NULL,
	applied timestamptz NOT NULL,
	CONSTRAINT django_migrations_pkey PRIMARY KEY (id)
);


-- public.django_session definition

-- Drop table

-- DROP TABLE public.django_session;

CREATE TABLE IF NOT EXISTS public.django_session (
	session_key varchar(40) NOT NULL,
	session_data text NOT NULL,
	expire_date timestamptz NOT NULL,
	CONSTRAINT django_session_pkey PRIMARY KEY (session_key)
);
CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


-- public.hourly_summary definition

-- Drop table

-- DROP TABLE public.hourly_summary;

CREATE TABLE IF NOT EXISTS public.hourly_summary (
	datetime timestamptz NULL,
	station_id int4 NULL,
	variable_id int4 NULL,
	min_value float4 NULL,
	max_value float4 NULL,
	avg_value float4 NULL,
	sum_value float4 NULL,
	num_records int4 NULL,
	created_at timestamptz NULL,
	updated_at timestamptz NULL,
	CONSTRAINT hourly_summary_uniq UNIQUE (datetime, station_id, variable_id)
);


-- public.last24h_summary definition

-- Drop table

-- DROP TABLE public.last24h_summary;

CREATE TABLE IF NOT EXISTS public.last24h_summary (
	datetime timestamptz NULL,
	station_id int4 NULL,
	variable_id int4 NULL,
	min_value float4 NULL,
	max_value float4 NULL,
	avg_value float4 NULL,
	sum_value float4 NULL,
	latest_value float4 NULL,
	num_records int4 NULL,
	CONSTRAINT last24h_summary_uniq UNIQUE (station_id, variable_id)
);


-- public.raw_data definition

-- Drop table

-- DROP TABLE public.raw_data;

CREATE TABLE IF NOT EXISTS public.raw_data (
	created_at timestamptz NOT NULL DEFAULT now(),
	updated_at timestamptz NOT NULL DEFAULT now(),
	datetime timestamptz NOT NULL,
	measured float8 NOT NULL,
	consisted float8 NULL,
	qc_range_description varchar(256) NULL,
	qc_step_description varchar(256) NULL,
	qc_persist_description varchar(256) NULL,
	manual_flag int4 NULL,
	qc_persist_quality_flag int4 NULL,
	qc_range_quality_flag int4 NULL,
	qc_step_quality_flag int4 NULL,
	quality_flag int4 NOT NULL,
	station_id int4 NOT NULL,
	variable_id int4 NOT NULL,
	observation_flag_id int4 NULL,
	is_daily bool NOT NULL DEFAULT false,
	remarks varchar(150) NULL,
	observer varchar(150) NULL,
	code varchar(60) NULL,
	ml_flag int4 NULL DEFAULT 1
);
CREATE INDEX raw_data_datetime_idx1 ON public.raw_data USING btree (datetime DESC);
CREATE UNIQUE INDEX raw_data_datetime_station_id_variable_id_uidx ON public.raw_data USING btree (datetime, station_id, variable_id);

SELECT create_hypertable('public.raw_data','datetime');

-- public.spatial_ref_sys definition

-- Drop table

-- DROP TABLE public.spatial_ref_sys;

CREATE TABLE IF NOT EXISTS public.spatial_ref_sys (
	srid int4 NOT NULL,
	auth_name varchar(256) NULL,
	auth_srid int4 NULL,
	srtext varchar(2048) NULL,
	proj4text varchar(2048) NULL,
	CONSTRAINT spatial_ref_sys_pkey PRIMARY KEY (srid),
	CONSTRAINT spatial_ref_sys_srid_check CHECK (((srid > 0) AND (srid <= 998999)))
);


-- public.wx_administrativeregiontype definition

-- Drop table

-- DROP TABLE public.wx_administrativeregiontype;

CREATE TABLE IF NOT EXISTS public.wx_administrativeregiontype (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(45) NOT NULL,
	CONSTRAINT wx_administrativeregiontype_pkey PRIMARY KEY (id)
);


-- public.wx_codetable definition

-- Drop table

-- DROP TABLE public.wx_codetable;

CREATE TABLE IF NOT EXISTS public.wx_codetable (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(45) NOT NULL,
	description varchar(256) NOT NULL,
	CONSTRAINT wx_codetable_name_key UNIQUE (name),
	CONSTRAINT wx_codetable_pkey PRIMARY KEY (id)
);
CREATE INDEX wx_codetable_name_b2b1c14e_like ON public.wx_codetable USING btree (name varchar_pattern_ops);


-- public.wx_country definition

-- Drop table

-- DROP TABLE public.wx_country;

CREATE TABLE IF NOT EXISTS public.wx_country (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	notation varchar(16) NOT NULL,
	"name" varchar(256) NOT NULL,
	description varchar(256) NULL,
	CONSTRAINT wx_country_name_key UNIQUE (name),
	CONSTRAINT wx_country_pkey PRIMARY KEY (id)
);
CREATE INDEX wx_country_name_9315ac0c_like ON public.wx_country USING btree (name varchar_pattern_ops);


-- public.wx_datafile definition

-- Drop table

-- DROP TABLE public.wx_datafile;

CREATE TABLE IF NOT EXISTS public.wx_datafile (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	ready_at timestamptz NULL,
	ready bool NOT NULL,
	initial_date timestamptz NULL,
	final_date timestamptz NULL,
	"source" varchar(30) NOT NULL,
	lines int4 NULL,
	prepared_by varchar(256) NULL,
	interval_in_seconds int4 NULL,
	CONSTRAINT wx_datafile_pkey PRIMARY KEY (id)
);


-- public.wx_datasource definition

-- Drop table

-- DROP TABLE public.wx_datasource;

CREATE TABLE IF NOT EXISTS public.wx_datasource (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	symbol varchar(8) NOT NULL,
	"name" varchar(32) NOT NULL,
	base_url varchar(200) NULL,
	"location" varchar(256) NULL,
	CONSTRAINT wx_datasource_name_key UNIQUE (name),
	CONSTRAINT wx_datasource_pkey PRIMARY KEY (id),
	CONSTRAINT wx_datasource_symbol_key UNIQUE (symbol)
);
CREATE INDEX wx_datasource_name_910eb909_like ON public.wx_datasource USING btree (name varchar_pattern_ops);
CREATE INDEX wx_datasource_symbol_19617b3a_like ON public.wx_datasource USING btree (symbol varchar_pattern_ops);


-- public.wx_decoder definition

-- Drop table

-- DROP TABLE public.wx_decoder;

CREATE TABLE IF NOT EXISTS public.wx_decoder (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(40) NOT NULL,
	description varchar(256) NOT NULL,
	CONSTRAINT wx_decoder_pkey PRIMARY KEY (id)
);


-- public.wx_district definition

-- Drop table

-- DROP TABLE public.wx_district;

CREATE TABLE IF NOT EXISTS public.wx_district (
	id bigserial NOT NULL,
	id_field int4 NOT NULL,
	district varchar(64) NOT NULL,
	acres float8 NOT NULL,
	hectares float8 NOT NULL,
	geom geometry(multipolygon, 4326) NOT NULL,
	CONSTRAINT wx_district_pkey PRIMARY KEY (id)
);
CREATE INDEX wx_district_geom_id ON public.wx_district USING gist (geom);


-- public.wx_flash definition

-- Drop table

-- DROP TABLE public.wx_flash;

CREATE TABLE IF NOT EXISTS public.wx_flash (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"type" varchar(60) NOT NULL,
	datetime timestamptz NOT NULL,
	latitude float8 NOT NULL,
	longitude float8 NOT NULL,
	peak_current int4 NOT NULL,
	ic_height int4 NOT NULL,
	num_sensors int4 NOT NULL,
	ic_multiplicity int4 NOT NULL,
	cg_multiplicity int4 NOT NULL,
	start_datetime timestamptz NOT NULL,
	duration int4 NOT NULL,
	ul_latitude float8 NOT NULL,
	ul_longitude float8 NOT NULL,
	lr_latitude float8 NOT NULL,
	lr_longitude float8 NOT NULL,
	CONSTRAINT wx_flash_pkey PRIMARY KEY (id)
);


-- public.wx_format definition

-- Drop table

-- DROP TABLE public.wx_format;

CREATE TABLE IF NOT EXISTS public.wx_format (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(40) NOT NULL,
	description varchar(256) NOT NULL,
	CONSTRAINT wx_format_name_key UNIQUE (name),
	CONSTRAINT wx_format_pkey PRIMARY KEY (id)
);
CREATE INDEX wx_format_name_027eb21e_like ON public.wx_format USING btree (name varchar_pattern_ops);


-- public.wx_ftpserver definition

-- Drop table

-- DROP TABLE public.wx_ftpserver;

CREATE TABLE IF NOT EXISTS public.wx_ftpserver (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(64) NOT NULL,
	host varchar(256) NOT NULL,
	port int4 NOT NULL,
	username varchar(128) NOT NULL,
	"password" varchar(128) NOT NULL,
	is_active_mode bool NOT NULL,
	CONSTRAINT wx_ftpserver_host_port_username_password_20a9bafa_uniq UNIQUE (host, port, username, password),
	CONSTRAINT wx_ftpserver_name_key UNIQUE (name),
	CONSTRAINT wx_ftpserver_pkey PRIMARY KEY (id)
);
CREATE INDEX wx_ftpserver_name_87bc5d35_like ON public.wx_ftpserver USING btree (name varchar_pattern_ops);


-- public.wx_interval definition

-- Drop table

-- DROP TABLE public.wx_interval;

CREATE TABLE IF NOT EXISTS public.wx_interval (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	symbol varchar(8) NOT NULL,
	description varchar(40) NOT NULL,
	default_query_range int4 NOT NULL,
	seconds int4 NULL,
	CONSTRAINT wx_interval_pkey PRIMARY KEY (id)
);


-- public.wx_neighborhood definition

-- Drop table

-- DROP TABLE public.wx_neighborhood;

CREATE TABLE IF NOT EXISTS public.wx_neighborhood (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(256) NOT NULL,
	CONSTRAINT wx_neighborhood_name_key UNIQUE (name),
	CONSTRAINT wx_neighborhood_pkey PRIMARY KEY (id)
);
CREATE INDEX wx_neighborhood_name_d0eff19b_like ON public.wx_neighborhood USING btree (name varchar_pattern_ops);


-- public.wx_noaatransmissionrate definition

-- Drop table

-- DROP TABLE public.wx_noaatransmissionrate;

CREATE TABLE IF NOT EXISTS public.wx_noaatransmissionrate (
	id bigserial NOT NULL,
	rate int4 NOT NULL,
	CONSTRAINT wx_noaatransmissionrate_pkey PRIMARY KEY (id),
	CONSTRAINT wx_noaatransmissionrate_rate_key UNIQUE (rate)
);


-- public.wx_noaatransmissiontype definition

-- Drop table

-- DROP TABLE public.wx_noaatransmissiontype;

CREATE TABLE IF NOT EXISTS public.wx_noaatransmissiontype (
	id bigserial NOT NULL,
	acronym varchar(5) NOT NULL,
	description varchar(255) NOT NULL,
	CONSTRAINT wx_noaatransmissiontype_acronym_key UNIQUE (acronym),
	CONSTRAINT wx_noaatransmissiontype_pkey PRIMARY KEY (id)
);
CREATE INDEX wx_noaatransmissiontype_acronym_2e481d24_like ON public.wx_noaatransmissiontype USING btree (acronym varchar_pattern_ops);


-- public.wx_periodicjobtype definition

-- Drop table

-- DROP TABLE public.wx_periodicjobtype;

CREATE TABLE IF NOT EXISTS public.wx_periodicjobtype (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(40) NOT NULL,
	description varchar(256) NOT NULL,
	CONSTRAINT wx_periodicjobtype_name_key UNIQUE (name),
	CONSTRAINT wx_periodicjobtype_pkey PRIMARY KEY (id)
);
CREATE INDEX wx_periodicjobtype_name_bc2906c2_like ON public.wx_periodicjobtype USING btree (name varchar_pattern_ops);


-- public.wx_physicalquantity definition

-- Drop table

-- DROP TABLE public.wx_physicalquantity;

CREATE TABLE IF NOT EXISTS public.wx_physicalquantity (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(16) NOT NULL,
	CONSTRAINT wx_physicalquantity_name_key UNIQUE (name),
	CONSTRAINT wx_physicalquantity_pkey PRIMARY KEY (id)
);
CREATE INDEX wx_physicalquantity_name_2291fabe_like ON public.wx_physicalquantity USING btree (name varchar_pattern_ops);


-- public.wx_qualityflag definition

-- Drop table

-- DROP TABLE public.wx_qualityflag;

CREATE TABLE IF NOT EXISTS public.wx_qualityflag (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	symbol varchar(8) NOT NULL,
	"name" varchar(256) NOT NULL,
	color varchar(18) NULL,
	CONSTRAINT wx_qualityflag_name_key UNIQUE (name),
	CONSTRAINT wx_qualityflag_pkey PRIMARY KEY (id),
	CONSTRAINT wx_qualityflag_symbol_key UNIQUE (symbol)
);
CREATE INDEX wx_qualityflag_name_294b5476_like ON public.wx_qualityflag USING btree (name varchar_pattern_ops);
CREATE INDEX wx_qualityflag_symbol_39deca55_like ON public.wx_qualityflag USING btree (symbol varchar_pattern_ops);


-- public.wx_samplingoperation definition

-- Drop table

-- DROP TABLE public.wx_samplingoperation;

CREATE TABLE IF NOT EXISTS public.wx_samplingoperation (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	symbol varchar(5) NOT NULL,
	"name" varchar(40) NOT NULL,
	CONSTRAINT wx_samplingoperation_name_key UNIQUE (name),
	CONSTRAINT wx_samplingoperation_pkey PRIMARY KEY (id),
	CONSTRAINT wx_samplingoperation_symbol_key UNIQUE (symbol)
);
CREATE INDEX wx_samplingoperation_name_12d271e5_like ON public.wx_samplingoperation USING btree (name varchar_pattern_ops);
CREATE INDEX wx_samplingoperation_symbol_79dccc93_like ON public.wx_samplingoperation USING btree (symbol varchar_pattern_ops);


-- public.wx_stationcommunication definition

-- Drop table

-- DROP TABLE public.wx_stationcommunication;

CREATE TABLE IF NOT EXISTS public.wx_stationcommunication (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(45) NOT NULL,
	description varchar(256) NOT NULL,
	color varchar(7) NOT NULL,
	CONSTRAINT wx_stationcommunication_pkey PRIMARY KEY (id)
);


-- public.wx_stationdatafilestatus definition

-- Drop table

-- DROP TABLE public.wx_stationdatafilestatus;

CREATE TABLE IF NOT EXISTS public.wx_stationdatafilestatus (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(128) NOT NULL,
	CONSTRAINT wx_stationdatafilestatus_pkey PRIMARY KEY (id)
);


-- public.wx_stationprofile definition

-- Drop table

-- DROP TABLE public.wx_stationprofile;

CREATE TABLE IF NOT EXISTS public.wx_stationprofile (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(45) NOT NULL,
	description varchar(256) NOT NULL,
	color varchar(7) NOT NULL,
	is_automatic bool NOT NULL,
	is_manual bool NOT NULL,
	CONSTRAINT wx_stationprofile_pkey PRIMARY KEY (id)
);


-- public.wx_unit definition

-- Drop table

-- DROP TABLE public.wx_unit;

CREATE TABLE IF NOT EXISTS public.wx_unit (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	symbol varchar(16) NOT NULL,
	"name" varchar(256) NOT NULL,
	CONSTRAINT wx_unit_name_key UNIQUE (name),
	CONSTRAINT wx_unit_pkey PRIMARY KEY (id),
	CONSTRAINT wx_unit_symbol_key UNIQUE (symbol)
);
CREATE INDEX wx_unit_name_9afc42cd_like ON public.wx_unit USING btree (name varchar_pattern_ops);
CREATE INDEX wx_unit_symbol_f5d7361a_like ON public.wx_unit USING btree (symbol varchar_pattern_ops);


-- public.wx_watershed definition

-- Drop table

-- DROP TABLE public.wx_watershed;

CREATE TABLE IF NOT EXISTS public.wx_watershed (
	id bigserial NOT NULL,
	watershed varchar(128) NOT NULL,
	"size" varchar(16) NOT NULL,
	acres float8 NOT NULL,
	hectares float8 NOT NULL,
	shape_leng float8 NOT NULL,
	shape_area float8 NOT NULL,
	geom geometry(multipolygon, 4326) NOT NULL,
	CONSTRAINT wx_watershed_pkey PRIMARY KEY (id)
);
CREATE INDEX wx_watershed_geom_id ON public.wx_watershed USING gist (geom);


-- public.wx_wmoprogram definition

-- Drop table

-- DROP TABLE public.wx_wmoprogram;

CREATE TABLE IF NOT EXISTS public.wx_wmoprogram (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(256) NOT NULL,
	description varchar(512) NULL,
	notation varchar(256) NULL,
	"path" varchar(256) NULL,
	CONSTRAINT wx_wmoprogram_name_key UNIQUE (name),
	CONSTRAINT wx_wmoprogram_pkey PRIMARY KEY (id)
);
CREATE INDEX wx_wmoprogram_name_6db9da81_like ON public.wx_wmoprogram USING btree (name varchar_pattern_ops);


-- public.wx_wmoregion definition

-- Drop table

-- DROP TABLE public.wx_wmoregion;

CREATE TABLE IF NOT EXISTS public.wx_wmoregion (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(256) NOT NULL,
	description varchar(256) NULL,
	notation varchar(256) NULL,
	CONSTRAINT wx_wmoregion_name_key UNIQUE (name),
	CONSTRAINT wx_wmoregion_pkey PRIMARY KEY (id)
);
CREATE INDEX wx_wmoregion_name_64651ae1_like ON public.wx_wmoregion USING btree (name varchar_pattern_ops);


-- public.wx_wmostationtype definition

-- Drop table

-- DROP TABLE public.wx_wmostationtype;

CREATE TABLE IF NOT EXISTS public.wx_wmostationtype (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(256) NOT NULL,
	description varchar(256) NULL,
	notation varchar(256) NULL,
	CONSTRAINT wx_wmostationtype_name_key UNIQUE (name),
	CONSTRAINT wx_wmostationtype_pkey PRIMARY KEY (id)
);
CREATE INDEX wx_wmostationtype_name_212904c7_like ON public.wx_wmostationtype USING btree (name varchar_pattern_ops);


-- public.wx_wxpermission definition

-- Drop table

-- DROP TABLE public.wx_wxpermission;

CREATE TABLE IF NOT EXISTS public.wx_wxpermission (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(256) NOT NULL,
	url_name varchar(256) NOT NULL,
	"permission" varchar(32) NOT NULL,
	CONSTRAINT wx_wxpermission_name_key UNIQUE (name),
	CONSTRAINT wx_wxpermission_pkey PRIMARY KEY (id)
);
CREATE INDEX wx_wxpermission_name_f17b1834_like ON public.wx_wxpermission USING btree (name varchar_pattern_ops);


-- public.auth_permission definition

-- Drop table

-- DROP TABLE public.auth_permission;

CREATE TABLE IF NOT EXISTS public.auth_permission (
	id serial NOT NULL,
	"name" varchar(255) NOT NULL,
	content_type_id int4 NOT NULL,
	codename varchar(100) NOT NULL,
	CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename),
	CONSTRAINT auth_permission_pkey PRIMARY KEY (id),
	CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


-- public.auth_user_groups definition

-- Drop table

-- DROP TABLE public.auth_user_groups;

CREATE TABLE IF NOT EXISTS public.auth_user_groups (
	id bigserial NOT NULL,
	user_id int4 NOT NULL,
	group_id int4 NOT NULL,
	CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id),
	CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id),
	CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


-- public.auth_user_user_permissions definition

-- Drop table

-- DROP TABLE public.auth_user_user_permissions;

CREATE TABLE IF NOT EXISTS public.auth_user_user_permissions (
	id bigserial NOT NULL,
	user_id int4 NOT NULL,
	permission_id int4 NOT NULL,
	CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id),
	CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id),
	CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


-- public.authtoken_token definition

-- Drop table

-- DROP TABLE public.authtoken_token;

CREATE TABLE IF NOT EXISTS public.authtoken_token (
	"key" varchar(40) NOT NULL,
	created timestamptz NOT NULL,
	user_id int4 NOT NULL,
	CONSTRAINT authtoken_token_pkey PRIMARY KEY (key),
	CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id),
	CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


-- public.django_admin_log definition

-- Drop table

-- DROP TABLE public.django_admin_log;

CREATE TABLE IF NOT EXISTS public.django_admin_log (
	id serial NOT NULL,
	action_time timestamptz NOT NULL,
	object_id text NULL,
	object_repr varchar(200) NOT NULL,
	action_flag int2 NOT NULL,
	change_message text NOT NULL,
	content_type_id int4 NULL,
	user_id int4 NOT NULL,
	CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0)),
	CONSTRAINT django_admin_log_pkey PRIMARY KEY (id),
	CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


-- public.django_celery_beat_periodictask definition

-- Drop table

-- DROP TABLE public.django_celery_beat_periodictask;

CREATE TABLE IF NOT EXISTS public.django_celery_beat_periodictask (
	id serial NOT NULL,
	"name" varchar(200) NOT NULL,
	task varchar(200) NOT NULL,
	args text NOT NULL,
	kwargs text NOT NULL,
	queue varchar(200) NULL,
	exchange varchar(200) NULL,
	routing_key varchar(200) NULL,
	expires timestamptz NULL,
	enabled bool NOT NULL,
	last_run_at timestamptz NULL,
	total_run_count int4 NOT NULL,
	date_changed timestamptz NOT NULL,
	description text NOT NULL,
	crontab_id int4 NULL,
	interval_id int4 NULL,
	solar_id int4 NULL,
	one_off bool NOT NULL,
	start_time timestamptz NULL,
	priority int4 NULL,
	headers text NOT NULL,
	clocked_id int4 NULL,
	expire_seconds int4 NULL,
	CONSTRAINT django_celery_beat_periodictask_expire_seconds_check CHECK ((expire_seconds >= 0)),
	CONSTRAINT django_celery_beat_periodictask_name_key UNIQUE (name),
	CONSTRAINT django_celery_beat_periodictask_pkey PRIMARY KEY (id),
	CONSTRAINT django_celery_beat_periodictask_priority_check CHECK ((priority >= 0)),
	CONSTRAINT django_celery_beat_periodictask_total_run_count_check CHECK ((total_run_count >= 0)),
	CONSTRAINT django_celery_beat_p_clocked_id_47a69f82_fk_django_ce FOREIGN KEY (clocked_id) REFERENCES public.django_celery_beat_clockedschedule(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT django_celery_beat_p_crontab_id_d3cba168_fk_django_ce FOREIGN KEY (crontab_id) REFERENCES public.django_celery_beat_crontabschedule(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT django_celery_beat_p_interval_id_a8ca27da_fk_django_ce FOREIGN KEY (interval_id) REFERENCES public.django_celery_beat_intervalschedule(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT django_celery_beat_p_solar_id_a87ce72c_fk_django_ce FOREIGN KEY (solar_id) REFERENCES public.django_celery_beat_solarschedule(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX django_celery_beat_periodictask_clocked_id_47a69f82 ON public.django_celery_beat_periodictask USING btree (clocked_id);
CREATE INDEX django_celery_beat_periodictask_crontab_id_d3cba168 ON public.django_celery_beat_periodictask USING btree (crontab_id);
CREATE INDEX django_celery_beat_periodictask_interval_id_a8ca27da ON public.django_celery_beat_periodictask USING btree (interval_id);
CREATE INDEX django_celery_beat_periodictask_name_265a36b7_like ON public.django_celery_beat_periodictask USING btree (name varchar_pattern_ops);
CREATE INDEX django_celery_beat_periodictask_solar_id_a87ce72c ON public.django_celery_beat_periodictask USING btree (solar_id);


-- public.wx_administrativeregion definition

-- Drop table

-- DROP TABLE public.wx_administrativeregion;

CREATE TABLE IF NOT EXISTS public.wx_administrativeregion (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(45) NOT NULL,
	administrative_region_type_id int8 NOT NULL,
	country_id int8 NOT NULL,
	CONSTRAINT wx_administrativeregion_pkey PRIMARY KEY (id),
	CONSTRAINT wx_administrativereg_administrative_regio_6a28da54_fk_wx_admini FOREIGN KEY (administrative_region_type_id) REFERENCES public.wx_administrativeregiontype(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_administrativeregion_country_id_7cb17f54_fk_wx_country_id FOREIGN KEY (country_id) REFERENCES public.wx_country(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_administrativeregion_administrative_region_type_id_6a28da54 ON public.wx_administrativeregion USING btree (administrative_region_type_id);
CREATE INDEX wx_administrativeregion_country_id_7cb17f54 ON public.wx_administrativeregion USING btree (country_id);


-- public.wx_measurementvariable definition

-- Drop table

-- DROP TABLE public.wx_measurementvariable;

CREATE TABLE IF NOT EXISTS public.wx_measurementvariable (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(40) NOT NULL,
	physical_quantity_id int8 NOT NULL,
	CONSTRAINT wx_measurementvariable_name_key UNIQUE (name),
	CONSTRAINT wx_measurementvariable_pkey PRIMARY KEY (id),
	CONSTRAINT wx_measurementvariab_physical_quantity_id_ed91d09d_fk_wx_physic FOREIGN KEY (physical_quantity_id) REFERENCES public.wx_physicalquantity(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_measurementvariable_name_cfa3d6be_like ON public.wx_measurementvariable USING btree (name varchar_pattern_ops);
CREATE INDEX wx_measurementvariable_physical_quantity_id_ed91d09d ON public.wx_measurementvariable USING btree (physical_quantity_id);


-- public.wx_noaadcp definition

-- Drop table

-- DROP TABLE public.wx_noaadcp;

CREATE TABLE IF NOT EXISTS public.wx_noaadcp (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	dcp_address varchar(256) NOT NULL,
	first_channel int4 NULL,
	second_channel int4 NULL,
	first_transmission_time time NOT NULL,
	transmission_window time NOT NULL,
	transmission_period time NOT NULL,
	last_datetime timestamptz NULL,
	first_channel_type_id int8 NULL,
	second_channel_type_id int8 NULL,
	CONSTRAINT wx_noaadcp_pkey PRIMARY KEY (id),
	CONSTRAINT wx_noaadcp_first_channel_type_i_4505f8ae_fk_wx_noaatr FOREIGN KEY (first_channel_type_id) REFERENCES public.wx_noaatransmissiontype(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_noaadcp_second_channel_type__5cd96fdd_fk_wx_noaatr FOREIGN KEY (second_channel_type_id) REFERENCES public.wx_noaatransmissiontype(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_noaadcp_first_channel_type_id_4505f8ae ON public.wx_noaadcp USING btree (first_channel_type_id);
CREATE INDEX wx_noaadcp_second_channel_type_id_5cd96fdd ON public.wx_noaadcp USING btree (second_channel_type_id);


-- public.wx_station definition

-- Drop table

-- DROP TABLE public.wx_station;

CREATE TABLE IF NOT EXISTS public.wx_station (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(256) NOT NULL,
	alias_name varchar(256) NULL,
	begin_date timestamptz NULL,
	end_date timestamptz NULL,
	longitude float8 NOT NULL,
	latitude float8 NOT NULL,
	elevation float8 NULL,
	code varchar(64) NOT NULL,
	wmo int4 NULL,
	wigos varchar(64) NULL,
	is_active bool NOT NULL,
	is_automatic bool NOT NULL,
	organization varchar(256) NULL,
	observer varchar(256) NULL,
	watershed varchar(256) NULL,
	z float8 NULL,
	datum varchar(256) NULL,
	"zone" varchar(256) NULL,
	ground_water_province varchar(256) NULL,
	river_code int4 NULL,
	river_course varchar(64) NULL,
	catchment_area_station varchar(256) NULL,
	river_origin varchar(256) NULL,
	easting float8 NULL,
	northing float8 NULL,
	river_outlet varchar(256) NULL,
	river_length int4 NULL,
	local_land_use varchar(256) NULL,
	soil_type varchar(64) NULL,
	site_description varchar(256) NULL,
	land_surface_elevation float8 NULL,
	screen_length float8 NULL,
	top_casing_land_surface float8 NULL,
	depth_midpoint float8 NULL,
	screen_size float8 NULL,
	casing_type varchar(256) NULL,
	casing_diameter float8 NULL,
	existing_gauges varchar(256) NULL,
	flow_direction_at_station varchar(256) NULL,
	flow_direction_above_station varchar(256) NULL,
	flow_direction_below_station varchar(256) NULL,
	bank_full_stage varchar(256) NULL,
	bridge_level varchar(256) NULL,
	access_point varchar(256) NULL,
	temporary_benchmark varchar(256) NULL,
	mean_sea_level varchar(256) NULL,
	data_type varchar(256) NULL,
	frequency_observation varchar(256) NULL,
	historic_events varchar(256) NULL,
	other_information varchar(256) NULL,
	hydrology_station_type varchar(64) NULL,
	is_surface bool NOT NULL,
	station_details varchar(256) NULL,
	remarks varchar(256) NULL,
	region varchar(256) NULL,
	utc_offset_minutes int4 NOT NULL,
	alternative_names varchar(256) NULL,
	wmo_station_plataform varchar(256) NULL,
	operation_status bool NOT NULL,
	communication_type_id int8 NULL,
	data_source_id int8 NULL,
	profile_id int8 NULL,
	wmo_program_id int8 NULL,
	wmo_region_id int8 NULL,
	wmo_station_type_id int8 NULL,
	relocation_date timestamptz NULL,
	network varchar(256) NULL,
	reference_station_id int8 NULL,
	country_id int8 NULL,
	CONSTRAINT wx_station_data_source_id_code_655b55f3_uniq UNIQUE (data_source_id, code),
	CONSTRAINT wx_station_pkey PRIMARY KEY (id),
	CONSTRAINT wx_station_communication_type_i_5b98d238_fk_wx_statio FOREIGN KEY (communication_type_id) REFERENCES public.wx_stationcommunication(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_station_country_id_9dedc73c_fk_wx_country_id FOREIGN KEY (country_id) REFERENCES public.wx_country(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_station_data_source_id_d40e9a27_fk_wx_datasource_id FOREIGN KEY (data_source_id) REFERENCES public.wx_datasource(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_station_profile_id_7a18534a_fk_wx_stationprofile_id FOREIGN KEY (profile_id) REFERENCES public.wx_stationprofile(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_station_reference_station_id_ed2e7165_fk_wx_station_id FOREIGN KEY (reference_station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_station_wmo_program_id_220010b3_fk_wx_wmoprogram_id FOREIGN KEY (wmo_program_id) REFERENCES public.wx_wmoprogram(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_station_wmo_region_id_6170fab5_fk_wx_wmoregion_id FOREIGN KEY (wmo_region_id) REFERENCES public.wx_wmoregion(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_station_wmo_station_type_id_b743b69f_fk_wx_wmostationtype_id FOREIGN KEY (wmo_station_type_id) REFERENCES public.wx_wmostationtype(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_station_communication_type_id_5b98d238 ON public.wx_station USING btree (communication_type_id);
CREATE INDEX wx_station_country_link_id_af9aebf0 ON public.wx_station USING btree (country_id);
CREATE INDEX wx_station_data_source_id_d40e9a27 ON public.wx_station USING btree (data_source_id);
CREATE INDEX wx_station_profile_id_7a18534a ON public.wx_station USING btree (profile_id);
CREATE INDEX wx_station_reference_station_id_ed2e7165 ON public.wx_station USING btree (reference_station_id);
CREATE INDEX wx_station_wmo_program_id_220010b3 ON public.wx_station USING btree (wmo_program_id);
CREATE INDEX wx_station_wmo_region_id_6170fab5 ON public.wx_station USING btree (wmo_region_id);
CREATE INDEX wx_station_wmo_station_type_id_b743b69f ON public.wx_station USING btree (wmo_station_type_id);


-- public.wx_stationdatafile definition

-- Drop table

-- DROP TABLE public.wx_stationdatafile;

CREATE TABLE IF NOT EXISTS public.wx_stationdatafile (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	utc_offset_minutes int4 NOT NULL,
	filepath varchar(1024) NOT NULL,
	file_hash varchar(128) NOT NULL,
	file_size int4 NOT NULL,
	observation text NULL,
	is_historical_data bool NOT NULL,
	override_data_on_conflict bool NOT NULL,
	decoder_id int8 NOT NULL,
	station_id int8 NOT NULL,
	status_id int8 NOT NULL,
	CONSTRAINT wx_stationdatafile_pkey PRIMARY KEY (id),
	CONSTRAINT wx_stationdatafile_decoder_id_1c420030_fk_wx_decoder_id FOREIGN KEY (decoder_id) REFERENCES public.wx_decoder(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_stationdatafile_station_id_dbad78c8_fk_wx_station_id FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_stationdatafile_status_id_da354870_fk_wx_statio FOREIGN KEY (status_id) REFERENCES public.wx_stationdatafilestatus(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_stationdatafile_decoder_id_1c420030 ON public.wx_stationdatafile USING btree (decoder_id);
CREATE INDEX wx_stationdatafile_file_hash_fb7e7a04 ON public.wx_stationdatafile USING btree (file_hash);
CREATE INDEX wx_stationdatafile_file_hash_fb7e7a04_like ON public.wx_stationdatafile USING btree (file_hash varchar_pattern_ops);
CREATE INDEX wx_stationdatafile_station_id_dbad78c8 ON public.wx_stationdatafile USING btree (station_id);
CREATE INDEX wx_stationdatafile_status_id_da354870 ON public.wx_stationdatafile USING btree (status_id);


-- public.wx_stationfile definition

-- Drop table

-- DROP TABLE public.wx_stationfile;

CREATE TABLE IF NOT EXISTS public.wx_stationfile (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(256) NULL,
	file varchar(100) NOT NULL,
	station_id int8 NOT NULL,
	CONSTRAINT wx_stationfile_pkey PRIMARY KEY (id),
	CONSTRAINT wx_stationfile_station_id_9d7ce100_fk_wx_station_id FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_stationfile_station_id_9d7ce100 ON public.wx_stationfile USING btree (station_id);


-- public.wx_stationfileingestion definition

-- Drop table

-- DROP TABLE public.wx_stationfileingestion;

CREATE TABLE IF NOT EXISTS public.wx_stationfileingestion (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	remote_folder varchar(1024) NOT NULL,
	file_pattern varchar(256) NOT NULL,
	cron_schedule varchar(64) NOT NULL,
	utc_offset_minutes int4 NOT NULL,
	delete_from_server bool NOT NULL,
	is_active bool NOT NULL,
	is_binary_transfer bool NOT NULL,
	is_historical_data bool NOT NULL,
	override_data_on_conflict bool NOT NULL,
	decoder_id int8 NOT NULL,
	ftp_server_id int8 NOT NULL,
	station_id int8 NOT NULL,
	CONSTRAINT wx_stationfileingestion_ftp_server_id_remote_fol_62ad9111_uniq UNIQUE (ftp_server_id, remote_folder, station_id),
	CONSTRAINT wx_stationfileingestion_pkey PRIMARY KEY (id),
	CONSTRAINT wx_stationfileingest_ftp_server_id_1f7c3994_fk_wx_ftpser FOREIGN KEY (ftp_server_id) REFERENCES public.wx_ftpserver(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_stationfileingestion_decoder_id_3642c375_fk_wx_decoder_id FOREIGN KEY (decoder_id) REFERENCES public.wx_decoder(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_stationfileingestion_station_id_9ee3556b_fk_wx_station_id FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_stationfileingestion_decoder_id_3642c375 ON public.wx_stationfileingestion USING btree (decoder_id);
CREATE INDEX wx_stationfileingestion_ftp_server_id_1f7c3994 ON public.wx_stationfileingestion USING btree (ftp_server_id);
CREATE INDEX wx_stationfileingestion_station_id_9ee3556b ON public.wx_stationfileingestion USING btree (station_id);


-- public.wx_stationimage definition

-- Drop table

-- DROP TABLE public.wx_stationimage;

CREATE TABLE IF NOT EXISTS public.wx_stationimage (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(256) NOT NULL,
	"path" varchar(100) NOT NULL,
	description varchar(256) NULL,
	station_id int8 NOT NULL,
	CONSTRAINT wx_stationimage_pkey PRIMARY KEY (id),
	CONSTRAINT wx_stationimage_station_id_6f149661_fk_wx_station_id FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_stationimage_station_id_6f149661 ON public.wx_stationimage USING btree (station_id);


-- public.wx_stationneighborhood definition

-- Drop table

-- DROP TABLE public.wx_stationneighborhood;

CREATE TABLE IF NOT EXISTS public.wx_stationneighborhood (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	neighborhood_id int8 NOT NULL,
	station_id int8 NOT NULL,
	CONSTRAINT wx_stationneighborhood_neighborhood_id_station_id_aed5fd74_uniq UNIQUE (neighborhood_id, station_id),
	CONSTRAINT wx_stationneighborhood_pkey PRIMARY KEY (id),
	CONSTRAINT wx_stationneighborho_neighborhood_id_ecc2dd88_fk_wx_neighb FOREIGN KEY (neighborhood_id) REFERENCES public.wx_neighborhood(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_stationneighborhood_station_id_5f5f10cc_fk_wx_station_id FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_stationneighborhood_neighborhood_id_ecc2dd88 ON public.wx_stationneighborhood USING btree (neighborhood_id);
CREATE INDEX wx_stationneighborhood_station_id_5f5f10cc ON public.wx_stationneighborhood USING btree (station_id);


-- public.wx_stationtype definition

-- Drop table

-- DROP TABLE public.wx_stationtype;

CREATE TABLE IF NOT EXISTS public.wx_stationtype (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(45) NOT NULL,
	description varchar(256) NOT NULL,
	parent_type_id int8 NULL,
	CONSTRAINT wx_stationtype_pkey PRIMARY KEY (id),
	CONSTRAINT wx_stationtype_parent_type_id_a59a8409_fk_wx_stationtype_id FOREIGN KEY (parent_type_id) REFERENCES public.wx_stationtype(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_stationtype_parent_type_id_a59a8409 ON public.wx_stationtype USING btree (parent_type_id);


-- public.wx_variable definition

-- Drop table

-- DROP TABLE public.wx_variable;

CREATE TABLE IF NOT EXISTS public.wx_variable (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	variable_type varchar(40) NOT NULL,
	symbol varchar(8) NOT NULL,
	"name" varchar(40) NOT NULL,
	"precision" int4 NULL,
	"scale" int4 NULL,
	color varchar(18) NULL,
	range_min float8 NULL,
	range_max float8 NULL,
	default_representation varchar(60) NULL,
	code_table_id int8 NULL,
	measurement_variable_id int8 NULL,
	sampling_operation_id int8 NULL,
	unit_id int8 NULL,
	persistence float8 NULL,
	persistence_hourly float8 NULL,
	range_max_hourly float8 NULL,
	range_min_hourly float8 NULL,
	step float8 NULL,
	step_hourly float8 NULL,
	persistence_window int4 NULL,
	persistence_window_hourly int4 NULL,
	CONSTRAINT wx_variable_pkey PRIMARY KEY (id),
	CONSTRAINT wx_variable_code_table_id_de5ca31b_fk_wx_codetable_id FOREIGN KEY (code_table_id) REFERENCES public.wx_codetable(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_variable_measurement_variable_7f4e48e1_fk_wx_measur FOREIGN KEY (measurement_variable_id) REFERENCES public.wx_measurementvariable(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_variable_sampling_operation_i_6f46f54a_fk_wx_sampli FOREIGN KEY (sampling_operation_id) REFERENCES public.wx_samplingoperation(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_variable_unit_id_cb3048db_fk_wx_unit_id FOREIGN KEY (unit_id) REFERENCES public.wx_unit(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_variable_code_table_id_de5ca31b ON public.wx_variable USING btree (code_table_id);
CREATE INDEX wx_variable_measurement_variable_id_7f4e48e1 ON public.wx_variable USING btree (measurement_variable_id);
CREATE INDEX wx_variable_sampling_operation_id_6f46f54a ON public.wx_variable USING btree (sampling_operation_id);
CREATE INDEX wx_variable_unit_id_cb3048db ON public.wx_variable USING btree (unit_id);


-- public.wx_variableformat definition

-- Drop table

-- DROP TABLE public.wx_variableformat;

CREATE TABLE IF NOT EXISTS public.wx_variableformat (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	lookup_key varchar(255) NOT NULL,
	format_id int8 NOT NULL,
	interval_id int8 NOT NULL,
	variable_id int8 NOT NULL,
	CONSTRAINT wx_variableformat_pkey PRIMARY KEY (id),
	CONSTRAINT wx_variableformat_format_id_86448e28_fk_wx_format_id FOREIGN KEY (format_id) REFERENCES public.wx_format(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_variableformat_interval_id_9a2a62a6_fk_wx_interval_id FOREIGN KEY (interval_id) REFERENCES public.wx_interval(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_variableformat_variable_id_332f94ff_fk_wx_variable_id FOREIGN KEY (variable_id) REFERENCES public.wx_variable(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_variableformat_format_id_86448e28 ON public.wx_variableformat USING btree (format_id);
CREATE INDEX wx_variableformat_interval_id_9a2a62a6 ON public.wx_variableformat USING btree (interval_id);
CREATE INDEX wx_variableformat_variable_id_332f94ff ON public.wx_variableformat USING btree (variable_id);


-- public.wx_wxgrouppermission definition

-- Drop table

-- DROP TABLE public.wx_wxgrouppermission;

CREATE TABLE IF NOT EXISTS public.wx_wxgrouppermission (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	group_id int4 NOT NULL,
	CONSTRAINT wx_wxgrouppermission_group_id_key UNIQUE (group_id),
	CONSTRAINT wx_wxgrouppermission_pkey PRIMARY KEY (id),
	CONSTRAINT wx_wxgrouppermission_group_id_e5b916df_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED
);


-- public.wx_wxgrouppermission_permissions definition

-- Drop table

-- DROP TABLE public.wx_wxgrouppermission_permissions;

CREATE TABLE IF NOT EXISTS public.wx_wxgrouppermission_permissions (
	id bigserial NOT NULL,
	wxgrouppermission_id int8 NOT NULL,
	wxpermission_id int8 NOT NULL,
	CONSTRAINT wx_wxgrouppermission_per_wxgrouppermission_id_wxp_b1e1e0d0_uniq UNIQUE (wxgrouppermission_id, wxpermission_id),
	CONSTRAINT wx_wxgrouppermission_permissions_pkey PRIMARY KEY (id),
	CONSTRAINT wx_wxgrouppermission_wxgrouppermission_id_1316a21a_fk_wx_wxgrou FOREIGN KEY (wxgrouppermission_id) REFERENCES public.wx_wxgrouppermission(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_wxgrouppermission_wxpermission_id_70fc5bfd_fk_wx_wxperm FOREIGN KEY (wxpermission_id) REFERENCES public.wx_wxpermission(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_wxgrouppermission_permissions_wxgrouppermission_id_1316a21a ON public.wx_wxgrouppermission_permissions USING btree (wxgrouppermission_id);
CREATE INDEX wx_wxgrouppermission_permissions_wxpermission_id_70fc5bfd ON public.wx_wxgrouppermission_permissions USING btree (wxpermission_id);


-- public.auth_group_permissions definition

-- Drop table

-- DROP TABLE public.auth_group_permissions;

CREATE TABLE IF NOT EXISTS public.auth_group_permissions (
	id bigserial NOT NULL,
	group_id int4 NOT NULL,
	permission_id int4 NOT NULL,
	CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id),
	CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id),
	CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


-- public.wx_dailysummarytask definition

-- Drop table

-- DROP TABLE public.wx_dailysummarytask;

CREATE TABLE IF NOT EXISTS public.wx_dailysummarytask (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"date" date NOT NULL,
	started_at timestamptz NULL,
	finished_at timestamptz NULL,
	station_id int8 NOT NULL,
	CONSTRAINT wx_dailysummarytask_pkey PRIMARY KEY (id),
	CONSTRAINT wx_dailysummarytask_station_id_8e5afffb_fk_wx_station_id FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_dailysummarytask_station_id_8e5afffb ON public.wx_dailysummarytask USING btree (station_id);


-- public.wx_datafilestation definition

-- Drop table

-- DROP TABLE public.wx_datafilestation;

CREATE TABLE IF NOT EXISTS public.wx_datafilestation (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	datafile_id int8 NOT NULL,
	station_id int8 NOT NULL,
	CONSTRAINT wx_datafilestation_pkey PRIMARY KEY (id),
	CONSTRAINT wx_datafilestation_datafile_id_51e40536_fk_wx_datafile_id FOREIGN KEY (datafile_id) REFERENCES public.wx_datafile(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_datafilestation_station_id_021d80cb_fk_wx_station_id FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_datafilestation_datafile_id_51e40536 ON public.wx_datafilestation USING btree (datafile_id);
CREATE INDEX wx_datafilestation_station_id_021d80cb ON public.wx_datafilestation USING btree (station_id);


-- public.wx_datafilevariable definition

-- Drop table

-- DROP TABLE public.wx_datafilevariable;

CREATE TABLE IF NOT EXISTS public.wx_datafilevariable (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	datafile_id int8 NOT NULL,
	variable_id int8 NOT NULL,
	CONSTRAINT wx_datafilevariable_pkey PRIMARY KEY (id),
	CONSTRAINT wx_datafilevariable_datafile_id_8bacf7b0_fk_wx_datafile_id FOREIGN KEY (datafile_id) REFERENCES public.wx_datafile(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_datafilevariable_variable_id_19a3b6a9_fk_wx_variable_id FOREIGN KEY (variable_id) REFERENCES public.wx_variable(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_datafilevariable_datafile_id_8bacf7b0 ON public.wx_datafilevariable USING btree (datafile_id);
CREATE INDEX wx_datafilevariable_variable_id_19a3b6a9 ON public.wx_datafilevariable USING btree (variable_id);


-- public.wx_dcpmessages definition

-- Drop table

-- DROP TABLE public.wx_dcpmessages;

CREATE TABLE IF NOT EXISTS public.wx_dcpmessages (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	datetime timestamptz NOT NULL,
	failure_code varchar(1) NOT NULL,
	signal_strength varchar(2) NOT NULL,
	frequency_offset varchar(2) NOT NULL,
	modulation_index varchar(1) NOT NULL,
	data_quality varchar(1) NOT NULL,
	channel varchar(3) NOT NULL,
	spacecraft_indicator varchar(1) NOT NULL,
	message_data_length varchar(5) NOT NULL,
	payload text NOT NULL,
	data_source_id int8 NOT NULL,
	noaa_dcp_id int8 NOT NULL,
	CONSTRAINT wx_dcpmessages_noaa_dcp_id_datetime_07d6c38c_uniq UNIQUE (noaa_dcp_id, datetime),
	CONSTRAINT wx_dcpmessages_pkey PRIMARY KEY (id),
	CONSTRAINT wx_dcpmessages_data_source_id_1890c900_fk_wx_datasource_id FOREIGN KEY (data_source_id) REFERENCES public.wx_datasource(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_dcpmessages_noaa_dcp_id_45cd8caa_fk_wx_noaadcp_id FOREIGN KEY (noaa_dcp_id) REFERENCES public.wx_noaadcp(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_dcpmessages_data_source_id_1890c900 ON public.wx_dcpmessages USING btree (data_source_id);
CREATE INDEX wx_dcpmessages_noaa_dcp_id_45cd8caa ON public.wx_dcpmessages USING btree (noaa_dcp_id);


-- public.wx_document definition

-- Drop table

-- DROP TABLE public.wx_document;

CREATE TABLE IF NOT EXISTS public.wx_document (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	alias varchar(256) NULL,
	file varchar(100) NOT NULL,
	processed bool NOT NULL,
	decoder_id int8 NULL,
	station_id int8 NOT NULL,
	CONSTRAINT wx_document_pkey PRIMARY KEY (id),
	CONSTRAINT wx_document_decoder_id_75c5b0f9_fk_wx_decoder_id FOREIGN KEY (decoder_id) REFERENCES public.wx_decoder(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_document_station_id_5651f6c9_fk_wx_station_id FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_document_decoder_id_75c5b0f9 ON public.wx_document USING btree (decoder_id);
CREATE INDEX wx_document_station_id_5651f6c9 ON public.wx_document USING btree (station_id);


-- public.wx_hourlysummarytask definition

-- Drop table

-- DROP TABLE public.wx_hourlysummarytask;

CREATE TABLE IF NOT EXISTS public.wx_hourlysummarytask (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	datetime timestamptz NOT NULL,
	started_at timestamptz NULL,
	finished_at timestamptz NULL,
	station_id int8 NOT NULL,
	CONSTRAINT wx_hourlysummarytask_pkey PRIMARY KEY (id),
	CONSTRAINT wx_hourlysummarytask_station_id_06038ca9_fk_wx_station_id FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_hourlysummarytask_station_id_06038ca9 ON public.wx_hourlysummarytask USING btree (station_id);


-- public.wx_hydromlprediction definition

-- Drop table

-- DROP TABLE public.wx_hydromlprediction;

CREATE TABLE IF NOT EXISTS public.wx_hydromlprediction (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"name" varchar(256) NOT NULL,
	hydroml_prediction_id int4 NOT NULL,
	variable_id int8 NOT NULL,
	CONSTRAINT wx_hydromlprediction_hydroml_prediction_id_va_97c701c2_uniq UNIQUE (hydroml_prediction_id, variable_id),
	CONSTRAINT wx_hydromlprediction_pkey PRIMARY KEY (id),
	CONSTRAINT wx_hydromlprediction_variable_id_d72ddc51_fk_wx_variable_id FOREIGN KEY (variable_id) REFERENCES public.wx_variable(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_hydromlprediction_variable_id_d72ddc51 ON public.wx_hydromlprediction USING btree (variable_id);


-- public.wx_hydromlpredictionmapping definition

-- Drop table

-- DROP TABLE public.wx_hydromlpredictionmapping;

CREATE TABLE IF NOT EXISTS public.wx_hydromlpredictionmapping (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	prediction_result varchar(32) NOT NULL,
	hydroml_prediction_id int8 NOT NULL,
	quality_flag_id int8 NOT NULL,
	CONSTRAINT wx_hydromlpredictionmapp_hydroml_prediction_id_qu_43723ef2_uniq UNIQUE (hydroml_prediction_id, quality_flag_id),
	CONSTRAINT wx_hydromlpredictionmapping_pkey PRIMARY KEY (id),
	CONSTRAINT wx_hydromlprediction_hydroml_prediction_i_89231aab_fk_wx_hydrom FOREIGN KEY (hydroml_prediction_id) REFERENCES public.wx_hydromlprediction(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_hydromlprediction_quality_flag_id_f34f7733_fk_wx_qualit FOREIGN KEY (quality_flag_id) REFERENCES public.wx_qualityflag(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_hydromlpredictionmapping_hydroml_prediction_id_89231aab ON public.wx_hydromlpredictionmapping USING btree (hydroml_prediction_id);
CREATE INDEX wx_hydromlpredictionmapping_quality_flag_id_f34f7733 ON public.wx_hydromlpredictionmapping USING btree (quality_flag_id);


-- public.wx_hydromlpredictionstation definition

-- Drop table

-- DROP TABLE public.wx_hydromlpredictionstation;

CREATE TABLE IF NOT EXISTS public.wx_hydromlpredictionstation (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	data_period_in_minutes int4 NOT NULL,
	interval_in_minutes int4 NOT NULL,
	neighborhood_id int8 NOT NULL,
	prediction_id int8 NOT NULL,
	target_station_id int8 NOT NULL,
	CONSTRAINT wx_hydromlpredictionstation_pkey PRIMARY KEY (id),
	CONSTRAINT wx_hydromlprediction_neighborhood_id_9aada20a_fk_wx_neighb FOREIGN KEY (neighborhood_id) REFERENCES public.wx_neighborhood(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_hydromlprediction_prediction_id_3fb81eaa_fk_wx_hydrom FOREIGN KEY (prediction_id) REFERENCES public.wx_hydromlprediction(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_hydromlprediction_target_station_id_f46ac928_fk_wx_statio FOREIGN KEY (target_station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_hydromlpredictionstation_neighborhood_id_9aada20a ON public.wx_hydromlpredictionstation USING btree (neighborhood_id);
CREATE INDEX wx_hydromlpredictionstation_prediction_id_3fb81eaa ON public.wx_hydromlpredictionstation USING btree (prediction_id);
CREATE INDEX wx_hydromlpredictionstation_target_station_id_f46ac928 ON public.wx_hydromlpredictionstation USING btree (target_station_id);


-- public.wx_noaadcpsstation definition

-- Drop table

-- DROP TABLE public.wx_noaadcpsstation;

CREATE TABLE IF NOT EXISTS public.wx_noaadcpsstation (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	start_date timestamptz NOT NULL,
	end_date timestamptz NULL,
	decoder_id int8 NOT NULL,
	format_id int8 NOT NULL,
	interval_id int8 NOT NULL,
	noaa_dcp_id int8 NOT NULL,
	station_id int8 NOT NULL,
	CONSTRAINT wx_noaadcpsstation_pkey PRIMARY KEY (id),
	CONSTRAINT wx_noaadcpsstation_decoder_id_34af8a08_fk_wx_decoder_id FOREIGN KEY (decoder_id) REFERENCES public.wx_decoder(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_noaadcpsstation_format_id_7e16076b_fk_wx_format_id FOREIGN KEY (format_id) REFERENCES public.wx_format(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_noaadcpsstation_interval_id_47a49aba_fk_wx_interval_id FOREIGN KEY (interval_id) REFERENCES public.wx_interval(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_noaadcpsstation_noaa_dcp_id_250f52ae_fk_wx_noaadcp_id FOREIGN KEY (noaa_dcp_id) REFERENCES public.wx_noaadcp(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_noaadcpsstation_station_id_db3cf819_fk_wx_station_id FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_noaadcpsstation_decoder_id_34af8a08 ON public.wx_noaadcpsstation USING btree (decoder_id);
CREATE INDEX wx_noaadcpsstation_format_id_7e16076b ON public.wx_noaadcpsstation USING btree (format_id);
CREATE INDEX wx_noaadcpsstation_interval_id_47a49aba ON public.wx_noaadcpsstation USING btree (interval_id);
CREATE INDEX wx_noaadcpsstation_noaa_dcp_id_250f52ae ON public.wx_noaadcpsstation USING btree (noaa_dcp_id);
CREATE INDEX wx_noaadcpsstation_station_id_db3cf819 ON public.wx_noaadcpsstation USING btree (station_id);


-- public.wx_periodicjob definition

-- Drop table

-- DROP TABLE public.wx_periodicjob;

CREATE TABLE IF NOT EXISTS public.wx_periodicjob (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	is_running bool NOT NULL,
	last_record int4 NOT NULL,
	periodic_job_type_id int8 NOT NULL,
	station_id int8 NOT NULL,
	CONSTRAINT wx_periodicjob_pkey PRIMARY KEY (id),
	CONSTRAINT wx_periodicjob_periodic_job_type_id_015ed981_fk_wx_period FOREIGN KEY (periodic_job_type_id) REFERENCES public.wx_periodicjobtype(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_periodicjob_station_id_9745d426_fk_wx_station_id FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_periodicjob_periodic_job_type_id_015ed981 ON public.wx_periodicjob USING btree (periodic_job_type_id);
CREATE INDEX wx_periodicjob_station_id_9745d426 ON public.wx_periodicjob USING btree (station_id);


-- public.wx_qcpersistthreshold definition

-- Drop table

-- DROP TABLE public.wx_qcpersistthreshold;

CREATE TABLE IF NOT EXISTS public.wx_qcpersistthreshold (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"interval" int4 NOT NULL,
	"window" int4 NOT NULL,
	minimum_variance float8 NOT NULL,
	station_id int8 NOT NULL,
	variable_id int8 NOT NULL,
	CONSTRAINT wx_qcpersistthreshold_pkey PRIMARY KEY (id),
	CONSTRAINT wx_qcpersistthreshold_station_id_variable_id_i_ada8f6f8_uniq UNIQUE (station_id, variable_id, "interval"),
	CONSTRAINT wx_qcpersistthreshold_station_id_b24a1473_fk_wx_station_id FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_qcpersistthreshold_variable_id_b9ba6d0a_fk_wx_variable_id FOREIGN KEY (variable_id) REFERENCES public.wx_variable(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_qcpersistthreshold_station_id_b24a1473 ON public.wx_qcpersistthreshold USING btree (station_id);
CREATE INDEX wx_qcpersistthreshold_variable_id_b9ba6d0a ON public.wx_qcpersistthreshold USING btree (variable_id);


-- public.wx_qcrangethreshold definition

-- Drop table

-- DROP TABLE public.wx_qcrangethreshold;

CREATE TABLE IF NOT EXISTS public.wx_qcrangethreshold (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"interval" int4 NULL,
	range_min float8 NULL,
	range_max float8 NULL,
	"month" int4 NOT NULL,
	station_id int8 NOT NULL,
	variable_id int8 NOT NULL,
	CONSTRAINT wx_qcrangethreshold_pkey PRIMARY KEY (id),
	CONSTRAINT wx_qcrangethreshold_station_id_variable_id_m_d9bfdc6f_uniq UNIQUE (station_id, variable_id, month, "interval"),
	CONSTRAINT wx_qcrangethreshold_station_id_5499ab50_fk_wx_station_id FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_qcrangethreshold_variable_id_d59d70f5_fk_wx_variable_id FOREIGN KEY (variable_id) REFERENCES public.wx_variable(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_qcrangethreshold_station_id_5499ab50 ON public.wx_qcrangethreshold USING btree (station_id);
CREATE INDEX wx_qcrangethreshold_variable_id_d59d70f5 ON public.wx_qcrangethreshold USING btree (variable_id);


-- public.wx_qcstepthreshold definition

-- Drop table

-- DROP TABLE public.wx_qcstepthreshold;

CREATE TABLE IF NOT EXISTS public.wx_qcstepthreshold (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	"interval" int4 NULL,
	step_min float8 NULL,
	step_max float8 NULL,
	station_id int8 NOT NULL,
	variable_id int8 NOT NULL,
	CONSTRAINT wx_qcstepthreshold_pkey PRIMARY KEY (id),
	CONSTRAINT wx_qcstepthreshold_station_id_variable_id_i_9f6553f7_uniq UNIQUE (station_id, variable_id, "interval"),
	CONSTRAINT wx_qcstepthreshold_station_id_efebc6e1_fk_wx_station_id FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_qcstepthreshold_variable_id_f45ea73f_fk_wx_variable_id FOREIGN KEY (variable_id) REFERENCES public.wx_variable(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_qcstepthreshold_station_id_efebc6e1 ON public.wx_qcstepthreshold USING btree (station_id);
CREATE INDEX wx_qcstepthreshold_variable_id_f45ea73f ON public.wx_qcstepthreshold USING btree (variable_id);


-- public.wx_ratingcurve definition

-- Drop table

-- DROP TABLE public.wx_ratingcurve;

CREATE TABLE IF NOT EXISTS public.wx_ratingcurve (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	start_date timestamptz NOT NULL,
	station_id int8 NOT NULL,
	CONSTRAINT wx_ratingcurve_pkey PRIMARY KEY (id),
	CONSTRAINT wx_ratingcurve_station_id_5fe7ea18_fk_wx_station_id FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_ratingcurve_station_id_5fe7ea18 ON public.wx_ratingcurve USING btree (station_id);


-- public.wx_ratingcurvetable definition

-- Drop table

-- DROP TABLE public.wx_ratingcurvetable;

CREATE TABLE IF NOT EXISTS public.wx_ratingcurvetable (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	h float8 NOT NULL,
	q float8 NOT NULL,
	rating_curve_id int8 NOT NULL,
	CONSTRAINT wx_ratingcurvetable_pkey PRIMARY KEY (id),
	CONSTRAINT wx_ratingcurvetable_rating_curve_id_5cdc12d0_fk_wx_rating FOREIGN KEY (rating_curve_id) REFERENCES public.wx_ratingcurve(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_ratingcurvetable_rating_curve_id_5cdc12d0 ON public.wx_ratingcurvetable USING btree (rating_curve_id);


-- public.wx_stationdataminimuminterval definition

-- Drop table

-- DROP TABLE public.wx_stationdataminimuminterval;

CREATE TABLE IF NOT EXISTS public.wx_stationdataminimuminterval (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	datetime timestamptz NOT NULL,
	minimum_interval time NULL,
	record_count int4 NOT NULL,
	ideal_record_count int4 NOT NULL,
	record_count_percentage float8 NOT NULL,
	station_id int8 NOT NULL,
	variable_id int8 NOT NULL,
	CONSTRAINT wx_stationdataminimumint_datetime_station_id_vari_a3da4a5e_uniq UNIQUE (datetime, station_id, variable_id),
	CONSTRAINT wx_stationdataminimuminterval_pkey PRIMARY KEY (id),
	CONSTRAINT wx_stationdataminimu_station_id_ec0495de_fk_wx_statio FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_stationdataminimu_variable_id_dd23392f_fk_wx_variab FOREIGN KEY (variable_id) REFERENCES public.wx_variable(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_stationdataminimuminterval_station_id_ec0495de ON public.wx_stationdataminimuminterval USING btree (station_id);
CREATE INDEX wx_stationdataminimuminterval_variable_id_dd23392f ON public.wx_stationdataminimuminterval USING btree (variable_id);


-- public.wx_stationvariable definition

-- Drop table

-- DROP TABLE public.wx_stationvariable;

CREATE TABLE IF NOT EXISTS public.wx_stationvariable (
	id bigserial NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL,
	first_measurement timestamptz NULL,
	last_measurement timestamptz NULL,
	"last_value" float8 NULL,
	height float8 NULL,
	last_data_datetime timestamptz NULL,
	last_data_value float8 NULL,
	last_data_code varchar(60) NULL,
	station_id int8 NOT NULL,
	variable_id int8 NOT NULL,
	CONSTRAINT wx_stationvariable_pkey PRIMARY KEY (id),
	CONSTRAINT wx_stationvariable_station_id_variable_id_9f772d22_uniq UNIQUE (station_id, variable_id),
	CONSTRAINT wx_stationvariable_station_id_fc9cb353_fk_wx_station_id FOREIGN KEY (station_id) REFERENCES public.wx_station(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT wx_stationvariable_variable_id_5adbdffd_fk_wx_variable_id FOREIGN KEY (variable_id) REFERENCES public.wx_variable(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX wx_stationvariable_station_id_fc9cb353 ON public.wx_stationvariable USING btree (station_id);
CREATE INDEX wx_stationvariable_variable_id_5adbdffd ON public.wx_stationvariable USING btree (variable_id);