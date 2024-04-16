import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import ClimateZone from '@/models/ClimateZone';
import SurfaceCover from '@/models/SurfaceCover';
import SurfaceRoughness from '@/models/SurfaceRoughness';
import Topography from '@/models/Topography';
import Season from '@/models/Season';
import User from '@/models/User';
import Status from '@/models/Status';

export default class HostEnvironment extends Model {
  static entity = 'host_environment';
  static fields() {
    return {
      id: this.string(''),
      host: this.string(''),
      climate_zone_id: this.string(''),
      climate_zone: this.belongsTo(ClimateZone,'climate_zone_id'),
      surface_cover_id: this.string(''),
      surface_cover: this.belongsTo(SurfaceCover,'surface_cover_id'),
      surface_roughness_id: this.string(''),
      surface_roughness: this.belongsTo(SurfaceRoughness,'surface_roughness_id'),
      topography_id: this.string(''),
      topography: this.belongsTo(Topography,'topography_id'),
      season_id: this.string(''),
      season: this.belongsTo(Season,'season_id'),
      valid_from: this.string(''),
      valid_to: this.string(''),
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

