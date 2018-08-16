# Data.World
**SLACK CHANNEL: TBD**
## Description:
The Adopt a Drain application will need to add and remove drains over time. 

### Contents 
### Curator Instructions:
* [Prepare Dataset](#prepare-dataset)
* [Upload Dataset](#upload-dataset)
* [Notifiy Developer](#notify-developer)

### Developer Instructions:
* [Clone/Pull Repo](#clone-repo)
* [Check Raw Data](#check-raw-data)
* [Setup Environment Variables](#env-variables)
* [Write/Update Scripts](#scripting)
* [Notify Maintainer](#notify-maintainer)

# Curator Instructions

## <a id="prepare-dataset">Prepare Dataset</a>
At this point, you have a spreadsheet with drain data.
    
### Dataset - Check Sheet

|    | Checks |
| :- | :- |
| * | Convert spreadsheet to a CSV file (if needed)  |
| * | CSV File Name: **gr-drains.csv**  |
| * | CSV File Columns: SUBTYPE, DRAIN_JURISDICTION, DRAIN_OWNER, Soure_ID, LOCAL_ID, FACILITYID, Subwatershed, POINT_X, POINT_Y  |
| * | Put **gr-drains.csv** in a folder you can easily find |
    
## <a id="upload-dataset">Upload Dataset</a>
Warning: Read all the instructions before you attempt an upload. 

### GitHub - Check Sheet 
 Finding links and buttons in GitHub can be challenging.  You need to do a litte reconnaissance before you upload gr-drain.csv. 
 
|    | GitHub Checks |
| :- | :- |
| * |  Confirm you are in the **raw-data** GitHub folder   |
| * |  Find the **adopt-a-drain** folder link  |
| * |  Find the **upload files** button  |
| * |  Find the **gr-drains.csv** file in that easy to find folder on your computer  |

### Upload Dataset
Read all before you start pressing buttons

| Step |  Task |
| :- | :- |
| 1. | **Click on the _adopt-a-drain_ folder link.**  |
|   | _Warning: once clicked these instructions will disappear, so commit the next few lines to memory_ |
|   | _Ignore any copies of **gr_drains.csv** int the folder, this is not a problem_ |
| 2. | **Click on the _update files_ button**  |
|   | _Opens upload page_ |
|   | _Follow instructions on the upload page_ |
| 3. | **Commit Section** |
|   | _Safe to ignore "file via update"_   |
|   | _Safe to ignore "add an optional extended description"_   |
|   | **Click on the _"Create a new branch for this commit and start a pull request"_ radio button** |
|   | _Accept the default pull request name (aka branch name)_
| 4. | **Click on the _"Propose Changes"_ button** |
|   | _Opens **pull request** page_ |
| 5. | **Move on to **Notify Developer** below|


## <a id="notify-developer">Notify Developer (aka Pull Request)</a>
Notification occurs during what GitHub call a **pull request.**  Is what it is.  

### Notification - Check Sheet

|    | Notification Checks |
| :- | :- |
| * | You should be on the **Open a pull request** page after uploading **gr_drains.csv.**  |
| * |  Find the "Assignees" link  |
| * |  Find the "Create pull request" button |

### Notification 
Read all before you start pressing buttons

| Step |  Task |
| :- | :- |
| 1. | **Click on the "Assignees" link** |
|   | **Select a Developer** (i.e, James Wilfong) |
| 2. | Ignore "Add files via upload" |
|   | Ignore "Leave a comment" |
| 3. | **Click "Create pull request** button |

### Done

# Developer Instructions
## <a id="clone-repo">Clone/Pull Repo</a>
TBD

## <a id="env-variables">Setup Environment Variables</a>
TBD

## <a id="scripting">Write/Update Scripts</a>
TBD

## <a id="notify-maintainer">Notify Maintainer</a>
TBD
