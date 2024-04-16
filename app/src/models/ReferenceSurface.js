import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class ReferenceSurface extends Model {
  static entity = 'reference_surface';
  static fields() {
    return {
      id: this.string(''),
      name: this.string(''),
      description: this.string('')
    };
  };
};

