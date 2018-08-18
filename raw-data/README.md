# Data.World - Raw Data Upload Step

## Responsibility 
* **Curator** is responsible for the Raw-Data-Upload Step

## Prerequisites
* Raw drain data file
* Citizen Lab Member
* GitHub account


# Data Upload Instructions

## Prepare Dataset
At this point, you have a spreadsheet with drain data.  Use the check sheet below to get yourself organized.
    
### Dataset - Check Sheet

|    | Checks |
| :- | :- |
| * | Convert spreadsheet (Excel, Numbers, ...) to a CSV file (if needed)  |
| * | CSV File Name: **gr-drains.csv**  |
| * | CSV File Columns: SUBTYPE, DRAIN_JURISDICTION, DRAIN_OWNER, Soure_ID, LOCAL_ID, FACILITYID, Subwatershed, POINT_X, POINT_Y  |
| * | Put **gr-drains.csv** in a local folder on your computer. |

* Column name changes will cause a delay while the developer fixes it.  
    
## Upload Dataset
Raw data needs to be uploaded to GitHub. Use the check sheet below to get yourself organized.
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


## Notify Developer (aka Pull Request)
Notification occurs during what GitHub call a **pull request.**  Is what it is.  

### Notification - Check Sheet

|    | Notification Checks |
| :- | :- |
| * | You should be on the **Open a pull request** page after uploading **gr_drains.csv.**  |
| * |  Find the "Assignees" link  |
| * |  Find the "Create pull request" button |

### Notification Steps
Read all before you start pressing buttons

| Step |  Task |
| :- | :- |
| 1. | **Click on the "Assignees" link** |
|   | **Select a Developer** (i.e, James Wilfong) |
| 2. | Ignore "Add files via upload" |
|   | Ignore "Leave a comment" |
| 3. | **Click "Create pull request** button |

### You should be done at this point. 

