import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class Record extends Model {
  static entity = 'record';
  static fields() {
    return {
      id: this.string(''),
      time: this.string(''),
      title: this.string(''),
      location: this.string(''),
      created: this.string(''),
      updated: this.string(''),
      resource_type: this.string(''),
      description: this.string(''),
      keywords: this.string(''),
      language: this.string(''),
      external_ids: this.attr(null),
      themes: this.attr(null),
      formats: this.attr(null),
      providers: this.attr(null),
      license: this.string(''),
      rights: this.string(''),
      links: this.attr(new LinksType([]))
    };
  };
};

