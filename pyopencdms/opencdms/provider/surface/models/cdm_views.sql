CREATE OR REPLACE VIEW surface.cdm_observed_property as
    SELECT
        t1.id  AS id,
        t1.symbol AS short_name,
        t1.name AS standard_name,
        t2.symbol AS units_symbol,
        t2.name AS units_name,
        NULL::text AS link
   FROM
        surface.wx_variable as t1
   LEFT JOIN
        surface.wx_unit as t2 ON t1.unit_id = t2.id;

CREATE OR REPLACE VIEW surface.cdm_hosts as
    SELECT
        t1.id as id,
        t1.name as name,
        t1.station_details as description,
        NULL::text as link,
        ST_SetSRID(ST_MakePoint(t1.longitude, t1.latitude), 4326) as location,
        t1.elevation as elevation,
        t1.wigos as wigos_station_identifier,
        NULL::text as facility_type,
        t1.begin_date as date_established,
        NULL::text as wmo_region,
        NULL::text as territory,
        t1.begin_date as valid_from,
        t1.end_date as valid_to,
        1 as version,
        t1.updated_at as change_date,
        NULL::text as user_id,
        1 as status_id,
        NULL::text as comments
    FROM
        surface.wx_station as t1;

CREATE OR REPLACE VIEW surface.cdm_observations as
 SELECT t3.id,
    t3.location,
    t3.elevation,
    t3.observation_type_id,
    t3.phenomenon_start,
    t3.phenomenon_end,
    t4.standard_name AS observed_property,
    t3.result_value,
    t4.units_name AS result_uom,
    t3.result_description,
    t3.result_quality,
    t3.result_time,
    t3.valid_from,
    t3.valid_to,
    t3.host_id,
    t3.observer_id,
    t3.observed_property_id,
    t3.report_id,
    t3.collection_id,
    t3.parameter,
    t3.feature_of_interest,
    t3.version,
    t3.change_date,
    t3.user_id,
    t3.status_id,
    t3.comments,
    t3.source_id
   FROM ( SELECT NULL::text AS id,
            t2.location,
            t2.elevation,
            NULL::text AS observation_type_id,
            t1.datetime AS phenomenon_start,
            t1.datetime AS phenomenon_end,
            t1.measured AS result_value,
            NULL::text AS result_description,
            jsonb_build_array(jsonb_build_object('scheme', 'surface', 'name', 'range', 'description', t1.qc_range_description, 'flag', t1.qc_range_quality_flag), jsonb_build_object('scheme', 'surface', 'name', 'step', 'description', t1.qc_step_description, 'flag', t1.qc_step_quality_flag), jsonb_build_object('scheme', 'surface', 'name', 'persistence', 'description', t1.qc_persist_description, 'flag', t1.qc_persist_quality_flag), jsonb_build_object('scheme', 'surface', 'name', 'manual', 'description', '', 'flag', t1.manual_flag), jsonb_build_object('scheme', 'surface', 'name', 'quality', 'description', '', 'flag', t1.quality_flag)) AS result_quality,
            t1.created_at AS result_time,
            NULL::timestamp without time zone AS valid_from,
            NULL::timestamp without time zone AS valid_to,
            t1.station_id AS host_id,
            NULL::text AS observer_id,
            t1.variable_id AS observed_property_id,
            NULL::text AS observing_procedure_id,
            NULL::text AS report_id,
            NULL::text AS collection_id,
            NULL::jsonb AS parameter,
            NULL::text AS feature_of_interest,
            1 AS version,
            t1.updated_at AS change_date,
            NULL::text AS user_id,
            1 AS status_id,
            t1.remarks AS comments,
            NULL::text AS source_id
           FROM surface.raw_data t1
             LEFT JOIN surface.cdm_hosts t2 ON t1.station_id = t2.id) t3
     LEFT JOIN surface.cdm_observed_property t4 ON t3.observed_property_id = t4.id;


create or replace view surface.synop_demo as
	select
		host_id, phenomenon_end,
		ST_AsText(location) as location,
		avg(elevation) as elevation,
		avg(case when observed_property_id=10 then result_value end) as air_temperature,
		avg(case when observed_property_id=19 then result_value end) as dew_point_temperature,
		avg(case when observed_property_id=60 then result_value end) as station_pressure,
		avg(case when observed_property_id=50 then result_value end) as wind_speed,
		avg(case when observed_property_id=55 then result_value end) as wind_from_direction
	from
		surface.cdm_observations
	where
		observed_property_id in (10,19, 60, 50, 55)
	group by
		host_id, phenomenon_end, location;