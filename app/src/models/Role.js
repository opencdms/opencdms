import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class Role extends Model {
  static entity = 'role';
  static fields() {
    return {
      id: this.string(''),
      authority: this.string(''),
      name: this.string(''),
      description: this.string('')
    };
  };
};

