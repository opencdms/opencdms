import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class Status extends Model {
  static entity = 'status';
  static fields() {
    return {
      id: this.string(''),
      name: this.string(''),
      description: this.string('')
    };
  };
};

