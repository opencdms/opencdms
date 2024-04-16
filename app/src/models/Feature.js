import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import FeatureType from '@/models/FeatureType';
import User from '@/models/User';
import Status from '@/models/Status';

export default class Feature extends Model {
  static entity = 'feature';
  static fields() {
    return {
      id: this.string(''),
      name: this.string(''),
      description: this.string(''),
      links: this.attr(new LinksType([])),
      feature_type_id: this.string(''),
      feature_type: this.belongsTo(FeatureType,'feature_type_id'),
      geometry: this.string(''),
      elevation: this.number(null),
      parent_id: this.string(''),
      parent: this.belongsTo(Feature,'parent_id'),
      properties: this.attr(null),
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

