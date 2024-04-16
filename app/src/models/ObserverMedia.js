import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import Observer from '@/models/Observer';
import Media from '@/models/Media';
import User from '@/models/User';
import Status from '@/models/Status';

export default class ObserverMedia extends Model {
  static entity = 'observer_media';
  static fields() {
    return {
      id: this.string(''),
      observer_id: this.string(''),
      observer: this.belongsTo(Observer,'observer_id'),
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

