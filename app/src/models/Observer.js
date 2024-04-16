import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import ControlSchedule from '@/models/ControlSchedule';
import User from '@/models/User';
import Status from '@/models/Status';

export default class Observer extends Model {
  static entity = 'observer';
  static fields() {
    return {
      id: this.string(''),
      name: this.string(''),
      description: this.string(''),
      links: this.attr(new LinksType([])),
      location: this.string(''),
      elevation: this.number(null),
      manufacturer: this.string(''),
      model: this.string(''),
      serial_number: this.string(''),
      firmware_version: this.string(''),
      control_schedule_id: this.string(''),
      control_schedule: this.belongsTo(ControlSchedule,'control_schedule_id'),
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

