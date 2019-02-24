"""
An example of using the wave function collapse with midi file.
It uses the mido library to load and export midi files
You should install mido using `pip install mido`
"""

import numpy as np
from mido import MidiFile, MidiTrack, Message, second2tick, MetaMessage
from mido.midifiles.midifiles import DEFAULT_TEMPO

from wfc import WaveFunctionCollapse

TEMPO = DEFAULT_TEMPO


def load_midi_sample(path):
    midi_file = MidiFile(path)
    notes = []
    time = 0.0
    prev_time = 0.0
    for msg in midi_file:
        time += msg.time
        if msg.is_meta:
            if msg.type == 'set_tempo':
                global TEMPO
                TEMPO = msg.tempo
        else:
            if msg.channel == 0:
                # TODO note_off
                if msg.type == 'note_on':
                    note = msg.bytes()
                    note.append(time - prev_time)
                    prev_time = time
                    notes.append(note)

    notes = np.array(notes)

    notes = np.expand_dims(notes, axis=0)
    notes = np.expand_dims(notes, axis=0)

    return notes, midi_file.ticks_per_beat


def export_midi(notes, path, ticks_per_beat):
    notes = np.squeeze(notes, axis=0)
    notes = np.squeeze(notes, axis=0)

    midi_file = MidiFile()
    midi_file.ticks_per_beat = ticks_per_beat
    track = MidiTrack()
    track.append(MetaMessage('set_tempo', tempo=TEMPO))
    midi_file.tracks.append(track)
    for note in notes:
        bytes = note.astype(int)
        msg = Message.from_bytes(bytes[0:3])
        time = int(second2tick(note[3], ticks_per_beat, TEMPO))
        msg.time = time
        track.append(msg)

    print(midi_file)
    midi_file.save(path)


if __name__ == '__main__':
    np.random.seed(42)

    grid_size = (1, 1, 100)
    pattern_size = (1, 1, 2)

    sample, ticks_per_beat = load_midi_sample('../samples/twinkle_twinkle.mid')

    print('sample shape:', sample.shape)

    wfc = WaveFunctionCollapse(grid_size, sample, pattern_size)
    wfc.run()

    notes = wfc.get_image()

    export_midi(notes, '../samples/output.mid', ticks_per_beat)
