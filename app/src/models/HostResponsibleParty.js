import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import ResponsibleParty from '@/models/ResponsibleParty';
import Role from '@/models/Role';
import Host from '@/models/Host';
import User from '@/models/User';
import Status from '@/models/Status';

export default class HostResponsibleParty extends Model {
  static entity = 'host_responsible_party';
  static fields() {
    return {
      id: this.string(''),
      responsible_party_id: this.string(''),
      responsible_party: this.belongsTo(ResponsibleParty,'responsible_party_id'),
      role_id: this.string(''),
      role: this.belongsTo(Role,'role_id'),
      host_id: this.string(''),
      host: this.belongsTo(Host,'host_id'),
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

