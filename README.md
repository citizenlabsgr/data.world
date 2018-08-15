# Data.World
**SLACK CHANNEL: TBD**
# Project Description:

The idea is a sharable staging area for wrangling data before transfer to an open data portal (e.g., https://data.world).  The repo stores raw data and wrangling scripts.  Citizen Lab members can push raw data into the repo and authorized members can write scripts to prepare data for transfer to an open data portal.  

With some effort, we can create a repository of data and scripts to facilitate future data wrangling and help keep our open data manageable. 

### Table of Contents
* [Definitions](#definitions)        
* [Members](#members)
* [Process Roles](#process-roles)
* [Data Flow](#data-flow)
* [Process Overview](#process-overview)
* [Data Processing](#data-processing)
* [Expectations](docs/expectations.md)
* [Wrangling](docs/wrangling.md)

### <a id="definitions">Definitions</a> 
* [Comma Separated Values](https://en.wikipedia.org/wiki/Comma-separated_values) (CSV).  CSV is a method of formatting values in a text file. 
* [GitHub](https://en.wikipedia.org/wiki/GitHub) is a technology for versioning files.
* [Open Data](https://en.wikipedia.org/wiki/Open_data)
* Open Data Portal is technology that facilitates the sharing of a dataset(s) via an application programming interface (API)

## <a id="members">Members</a>
Members and areas of responsibility.

| Name       | Role           | [Raw-data](raw-data/)  | [Clean-data](clean-data/) | [Scripts](scripts/) |
| :-              | :-                | :-:              | :-:                |  :-:        |
| Cara D     | Curator      | [X](raw-data/) | [X](clean-data/)  |     |
| Eileen B   | Curator      | [X](raw-data/) |    |     |
| James W | Developer  | [X](raw-data/) | [X](clean-data/) | [X](scripts/)  |
| Jace B     | Maintainer |    |    |  [X](scripts/)  |



## <a id="process-roles">Process Roles</a>
Declares the duties of members.

| Curator                  | Developer                     | Maintainer                |
| :------------------      | :---------------------        | :-----------------------  |
| Curates dataset(s)       | Writes/Updates scripts        | Puts data into production |
| Loads raw dataset to GIT | Tests dataset load            | Removes data from production |
| Creates GIT pull request | Maintains GIT scripts folder  |  | 
| Signoff on Prod dataset load  | Maintains GIT tmp-data folder | Maintains the GIT master branch |
|                          | Maintains clean-data folder   | Maintains the Prod Environment |
|                          | Creates clean-data set        |  |
|                          | Maintains Dev Environment     |  |
|                          | Creates GIT pull request      |  |
|                          | Adds raw-data  sub-folders    |  |

## <a id="data-flow">Data Flow</a>
The path which data moves through the process.

| Local      |    | GitHub     |    | Data.World.Test |    | Data.World.Prod |
| :-         | :- | :-         | :- | :-              | :- | :- |
| Curator    | >  | raw-data   |    |                 |    |  |
| Developer  | <  | raw-data   |    |                 |    |  |
|            | >  | clean-data | >  | test-data       |    |  | 
| Maintainer | <  | clean-data |    |                 |    |  |
|            | >  |            |    |                 | >  | open-data |
| App(s)     | <  |            |    |                 | <  | open-data |

## <a id="process-overview">Process Overview</a>
This is a best case scenario with no failures. Use as a guide to a successful completion of the process.   

| Curator                 |    | Developer                  |    | Maintainer                   |
| :---------------------- | :- | :------------------------- | :- | :--------------------------- |
| Prepare Dataset CSV |     |    |                            |    |                              |
| Upload Dataset          |    |                            |    |                              | 
| Create GIT pull request |    |                            |    |                              | 
| Notify Developer        | >  | Download Repo              |    |                              |
|                         |    | Setup Environment Variables |    |                             |
|                         |    | Write/Update Script        |    |                              |
|                         |    | Test Script                |    |                              |
|                         |    | Test Data Load             |    |                              |
|                         |    | Test Application           |    |                              |
|                         |    | Upload Branch              |    |                              |
|                         |    | Notify Maintainer          | >  | Download refresh-data Branch | 
|                         |    |                            |    | Setup Prod Data Environment  | 
|                         |    |                            |    | Deploy to Production         |
|                         |    |                            |    | Deployment Check             |
| Deployment Check        |    |                            | <  | Notify Curator               |
| Approve Deployment      |    |                            |    |                              |
| Notify Maintainer       | >  |                            |    | Update master Branch         |



## <a id="data-processing">Data Processing</a>
* Curator 
* Developer
* Maintainer 




    


