import { createRouter, createWebHashHistory } from 'vue-router'
import routes from './routes'

// utilities
import {loadData} from '@/utils/load-data.js';

// import models for pinia-orm
import {useRepo} from 'pinia-orm';
import ApplicationState from '@/models/ApplicationState';
// referencee data
import ClimateZone from '@/models/ClimateZone';
import ControlSchedule from '@/models/ControlSchedule';
import Exposure from '@/models/Exposure';
import FacilityType from '@/models/FacilityType';
import FeatureType from '@/models/FeatureType';
import MaintenanceSchedule from '@/models/MaintenanceSchedule';
import MediaType from '@/models/MediaType';
import ObservationType from '@/models/ObservationType';
import ObservedProperty from '@/models/ObservedProperty';
import ObservingMethod from '@/models/ObservingMethod';
import ObservingProcedure from '@/models/ObservingProcedure';
import Programme from '@/models/Programme';
import ReferenceSurface from '@/models/ReferenceSurface';
import Season from '@/models/Season';
import Status from '@/models/Status';
import SourceType from '@/models/SourceType';
import SurfaceCover from '@/models/SurfaceCover';
import SurfaceRoughness from '@/models/SurfaceRoughness';
import Territory from '@/models/Territory';
import TimeZone from '@/models/TimeZone';
import Topography from '@/models/Topography';
import WmoRegion from '@/models/WmoRegion';
// business / master data
import User from '@/models/User';
import Host from '@/models/Host';
import Deployment from '@/models/Deployment';
import Observer from '@/models/Observer';
import ObserverCharacteristics from '@/models/ObserverCharacteristics';
import Feature from '@/models/Feature';

import * as Wkt from 'wicket';

import {flatten_geojson} from '@/utils/geojson.js';

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes,
  scrollBehavior() {
    // always scroll to top
    return { top: 0 }
  },
})

router.beforeEach( async () => {
  if( useRepo(ClimateZone).all().length === 0){await loadData(process.env.API + '/vocabularies/climate_zone/items?f=csv', true).then( (result) => { useRepo(ClimateZone).save(result) })};
  if( useRepo(ControlSchedule).all().length === 0){await loadData('/data/reference-data/control_schedule.psv').then( (result) => { useRepo(ControlSchedule).save(result) })}; // TODO
  if( useRepo(Exposure).all().length === 0){await loadData(process.env.API + '/vocabularies/exposure/items?f=csv', true).then( (result) => { useRepo(Exposure).save(result) })};
  if( useRepo(FacilityType).all().length === 0){await loadData(process.env.API + '/vocabularies/facility_type/items?f=csv', true).then( (result) => { useRepo(FacilityType).save(result) })};
  if( useRepo(FeatureType).all().length === 0){await loadData(process.env.API + '/vocabularies/feature_type/items?f=csv', true).then( (result) => { useRepo(FeatureType).save(result) })};
  if( useRepo(MaintenanceSchedule).all().length === 0){await loadData('/data/reference-data/maintenance_schedule.psv').then( (result) => { useRepo(MaintenanceSchedule).save(result) })};  // TODO
  if( useRepo(MediaType).all().length === 0){await loadData(process.env.API + '/vocabularies/media_type/items?f=csv', true).then( (result) => { useRepo(MediaType).save(result) })};
  if( useRepo(ObservationType).all().length === 0){await loadData(process.env.API + '/vocabularies/observation_type/items?f=csv', true).then( (result) => { useRepo(ObservationType).save(result) })};
  if( useRepo(ObservedProperty).all().length === 0){await loadData(process.env.API + '/vocabularies/observed_property/items?f=csv', true).then( (result) => { useRepo(ObservedProperty).save(result) })};
  if( useRepo(ObservingMethod).all().length === 0){await loadData(process.env.API + '/vocabularies/observing_method/items?f=csv', true).then( (result) => { useRepo(ObservingMethod).save(result) })};
  if( useRepo(ObservingProcedure).all().length === 0){await loadData(process.env.API + '/vocabularies/observing_procedure/items?f=csv', true).then( (result) => { useRepo(ObservingProcedure).save(result) })};
  if( useRepo(Programme).all().length === 0){await loadData(process.env.API + '/vocabularies/programme/items?f=csv', true).then( (result) => { useRepo(Programme).save(result) })};
  if( useRepo(ReferenceSurface).all().length === 0){await loadData(process.env.API + '/vocabularies/reference_surface/items?f=csv', true).then( (result) => { useRepo(ReferenceSurface).save(result) })};
  if( useRepo(Season).all().length === 0){await loadData(process.env.API + '/vocabularies/season/items?f=csv', true).then( (result) => { useRepo(Season).save(result) })};
  if( useRepo(SourceType).all().length === 0){await loadData(process.env.API + '/vocabularies/source_type/items?f=csv', true).then( (result) => { useRepo(SourceType).save(result) })};
  if( useRepo(Status).all().length === 0){await loadData(process.env.API + '/vocabularies/status/items?f=csv', true).then( (result) => { useRepo(Status).save(result) })};
  if( useRepo(SurfaceCover).all().length === 0){await loadData(process.env.API + '/vocabularies/surface_cover/items?f=csv', true).then( (result) => { useRepo(SurfaceCover).save(result) })};
  if( useRepo(SurfaceRoughness).all().length === 0){await loadData(process.env.API + '/vocabularies/surface_roughness/items?f=csv', true).then( (result) => { useRepo(SurfaceRoughness).save(result) })};
  if( useRepo(Territory).all().length === 0){await loadData(process.env.API + '/vocabularies/territory/items?f=csv', true).then( (result) => { useRepo(Territory).save(result) })};
  if( useRepo(TimeZone).all().length === 0){await loadData(process.env.API + '/vocabularies/time_zone/items?f=csv', true).then( (result) => { useRepo(TimeZone).save(result) })};
  if( useRepo(Topography).all().length === 0){await loadData(process.env.API + '/vocabularies/topography/items?f=csv', true).then( (result) => { useRepo(Topography).save(result) })};
  if( useRepo(WmoRegion).all().length === 0){await loadData(process.env.API + '/vocabularies/wmo_region/items?f=csv', true).then( (result) => { useRepo(WmoRegion).save(result) })};
  if( useRepo(User).all().length === 0){await loadData(process.env.API + '/vocabularies/user/items?f=csv', true).then( (result) => { useRepo(User).save(result) })};
  if( useRepo(Host).all().length === 0){await loadData(process.env.API + '/collections/stations/items?limit=1000&f=json', true).then( (result) => flatten_geojson(result.features) ).then( (result) => { useRepo(Host).save(result) })};
  if( useRepo(Deployment).all().length === 0){await loadData(process.env.API + '/vocabularies/deployment/items?limit=1000&f=csv', true).then( (result) => { useRepo(Deployment).save(result) })};
  if( useRepo(Observer).all().length === 0){await loadData(process.env.API + '/collections/observer/items?limit=1000&f=json', true).then( (result) => flatten_geojson(result.features) ).then( (result) => { useRepo(Observer).save(result) })};
  if( useRepo(ObserverCharacteristics).all().length === 0){await loadData(process.env.API + '/vocabularies/observer_characteristics/items?limit=1000&f=csv', true).then( (result) => { useRepo(ObserverCharacteristics).save(result) })};
  // if( useRepo(Feature).all().length === 0){await loadData(process.env.API + '/collections/ontario_watershed/items?limit=1000&f=json', true).then( (result) => flatten_geojson(result.features) ).then( (result) => { useRepo(Feature).save(result) })};
  useRepo(ApplicationState).save({ 'key': 'databaseReady', 'value': 'ready'})
});

export default router
