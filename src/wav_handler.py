import os
import soundfile as sf
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
from functools import partial
import wavpreprocess

def process_audio_file(row_dict, input_root_dir, output_root_dir):
    try:
        audio_filename = row_dict['audio_filename']
        input_file_path = os.path.join(input_root_dir, audio_filename)
        output_dir = os.path.join(output_root_dir, os.path.splitext(audio_filename)[0])
        os.makedirs(output_dir, exist_ok=True)

        segments = wavpreprocess.split_wav_into_segments(input_file_path)
        print(f"Processed {audio_filename}")
        for i, (segment, sr) in enumerate(segments):
            segment_filename = os.path.join(output_dir, f"segment_{i + 1}.wav")
            sf.write(segment_filename, segment, sr)
    except Exception as e:
        print(f"Error processing {row_dict['audio_filename']}: {e}")

def main():
    df = pd.read_csv('data/processed/maestro-v3.0.0_filtered.csv')
    input_root_dir = 'data/maestro-v3.0.0'
    output_root_dir = 'data/wav_processed'
    rows = [row.to_dict() for _, row in df.iterrows()]
    with ProcessPoolExecutor() as executor:
        process_func = partial(process_audio_file, input_root_dir=input_root_dir, output_root_dir=output_root_dir)
        executor.map(process_func, rows)

if __name__ == '__main__':
    main()
