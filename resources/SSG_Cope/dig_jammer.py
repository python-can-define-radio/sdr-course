import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    from paragradio.v2025_03 import PSK_Tx_loop
    mo.md("# Digital Jammer")
    return PSK_Tx_loop, mo


@app.cell
def launch(PSK_Tx_loop, amp, cfsli, ifgdd, mod, oswitch, sr):
    PSK_Tx_loop.config(running=oswitch.value,
                       center_freq=cfsli.value*1e6,
                       data=[1, 0, 1, 1, 0, 1, 1, 0],
                       amplitude=int(amp.value),
                       samp_rate=sr.value*1e6,
                       if_gain=int(ifgdd.value),
                       modulation=mod.value
                      )
    return


@app.cell
def create_ui(mo):
    oswitch = mo.ui.switch(label="Off/On")
    cfsli = mo.ui.slider(1, 6000, 1, 2494, label="Center Frequency", show_value=True)
    mygaindd = [str(i) for i in range(0, 48, 1)]
    ifgdd = mo.ui.dropdown(mygaindd, label="IF Gain", value="47")
    myampdd = [str(i+1) for i in range(20)]
    amp = mo.ui.dropdown(myampdd, label="Amplitude", value="9")
    sr = mo.ui.slider(2, 20, 1, 20, label="Sample Rate", show_value=True)
    mod = mo.ui.dropdown(["BPSK", "QPSK", "DQPSK", "8PSK", "16QAM"], label="Modulation", value="BPSK")
    return amp, cfsli, ifgdd, mod, myampdd, mygaindd, oswitch, sr


@app.cell
def render_ui(amp, cfsli, ifgdd, mo, mod, oswitch, sr):
    mo.vstack([oswitch, mo.md(f"{cfsli}MHz"), mo.md(f"{sr}Msps"), mo.md(f"{ifgdd}dB"), mo.md(f"{amp}"),  mo.md(f"{mod}")], justify="start")
    return


@app.cell
def documentation(PSK_Tx_loop, mo):
    mo.md(PSK_Tx_loop.config.__doc__)
    return


if __name__ == "__main__":
    app.run()
