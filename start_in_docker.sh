# start biscuit docker conatiner with /mnt as the src directory, and pop a shell
# run ./mntsync.sh to sync up the biscuit code
# and run make qemu to start biscuit
# use ctrl-a x to exit qemu (ctrl+a, let go of key, then hit x)  

docker run -v $(pwd)/biscuit:/mnt -it biscuit  bash
