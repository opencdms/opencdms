import { mapRepos } from 'pinia-orm';

import FacilityType from '@/models/FacilityType';
import WmoRegion from '@/models/WmoRegion';
import Territory from '@/models/Territory';
import TimeZone from '@/models/TimeZone';
import User from '@/models/User';
import Status from '@/models/Status';

export default {
  computed: {
    ...mapRepos({
      facilityType: FacilityType
    })
  },
  mounted () {
  }
}
