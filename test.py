# from curses import window
import moderngl_window as  mglw

class App(mglw.WindowConfig):
    window_size = 600, 600
    resource_dir = '.'
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.quad = mglw.geometry.quad_fs()
        self.prog = self.load_program(vertex_shader='vertex.glsl', fragment_shader='fragment.glsl' )
    def render(self, time, frame_time):
        self.ctx.clear()
        self.quad.render(self.prog)


if __name__ == "__main__":
    mglw.run_window_config(App)