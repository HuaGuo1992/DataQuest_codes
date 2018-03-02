## 1. Introduction ##

/home/dq$ ls -l

## 2. Moving Problematic Files to a Separate Folder ##

/home/dq$ mv forest_fires.cssv ./problematic/

## 3. Fixing File Extensions ##

/home/dq/problematic$ mv forest_fires.cssv forest_fires.csv

## 4. Consolidating Files ##

/home/dq$ mv problematic/ csv_datasets

## 5. Restricting Permissions ##

/home/dq$ chmod 0740 csv_datasets/