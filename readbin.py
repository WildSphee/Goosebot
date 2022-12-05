# ‘52’, ‘49’, ‘46’, ‘46’, ‘14’, ‘60’, ‘28’, ‘00’, ‘57’, ‘41’, ‘56’, ‘45’, ‘66’, ‘6D’, ‘74’, ‘20
# 10’, ‘00’, ‘00’, ‘00’, ‘01’, ‘00’, ‘01’, ‘00’, ‘22’, ‘56’, ‘00’, ‘00’, ‘44’, ‘AC’, ‘00’, ‘00
# 02’, ‘00’, ‘10’, ‘00’, ‘64’, ‘61’, ‘74’, ‘61’, ‘F0’, ‘5F’, ‘28’, ‘00’


def ogg2wav(ofn):
    wfn = ofn.replace('.ogg','.wav')
    x = AudioSegment.from_file(ofn)
    x.export(wfn, format='wav')    # maybe use original resolution to make smaller
