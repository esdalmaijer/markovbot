# -*- coding: utf-8 -*-
#
# For installation instructions and more information, please refer to:
# http://www.pygaze.org/2016/03/tutorial-creating-a-twitterbot/
# (This includes instructions to install the Twitter library used here)
#
# This file is part of markovbot, created by Edwin Dalmaijer
# GitHub: https://github.com/esdalmaijer/markovbot
#
# Markovbot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# Markovbot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with markovbot.  If not, see <http://www.gnu.org/licenses/>.

import sys

# Check what version we're currently running, and import the corresponding
# MarkovBot class.
if sys.version_info[0] == 3:
    try:
        from markovbot35 import MarkovBot
    except:
        from markovbot.markovbot35 import MarkovBot
else:
    try:
        from markovbot27 import MarkovBot
    except:
        from markovbot.markovbot27 import MarkovBot
