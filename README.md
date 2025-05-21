# CloudFinder25w21a
Most of the code comes from: [https://github.com/humhue/cloudfinder] (Cloudfinder but for 25w20a- worlds)

Go Check it out! Could not be possible without it.

In 25w21a, the cloud patterns changed. This code is designed to find the estimated z coordinates of 25w21a+ worlds using clouds.

Steps
1. Setting up 🛠️: Download the code and extract it
  
   (You must have Python to use this)
   [https://www.python.org/downloads/]

2. Inputting Data 📝: Open pattern.txt, here you will enter your data.

   You will type 1 if there is a cloud blob, 0 if there is not, and ? if you're not sure.
   Each row must have the same number of numbers (Just fill the row that has less with ?)

   So this can't work
   ```
   11101?
   101
   ```
   But this <b>can</b>
   ```
   11101?
   101???
   ```
(Doesn't matter the direction you enter the clouds)
Then press Save. (Or Ctrl + S)

3. Running 🚀: Left-click the folder that contains the code, clouds.png, and pattern.txt. (Not the folder that contains the folder which contains the cf.py)
  
   Press open in terminal. Then you will type
   
```
python cf.py
```
   You should get result/s
   (If you don't, the data you entered is wrong)
   
Improvements
- Uses alpha to make it more accurate
- Improved rotation logic to make it cleaner, less buggy, and more efficient
  
If you need help, you can dm on discord (xVoid879#7107) or join the Minecraft@home discord.

Please give feedback
