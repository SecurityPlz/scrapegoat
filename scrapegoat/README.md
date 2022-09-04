Tool name - scrapegoat
Team Members - Ryan, Matticus


Member links: 

Matticus:
https://www.linkedin.com/in/mattic 
https://github.com/SecurityPlz

Ryan:


Tool Description:

scrapegoat.py takes in a json formatted file from the snscrape twitter-user api, individualizes the json objects, and presents links embedded within the 'content' section for review by the researcher


Installation(tested on Pop_Os linux): 

1.) Ensure that git is installed
2.) Ensure that python3.8 or higher is installed
3.) Ensure that pip is installed
	sudo apt install python3-pip
4.) Ensure snscrape is installed
	sudo pip3 install snscrape
5.) Create a directory for snscrape-output
	mkdir ~/snscrape-output
        cd ~/snscrape-output
6.) Query the twitter-user api with the --jsonl flag and redirect the output to a file
        snsscrape --jsonl twitter-user foo > ~/snscrape-output/foo.out
7.) Clone the repository for scrapegoat
	git clone https://github.com/bellingcat/hackathon> 
8.) Change directory to the tools new home
	cd ~/bellingcat-hackathon-1/scrapegoat
9.) Feed our query from step 6 into scrapegoat
	python3 ./scrapegoat.py < ~/snscrape-output/foo.out 
10.) Repeat steps 6-9 as perscribed by your hackers intuition


Usage

The MVP version of this tool (v1) can only be used (as configured) to do exactly what is described above in the install/practical example above. Stay tuned for more and better usage capabilities


Additional Information

    Next steps: Finish parsing links from output and implement tldextract for domain matching and frequency analysis
    At this stage in development, the tool is only presenting links from the dataset. We would like the tool to tell the researcher about the links, and to enable the tool to be looking at other pieces of data, and to inform the researcher on those as well.
    The purpose that we have for this project was to make a simple and easy to use data processing tool for the output of an api request, the scope was picked according to our skill level, and to what we thought would be useful; and MVP acheivable in a weekend.

 
Acknowledgments
    Thank you to Bellingcat for hosting the hackathon that gave birth to this, and other useful and fun tools. Thank you to my teamate Ryan for stepping outside of his comfort zone to assist with the creation of this tool, and thank you to the discerning user who provides feedback, issues, and pull requests on our humble tool.
