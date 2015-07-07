"""
This module contains the main logic to run all the logic defined
"""

import commands
import xml.etree.ElementTree as ET
from optparse import OptionParser
from os import environ
from tabulate import tabulate
from subprocess import call
import ConfigParser
from myhelp.storage import *

TAGS_XML_DIR = environ["HOME"] + "/.mypy/myhelp/tags.xml"

def run():
    """Main method where all logic is defined"""
    
    config = ConfigParser.RawConfigParser()
    config.read(environ["HOME"] + "/.mypy/myhelp/myhelp.cfg")
    editor = config.get("Editor","path")
    if not editor:
	print "Not Editor defined!"
        quit()
    
    config_option_help="'show' - displays configured options, 'set [section] [name] [value]' - sets config under a section,'set [name] [value]' - sets configuration globally" 

    parser = OptionParser()
    
    parser.add_option("-a", "--add", action="store", type="string", dest="addfile", help="adds a notes")
    parser.add_option("-c", "--config", action="store", type="string", dest="config", help=config_option_help)
    parser.add_option("-e", "--edit", action="store", type="string", dest="editfile", help="edits a notes")
    parser.add_option("-o", "--open", action="store", type="string", dest="openfile", help="opens a notes")
    parser.add_option("-r", "--remove", action="store", type="string", dest="remove", help="removes a notes")

    options, args = parser.parse_args()

    tree = ET.parse(environ["HOME"] + "/.mypy/myhelp/tags.xml")

    root = tree.getroot()
    roottags = root.find('tags')
    tags = roottags.iter('tag')
    rootfiles = root.find('files')
    files = rootfiles.iter('file')
    
    if options.config:
        if options.config == "show":
            config_option_list=''
            config_sections = config.sections()
            for section in config_sections:
                config_option_list=config_option_list+section+"\n"
                section_items =config.items(section)
                for item in section_items:
                    config_option_list=config_option_list+"    "+item[0]+"    "+item[1]+"\n" 
            print config_option_list
            quit()
        
    def add_notes(note_name,existing_tags):
       call([editor,environ["HOME"] + "/.mypy/myhelp/notes/"+note_name+".note"])
       definedtags = raw_input("Define Tags (separated by spaces): ").split(" ")
       definedtags.append(note_name)
       print definedtags
       print existing_tags
       definedtags=list(set(definedtags)-set(existing_tags))
       print definedtags
       quit()
       if len(definedtags)>0:
           modify_tags_xml(note_name,definedtags)  

    def get_tags_from_file(note_name):
        fil = get_file_from_files(note_name)       
        filetags = fil.iter('tag')
        filetaglist=[]
        for tag in filetags:
            filetaglist.append(tag.text)
        return filetaglist

    if options.addfile:
       if isFile(options.addfile):
           existing_tags=get_tags_from_file(options.addfile)
           raw_input("Note exists with tags - "+" ".join(existing_tags)+"\nDo you want to edit the notes ? [Press enter to continue]\n") 
       add_notes(options.addfile,existing_tags)
       quit()

    if options.editfile:
        if isFile(options.editfile):
            add_notes(note_name,[])
        else:
           raw_input("Note doesn't exist.\nDo you want add note ? [Press enter to continue]")     
           add_notes(note_name)
        
    if options.remove:
        pass
    
    if len(args) != 1:
        print "Please use a search term\n example : myhelp <some tag word> "
        quit()

    table={"File":[],"Results":[]}
    for tag in tags:
        if tag.attrib["value"] == args[0]:
            fileelements = tag.iter("file")
            for fileelement in fileelements:
                f = open(
                    environ["HOME"] + "/.mypy/myhelp/notes/" + fileelement.text+".note", "r")
		table["File"].append(fileelement.text)
		table["Results"].append(f.read())
                f.close()

    print tabulate(table,headers="keys",tablefmt="grid")
if __name__ == "__main__":
    run()
