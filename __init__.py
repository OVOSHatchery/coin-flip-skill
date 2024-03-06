# Copyright 2017 Willem Ligtenberg
#
# Coin flip skill is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Coin flip skill is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

import random
from os.path import join

from ovos_workshop.intents import IntentBuilder
from ovos_workshop.skills import OVOSSkill

__author__ = 'Willem Ligtenberg'


class CoinFlipSkill(OVOSSkill):

    def initialize(self):
        coin_flip_intent = IntentBuilder("CoinFlipIntent"). \
            require("CoinFlipKeyword").build()
        self.register_intent(coin_flip_intent, self.handle_coin_flip_intent)

    def handle_coin_flip_intent(self, message):
        # self.speak_dialog("flip.coin")
        self.play_audio(join(self.root_dir, "mp3", "coin-flip.mp3"))
        if bool(random.getrandbits(1)):
            self.speak_dialog("heads")
        else:
            self.speak_dialog("tails")
