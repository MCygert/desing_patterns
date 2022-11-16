from bridge import AdvancedRemote, Tv

if __name__ == "__main__":
    remote = AdvancedRemote(Tv())
    remote.toggle_power()
