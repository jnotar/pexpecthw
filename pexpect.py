#! /usr/bin/python

from __future__ import division

import glob, pexpect

def function(nexus, numgen = 2000):
    child = pexpect.spawn("mb -i %s" %(nexus)) #initalize interactive mode
    child.sendline("set nowarn = yes") #send command to mr bayes
    child.sendline("mcmcp ngen = %d" %(numgen)) #tell mr bayes to substitute numgen
    child.sendline("mcmc")
    child.sendline("no")
    child.sendline("quit")


def function_2(nexus):
    child = pexpect.spawn("mb -i %s" %(nexus)) #initalize interactive mode
    child.sendline("execute %s" %(nexus)) #run some stuff
    child.sendline("sumt")
    #child.expect("MrBayes >") #not sure if I need this?
    child.sendline("sump")
    child.sendline("quit")

files = glob.glob("*")
t_files = glob.glob("*.t")

print(str("There are " + str(len(files)) + " total files in the current directory and " + str(len(t_files)) + " files that end in '.t'"))

function("primates2.nex")

function_2("primates2.nex")

files2 = glob.glob("*")
t_files2 = glob.glob("*.t")

print(str("There are " + str(len(files2)) + " total files in the current directory and " + str(len(t_files2)) + " files that end in '.t'"))

print("These files end in '.t': " + str(t_files2))
