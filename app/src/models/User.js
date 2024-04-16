import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

const LATEST = "tag:beta.opencdms.org,2023:/vocab/status/draft";

export default class User extends Model {
  static entity = 'user';
  static fields() {
    return {
      id: this.string(''),
      name: this.string(''),
      description: this.string('')
    };
  };
};

