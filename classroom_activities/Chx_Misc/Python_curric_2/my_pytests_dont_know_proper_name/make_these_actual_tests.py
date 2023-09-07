"""This demonstrates a few functions. We may turn it into an exercise."""
from pcdr import gnuradio_write_file, makeComplexWave_time, createTimestamps_samprate

if __name__ == "__main__":
    tot_time = 0.5
    timestamps, wave = makeComplexWave_time(tot_time, 1000, 200)
    gnuradio_write_file(wave, "samprate_2e6_basic_wave.complex", chunk_size=2)

    from pcdr import gnuradio_read_file
    import matplotlib.pyplot as plt

    dat = gnuradio_read_file("samprate_2e6_basic_wave.complex", chunk_size=2)
    timestamps = createTimestamps_samprate(len(dat))
    plt.plot(timestamps, dat.real, "bo-")
    plt.plot(timestamps, dat.imag, "ro-")
    plt.show()
