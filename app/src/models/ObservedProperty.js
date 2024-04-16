import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import User from '@/models/User';
import Status from '@/models/Status';

export default class ObservedProperty extends Model {
  static entity = 'observed_property';
  static fields() {
    return {
      id: this.string(''),
      authority: this.string(''),
      short_name: this.string(''),
      standard_name: this.string(''),
      units: this.string(''),
      description: this.string(''),
      links: this.attr(new LinksType([])),
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

