import os
import subprocess


# hex -ncpu 2 -noexec <job1.mac >job1.log # job2 starts after job1
# hex -ncpu 2 -noexec <job2.mac >job2.log

def runHex(file):
    pdbPaths = []
    macPaths = []
    for root, dirs, files in os.walk(file):
         for f in files:
             if f.split(".")[-1] == "mac":
                 subprocess.call([ "hex", "-ngpu", "-noexec", "<%s"%(f), ">%s"%(f + ".log") ], shell=True)


macPath = "/Users/csx/Downloads/bioInfo/pdbs/ACE2"
runHex(macPath)