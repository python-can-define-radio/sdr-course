### Temporarily commenting out the guizero import until we actually make this
# from guizero import App, Text, PushButton, Picture, TextBox, Combo, Box, CheckBox, MenuBar, Window
import ipaddress
import tkinter as tk
import PIL

## header:  
##   data:image/png;base64,
IMAGE_DATA = "iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAMAAABHPGVmAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAB8lBMVEX////4+fe3wrBxhmJSa0BKZTdJZDb4+fihr5hPaTxHYjO2wa9IZDVwhWFHYzRQaj5IYzVSaz9cdUpddktRaz9KZDdIYzR6jmzL08jj5+Lk5+TK0sd5jWtof1j7+/35+vv5+ftmfVZGYjKYp473+Pn4+fqXpoyisJn6+/yhsJn3+fn6+/3M08mfrZegrphFYTFHYjRJZDd0iWahr5l1imf9/f/8/f6jsZr8/f/8/P76+vxGYjOMnYH29/f4+fuLnH/d4dzi5uGls5yhsJigr5fN1MmKnH5Qaz5DYC9pf1nl6eSQoYVEYTBDXy+frpZNaDq7xbbJ0cRRbD6Ak3Py8/Pu8O96jm17jm3u8e/x8/NXcEXQ182yvatLZjhMZzm0v62ZqI/3+PhlfFVmfVVlfFSxvKqBlHOQoIXn6udsgl1gd0/c4dpJZDVKZTart6PW3NRackhJZTbr7uv09fWKnH/z9fVxh2NRaz7Cy77ByrxQaj2Jmn309vZyh2Nac0iqt6Kkspv7/P3d4ttgeFD8/P/8/P2RoodqgVubqpJsglxWcETT2dBVbkJddkzl6eXl6OVVb0PR2M/7/P7R2M5rgVyerJXM1MlMaDhTbj5QazqmtJyYqI3l6uPj6OHu8e75+vyYp43m6eZTbUFPajxvhGC4wrCuH8EhAAAAAWJLR0QAiAUdSAAAAAlwSFlzAAAAYAAAAGAA8GtCzwAAAAd0SU1FB+cIFgcHNZ4qhnkAAARkSURBVGje7dr7d9NUHADwsHFvuxBCpG20U3dLbExq2EhJS9eEAoOhPMd76sYU8MFrAzZR3g9BGaJziPJ+g/6fJk3R3JTe9JHknGm/P7Q533Oaz829t7ff3Iai5nV0zgcQBBIQzO/smEdRkWgXHRBRZuiuaIRa0MUER1jBdC2gFrLBGgCwC6lFAfaVHXARFbhhKuEgwRsAtJE28j9AIEeIer7M3ghk31gcqxmL46w344kk+DffSnbXjOTb73CtI/y7yR6UqhmoJ7mEbxkR3kNpkRBp9L7QOiLJZESWfEAyXkjGH+QDQviGIKVmIL8QtLS3r0b0LkU+IUrvMpVVVdYMFQtWXdar+ITIfSrkVJXLZjkc4aDaJ/uGsNxyTcvxfE5z9pW2nGN9RFRVy68oCEJhheyIvKb6eSUm0l+UBEEq6sEhLJcrSFZ3SRlHFHK+dheb5QXBXAfNV2fw2bmHhNFdoQy8NYXz1hTOO9ct32dXGF/G4JeVUBbIEJZ68zceyTUD+fIbb6wsybqYTq+qnDWVTqcqh6vSaVGXS6uNlhEYXykV1iA0sHad9QUcXI/Q+kHraN3aAYTWFKQPP/IsIesoU40NGzeh0uYt5ZVk61BPz9DW8uGWzSW0aeMGw4cy1VS2bVfkHTvtc9FRRYnSdn7nDlnZvq2OirsOxNi1G+0Ztk/sRAD98Sfo012eI1IPwoyMyvreMViNwM8+1+XREe+9GW+E3bcfDRx4tQPjRAD7RRLt3+e9OeOJsAcGnCfCELsBX3oqXggc24t1CY5wI6O6/tWY19h7IfTwHrTbMbg4AoyvHZOiWaRqmroQbHo3i9AHS+jQYUdLXQigDx9CpYMel0JG+CNHdVEbdzTUjcBxTdSPHiHf0ZGQCQiPIf34CeedpxsB3InjOjo2CSeavRK6cwp9cxLriyoE0Ce/RVPfETuMhMBTp2X5zFlsVKsRePaMLJ8+RRp7EmKcO4+mLuBtrEYAfWEKnT9HWsIICHfR7O1Lk3gTX4PAyUvmyF0k7BnURuDE5e+LV6665o0h5fOSq9X81Ss//Hh5onaHEZD4NU0bds9NLmcWYO5G88Oadi3eEJKAdgCzymIhTGB5wKgqA6wjZ94slThQ+ViiDiTLGmwl1HKtZbAJLG8XYK68+ir7T56EJOD0dby0uj49Tsz/9No8EWFu/FzEK6vi6C/jjeeJCDfzK8I3T9BsjGs8T0Zi3Sn8Q6nu8skazLeRNtJG5gYya96wWSGK9ntqdoZrPE9EmJu/3cLvDW/9fpNpPE9EAPPHbSkTHRy6g9CdocFoRro9zTSTJyLl7aa79+4/UJQH9+/dFcpbUM3kSYhVCdIPHz1+IopPHj96SFdSDefJV2KGUOiXn6ZST+X+gtBKnogYz57bf8E8f2a0kici8EUsFpuZMV9ewFbyROTfv8pga3ki4nO0kTYy15H/znMroTzmE8oDSyE8etVBRaIv63g2oOmA9MtohKIiHX/Gg3wc7q8I9TdN+WzVXUDg+QAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAyMy0wOC0yMlQxMTowNzo1My0wNDowMO2vIKoAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMjMtMDgtMjJUMTE6MDc6NTMtMDQ6MDCc8pgWAAAAAElFTkSuQmCC"



def calculate():
    global boxContents
    
    try:
        net4 = ipaddress.ip_network(f'{Ip_Address.value}/{cidr.value}', strict=False)
    except ValueError as e:
        boxContents = [
            Text(box2, text=f"ValueError: That is not a valid Network ID"),
            Text(box2, text=f"with /{cidr.value} as the Subnet Mask"),
            Text(box2, text=f"{e}")
        ]     
        return
    
    hosts = 2**(32-int(cidr.value))
    image = tk.PhotoImage(data=IMAGE_DATA)
    boxContents = [
        Text(box2, f"Your Network ID is {net4[0]}"),
        Text(box2, f"Your Broadcast ID is {net4[-1]}"),
        Text(box2, f"Your Subnet Mask is {net4.netmask}"),
        Text(box2, f"You have {hosts-2} available IP addresses"),
        Text(box2, f"Your available host range is:"),
        Text(box2, f"{net4[1]} to"),
        Text(box2, f"{net4[-2]}"),
        Picture(box2, image=image, align="bottom", height=100, width=100),
        Box(app, height=10, width="fill"),
        Text(app, text="Happy Networking")
    ]
    
def reset():
    global boxContents
    for item in boxContents:
        item.destroy()
     
def ch_message():
    if checkbox.value == 1:
        enterNID.value ="Please enter any Host ID from your subnet in the box below."   
    else:
        enterNID.value ="Please enter a valid IPv4 Network ID in the box below."

def enable_calc():
    IP_Address_Length = ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
    if len(Ip_Address.value) in IP_Address_Length:
        button1.enable()
        button2.enable()
        cidr_message.show()
        cidr.show()
    else:
        button1.enable()
        button2.enable()
        cidr_message.show()
        cidr.show()

def edit_function():
    print("Edit option")

def popup():
    window = Window(app, height=500, width=500, title="About Me")
    window.bg = "yellow"
    Box(window, height=200, width="fill")
    Text(window, text="I'm me (who else would I be?)")

def readme():
    window = Window(app, height=250, width=600, title="Read Me")
    window.bg = "yellow"
    Text(window, text="The Checkbox is just for show\n"
        "the calculator is fully functional with any IP address\n"
        "regardless of whether you use the checkbox or not\n"
        "1) You must enter an IP Address to begin.\n"
        "2) Then select your 'slash notation' (CIDR).\n"
        "3) Thats the box with the red 8 on it.\n"
        "4) Finally click the calculate button.\n"
        "5) Reset and repeat as needed.")
    Text(window, text="NOTE: If you get an error be sure to hit reset to clear the window")


if __name__ == "__main__":
    app = App(title="Subnet Calculator")
    app.height = 750
    app.width = 1000
    app.text_color = "blue"
    app.text_size = 15
    app.bg = "aquamarine"
    Box(app, align="left", height="fill", width=20)
    Box(app, align="right", height="fill", width=20)
    Box(app, align="top", height=20, width="fill")
    Box(app, align="bottom", height=20, width="fill")

    menubar = MenuBar(app, toplevel=["File", "Edit", "About"],
                    options=[
                        [ ["Calculate", calculate], ["Reset", reset] ],
                        [ ["Just for looks", edit_function], ["I don't really do anything!", edit_function] ],
                        [ ["About the Author", popup], ["Read me", readme] ]
                    ])

    welcome = Text(app, text="Welcome to the IP Subnet Calculator app!")
    welcome.text_size = 26

    box1 = Box(app, width=900, height=200, border=False)
    Box(box1, align="left", height="fill", width=10)
    Box(box1, align="right", height="fill", width=10)
    Box(box1, align="top", height=10, width="fill")
    Box(box1, align="bottom", height=10, width="fill")

    enterNID = Text(box1, text="Please enter a valid IPv4 Network ID in the box below.")
    Ip_Address = TextBox(box1, width=14, command=enable_calc)
    Ip_Address.bg = "white"
    Ip_Address.text_color = "red"
    checkbox = CheckBox(box1, text="I don't know the Network ID let me use a host address!", command=ch_message)
    checkbox.text_size = 10
    Box(box1, height=10, width="fill")

    cidr_message = Text(box1, text="Please choose a CIDR value from the dropdown menu for your subnet.")
    cidr_message.hide()
    cidr = Combo(box1, options= list(range(8, 30+1)))
    cidr.bg = "white"
    cidr.text_color = "red"
    cidr.hide()
    Text(box1, text="")

    box2 = Box(app, width=900, height=400, border=True)
    box2.bg = "teal"
    box2.text_size = 22
    Box(box2, align="left", height="fill", width=10)
    Box(box2, align="right", height="fill", width=10)
    Box(box2, align="top", height=10, width="fill")
    Box(box2, align="bottom", height=10, width="fill")

    button1 = PushButton(box2, text="Calculate", command=calculate, enabled=False)
    button1.text_size = 12
    button1.text_color = "orange"
    button1.align = "left"
    button1.bg = "green"
    button2 = PushButton(box2,  text="  Reset  ", command=reset, enabled=False)
    button2.text_size = 12
    button2.text_color = "orange"
    button2.align = "right"
    button2.bg = "green"


    app.display()
    

