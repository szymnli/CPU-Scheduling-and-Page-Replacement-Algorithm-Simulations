class FIFO:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = []
        self.page_faults = 0

    def run(self, reference_string):
        self.frames = []
        self.page_faults = 0
        queue = []

        for page in reference_string:
            if page not in self.frames:
                self.page_faults += 1
                if len(self.frames) < self.num_frames:
                    self.frames.append(page)
                    queue.append(page)
                else:
                    # Usuwanie najstarszej strony
                    oldest = queue.pop(0)
                    self.frames.remove(oldest)
                    self.frames.append(page)
                    queue.append(page)
        return self.page_faults
