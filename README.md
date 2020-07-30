# Python_Election_Analysis

## Overview

The purpose of this Election Audit Analysis was to take the original election audit analysis about the candidate and make it complete by adding the county votes and breakdown of the counties and respective percentages of votes. The final output of the analysis would be sent to a text file in a summary format that is easily consumable by anyone who wants to view the winning county and candidate information.


## Election-Audit Results

### How many votes were cast in this congressional election?

There were a total of 369,711 votes cast in this congressional election.

### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

The total breakdown of county votes per precinct was:

Jefferson: 10.5% (38,855)

Denver: 82.8% (306,055)

Arapahoe: 6.7% (24,801)

### Which county had the largest number of votes?

Denver County had the largest number of votes, with 306,055 or 82.8% of the entire total votes.

### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

The breakdown of the number of votes and the percentage of total votes is as follows:

Charles Casper Stockham: 23.0% (85,213)

Diana DeGette: 73.8% (272,892)

Raymon Anthony Doane: 3.1% (11,606)

Here is the image of the text file output to validate these results:

https://github.com/jasonatoledo/Python_Election_Analysis/blob/master/Resources/txt.file.photo.png

### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

The candidate that won the election is:

* Winner: Diana DeGette

* Total of 272,892 votes 

* 73.8% of the total votes

## Election-Audit Summary

This script proved very useful for determining the winners, number of votes, and the percentage of votes for the county and candidates. It could be used for any election given a some of easy modifications:

1) Ensure the files to load and save are updated with new paths and proper corresponding path names that will be read/written to

2) Adjust the candidate name and county name column values as needed

3) If there are other pieces of information, such as state or district, the code blocks used for county/candidate could be slightly altered to include additional data. The column would have to be added to where the candidate/county name values are derived.
