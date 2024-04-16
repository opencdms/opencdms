import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import MediaType from '@/models/MediaType';

export default class Media extends Model {
  static entity = 'media';
  static fields() {
    return {
      id: this.string(''),
      media_type_id: this.string(''),
      media_type: this.belongsTo(MediaType,'media_type_id'),
      description: this.string(''),
      created: this.string(''),
      creator: this.string(''),
      rights: this.number(null),
      source: this.string(''),
      data: this.attr(null)
    };
  };
};

