import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def imports():
    import marimo as mo
    from paragradio.v2025_03 import SpecAn
    mo.md("# Spectrum Analyzer")
    return SpecAn, mo


@app.cell
def launch(SpecAn, bbg, cfslider, hwbbfiltsw, ifg, oswitch, sr):
    hwbbfilt = 28e6
    if hwbbfiltsw.value == True:
        hwbbfilt = 1.75e6

    SpecAn.config(running=oswitch.value,
                 center_freq=cfslider.value * 1e6,
                 if_gain=ifg.value,
                 bb_gain=bbg.value,
                 samp_rate=sr.value * 1e6,
                 hw_bb_filt=hwbbfilt)
    return (hwbbfilt,)


@app.cell
def create_ui(mo):
    cfslider = mo.ui.slider(1, 6000, 1, 2000, orientation="vertical", label="Freq MHz", show_value=True)
    ifg = mo.ui.slider(0,40,8,24, label="IF Gain", show_value=True, orientation="vertical")
    bbg = mo.ui.slider(0, 62, 2, 40, label="BB Gain", show_value=True, orientation="vertical")
    sr = mo.ui.slider(2, 20, 1, 20, label="SR Msps", show_value=True, orientation="vertical")
    oswitch = mo.ui.switch(label="Power Off/On")
    hwbbfiltsw = mo.ui.switch(label="HW BB Filter Off/On")
    title = mo.md("## Specan Controls")
    return bbg, cfslider, hwbbfiltsw, ifg, oswitch, sr, title


@app.cell
def render_ui(bbg, cfslider, hwbbfiltsw, ifg, mo, oswitch, sr, title):
    oao = mo.vstack([oswitch, hwbbfiltsw])
    sbs = mo.hstack([cfslider, sr, ifg, bbg, oao], justify='start')
    wcc = mo.vstack([title, sbs])
    wcc
    return oao, sbs, wcc


@app.cell
def documentation(SpecAn, mo):
    mo.md(SpecAn.config.__doc__)
    return


if __name__ == "__main__":
    app.run()
