import numpy as np
from mido import MidiFile, MidiTrack, Message, second2tick
from mido.midifiles.midifiles import DEFAULT_TEMPO, DEFAULT_TICKS_PER_BEAT

from wfc import WaveFunctionCollapse


def load_midi_sample(path):
    midi_file = MidiFile(path)
    notes = []
    time = 0.0
    prev_time = 0.0
    for msg in midi_file:
        time += msg.time
        if not msg.is_meta:
            if msg.channel == 0 or True:
                if msg.type == 'note_on':
                    note = msg.bytes()
                    note.append(time - prev_time)
                    prev_time = time
                    notes.append(note)

    notes = np.array(notes)

    notes = np.expand_dims(notes, axis=0)
    notes = np.expand_dims(notes, axis=0)
    return notes


def export_midi(notes, path):
    notes = np.squeeze(notes, axis=0)
    notes = np.squeeze(notes, axis=0)

    midi_file = MidiFile()
    track = MidiTrack()
    midi_file.tracks.append(track)
    for note in notes:
        bytes = note.astype(int)
        msg = Message.from_bytes(bytes[0:3])
        time = int(second2tick(note[3], DEFAULT_TICKS_PER_BEAT, DEFAULT_TEMPO))
        msg.time = time
        track.append(msg)

    midi_file.save(path)


if __name__ == '__main__':
    np.random.seed(42)

    grid_size = (1, 1, 100)
    pattern_size = (1, 1, 2)

    sample = load_midi_sample('../samples/twinkle_twinkle.mid')
    print('sample shape:', sample.shape)

    wfc = WaveFunctionCollapse(grid_size, sample, pattern_size)
    wfc.run()

    notes = wfc.get_image()

    export_midi(notes, '../samples/output.mid')
