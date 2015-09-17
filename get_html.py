from bs4 import BeautifulSoup
import urllib2

def get_html_string(url):
	# takes a url as a string and 
	# returns the html from that page as a string

	url = url
	page = urllib2.urlopen(url)
	html_string = BeautifulSoup(page.read())
	return html_string

get_html_string("http://unimpressedcats.tumblr.com/")