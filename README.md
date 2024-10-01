# PA 00

For this assignment, you will submit TWO files -- the readme and the script file. 


Edit this README file to include a brief biography of yourself. Your README should include the following elements:
* Headers (one or more)
* Emphasis (italics or/and bold)
* Lists
* Images: add a picture (of yourself or something else) to your repo and embed it in your README
* Links
* A summary and reflection of the Git/GitHub workflow you adopted for this homework, and of your experience with Markdown (e.g., provide a summary of the workflow you adopted, and add some comments about something new you learned, something that surprised you, etc.)

# Andrew Koller
### *Academic Stuff* 

Hey everyone! My name is Andrew Koller and I'm in the MAPSS psychology program. I earned by BA from DePaul University with a doulbe major in psychology and philosophy, and a minor in German. After graduating, I went into a data sciences and visualization coding bootcamp at Northwestern, as I felt I needed to build some quantitative skills to compliment the qualitative skill set I developed in psychology and philosophy. While I learned a lot about coding in my bootcamp, it went very quickly and I have a lot of gaps in my coding logic. I'm really looking forward to bridging those gaps in this course! 

As far as my research interests are concerened, I'm fascinated by morality and how it effects our decision making. I'm currently attached to the Social Cognitive Neuroscience lab lead by Dr. Jean Decety and I started work on my thesis topic back in June. Right now, I'm developing a study that investigates the correlation between moral conviction and Medical Assistance in Dying (MAiD) decision-making. To accomplish this, I need to generate LLM and ML generated avatars of terminally ill cancer patients. These will serve as the stimulus for my study. In case anyone's interested in how these avatars are generated, here's my current - and subject to a lot of change - workflow:

1. Generate patient characteristics using python. This takes a series of lists that contain characteristics, which are randomly chosen using python's 'random' library. These characteristics are added to a .csv file.
2. The CSV file is read into Claude 3.5 Sonnet's API to generate:
    - An appropriate name based on race/ ethnicity and gender
    - A ~400 word narrative requesting MAiD based on the randomly generated patient characteristics. 
3. Using ElevenLabs to generate a voice for our narrative.
4. Using a pre-trained StyleGan2 model to generate realistic headshot for the avatar. This model was actually created in part by Alexander Todorov here at UChicago. It allows the user to generate faces based on control characteristics. The only downside is that it has to be accessed via its API, and the API is underdeveloped at this time. 

Steps 1, 2, and 4 are close to being done, although I may need to switch my image generation model. 
**If anyone has any suggestions for image generation models, please let me know!**
<br>

### *Personal Stuff* ###
Outside of academics, Here are some interesting things about me:
- I love to cook
- I love to explore new restaurants 
- I love to travel
- I do a bit of photography as a hobby
- I'm from a Northern suburb of Chicago, and moved to downtown Chicago 10 years ago
- My favorite philosophers are Nietzsche, Socrates, and Aristotle. **If you ever want to talk philosophy, please reach out!**

Here's me in front of Beecher, Green, Kelly Hall (I know, it's convoluted). If you every need to find me, I'm usually in Green 310.
![image](IMG_0096.jpeg)
<br>

I also have a [website](https://andrewkoller.org/) that I put together. It's not much, but I made it from scratch with the help of Claude 3.5. If you're interested in making your own website, feel free to use any of the code from my website to build your own! 

### *GitHub Workflow and Experience with Markdown* ###

For this assignment, I cloned the repo using `git clone` along with the SSH URL. After cloning, I opened the repo in VScode and began to edit the README file. I have worked with markdown in the past ([Here's the README](https://github.com/AEKoller/MADAIN) for a project I did earlier this year), so I didn't learn too many new tricks. I did, however, learn to deal with a quirks in Markdown while working in this assignment:
* If you're going to *italicize* or **bold** your text, the `*` needs to be attached to the word it is bolding
* A paragraph with an insertion within it (like with a hyperlink or an image) needs to be seperated from a any preceeding page breaks or `<br>`.

after completing the Markdown doc, I saved my work in VScode, used the `git add .` script to add all the files from my local repo, and used `git commit -m "final push"` to commit the files and add a commit message. Finally, I used `git push origin main` to push my files to my online Github repo. 

## 📚  Resources 
* [A short video explaining what GitHub is](https://www.youtube.com/watch?v=w3jLJU7DT5E&feature=youtu.be) 
* [Git and GitHub learning resources](https://docs.github.com/en/github/getting-started-with-github/git-and-github-learning-resources) 
* [Understanding the GitHub flow](https://guides.github.com/introduction/flow/)
* [How to use GitHub branches](https://www.youtube.com/watch?v=H5GJfcp3p4Q&feature=youtu.be)
* [Interactive Git training materials](https://githubtraining.github.io/training-manual/#/01_getting_ready_for_class)
* [GitHub's Learning Lab](https://github.com/apps/github-learning-lab)
* [Education community forum](https://education.github.community/)
* [GitHub community forum](https://github.community/)
