# Data.World
**SLACK CHANNEL: TBD**
## Description:
The Adopt a Drain application will need to add and remove drains over time. 

### Contents 
### Curator Instructions:
* [Prepare Dataset](#prepare-dataset)
* [Upload Dataset](#upload-dataset)
* [Create GIT Pull Request](#pull-request)
* [Notifiy Developer](#notify-developer)

### Developer Instructions:
* [Clone/Pull Repo](#clone-repo)
* [Check Raw Data](#check-raw-data)
* [Setup Environment Variables](#env-variables)
* [Write/Update Scripts](#scripting)
* [Notify Maintainer](#notify-maintainer)

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
 
|    | Checks |
| :- | :- |
| * |  Confirm you are in the **raw-data** GitHub folder   |
| * |  Find the **adopt-a-drain** folder link  |
| * |  Find the **upload files** button  |
| * |  Find the **gr-drains.csv** file in that easy to find folder on your computer  |

* Upload (Read all before you start pressing buttons)
    * Click on the **adopt-a-drain** folder link. Warning: once clicked these instructions will disappear, so commit the next few lines to memory
    * Once in the **adopt-a-drain** folder, you may see previous copies of **gr_drains.csv**... not a problem
    * Click on the **update files** button, the page will change to allow uploading files.  _Follow instructions on the upload page_
    * Click on the " Create a new branch for this commit and start a pull request" radio button in the Commit Section, 
    * Click on the **Propose Changes** button, the page will change to the **Open a pull request** page

## <a id="notify-developer">Notify Developer (aka Pull Request)</a>
Notification occurs during what GitHub call a **pull request.**  Is what it is.  

### Notification - Check Sheet

|    | Notification Checks |
| :- | :- |
| * | You should be on the **Open a pull request** page after uploading **gr_drains.csv.**  |
| * |    |
| * |    |
| * |    |

## <a id="clone-repo">Clone/Pull Repo</a>
TBD

## <a id="env-variables">Setup Environment Variables</a>
TBD

## <a id="scripting">Write/Update Scripts</a>
TBD

## <a id="notify-maintainer">Notify Maintainer</a>
TBD
