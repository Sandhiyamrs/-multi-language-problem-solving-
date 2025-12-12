# Duplicate File Finder

## Problem
Detect duplicate files in a folder by comparing file hashes (MD5).  
Enhancement: Show duplicates grouped and total space wasted.

## Input
- Folder path

## Output
- List of duplicate file pairs
- Total number of duplicates
- Total space used by duplicates

## Constraints
- Works for all file types
- Efficient for large folders

## Example
Input: Folder containing 2 identical files
Output: 
Duplicate files found:
file1.txt == file2.txt
Total duplicates: 1
Total space wasted: 5 KB

## Why This Problem Is Useful
- Helps clean storage
- Detect redundant files in PCs, servers, or cloud storage

