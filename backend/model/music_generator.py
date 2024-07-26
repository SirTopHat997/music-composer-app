import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.protobuf import generator_pb2, music_pb2

def generate_music(user_id):
    # Load pre-trained model
    bundle = mm.sequence_generator_bundle.read_bundle_file('path_to_model/melody_rnn.mag')
    generator_map = melody_rnn_sequence_generator.get_generator_map()
    melody_rnn = generator_map['attention_rnn'](checkpoint=None, bundle=bundle)
    
    # Set up the generator
    melody_rnn.initialize()
    qpm = 120
    generator_options = generator_pb2.GeneratorOptions()
    generator_options.args['temperature'].float_value = 1.0
    generate_section = generator_options.generate_sections.add(start_time=0, end_time=32)
    
    # Generate a sequence
    sequence = melody_rnn.generate(music_pb2.NoteSequence(), generator_options)
    
    # Save as MIDI file
    midi_path = f'generated_music/{user_id}.mid'
    mm.sequence_proto_to_midi_file(sequence, midi_path)
    return midi_path
