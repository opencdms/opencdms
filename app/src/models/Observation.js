import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import ObservationType from '@/models/ObservationType';
import Host from '@/models/Host';
import Observer from '@/models/Observer';
import ObservedProperty from '@/models/ObservedProperty';
import ObservingProcedure from '@/models/ObservingProcedure';
import Collection from '@/models/Collection';
import Feature from '@/models/Feature';
import User from '@/models/User';
import Status from '@/models/Status';
import Source from '@/models/Source';

export default class Observation extends Model {
  static entity = 'observation';
  static fields() {
    return {
      id: this.string(''),
      location: this.string(''),
      elevation: this.number(null),
      observation_type_id: this.string(''),
      observation_type: this.belongsTo(ObservationType,'observation_type_id'),
      phenomenon_start: this.string(''),
      phenomenon_end: this.string(''),
      result_value: this.number(null),
      result_uom: this.string(''),
      result_description: this.string(''),
      result_quality: this.attr(null),
      result_time: this.string(''),
      valid_from: this.string(''),
      valid_to: this.string(''),
      host_id: this.string(''),
      host: this.belongsTo(Host,'host_id'),
      observer_id: this.string(''),
      observer: this.belongsTo(Observer,'observer_id'),
      observed_property_id: this.string(''),
      observed_property: this.belongsTo(ObservedProperty,'observed_property_id'),
      observing_procedure_id: this.string(''),
      observing_procedure: this.belongsTo(ObservingProcedure,'observing_procedure_id'),
      collection_id: this.string(''),
      collection: this.belongsTo(Collection,'collection_id'),
      parameter: this.attr(null),
      feature_id: this.string(''),
      feature: this.belongsTo(Feature,'feature_id'),
      _version: this.number(null),
      _change_date: this.string(''),
      _user_id: this.string(''),
      _user: this.belongsTo(User,'_user_id'),
      _status_id: this.string(''),
      _status: this.belongsTo(Status,'_status_id'),
      comments: this.string(''),
      _source_id: this.string(''),
      _source: this.belongsTo(Source,'_source_id'),
      _source_identifier: this.string('')
    };
  };
};

