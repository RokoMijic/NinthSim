from enum import unique, Enum

class Size(Enum):
    small = 'small'
    medium = 'medium'
    big = 'big'


# game-related constants

# allowed stats and their groupings

GENERAL_STAT_NAMES = ["Adv", "Mar", "Dis"]
DEFENSIVE_STAT_NAMES = ["HP", "Def", "Res", "Arm"]
OFFENSIVE_STAT_NAMES = [ "Att", "Off", "Str", "AP", "Agi" ]



GENERAL_AND_DEFENSIVE_STAT_NAMES = GENERAL_STAT_NAMES + DEFENSIVE_STAT_NAMES
ALL_STAT_NAMES = GENERAL_STAT_NAMES + DEFENSIVE_STAT_NAMES + OFFENSIVE_STAT_NAMES

# allowed facings

from enum import Enum

@unique
class FACING(Enum):
    FRONT = 'FRONT'
    FLANK = 'FLANK'
    REAR = 'REAR'

# allowed types

@unique
class MODEL_TYPE(Enum):
    INFANTRY = 'INFANTRY'
    CAVALRY = 'CAVALRY'
    BEAST = 'BEAST'
    CHARIOT = 'CHARIOT'

# allowed sizes

@unique
class MODEL_SIZE(Enum):
    STANDARD = 'STANDARD'
    LARGE = 'LARGE'
    GIGANTIC = 'GIGANTIC'


#     Number of allowed supporting attacks

ALLOWED_SUPPORTING_ATTACKS = {MODEL_SIZE.STANDARD: 1, MODEL_SIZE.LARGE: 3, MODEL_SIZE.GIGANTIC: 4}




# allowed special rules

GENERAL_SPECIAL_RULES = ["FEAR", "FEARLESS", "UNBREAKABLE"]
DEFENSIVE_SPECIAL_RULES = ["FORTITUDE", "AEGIS", "DISTRACTING", "PARRY", "HARD_TARGET"]
OFFENSIVE_SPECIAL_RULES = ["HATRED", "POISON", "LETHALSTRIKE" , "LIGHTNING_REFLEXES", "FIER", "HARNESSED"]

GENERAL_AND_DEFENSIVE_SPECIAL_RULES = GENERAL_SPECIAL_RULES + DEFENSIVE_SPECIAL_RULES
ALL_SPECIAL_RULES = GENERAL_SPECIAL_RULES + DEFENSIVE_SPECIAL_RULES + OFFENSIVE_SPECIAL_RULES

# tables for hitting and wounding

TO_HIT_TABLE =   { -10: 1, -9: 1, -8: 1, -7: 2, -6: 2, -5: 2, -4: 2, -3: 3, -2: 3, -1: 3,
                       0: 3, 1: 4, 2: 4, 3: 4, 4: 5, 5: 5, 6: 5, 7: 5, 8: 5, 9: 5, 10: 5  }

TO_WOUND_TABLE = { -10: 1, -9: 1, -8: 1, -7: 1, -6: 1, -5: 1, -4: 1, -3: 1, -2: 1, -1: 2,
                       0: 3, 1: 4, 2: 5, 3: 5, 4: 5, 5: 5, 6: 5, 7: 5, 8: 5, 9: 5, 10: 5  }