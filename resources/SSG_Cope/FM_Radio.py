import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def imports():
    import marimo as mo
    from paragradio.v2025_03 import WBFM_Rx
    # from num2words import num2words
    mo.md("# FM Radio")
    return WBFM_Rx, mo


@app.cell
def launch(WBFM_Rx, bbg, cfnum, chw, freqoff, hwf, ifg, oswitch):
    WBFM_Rx.config(running=oswitch.value,
                  center_freq=cfnum.value*1e6,
                  if_gain=int(ifg.value),
                  bb_gain=bbg.value,
                  hw_bb_filt=hwf.value*1e6,
                  freq_offset=freqoff.value*1e3,
                  channel_width=int(chw.value)*1e3
                  )
    return


@app.cell
def create_ui(mo):
    oswitch = mo.ui.switch(label="Off/On")
    cfnum = mo.ui.number(87.9, 107.9, .200, 93.9, label="Center Frequency")
    myddlist = [str(i) for i in range(0, 48, 8)]
    mydddict = {str(num):num for num in range(0, 48, 8)}
    ifg = mo.ui.dropdown(mydddict, value = "32", label="IF Gain")
    bbg = mo.ui.slider(0, 62, 2, 40, label="BB Gain", show_value=True)
    hwf = mo.ui.slider(1.75, 28, 1, 1.75, label="Hw BB Filter", show_value=True)
    freqoff = mo.ui.number(0, 400, 100, 100, label="Frequency Offset")
    chw = mo.ui.radio(["120", "160", "200"], label="Channel Width in kHz", value="200")
    return bbg, cfnum, chw, freqoff, hwf, ifg, mydddict, myddlist, oswitch


@app.cell
def render_ui(bbg, cfnum, chw, freqoff, hwf, ifg, mo, oswitch):
    stack = mo.vstack([oswitch, mo.md(f"{cfnum}MHz"), mo.md(f"{ifg}dB"), mo.md(f"{bbg}dB"), mo.md(f"{hwf}MHz"), mo.md(f"{freqoff} kHz"), mo.md(f"{chw}")], justify="start")
    stack
    return (stack,)


@app.cell
def documentation(WBFM_Rx, mo):
    mo.md(WBFM_Rx.config.__doc__)
    return


if __name__ == "__main__":
    app.run()
