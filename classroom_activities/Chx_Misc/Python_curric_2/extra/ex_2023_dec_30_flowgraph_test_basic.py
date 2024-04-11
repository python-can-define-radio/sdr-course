import numpy as np
from gnuradio import blocks, audio
import matplotlib.pyplot as plt
from pcdr._queue.sink import _QueuedSink
from pcdr._queue.source import _QueuedSource



if __name__ == "__main__":
    siz = 96000
    samp_rate = 48000
    qsink = _QueuedSink(blocks.wavfile_sink, np.float32, siz, ["testf.wav", 1, samp_rate, blocks.FORMAT_WAV, blocks.FORMAT_PCM_16])
    # qsink = QueuedSink(audio.sink, np.float32, siz, [samp_rate])

    timestamps = np.linspace(0, 2, 2*samp_rate, endpoint=False)
    print(timestamps)
    y = np.sin(1000 * 2 * np.pi * timestamps)
    qsink.put(y)
    y = np.sin(500 * 2 * np.pi * timestamps)
    qsink.put(y)
    plt.plot(timestamps[:200], y[:200], ".")
    plt.show()

    # chunk_size = 133
    # sour = QueuedSource(Blk_source_output_arb_num, np.float32, chunk_size)
    # sink = QueuedSink(Blk_sink_print, np.float32, chunk_size, sink_block_args=[100])
    # while True:
    #     piece = sour.get()
    #     sink.put(piece)
    
    
    # time.sleep(5)
    # sour.stop_and_wait()
    # sink.stop_and_wait()

    ##################
    ## Ex 2 

    # import pcdr.sources
    # import pcdr.demod
    # import pcdr.sinks

    # hackrf = pcdr.sources.HackRF()
    # demodulator = pcdr.demod.WBFM()
    # audioSink = pcdr.sinks.audio()

    # freq = 104.3e6
    # while True:
    #     data = hackrf.get()
    #     audio = demodulator.process(data)
    #     audioSink.play(audio)
    #     time.sleep(2)
    #     hackrf.set_freq()
    #     freq += 0.2e6
        



