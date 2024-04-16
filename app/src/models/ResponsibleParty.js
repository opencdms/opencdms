import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class ResponsibleParty extends Model {
  static entity = 'responsible_party';
  static fields() {
    return {
      id: this.string(''),
      name: this.string(''),
      position_name: this.string(''),
      organization: this.string(''),
      logo: this.attr(null),
      contact_information: this.attr(null)
    };
  };
};

