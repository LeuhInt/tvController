class TvRemote:
    def __init__(self):
        self.power = False
        self.mute = False
        self.volume = 0
        self.channel = 0
        self.channelName = ''

    def powerOn(self):
        self.power = True

    def powerOff(self):
        self.power = False

    def muteOn(self):
        self.mute = True

    def muteOff(self):
        self.mute = False

    def raiseVolume(self):
        if self.volume < 100:
            self.volume += 1

    def lowerVolume(self):
        if self.volume > 0:
            self.volume -= 1

    def upperChannel(self):
        if self.channel < 9:
            self.channel += 1

    def lowerChannel(self):
        if self.channel > 0:
            self.channel -= 1

    def setChannel(self):
        channels = {
            0: 'Unavailable',
            1: 'SBT',
            2: 'GLOBO',
            3: 'RECORD',
            4: 'Prime Video',
            5: 'Netflix',
            6: 'HBO',
            7: 'GNT',
            8: 'Tv Cultura',
            9: 'BAND',
        }
        try:
            channel = int(input('Choice a Channel: '))
            if channel in channels:
                self.channel = channel
                self.channelName = channels[channel]
            else:
                print('Invalid Choice')
        except ValueError:
            print('Invalid input. Please enter an integer')

    def getInfo(self):
        if self.power == True:
            print("TV Info")
            print('-' * 30)
            print(f'Channel: {self.channel}')
            print(f'Channel Name: {self.channelName}')
            print(f'Volume: {self.volume}')
            print(f'Mute Mode: {self.mute}')
            print('-' * 30)


oTvRemote = TvRemote()
oTvRemote.powerOn()
# oTvRemote.getInfo()
oTvRemote.setChannel()
oTvRemote.raiseVolume()
# oTvRemote.lowerChannel()
oTvRemote.muteOn()
oTvRemote.getInfo()
