#!BPY

#"""
#Name: 'RailSim Bigex (.igs)...'
#Blender: 248
#Group: 'Export'
#Tooltip: 'Exports to Rail Sim intermediate geometry shape format (.igs)'
#"""
__author__  = ["HenningBR218"]
__url__     = ("www.blender.org",
               "www.railsimulator.com",
               "http://rail-sim.de/railsim/forumnew",
               "http://rail-sim.de/railsimnew",
               "http://forums.uktrainsim.com")
__version__ = "2.0.158 2010-04-21"
__bypdoc__  = """\

Exporter for Rail Sim IGS format files

Writes Rail Simulator IGS format files from Blender.

Comments, questions, suggestions for improvements?
Drop me a note: HenningBR218 ( a t ) b188 ( d o t ) de

"""
# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software: you can redistribute it and/or modify
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# ***** END GPL LICENCE BLOCK *****
# --------------------------------------------------------------------------

from sys import version

# Check Python version
if version.split()[0].split('.')[0] is '2' and \
   version.split()[0].split('.')[1] is '5':
  from bigex25 import InitGUI
elif version.split()[0].split('.')[0] is '2' and \
     version.split()[0].split('.')[1] is '6':
  from bigex26 import InitGUI
else:
  exit('\nError: Only Python versions 2.5 and 2.6 are supported currently!\n')

##### preset script default behavior values
### script behavior (script internal switches)
gFlags = {
'EXPORT_LOG'             :  1     , # 0: no export log
                                    # 1: write logfile '<igs file name>_exp.log'
                                    # Maximum log level depth is 42
'SCREENDUMPLEVEL'        :  1     , # Console/screen log level depth: 
                                    # 0: none, 1: header only, 
                                    # 2: more, 42: all
'LOGFILEDUMPLEVEL'       : 42     , # same for log file logging depth
'DUMP_OBJECT_OFFSET_LIST':  0       # 1: dump igs object address offset table 
                                    # 0: don't do that 
}

if __name__ == '__main__':
  InitGUI(gFlags)
