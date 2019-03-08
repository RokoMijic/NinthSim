from src.main.engine.data.statlinegeneral import StatlineGeneral
from src.main.engine.data.modelpart import ModelPart
from src.main.engine.constants import GENERAL_AND_DEFENSIVE_SPECIAL_RULES

from typing import List

class Model(StatlineGeneral):

    def __init__(self, modelname, gendefstatvalues, gendefspecialrules, modelparts: List[ModelPart]):

        StatlineGeneral.__init__(self,gendefstatvalues)

        if not set(gendefspecialrules) <= set(GENERAL_AND_DEFENSIVE_SPECIAL_RULES):
            raise ValueError("At least one provided special rule is not valid: %s" % gendefspecialrules)

        self.modelname = str(modelname)
        self.specialrules = gendefspecialrules
        self.modelparts = modelparts

    def __repr__(self):
        return "\n" + str(self.modelname) + "\n" + StatlineGeneral.__repr__(self) + "  |  " + ", ".join(self.specialrules) + "\n" +  "\n".join( [str(mp) for mp in self.modelparts ] )

