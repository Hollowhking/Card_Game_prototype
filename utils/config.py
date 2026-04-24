class Config:
    #COLORS:
    BLACK  = (0,0,0)
    D_GREY = (5,5,5)
    GREY   = (96,96,96)
    L_GREY = (160,160,160)
    WHITE  = (255,255,255)
    RED    = (255,0,0)
    BLUE   = (0, 0, 255)
    #MetaVariables:
    window_width  = 1600
    window_height = 1200
    FPS           = 60
    scaling_val   = 5
    #Sizing Vars:
    base_tile_size = 16
    tile_size = base_tile_size * scaling_val

    #Size of map area:
    game_Map_Starting_Y  = tile_size
    game_Map_Area_Width  = 16
    game_Map_Area_Height = 10

    #Pathing Vars:
    tile_directory = "res/tiles"
    map_directory  = "res/Rooms"
    #Player config settings:

    # Game Values:
    num_tile_options = 10

    #DEBUG SETTINGS:
    logging_level = "INFO"
    highlightHoverTile = True

    #Clock Vars:
    Max_Turn_Timer   = 5
    enemy_Turn_Timer = 3
    movement_buffer_time_limit_seconds = 0.5

    move_action_dur = 0.01
    #=================