import pygame as pg

class Timer:
    def __init__(self, frames, wait=100, frameindex=0, step=1, loop=False):
        self.frames = frames
        self.wait = wait
        self.frameindex = frameindex
        self.step = step
        self.loop = loop

        self.finished = False
        self.lastframe = frames if step == 1 else 0
        self.last = None

    def frame_index(self):
        current = pg.time.get_ticks()
        if self.last is None:
            self.last = current
            self.frameindex = 0 if self.step == 1 else len(self.frames) - 1
            return 0 
        elif not self.finished and current - self.last > self.wait:
            self.frameindex += self.step
            if self.loop and self.frameindex == self.lastframe:
                self.finished = True
            else:
                self.frameindex %= self.frames
            self.last = current
        return self.frameindex
    
    def reset(self):
        self.last = None
        self.finished = False
    
    def __repr__(self):
        return 'Timer(frames={}, wait={}, index={})'.format(self.frames,
                                                            str(self.wait),
                                                            str(self.frameindex))
    
    def image_rect(self):
        return self.frames[self.frame_index()]
    
class DualTimer:
    def __init__(self, frames1, frames2, wait1=100, wait2=100, wait_switch_timers=1000,
                frameindex1=0, frameindex2=0, step1=1, step2=1, loop=False):

        self.wait_switch_timers = wait_switch_timers
        self.timer1 = Timer(frames1, wait1, frameindex1, step1, loop)
        self.timer2 = Timer(frames2, wait2, frameindex2, step2, loop)
        self.timer = self.timer1   

        self.current = pg.time.get_ticks()
        self.lastswitch = self.current

    def frame_index(self):
        current = pg.time.get_ticks()
        if current - self.lastswitch > self.wait_switch_timers:
            self.timer = self.timer2 if self.timer == self.timer1 else self.timer1
            self.lastswitch = current
        return self.timer.frame_index()

    def reset(self):
        self.timer1.reset()
        self.timer2.reset()
        self.timer = self.timer1

    def __str__(self): return 'DualTimer(' + str(self.timer1) + ',' + str(self.timer2) + ')'

    def imagerect(self):
        dualTimerImg = self.frame_index()
        return self.timer.frames[dualTimerImg]