import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class MaintenanceSchedule extends Model {
  static entity = 'maintenance_schedule';
  static fields() {
    return {
      id: this.string(''),
      name: this.string(''),
      description: this.string('')
    };
  };
};

