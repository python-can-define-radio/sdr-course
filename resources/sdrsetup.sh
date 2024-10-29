#!/bin/bash
echo "Enter the ip address provided by the instructor."
read ipaddr_to_fetch
zip_dl_dir=~/.sdr_angel_zip_temp
mkdir "$zip_dl_dir"
curl -L -o "$zip_dl_dir/sdr_proot_env.zip" "http://$ipaddr_to_fetch:8000/sdr_proot_env.zip"
unzip -d ~ "$zip_dl_dir/sdr_proot_env.zip"
rm -r "$zip_dl_dir"
ln -s ~/.sdr_proot_env/run_sdr_angel.sh ~/.local/bin/sdrangel
chmod +x ~/.sdr_proot_env/run_sdr_angel.sh
source ~/.profile
echo "You should now be able to run the command `sdrangel` from the terminal. You may need to log out and log in."

