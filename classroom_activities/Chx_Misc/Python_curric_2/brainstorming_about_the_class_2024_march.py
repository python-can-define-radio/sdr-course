from guizero import App, PushButton

app = App()
button = PushButton(app, text="jam")
app.display()



# import pcdr.simple
# import time
# receiver = osmocomReciever()
# receiver.set_frequency(50e6)
# receiver.record()
# time.sleep(3)
# receiver.stop_recording()
# receiver.save_recording("some_filename.complex")