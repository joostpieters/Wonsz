import cx_Freeze

executables = [cx_Freeze.Executable("Snake.py")]

cx_Freeze.setup(
    neme="Snake",
    options={"build_exe":{"packages": ["pygame"], "include_files":["snakeHead.png","Snake-Pixel2.png"]}},
    description = "Snake Game",
    executables = executables
