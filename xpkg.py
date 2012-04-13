#!/usr/bin/python2.7

# XPKG - Xilitra PacKaGe manager

import os, sys
import getopt
import argparse

def main():
    opts = argparse.ArgumentParser(description='Xilitra Package System')
    opts.add_argument("-i", help="Install package PKGS", metavar="PKGs", action='store', dest="install", nargs="+")
    opts.add_argument("-r", help="Remove package PKGS", metavar="PKGs", action='store', dest="remove", nargs="+")
    opts.add_argument("-u", help="Update packages database", action='store_true', dest="update")
    
    args = opts.parse_args()
    if args.install:
        install_package(args.install)
    elif args.remove:
        remove_package(args.remove)
    elif args.update:
        update_packages()
    
def install_package(packages):
    from applets import install
    install.init(packages)
    
def remove_package(packages):
    from applets import remove
    remove.init(packages)
    
def update_packages():
    from applets import update
    update.init()

if __name__ == "__main__":
    main()
else:
    print "XPKG not designed for import into another programs!"
