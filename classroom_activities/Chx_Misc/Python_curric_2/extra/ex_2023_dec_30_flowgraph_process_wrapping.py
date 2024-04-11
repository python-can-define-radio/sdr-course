import numpy as np
# import pcdr.queue.sink 



if __name__ == "__main__":
    # wav file source -> fm modulate -> file sink
    # audio_samp_rate = 48_000
    modulated_samp_rate = 480_000
    # audio_chunk_size = 4_800
    modulated_chunk_size = 480_000
    # wavsource = QueuedSource(blocks.wavfile_source, np.float32, audio_chunk_size, ["testf.wav", False])

    # mod = functionalize_proc_blk(analog.wfm_tx, np.float32, np.complex64,
                                #  in_chunk_size=audio_chunk_size, out_chunk_size=modulated_chunk_size,
                                #  proc_blk_args=[audio_samp_rate, modulated_samp_rate])
    file_sink = pcdr.queue.sink.file_sink(modulated_chunk_size, np.complex64, "somecomplexfile.complex", unbuffered=True)

    timestamps = np.linspace(0, 1, 100_000, endpoint=False)
    print(timestamps)
    y = 0.1 * (
        np.random.normal(size=modulated_samp_rate) + 
        np.random.normal(size=modulated_samp_rate) * 1j
    )
    y[0:100_000] = np.exp(40_000 * 2 * np.pi * timestamps * 1j)
    # (np.exp(40_000 * 2 * np.pi * timestamps * 1j) + 
    #     np.exp(50_000 * 2 * np.pi * timestamps * 1j) +
    #     np.exp(30_000 * 2 * np.pi * timestamps * 1j) +
    #     np.exp(20_000 * 2 * np.pi * timestamps * 1j) 
    # ) + 
    file_sink.put(y)
    # y = 
    # file_sink.put(y)
    # y = 
    # file_sink.put(y)
    # y = 
    # file_sink.put(y)
    print("no sleep")
    file_sink.stop_and_wait()
    # for x in range(10):
    #     audio_data = wavsource.get()
    #     modulated = mod(audio_data)
    #     file_sink.put(modulated)


