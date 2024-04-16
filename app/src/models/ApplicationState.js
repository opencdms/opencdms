import { Model } from 'pinia-orm'
export default class ApplicationState extends Model {
  static entity = 'applicationState';
  static primaryKey = 'key';
  static fields() {
    return {
      key: this.string(''),
      value: this.string('')
   }
  }
}
