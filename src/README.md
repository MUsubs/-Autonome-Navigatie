# Guide to making the data set

## Step 1
Open roi_tracking
Insert the name of the video at placeholder \*\*VIDEO**
Insert the name the frames will get at placeholder \*\*NAME** (ex. name of used video)
Run roi_tracking
If bounding box doesn't work well press R to draw again, press SPACE to continue vid

## Step 2
Open labeling_thing
Insert the name the json will get at placeholder \*\*NAME** (ex. name of used video)
Run labeling_thing

## Step 3
Repeat steps 1 and 2 for all the necessary videos

## Step 4
Run json_format_and_merging

## Step 5
Save the combined file you get from step 4 in a different folder

## Step 6
Run json_verwijderen
ATTENTION: WILL DELETE EVERY JSON FILE IN THIS FOLDER