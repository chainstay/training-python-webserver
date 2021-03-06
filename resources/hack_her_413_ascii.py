from asciimatics.effects import Cycle, Stars, Effect
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import StopApplication

def welcome_screen(screen):
    # create `effects` that asciimatics will display in the screen
    effects = [
        # main title
        Cycle(
            screen,
            FigletText("HackHer413", font='univers'),
            int(screen.height / 3 - 2)),
        # subtitle
        Cycle(
            screen,
            FigletText("I beelong", font='o8'),
            int(screen.height / 2)),
        # exit prompt
        Cycle(
            screen,
            FigletText("PRESS ANY KEY TO EXIT", font='digital'),
            int((screen.height / 2) * 1.5)),
        Stars(screen, 200),
        # allow exiting with a keypress
        StopOnKeypress(screen),
    ]
    screen.play(
        [Scene(effects, 500)],
    )


class StopOnKeypress(Effect):
    """
    Include this effect to allow the visualization to be stopped on any
    keypress, except for modifiers like `shift` and `ctl`
    """
    def _update(*args, **kwargs):
        pass

    def stop_frame(*args, **kwargs):
        pass

    def reset(*args, **kwargs):
        pass

    def update(*args, **kwargs):
        pass

    def process_event(event, *args, **kwargs):
        if event:
            raise StopApplication('The application was halted')
        return None


def main():
    try:
        # create ascii screen and show on terminal
        Screen.wrapper(welcome_screen)
    except KeyboardInterrupt:  # silence error reporting on cancellation
        pass
    print('\n\n')
    print('  AAA                                                     ')
    print(' AAAAA  ww      ww   eee   sss   oooo  mm mm mmmm    eee  ')
    print('AA   AA ww      ww ee   e s     oo  oo mmm  mm  mm ee   e ')
    print('AAAAAAA  ww ww ww  eeeee   sss  oo  oo mmm  mm  mm eeeee  ')
    print('AA   AA   ww  ww    eeeee     s  oooo  mmm  mm  mm  eeeee ')
    print('                           sss                            ')
    print('\n\n')
    print('Well done! You are ready to start running some Python code!')
    print('\n')


if __name__ == '__main__':
    main()
