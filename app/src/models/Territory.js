import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import WmoRegion from '@/models/WmoRegion';
import User from '@/models/User';
import Status from '@/models/Status';

export default class Territory extends Model {
  static entity = 'territory';
  static fields() {
    return {
      id: this.string(''),
      ISO3c: this.string(''),
      name: this.string(''),
      description: this.string(''),
      wmo_region_id: this.string(''),
      wmo_region: this.belongsTo(WmoRegion,'wmo_region_id'),
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

