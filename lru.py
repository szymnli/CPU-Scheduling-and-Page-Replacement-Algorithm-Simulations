class LRU:
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.frames = []
        self.page_faults = 0

    def run(self, reference_string):
        self.frames = []
        self.page_faults = 0
        recently_used = []

        for page in reference_string:
            if page not in self.frames:
                self.page_faults += 1
                if len(self.frames) < self.num_frames:
                    self.frames.append(page)
                else:
                    # Usunięcie najdawniej używanej strony
                    lru_page = recently_used.pop(0)
                    self.frames.remove(lru_page)
                    self.frames.append(page)
            else:
                recently_used.remove(page)
            recently_used.append(page)
        return self.page_faults

    def get_stats(self):
        return {
            "page_faults": self.page_faults
        }