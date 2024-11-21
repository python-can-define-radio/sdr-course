#!/bin/bash
## Assumptions:
## - The instructor is running an http server on port 8000
##   (perhaps using `python3 -m http.server`)
##   with the file "sdr_proot_env.tar" available.
## - The file "sdr_proot_env.tar" contains one directory,
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
##      - was obtained by extracting a rootfs.tar.xz from here:
##          https://images.linuxcontainers.org/images/ubuntu/jammy/amd64/default/
##      - has sdrangel installed inside of it from the .deb file on the sdrangel release page:
##          https://github.com/f4exb/sdrangel/releases
## Further reading:
## - Some details about how to work with proot are listed here:
##     https://github.com/python-can-define-radio/more-sdr/blob/main/2024-07-11/proot-directions.md

cd /run/user
directories=($(ls -d */))
if [ -z "$directories" ]; then
    echo "Samba does not appear to be mounted. Specifically, didn't find any directories in $(pwd).";
fi

for dir in "${directories[@]}"; do
    # Remove the trailing slash from the directory name
    dir=${dir%/}
    # Check if the directory name contains more than 5 digits
    if [[ "$dir" =~ [0-9]{6,} ]]; then
        usernumber=$dir
        break
    fi
done 

cd $usernumber
cd gvfs

if [ -z "$(ls)" ]; then
    echo "No samba shares appear to be mounted. Specifically, didn't find anything in $(pwd)";
    exit
fi

studentdir="$(ls | grep student || true)"

if [ -z "$studentdir" ]; then
    echo "Student samba share does not appear to be mounted. Specifically, didn't find anything containing the word student in $(pwd)";
    exit    
fi
# studentdir=$(ls -lt | grep "^d" | grep "student" | head -n 1 | awk '{print $NF}')
cd $studentdir # chooses just the student samba dir in the event the instructor is linked to both inst samba and student samba
samba_root=$(pwd)

source_file_sdr_angel_tar="$samba_root/sdr_resources/sdr_angel_tar"
destination_dir_sdr_angel_tar="$HOME/Desktop/sdr_angel_tar"  

echo "Copying the SDR Angel tar folder"
echo "It is not locked up or stuck be patient the sdr_angel_tar folder is large and may take a minute to download."
cp -r "$source_file_sdr_angel_tar" "$destination_dir_sdr_angel_tar"

if [ $? -eq 0 ]; then
    echo -e "\e[32m- Successfully copied sdr angel tar folder to the Desktop.\e[35m"
else
    echo "Move failed."
fi 

echo "Extracting tar file."
tar -xf "$destination_dir_sdr_angel_tar/sdr_proot_env.tar" --directory=$HOME
rm -r "$destination_dir_sdr_angel_tar"
chmod +x ~/.sdr_proot_env/run_sdr_angel.sh
ln -s ~/.sdr_proot_env/run_sdr_angel.sh ~/.local/bin/sdrangel
source ~/.profile
echo "You should now be able to run the command `sdrangel` from the terminal. You may need to log out and log in."
