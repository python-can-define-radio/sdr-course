import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def imports():
    import marimo as mo
    from paragradio.v2025_03 import Noise_Tx
    mo.md("# Noise Jammer")
    return Noise_Tx, mo


@app.cell
def launch(Noise_Tx, amp, cfnum, fcfsli, ftwsli, ifgdd, oswitch, sr):
    Noise_Tx.config(running=oswitch.value,
                    amplitude=int(amp.value),
                    center_freq=cfnum.value*1e6,
                    noise_type="gaussian",
                    filter_cutoff_freq=fcfsli.value*1e3,
                    filter_transition_width=ftwsli.value*1e3,
                    samp_rate=sr.value*1e6,
                    if_gain=int(ifgdd.value)
                   )
    return


@app.cell
def create_ui(mo):
    oswitch = mo.ui.switch(label="Off/On")
    myampdd = [str(i+1) for i in range(50)]
    amp = mo.ui.dropdown(myampdd, label="Amplitude", value="1")
    cfnum = mo.ui.number(1, 6000, 1, 2494, label="Center Frequency")
    mygaindd = [str(i) for i in range(0, 48, 1)]
    ifgdd = mo.ui.dropdown(mygaindd, label="IF Gain", value="32")
    fcfsli = mo.ui.slider(2, 400, 1, 200, label="Filter Cutoff Frequency", show_value=True)
    ftwsli = mo.ui.slider(2, 400, 1, 200, label="Filter Transition Width", show_value=True)
    sr = mo.ui.slider(2, 20, 1, 20, label="Sample Rate", show_value=True)
    return amp, cfnum, fcfsli, ftwsli, ifgdd, myampdd, mygaindd, oswitch, sr


@app.cell
def render_ui(amp, cfnum, fcfsli, ftwsli, ifgdd, mo, oswitch, sr):
    mo.vstack([oswitch, mo.md(f"{cfnum}MHz"), amp, mo.md(f"{ifgdd}dB"), mo.md(f"{fcfsli}kHz"), mo.md(f"{ftwsli}kHz"), mo.md(f"{sr}Msps")], justify="start")
    return


@app.cell
def documentation(Noise_Tx, mo):
    mo.md(Noise_Tx.config.__doc__)
    return


if __name__ == "__main__":
    app.run()
