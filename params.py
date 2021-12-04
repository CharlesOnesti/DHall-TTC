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