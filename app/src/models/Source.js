import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import SourceType from '@/models/SourceType';
import User from '@/models/User';
import Status from '@/models/Status';

export default class Source extends Model {
  static entity = 'source';
  static fields() {
    return {
      id: this.string(''),
      name: this.string(''),
      description: this.string(''),
      source_type_id: this.string(''),
      source_type: this.belongsTo(SourceType,'source_type_id'),
      links: this.attr(new LinksType([])),
      processor: this.string(''),
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

