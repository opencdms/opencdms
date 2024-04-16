// import pinia and pinia-orm components
import { mapRepos } from 'pinia-orm';

// import models
import FacilityType from '@/models/FacilityType';
import WmoRegion from '@/models/WmoRegion';
import Territory from '@/models/Territory';
import TimeZone from '@/models/TimeZone';
import User from '@/models/User';
import Status from '@/models/Status';
import Host from '@/models/Host';

export default {
  name: 'cdm',
  computed: {
    ...mapRepos({
      facilityTypeRepo: FacilityType,
      wmoRegionRepo: WmoRegion,
      territoryRepo: Territory,
      timeZoneRepo: TimeZone,
      userRepo: User,
      statusRepo: Status,
      hostRepo: Host
    })
  },
  methods: {
  }
}
