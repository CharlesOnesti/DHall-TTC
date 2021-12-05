from particularagent import ParticularAgent
from rivercentralagent import RiverCentralAgent

seed = 1

riverEastHouses = ['dunster', 'leverett', 'mather']
riverCentralHouses = ['adams', 'lowell', 'quincy']
riverWestHouses = ['winthrop', 'kirkland', 'eliot']
allRiverHouses = ['dunster', 'leverett', 'mather', 'adams', 'lowell', 'quincy', 'winthrop', 'kirkland', 'eliot']
quadHouses = ['cabot', 'currier', 'pfoho']

test_params = {
  'adams': {
    'QuadAgent': 1,
    'ParticularAgent': {
      'dunster': 1,
    },
  },
  'currier': {
    'RiverCentralAgent': 1,
  },
  'dunster': {
    'ParticularAgent': {
      'adams': 1
    },
  }
}

test_params_3 = {
  'adams': {
    'QuadAgent': 2,
    'ParticularAgent': {
      'dunster': 1,
    },
  },
  'currier': {
    'RiverCentralAgent': 2,
  },
  'dunster': {
    'ParticularAgent': {
      'adams': 1
    }
  },
  'mather': {
    'QuadAgent': 1,
  }
}


agent_params = {
  'adams': {
    'QuadAgent': 5,
    'AllRiverAgent': 5,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3,
    },
    'DummyAgent': {
      'pfoho': 4,
    },
  },
  'dunster': {
    'QuadAgent': 5,
    'AllRiverAgent': 5,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3,
    },
    'DummyAgent': {
      'pfoho': 4,
    },
  },
  'cabot': {
    'QuadAgent': 5,
    'AllRiverAgent': 5,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3,
    },
    'DummyAgent': {
      'pfoho': 4,
    },
  },
  'currier': {
    'QuadAgent': 5,
    'AllRiverAgent': 5,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3,
    },
    'DummyAgent': {
      'pfoho': 4,
    },
  },
  'eliot': {
    'QuadAgent': 5,
    'AllRiverAgent': 5,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3,
    },
    'DummyAgent': {
      'pfoho': 4,
    },
  },
  'kirkland': {
    'QuadAgent': 5,
    'AllRiverAgent': 5,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3,
    },
    'DummyAgent': {
      'pfoho': 4,
    },
  },
  'leverett': {
    'QuadAgent': 5,
    'AllRiverAgent': 5,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3,
    },
    'DummyAgent': {
      'pfoho': 4,
    },
  },
  'lowell': {
    'QuadAgent': 5,
    'AllRiverAgent': 5,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3,
    },
    'DummyAgent': {
      'pfoho': 4,
    },
  },
  'mather': {
    'QuadAgent': 5,
    'AllRiverAgent': 5,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3,
    },
    'DummyAgent': {
      'pfoho': 4,
    },
  },
  'pfoho': {
    'QuadAgent': 5,
    'AllRiverAgent': 5,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3,
    },
    'DummyAgent': {
      'pfoho': 4,
    },
  },
  'quincy':  {
    'QuadAgent': 5,
    'AllRiverAgent': 5,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3,
    },
    'DummyAgent': {
      'pfoho': 4,
    },
  },
  'winthrop':  {
    'QuadAgent': 5,
    'AllRiverAgent': 5,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3,
    },
    'DummyAgent': {
      'pfoho': 4,
    },
  },
}

Weekday_Lunch = {
  'adams': {
    'QuadAgent': 10,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'ParticularAgent': {
      'dunster': 3, 'leverett': 3, 'mather': 3, 'lowell': 3, 'quincy': 3, 'winthrop': 3, 'kirkland': 3, 'eliot': 3,
    },
    'DummyAgent': {
      'pfoho': 100,
    },
  },
  'dunster': {
    'QuadAgent': 10,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'leverett': 3, 'mather': 3, 'adams': 3, 'lowell': 3, 'quincy': 3, 'winthrop': 3, 'kirkland': 3, 'eliot': 3,
    },
  },
  'cabot': {
    'AllRiverAgent': 50,
    'RiverEastAgent': 50,
    'RiverWestAgent': 50,
    'RiverCentralAgent': 100,
    'ParticularAgent': {
      'dunster': 3, 'leverett': 3, 'mather': 3, 'adams': 3, 'lowell': 3, 'quincy': 3, 'winthrop': 3, 'kirkland': 3, 'eliot': 3, 'currier': 3, 'pfoho': 3,
    },
  },
  'currier': {
    'AllRiverAgent': 50,
    'RiverEastAgent': 50,
    'RiverWestAgent': 50,
    'RiverCentralAgent': 100,
    'ParticularAgent': {
      'dunster': 3, 'leverett': 3, 'mather': 3, 'adams': 3, 'lowell': 3, 'quincy': 3, 'winthrop': 3, 'kirkland': 3, 'eliot': 3, 'cabot': 3, 'pfoho': 3,
    },
  },
  'eliot': {
    'QuadAgent': 5,
    'RiverEastAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3, 'leverett': 3, 'mather': 3, 'adams': 3, 'lowell': 3, 'quincy': 3, 'winthrop': 3, 'kirkland': 3,
    },
  },
  'kirkland': {
    'QuadAgent': 5,
    'AllRiverAgent': 5,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3, 'leverett': 3, 'mather': 3, 'adams': 3, 'lowell': 3, 'quincy': 3, 'winthrop': 3, 'eliot': 3,
    },
    'DummyAgent': {
      'pfoho': 4,
    },
  },
  'leverett': {
    'QuadAgent': 5,
    'AllRiverAgent': 5,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3, 'mather': 3, 'adams': 3, 'lowell': 3, 'quincy': 3, 'winthrop': 3, 'kirkland': 3, 'eliot': 3,
    },
    'DummyAgent': {
      'pfoho': 4,
    },
  },
  'lowell': {
    'QuadAgent': 10,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'ParticularAgent': {
      'dunster': 3, 'leverett': 3, 'mather': 3, 'adams': 3, 'quincy': 3, 'winthrop': 3, 'kirkland': 3, 'eliot': 3,
    },
    'DummyAgent': {
      'cabot': 100,
    },
  },
  'mather': {
    'QuadAgent': 10,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3, 'leverett': 3, 'adams': 3, 'lowell': 3, 'quincy': 3, 'winthrop': 3, 'kirkland': 3, 'eliot': 3,
    },
  },
  'pfoho': {
    'AllRiverAgent': 50,
    'RiverEastAgent': 50,
    'RiverWestAgent': 50,
    'RiverCentralAgent': 100,
    'ParticularAgent': {
      'dunster': 3, 'leverett': 3, 'mather': 3, 'adams': 3, 'lowell': 3, 'quincy': 3, 'winthrop': 3, 'kirkland': 3, 'eliot': 3, 'cabot': 3, 'currier': 3,
    },
  },
  'quincy':  {
    'QuadAgent': 10,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'ParticularAgent': {
      'dunster': 3, 'leverett': 3, 'mather': 3, 'adams': 3, 'lowell': 3, 'winthrop': 3, 'kirkland': 3, 'eliot': 3,
    },
    'DummyAgent': {
      'currier': 100,
    },
  },
  'winthrop':  {
    'QuadAgent': 10,
    'RiverEastAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 3, 'leverett': 3, 'mather': 3, 'adams': 3, 'lowell': 3, 'quincy': 3, 'kirkland': 3, 'eliot': 3,
    },
  },
}




Weekday_Dinner = {
  'adams': {
    'QuadAgent': 10,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'ParticularAgent': {
      'dunster': 10, 'leverett': 10, 'mather': 10, 'lowell': 10, 'quincy': 10, 'winthrop': 10, 'kirkland': 10, 'eliot': 10,
    },
    'DummyAgent': {
      'pfoho': 100,
    },
  },
  'dunster': {
    'QuadAgent': 10,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'leverett': 10, 'mather': 10, 'adams': 10, 'lowell': 10, 'quincy': 10, 'winthrop': 10, 'kirkland': 10, 'eliot': 10,
    },
  },
  'cabot': {
    'AllRiverAgent': 50,
    'RiverEastAgent': 50,
    'RiverWestAgent': 50,
    'RiverCentralAgent': 100,
    'ParticularAgent': {
      'dunster': 10, 'leverett': 10, 'mather': 10, 'adams': 10, 'lowell': 10, 'quincy': 10, 'winthrop': 10, 'kirkland': 10, 'eliot': 10, 'currier': 10, 'pfoho': 10,
    },
  },
  'currier': {
    'AllRiverAgent': 50,
    'RiverEastAgent': 50,
    'RiverWestAgent': 50,
    'RiverCentralAgent': 100,
    'ParticularAgent': {
      'dunster': 10, 'leverett': 10, 'mather': 10, 'adams': 10, 'lowell': 10, 'quincy': 10, 'winthrop': 10, 'kirkland': 10, 'eliot': 10, 'cabot': 10, 'pfoho': 10,
    },
  },
  'eliot': {
    'QuadAgent': 5,
    'RiverEastAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 10, 'leverett': 10, 'mather': 10, 'adams': 10, 'lowell': 10, 'quincy': 10, 'winthrop': 10, 'kirkland': 10,
    },
  },
  'kirkland': {
    'QuadAgent': 5,
    'AllRiverAgent': 5,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 10, 'leverett': 10, 'mather': 10, 'adams': 10, 'lowell': 10, 'quincy': 10, 'winthrop': 10, 'eliot': 10,
    },
    'DummyAgent': {
      'pfoho': 4,
    },
  },
  'leverett': {
    'QuadAgent': 5,
    'AllRiverAgent': 5,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 10, 'mather': 10, 'adams': 10, 'lowell': 10, 'quincy': 10, 'winthrop': 10, 'kirkland': 10, 'eliot': 10,
    },
    'DummyAgent': {
      'pfoho': 4,
    },
  },
  'lowell': {
    'QuadAgent': 10,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'ParticularAgent': {
      'dunster': 10, 'leverett': 10, 'mather': 10, 'adams': 10, 'quincy': 10, 'winthrop': 10, 'kirkland': 10, 'eliot': 10,
    },
    'DummyAgent': {
      'cabot': 100,
    },
  },
  'mather': {
    'QuadAgent': 10,
    'RiverWestAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 10, 'leverett': 10, 'adams': 10, 'lowell': 10, 'quincy': 10, 'winthrop': 10, 'kirkland': 10, 'eliot': 10,
    },
  },
  'pfoho': {
    'AllRiverAgent': 50,
    'RiverEastAgent': 50,
    'RiverWestAgent': 50,
    'RiverCentralAgent': 100,
    'ParticularAgent': {
      'dunster': 10, 'leverett': 10, 'mather': 10, 'adams': 10, 'lowell': 10, 'quincy': 10, 'winthrop': 10, 'kirkland': 10, 'eliot': 10, 'cabot': 10, 'currier': 10,
    },
  },
  'quincy':  {
    'QuadAgent': 10,
    'RiverEastAgent': 5,
    'RiverWestAgent': 5,
    'ParticularAgent': {
      'dunster': 10, 'leverett': 10, 'mather': 10, 'adams': 10, 'lowell': 10, 'winthrop': 10, 'kirkland': 10, 'eliot': 10,
    },
    'DummyAgent': {
      'currier': 100,
    },
  },
  'winthrop':  {
    'QuadAgent': 10,
    'RiverEastAgent': 5,
    'RiverCentralAgent': 5,
    'ParticularAgent': {
      'dunster': 10, 'leverett': 10, 'mather': 10, 'adams': 10, 'lowell': 10, 'quincy': 10, 'kirkland': 10, 'eliot': 10,
    },
  },
}