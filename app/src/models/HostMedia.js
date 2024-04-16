import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import Host from '@/models/Host';
import Media from '@/models/Media';
import User from '@/models/User';
import Status from '@/models/Status';

export default class HostMedia extends Model {
  static entity = 'host_media';
  static fields() {
    return {
      id: this.string(''),
      host_id: this.string(''),
      host: this.belongsTo(Host,'host_id'),
      media_id: this.string(''),
      media: this.belongsTo(Media,'media_id'),
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

