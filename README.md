# Game Audio Directory Manager (Work In Progress)

This tools works with the host computers file system and the Wwise Authoring API.
 
It allows an audio designer to quickly move files from the DAW to an Audio Directory, into Wwise, and finally into Unreal. All while generating the appropriate file directories along the way. This way, they only have to type the filename once, and never have to create a folder or Wwise container, when used appropriately. 

It works by parsing a filename (e.g. ply_fts_grass_walk_1.wav) into a list of strings and compares that against a dictionary of abbreviations (of popular audio terminology i.e. Foley, impact, weapon, whoosh, footstep, engine, etc.). 
It then creates those folders (i.e. /Player/Footsteps/Grass/Walk/) under a given parent folder, copies the files into the lowest sub-folder, and spits out a change list of everything that was modified as a .yaml file. 
When importing to Wwise, it reads the change list, imports the files, and creates appropriate containers if specified

Will include more options for Wwise containers in the future.
