# Data.World
**SLACK CHANNEL: TBD**
# Conventions and Expectation:
Conventions and Expectations
### Open Data Portals
An Open Data Portal stores digital versions of places, things, and ideas.
* Using third party Open Data Portal is preferred to hosting open data in Citizen Labs' open data portal, Using the Citizen Labs’ open data portal is preferred using nothing
### API
Application Programming Interfaces are a fundamental part of sharing. 
* An API is preferred to a direct connection to a database. Direct connections are discouraged. 
* Maintainers should keep Citizen Labs’ API keys in a secure place
* Developers should keep personal/development API keys in a secure place
* Curators should not need API keys 
### Versioning
Versioning allows structural changes in a table to occur without breaking the application(s).  Well at least not breaking them right away.   
* Be nice to other applications sharing a dataset by versioning 
* A new version is required when a column name changes
* A new version is required when adding a column to an existing version
* Versions should be few, no more than 3 version are in the open data portal at a time
* When a fourth version is required, the first version is removed
### Table Names
* A noun is preferred to a verb when naming tables
* Plurals are preferred to singular nouns when naming tables
* Underscores are the preferred separator.  Spaces and hyphens are not recommended.
* Lowercase is preferred to everything else
* Don't change the name of the original source file. You may not be the curator of the file so keep the file as recognizable to the curator as possible for ease of communications.
### Column Names
* Underscores are the preferred separator.  Spaces and hyphens are not recommended.
* Column names prefixed with a table abbreviation are preferred to column names with no prefix.
* Lowercase is preferred to everything else
### Identity Names
* Alphanumeric identity values should have column names with the suffix "_id"
* Numeric identity column names should have column names with the suffix "_no"
### Identity Values
* A universally unique identifier (UUID) value is preferred to a locally unique identity value, a locally unique identity is preferred to no identity, things with no identity are not things at all. 
### Date Values
* ISO 8601 date standard is preferred to any other standard  
### Geographic Object Values
* OGC WKT is preferred to proprietary formats





    


