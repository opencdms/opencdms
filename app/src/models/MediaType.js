import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class MediaType extends Model {
  static entity = 'media_type';
  static fields() {
    return {
      id: this.string(''),
      name: this.string(''),
      description: this.string('')
    };
  };
};

