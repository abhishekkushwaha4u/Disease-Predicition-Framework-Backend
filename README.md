This is the backend for our Tarp Project 2021-22
It has all the routes related to our project on disease prediction and other components

Some key features of the backend routes are:-

1) Disease Prediction Routes for 6 different diseases
    a) **Diabetes**
    b) **Kidney**
    c) **Liver**
    d) **Malaria**
    e) **Pneumonia**(*Lungs*)
    f) **Skin**

2) A Route for interacting with the chatbot(`intent-based` and built on `bag of words model`)

3) A route for scraping hospitals nearby based on `pincode` and `city`

To setup this backend for local use, we need to setup two stuff:

1) The basic backend
2) Geckodriver(for selenium)


How to install GeckoDriver on Windows?

In this section, we will see how we can download, setup, and use GeckoDriver on the Windows operating system. There are different ways to set it up for your selenium scripts, which we will be discussing in detail. Consequently, let’s first start with downloading the driver executable for the Windows platform:

*How To Download GeckoDriver on Windows?*
1. Firstly, we can download the platform-specific GeckoDriver (preferably the latest version) directly from Github. As we are downloading it for the Windows 64-bit platform, so we will download the file “geckodriver-<latest-version>-win64.zip” as shown in the below screenshot:

<img src="https://cdn-anlbg.nitrocdn.com/dKKErbUyoNysjatCgltCzbTJJilTMwLi/assets/static/optimized/rev-4b21c3b/wp-content/uploads/sites/1/nggallery/selenium-1/4-Downloading-GeckoDriver-from-Github.png" alt="Geckodriver Github" />

2. Secondly, extract the downloaded *gecko driver zip file*.

<img src="https://cdn-anlbg.nitrocdn.com/dKKErbUyoNysjatCgltCzbTJJilTMwLi/assets/static/optimized/rev-4b21c3b/wp-content/uploads/sites/1/nggallery/selenium-1/5-Extract-GeckoDriver-from-downloaded-ZIP.png" alt="Zip Extract" />

3. Thirdly, please select a destination to save it.

<img src="https://cdn-anlbg.nitrocdn.com/dKKErbUyoNysjatCgltCzbTJJilTMwLi/assets/static/optimized/rev-4b21c3b/wp-content/uploads/sites/1/nggallery/selenium-1/6-Save-GeckoDriver-to-the-specified-directory.png" alt="Geckodriver Zip Decompress to Specific Directory" />


*Adding Geckodriver to path*

1. Firstly, open properties by right-clicking on This PC.

2. Secondly, open Advanced System Settings and click on Environment Variables.

<img src="https://cdn-anlbg.nitrocdn.com/dKKErbUyoNysjatCgltCzbTJJilTMwLi/assets/static/optimized/rev-4b21c3b/wp-content/uploads/sites/1/nggallery/selenium-1/8-Opening-System-Environment-Variables.png" alt="Environment Variable" />

3. Thirdly, under the System variables, select *Path* and click on *Edit*

<img src="https://cdn-anlbg.nitrocdn.com/dKKErbUyoNysjatCgltCzbTJJilTMwLi/assets/static/optimized/rev-4b21c3b/wp-content/uploads/sites/1/nggallery/selenium-1/9-Editing-the-System-Path.png" alt="Editing System Path" />

4. After that, we need to append the *path of the GeckoDriver*. Click on **New** and paste the path at the last editable row and click on **OK**. Moreover, we need to specify the folder path where the *GeckoDriver* executable file resides. In our case, it was **"E:\drivers."**

<img src="https://cdn-anlbg.nitrocdn.com/dKKErbUyoNysjatCgltCzbTJJilTMwLi/assets/static/optimized/rev-4b21c3b/wp-content/uploads/sites/1/nggallery/selenium-1/10-Adding-Driver-Path-to-System-Variables.png" alt="Edit environment Variable" />

5. After closing all the subsequent windows, we can use *GeckoDriver* without using the system property code. Note that we might have to restart our system for the Environment Variables changes to take effect.

*Setting up backend locally*

1) We need to create a virtual environment for this project. For that we need to do
    a) `pip install virtualenv`
    
    b) `virtualenv env`
2) To activate the virtual environment we do: `.\env\Scripts\activate`
3) To install requirements: `pip install -r requirments.txt`
4) To run the server: `python manage.py runserver`

Note:

1) Project has been compiled and tested on the latest version of python(ver 3.9.5) so might not work on python 2.7
2) Docs for the routes made in this project can be found (here)[https://documenter.getpostman.com/view/7132402/TzRSfSkr]