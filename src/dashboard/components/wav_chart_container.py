from helpers.spectrogram_plot import draw_spectrogram
from helpers.waveform_plot import draw_waveform
from helpers.rms_plot import draw_rms
from helpers.mel_spectrogram_plot import draw_mel_spectrogram
from helpers.mfcc_plot import draw_mfcc
from helpers.stft_plot import draw_stft
from helpers.fft_plot import draw_fft

def draw_chart(y, sr, chart_selection):
    match(chart_selection):
        case 'None':
            pass
        case 'RMS':
            draw_rms(y)
        case 'Waveform':
            draw_waveform(y, sr)
        case 'Spectrogram':
            draw_spectrogram(y, sr)
        case 'Mel-Spectrogram':
            draw_mel_spectrogram(y, sr)
        case 'MFCC':
            draw_mfcc(y, sr)
        case 'STFT':
            draw_stft(y, sr)
        case 'FFT':
            draw_fft(y, sr)
