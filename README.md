<H1> EPI-REMINDER </H1>
<h2># What it does</h2>

  ->Streamlines anime episode tracking by integrating seamlessly with your Gmail.<Br>
  ->Generates personalized reminders for upcoming episodes of your chosen anime.<br
  ->Includes convenient watch links directly in your inbox for effortless access.<br><br>
<h2># Requirements</h2>

 ->Python 3.x (https://www.python.org/downloads/)<br>
 ->beautifulsoup4 (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)<br>
 ->gspread (https://pypi.org/project/gspread/)<br>
 ->google-api-python-client (https://github.com/googleapis/google-api-python-client)<br>
 ->oauth2client (https://pypi.org/project/oauth2/)<br>
 ->schedule (https://schedule.readthedocs.io/)<br><br>
 <h2># Installation</h2>
 <h3>Clone the repository</h3>
 <pre>git clone https://github.com/SrivathsG/Anime-reminder/tree/main</pre>
 <h3>Install the requirements</h3>
 <p> Go to the directory where you downloaded then </p>
 <pre>pip install -r requirements.txt</pre>
 <h4> Run the input.exe application</h4>
 <p> From the application register or login your <b>Gmail</b> id and select the anime you wish to receive the notification for.</p>
<h2> Schedule the reminder service </h2>
<h4>Follow the platform-specific instructions carefully:</h4>
<h3>
macOS:</h3>

  o Open System Preferences > Users & Groups > Your Username > Login Items.
  o click the "+" button and select "Anime Reminder Gmail" from Applications.
  o In the "Command" field, enter:
  <pre>python Animelist.py schedule
</pre>
<h3>Windows 11:</h3>

  o Press Windows Key + R to open the Run dialog.
  o Type shell:startup and press Enter.
  o Create a new text file (e.g., anime_reminder.bat) and paste the following content
  <pre>python Animelist.py schedule</pre>
  o Save the file and close the notepad window.
 
