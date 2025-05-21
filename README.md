# CloudFinder25w21a
Most of the code comes from: [https://github.com/humhue/cloudfinder]
Go Check it out! Could not be possible without it.

In 25w21a, the cloud patterns changed. This code is designed to find the estimated z coordinates of 25w21a+ worlds using clouds.

Steps
1. Setting up 🛠️: Download it and Extract it (You must have python to use this)
   [https://www.python.org/downloads/]

2. Inputting Data 📝: Open pattern.txt, here you will enter your data
   You will type 1 if there is a cloud blob, 0 and if there is not, and ? if your not sure.
   Each row must have the same number of numbers (Just fill the row that has less with ?)
   So this can't work
   ```
   11101?
   101
   ```
   But this can
   ```
   11101?
   101???
   ```
(Doesn't matter the direction you enter the clouds)
Then press Save. (Or Ctrl + S)

3. Running 🚀: Left Click the folder that contains the code, clouds.png, and pattern.txt. Press open in terminal. Then you will type 
```
python cf.py
```
   You should get result/s
   (If you don't, the data you entered is wrong)
   
Improvements
- Uses alpha to make it more accurate
- Improved rotation logic to make it cleaner, less buggy, and more efficient
  
