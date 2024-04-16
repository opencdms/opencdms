import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import Observer from '@/models/Observer';
import ObservedProperty from '@/models/ObservedProperty';
import ObservingMethod from '@/models/ObservingMethod';
import User from '@/models/User';
import Status from '@/models/Status';

export default class ObserverCharacteristics extends Model {
  static entity = 'observer_characteristics';
  static fields() {
    return {
      id: this.string(''),
      observer_id: this.string(''),
      observer: this.belongsTo(Observer,'observer_id'),
      observed_property_id: this.string(''),
      observed_property: this.belongsTo(ObservedProperty,'observed_property_id'),
      observing_method_id: this.string(''),
      observing_method: this.belongsTo(ObservingMethod,'observing_method_id'),
      measurement_units: this.number(null),
      drift_per_unit_time: this.number(null),
      unit_time: this.number(null),
      valid_min: this.number(null),
      valid_max: this.number(null),
      measurement_uncertainty: this.number(null),
      measurement_accuracy: this.number(null),
      measurement_repeatability: this.number(null),
      measurement_resolution: this.number(null),
      _version: this.number(null),
      _change_date: this.string(''),
      _user_id: this.string(''),
      _user: this.belongsTo(User,'_user_id'),
      _status_id: this.string(''),
      _status: this.belongsTo(Status,'_status_id'),
      comments: this.string('')
    };
  };
};

