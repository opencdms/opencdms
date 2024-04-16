import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import Host from '@/models/Host';
import Programme from '@/models/Programme';
import User from '@/models/User';
import Status from '@/models/Status';

export default class HostAffiliation extends Model {
  static entity = 'host_affiliation';
  static fields() {
    return {
      id: this.string(''),
      host_id: this.string(''),
      host: this.belongsTo(Host,'host_id'),
      programme_id: this.string(''),
      programme: this.belongsTo(Programme,'programme_id'),
      valid_from: this.string(''),
      valid_to: this.string(''),
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

