import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class ControlSchedule extends Model {
  static entity = 'control_schedule';
  static fields() {
    return {
      id: this.string(''),
      name: this.string(''),
      description: this.string('')
    };
  };
};

