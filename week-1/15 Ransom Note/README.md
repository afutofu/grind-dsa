# Ransom Note

DS: Arrays & Buckets

- Return false if ransomNote length is greater than magazine length
- Initialize array of length 26 for each of the 26 letters in the alphabet for an alphabet counter
- Fill in values by iterating over each character in the magazine string incrementing its letter value in the alphabet counter
- Decrement values from the alphabet counter by checking its value with ransomNote
- If at any point any value in the alphabet counter goes below 0, return false because it means the magazine was not sufficient
- If the looop finishes then return true because it means that the magazine could construct the ransomNote string
