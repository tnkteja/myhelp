"""
"""
import xml.etree.ElementTree as ET

def isFile(note_name):
        for fil in files:
            value = fil.attrib["value"]
            if value == note_name:
                return True
        return False

def get_file_from_files(note_name):
        for fil in files:
            value = fil.attrib['value']
            if value == note_name:
               return fil
        newfile = ET.Element('file')
        newfile.set("value", note_name)
        rootfiles.append(newfile)
        return newfile

def get_tag_from_tags(tagname):
        for tag in tags:
            value = tag.attrib['value']
            if value == tagname:
               return tag
        newtag = ET.Element('tag')
        newtag.set("value", tagname)
        roottags.append(newtag)
        return newtag

def add_tags_to_file(fil,definedtags):
        for definedtag in definedtags:
                tagelement = ET.Element('tag')
                tagelement.text = definedtag
                fil.append(tagelement)

def add_file_to_tag(note_name,tag):
        newfileelement = ET.Element('file')
        newfileelement.text = note_name
        tag.append(newfileelement)

def get_tags_from_file(note_name):
        fil = get_file_from_files(note_name)
        filetags = fil.iter('tag')
        filetaglist=[]
        for tag in filetags:
            filetaglist.append(tag.text)
        return filetaglist

def modify_tags_xml(note_name,definedtags):
    fil = get_file_from_files(note_name)
    add_tags_to_file(fil,definedtags)

    for definedtag in definedtags:
        tag = get_tag_from_tags(definedtag)
        add_file_to_tag(note_name,tag)
        global TAGS_XML_DIR
        tree.write(TAGS_XML_DIR)

