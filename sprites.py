from functions.iterate_sprites_function import *
from constants import *
from variables import *
from rects import *

#Sprite Crates
path_crate = "sprites/crate_"
iterate_sprites(10, path_crate, crate_states, crate_width, crate_height)

#Sprite Locks
path_lock = "sprites/lock_"
iterate_sprites(3, path_lock, lock_states, lock_width, lock_height)