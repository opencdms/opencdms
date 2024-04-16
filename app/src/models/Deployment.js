import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import Host from '@/models/Host';
import Observer from '@/models/Observer';
import ReferenceSurface from '@/models/ReferenceSurface';
import Exposure from '@/models/Exposure';
import MaintenanceSchedule from '@/models/MaintenanceSchedule';
import User from '@/models/User';
import Status from '@/models/Status';

export default class Deployment extends Model {
  static entity = 'deployment';
  static fields() {
    return {
      id: this.string(''),
      host_id: this.string(''),
      host: this.belongsTo(Host,'host_id'),
      observer_id: this.string(''),
      observer: this.belongsTo(Observer,'observer_id'),
      valid_from: this.string(''),
      valid_to: this.string(''),
      installation_height: this.number(null),
      reference_surface_id: this.string(''),
      reference_surface: this.belongsTo(ReferenceSurface,'reference_surface_id'),
      exposure_id: this.string(''),
      exposure: this.belongsTo(Exposure,'exposure_id'),
      configuration: this.string(''),
      maintenance_schedule_id: this.string(''),
      maintenance_schedule: this.belongsTo(MaintenanceSchedule,'maintenance_schedule_id'),
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

