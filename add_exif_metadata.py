import importlib
exiftool = importlib.import_module("pyexiftool")

files = ["G:\\datasets\\mining_district\\exiftool_test\\60004069.pdf"]

with exiftool.ExifTool as et:
    metadata = et.get_metadata_batch(files)


for d in metadata:
    print("{:20.20} {:20.20}".format(d["SourceFile"],
                                     d["EXIF:DateTimeOriginal"]))