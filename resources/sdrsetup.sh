#!/bin/bash
## Assumptions:
## - The instructor is running an http server on port 8000
##   (perhaps using `python3 -m http.server`)
##   with the file "sdr_proot_env.zip" available.
## - The file "sdr_proot_env.zip" contains one directory,
##   which is named ".sdr_proot_env" (Note the preceeding dot).
## - The directory ".sdr_proot_env" contains...
##   - a script, "run_sdr_angel.sh"
##   - anything else needed.
## Other notes:
## - Currently (2024 Oct), the `.sdr_proot_env" contains:
##   - the aforementioned "run_sdr_angel.sh", with these contents:
##       #!/bin/bash
##       ~/.sdr_proot_env/proot -R ~/.sdr_proot_env/rootfs /usr/bin/sdrangel
##   - the `proot` executable, which is referenced in "run_sdr_angel.sh"
##   - a rootfs folder which...
##      - was obtained by extracting a rootfs.tar.xz from here: https://images.linuxcontainers.org/images/ubuntu/jammy/amd64/default/
##      - has sdrangel installed inside of it from the .deb file on the sdrangel release page: https://github.com/f4exb/sdrangel/releases
## Further reading:
## - Some details about how to work with proot are listed here: https://github.com/python-can-define-radio/more-sdr/blob/main/2024-07-11/proot-directions.md


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
