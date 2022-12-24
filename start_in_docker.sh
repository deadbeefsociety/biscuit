# start biscuit docker conatiner with /mnt as the src directory, and pop a shell
# run ./mntsync.sh to sync up the biscuit code
# and run make qemu to start biscuit
# use ctrl-a x to exit qemu (ctrl+a, let go of key, then hit x)  

# using --privileged if u want to use kvm
# exposing 1234 for gdb port
docker run -p1234:1234  -v $(pwd)/biscuit:/mnt -it biscuit  bash
