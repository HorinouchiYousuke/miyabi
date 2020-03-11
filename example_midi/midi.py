# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:49:50 2020

@author: yhori
"""

#import os
import pretty_midi

#original_path = os.path.normpath('C:\Users\yhori\Documents\HamakawaLab\Miyabi\Programing\miyanomiya\プリプロ\Dataset\3つの新しいエチュード\1-1\120\original.mid')
#practice_path = os.path.normpath('C:\Users\yhori\Documents\HamakawaLab\Miyabi\Programing\miyanomiya\プリプロ\Dataset\3つの新しいエチュード\1-1\120\practice.mid')

original_data = pretty_midi.PrettyMIDI('original.mid')
practice_data = pretty_midi.PrettyMIDI('practice.mid')

with open('original_piano_roll.txt', 'w') as f:
    f.write(str(original_data.get_piano_roll()))
with open('practice_piano_roll.txt', 'w') as f:
    f.write(str(practice_data.get_piano_roll()))
#print(original_data.get_piano_roll())
#print(practice_data.get_piano_roll())
with open('original_synthesize.txt', 'w')as f:
    f.write(str(original_data.synthesize()))
with open('practice_synthesize.txt', 'w')as f:
    f.write(str(practice_data.synthesize()))
#print(original_data.synthesize())
#print(practice_data.synthesize())
