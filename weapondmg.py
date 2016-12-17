#weapon dmg

def attackdmg(base=0, str=0, dex=0, skill=0, fight=0, slay=0, zerk=False, starving=False):

Damage = {[1d(Base damage * Stat modifier)-0.66] * Weapon skill modifier * Fighting modifier
         + Misc modifiers + Slaying bonuses}
         * Final multipliers  + Stabbing bonus - AC damage reduction
