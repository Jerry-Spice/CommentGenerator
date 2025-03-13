# Comment Generator

Created by Josh Brandon

## About

Something I dislike about my classes is that I have to write comments for everything. I mean everything. Originally this was meant to automate the comments I had to write for JavaDocs. However now I need to write comments so that my code looks nice and so that I can remember what functions do what.
I've officially reached the point where I stop working on something and need to read my own comments to remember how to use things.
There is not an easy way to create code to write comments that describe the actual processes I create. That part is still up to me. However I like having the code editor prompt me with the quick information about functions I write.
I also have recently transitioned into writing libraries for personal use so having comments that describe what the function does as opposeed to how it works are much more useful.

So this code does that. It creates my function headers for me. That's it.

## Use

My terminal prompt looks like this but you can use it however you like for your terminal propmt. Just make sure to use the same format for the program.

```
UserGuy@~$ python3 main.py <FILENAME>
```

I've also written some bash code for Linux and Mac users to make this easier. Keep in mind I'm not the best at bash so I didn't make it so it works for multiple files.

```
comment() {
    echo -e "Commenting $1\n"
    python3 <PATH_TO_YOUR_COPY_OF_THIS_CODE>/CommentGenerator/main.py $1
    echo -e "Done!"
}
```

## Config

If you are commenting a file that is not found in the config file then you will be prompted like this:

```
Figuring format from Config...
Config for filetype '<FILETPYE_THAT_IS_WEIRD>' not found...
Would you like to create one [y/n]?
```

```
y
```

```
Multiline Comment Declarations (enter both start and end declaration for multiline comments seperated by a comma):
Function Declaration (type 'default' to use the default identification '[A-Za-z0-9_*]{3,20} [A-Za-z0-9_]{1,50}?[\\(]'):
Comment Structure (use 'FUNCTION', 'ARG', and 'DESCRIPTION' to mark out where each section should go. type 'default' for default structure 'FUNCTION\\n @param ARG\\n @description DESCRIPTION\\n'):
```

If you use the default option make sure to type out 'default' or else it will actually use whatever misspelling of that you typed.
If there are issues with the config of the file format feel free to open config.json in a text editor and just delete the block of config info relevant to the config you messed up. :)
