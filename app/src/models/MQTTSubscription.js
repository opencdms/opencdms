import { Model } from 'pinia-orm'

export default class MQTTSubscription extends Model {
  static entity = 'mqtt_subscription' ;
  static fields(){
    return{
      id: this.string(''),
      topic: this.string(''), // topic we are subscribing to
      bucket: this.string(''), // where to put the data
      process: this.string(''), // process to use to process the data
      collection: this.string(''), // which collection to associate with this subscription
      subscribed: this.boolean(false) // current status of the process
    }
  }
}
